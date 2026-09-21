import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING,
        )

    def test_all_heading_levels(self):
        for i in range(1, 7):
            block = "#" * i + " Heading"

            self.assertEqual(
                block_to_block_type(block),
                BlockType.HEADING,
            )

    def test_heading_too_many_hashes(self):
        self.assertEqual(
            block_to_block_type("####### Heading"),
            BlockType.PARAGRAPH,
        )

    def test_heading_requires_space(self):
        self.assertEqual(
            block_to_block_type("#Heading"),
            BlockType.PARAGRAPH,
        )

    def test_code_block(self):
        block = "```\nprint('hello')\n```"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE,
        )

    def test_multiline_code_block(self):
        block = "```\nline one\nline two\nline three\n```"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE,
        )

    def test_code_block_requires_starting_backticks(self):
        block = "print('hello')\n```"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_code_block_requires_ending_backticks(self):
        block = "```\nprint('hello')"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_quote(self):
        block = "> This is a quote"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_multiline_quote(self):
        block = "> First line\n> Second line\n> Third line"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_quote_without_space(self):
        block = ">First line\n>Second line"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_quote_requires_every_line(self):
        block = "> First line\nSecond line"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list(self):
        block = "- First\n- Second\n- Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST,
        )

    def test_single_unordered_list_item(self):
        self.assertEqual(
            block_to_block_type("- One item"),
            BlockType.UNORDERED_LIST,
        )

    def test_unordered_list_requires_space(self):
        block = "- First\n-Second"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list_requires_every_line(self):
        block = "- First\n- Second\nThird"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST,
        )

    def test_single_ordered_list_item(self):
        self.assertEqual(
            block_to_block_type("1. First"),
            BlockType.ORDERED_LIST,
        )

    def test_ordered_list_must_start_at_one(self):
        block = "2. First\n3. Second\n4. Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_must_increment(self):
        block = "1. First\n3. Second\n4. Third"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_requires_space(self):
        block = "1. First\n2.Second"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_requires_every_line(self):
        block = "1. First\n2. Second\nNot a list item"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_paragraph(self):
        block = "This is a normal paragraph."

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_multiline_paragraph(self):
        block = "This is line one.\nThis is line two."

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()
