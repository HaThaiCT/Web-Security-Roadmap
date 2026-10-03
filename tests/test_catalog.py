import json
import tempfile
import unittest
from pathlib import Path

import yaml


class CatalogFixtureTests(unittest.TestCase):
    def test_upstream_fixture_mapping_preserves_all_entries(self):
        entries = [
            {"id": "one", "url": "https://example.com/1", "title": "One"},
            {"id": "two", "url": "https://example.com/2", "title": "Two"},
        ]
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            index = root / "index.json"
            mapping = root / "mapping.yml"
            index.write_text(json.dumps({"entries": entries}), encoding="utf-8")
            mapping.write_text(
                yaml.safe_dump({"entries": [{"upstream_id": "one"}, {"upstream_id": "two"}]}),
                encoding="utf-8",
            )
            loaded = json.loads(index.read_text(encoding="utf-8"))["entries"]
            mapped = yaml.safe_load(mapping.read_text(encoding="utf-8"))["entries"]
            self.assertEqual({e["id"] for e in loaded}, {m["upstream_id"] for m in mapped})

    def test_curated_resource_requires_verification_evidence(self):
        row = {
            "id": "example",
            "title": "Example",
            "url": "https://example.com",
            "type": "documentation",
            "language": "en",
            "difficulty": "beginner",
            "audiences": ["learner"],
            "primary_topic": "http",
            "tier": "core",
            "annotation": "Useful resource.",
            "cost": "free",
            "access": "public",
            "verification": {"status": "content-reviewed", "evidence": "Relevant content inspected."},
            "provenance": {"origin": "additional-research", "upstream_ids": []},
        }
        self.assertIn("evidence", row["verification"])
        self.assertEqual(row["language"], "en")

    def test_repository_taxonomy_and_resources_pass_validation(self):
        root = Path(__file__).resolve().parents[1]
        taxonomy_path = root / "data" / "taxonomy.yml"
        self.assertTrue(taxonomy_path.exists())
        tax = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))
        chapter_ids = [c["id"] for c in tax.get("chapters", [])]
        self.assertEqual(len(chapter_ids), 9)
        topic_ids = {t["id"] for c in tax.get("chapters", []) for t in c.get("topics", [])}
        self.assertIn("http", topic_ids)
        self.assertIn("dns-tls", topic_ids)
        self.assertIn("applied-crypto", topic_ids)
        self.assertIn("distributed-components", topic_ids)
        self.assertIn("mfa-passkeys", topic_ids)
        self.assertIn("business-logic", topic_ids)
        self.assertIn("ldap-xpath", topic_ids)
        self.assertIn("dns-rebinding", topic_ids)
        self.assertIn("grpc-soap", topic_ids)
        self.assertIn("webhooks-saas", topic_ids)
        self.assertIn("payments-workflows", topic_ids)
        self.assertIn("metadata-serverless", topic_ids)
        self.assertIn("side-channels", topic_ids)
        self.assertIn("secure-design", topic_ids)

        # Check that all resource files have valid primary_topics
        resources_dir = root / "data" / "resources"
        covered_topics = set()
        for rpath in resources_dir.glob("*.yml"):
            data = yaml.safe_load(rpath.read_text(encoding="utf-8")) or []
            for item in data:
                self.assertIn(item["primary_topic"], topic_ids, f"{rpath}: unknown primary_topic {item.get('primary_topic')}")
                self.assertEqual(item["language"], "en")
                self.assertIn(item["tier"], {"core", "extended"})
                self.assertTrue(item.get("verification", {}).get("evidence"))
                covered_topics.add(item["primary_topic"])

        # Verify 100% full coverage across all 79 topics
        self.assertEqual(len(topic_ids), 79)
        missing_topics = topic_ids - covered_topics
        self.assertEqual(missing_topics, set(), f"Missing resource coverage for topics: {missing_topics}")

    def test_no_unauthored_placeholders_in_topic_docs(self):
        root = Path(__file__).resolve().parents[1]
        topics_dir = root / "docs" / "topics"
        placeholder = "To be authored during curation"
        for md_file in topics_dir.glob("**/README.md"):
            content = md_file.read_text(encoding="utf-8")
            self.assertNotIn(
                placeholder,
                content,
                f"Found unauthored placeholder in {md_file.relative_to(root)}",
            )


if __name__ == "__main__":
    unittest.main()
