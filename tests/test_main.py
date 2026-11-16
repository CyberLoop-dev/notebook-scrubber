import unittest
from main import scrub


class ScrubTests(unittest.TestCase):
    def test_removes_code_output_and_count(self):
        source = {"cells":[{"cell_type":"code","source":["x=1"],"outputs":[{"data":{}}],"execution_count":3}]}
        result, changed = scrub(source)
        self.assertEqual(changed, 1)
        self.assertEqual(result["cells"][0]["outputs"], [])
        self.assertIsNone(result["cells"][0]["execution_count"])
        self.assertEqual(source["cells"][0]["execution_count"], 3)

    def test_preserves_markdown(self):
        source = {"cells":[{"cell_type":"markdown","source":["hello"]}]}
        result, changed = scrub(source)
        self.assertEqual(changed, 0)
        self.assertEqual(result, source)


if __name__ == "__main__":
    unittest.main()
