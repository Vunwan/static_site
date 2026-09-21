import unittest

from markdown_to_html import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_whitespace(self):
        markdown = "#   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_with_other_headers(self):
        markdown = "## Subtitle\n\n# Main Title\n\n### Another heading"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_missing(self):
        markdown = "## Hello\n\nThis has no h1."
        
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
