import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\n"
                "This is the same paragraph on a new line",
                "- This is a list\n"
                "- with items",
            ],
        )

    def test_single_block(self):
        md = "This is a single block."

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is a single block.",
            ],
        )

    def test_multiple_blocks(self):
        md = """
First block

Second block

Third block
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_excessive_newlines(self):
        md = """
First block



Second block




Third block
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_leading_and_trailing_whitespace(self):
        md = """

   First block   

   Second block   

"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
            ],
        )

    def test_multiline_block(self):
        md = """
This is line one
This is line two
This is line three

This is another block
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is line one\nThis is line two\nThis is line three",
                "This is another block",
            ],
        )

    def test_empty_markdown(self):
        md = ""

        blocks = markdown_to_blocks(md)

        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        md = "   \n\n   \n\n   "

        blocks = markdown_to_blocks(md)

        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()
