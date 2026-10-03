#!/usr/bin/env python3
"""Check external link reachability without changing catalog data."""
from __future__ import annotations

import argparse
import json
import socket
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_DIR = ROOT / "data" / "resources"
UPSTREAM_INDEX = ROOT / "data" / "upstream" / "awesome-web-security" / "index.json"


def collect_urls(include_upstream: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if RESOURCE_DIR.exists():
        for path in sorted(RESOURCE_DIR.glob("*.yml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
            for item in data if isinstance(data, list) else []:
                if isinstance(item, dict) and item.get("url"):
                    rows.append({"source": str(path.relative_to(ROOT)), "id": str(item.get("id", "")), "url": str(item["url"])})
    if include_upstream and UPSTREAM_INDEX.exists():
        data = json.loads(UPSTREAM_INDEX.read_text(encoding="utf-8"))
        for item in data.get("entries", []):
            if isinstance(item, dict) and item.get("url"):
                rows.append({"source": "upstream", "id": str(item.get("id", "")), "url": str(item["url"])})
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for row in rows:
        key = row["url"]
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique


def request_code(url: str, method: str, timeout: int) -> int:
    request = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": "practical-awesome-web-security-link-check/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:  # noqa: S310 catalog URLs are untrusted but not executed
        return response.getcode()


def classify(url: str, timeout: int) -> dict[str, object]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return {"status": "invalid", "detail": "not an HTTP(S) URL"}
    try:
        code = request_code(url, "HEAD", timeout)
    except urllib.error.HTTPError as exc:
        code = exc.code
        if code in {403, 404, 405}:
            try:
                get_code = request_code(url, "GET", timeout)
            except urllib.error.HTTPError as get_exc:
                if get_exc.code in {403, 429, 401}:
                    return {"status": "blocked", "code": get_exc.code, "detail": get_exc.reason}
                if get_exc.code == 404:
                    return {"status": "dead", "code": get_exc.code, "detail": get_exc.reason}
                return {"status": "http-error", "code": get_exc.code, "detail": get_exc.reason}
            except (urllib.error.URLError, socket.timeout, TimeoutError) as get_exc:
                return {"status": "unknown", "detail": f"HEAD returned {code}; GET failed: {get_exc}"}
            if 200 <= get_code < 400:
                return {"status": "reachable", "code": get_code, "detail": f"GET fallback after HEAD {code}"}
            return {"status": "http-error", "code": get_code, "detail": f"GET fallback after HEAD {code}"}
        if code in {429, 401}:
            return {"status": "blocked", "code": code, "detail": exc.reason}
        return {"status": "http-error", "code": code, "detail": exc.reason}
    except (urllib.error.URLError, socket.timeout, TimeoutError) as exc:
        return {"status": "unknown", "detail": str(exc)}
    if 200 <= code < 400:
        return {"status": "reachable", "code": code}
    return {"status": "http-error", "code": code}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-upstream", action="store_true", help="Also check full upstream catalog URLs; this can be slow/noisy.")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of URLs for a smoke check.")
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    urls = collect_urls(args.include_upstream)
    if args.limit:
        urls = urls[: args.limit]
    results = []
    for row in urls:
        result = dict(row)
        result.update(classify(row["url"], args.timeout))
        results.append(result)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            print(f"{result['status']}\t{result.get('code','')}\t{result['id']}\t{result['url']}")
    dead = [r for r in results if r.get("status") == "dead"]
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())
