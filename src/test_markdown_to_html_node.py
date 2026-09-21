import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and "
            "<code>code</code> here</p>"
            "</div>",
        )

    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "</code></pre></div>",
        )

    def test_heading(self):
        md = "# This is a heading"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )

    def test_all_heading_levels(self):
        for level in range(1, 7):
            md = f'{"#" * level} Heading {level}'

            node = markdown_to_html_node(md)
            html = node.to_html()

            self.assertEqual(
                html,
                f"<div><h{level}>Heading {level}</h{level}></div>",
            )

    def test_blockquote(self):
        md = "> This is a quote"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )

    def test_multiline_blockquote(self):
        md = """
> First line
> Second line
> Third line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>"
            "First line\nSecond line\nThird line"
            "</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item
- Second item
- Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item</li>"
            "<li>Third item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li>"
            "<li>Third item</li></ol></div>",
        )

    def test_link(self):
        md = "This is a [link](https://boot.dev)."

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            '<div><p>This is a <a href="https://boot.dev">'
            "link</a>.</p></div>",
        )

    def test_image(self):
        md = "This is an ![image](https://example.com/image.png)."

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            '<div><p>This is an '
            '<img src="https://example.com/image.png" alt="image"></img>'
            ".</p></div>",
        )

    def test_inline_markdown(self):
        md = (
            "This has **bold**, _italic_, and "
            "`code`."
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This has <b>bold</b>, <i>italic</i>, and "
            "<code>code</code>.</p></div>",
        )

    def test_multiple_blocks(self):
        md = """
# Heading

This is a paragraph.

- One
- Two

1. First
2. Second

> A quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading</h1>"
            "<p>This is a paragraph.</p>"
            "<ul><li>One</li><li>Two</li></ul>"
            "<ol><li>First</li><li>Second</li></ol>"
            "<blockquote>A quote</blockquote>"
            "</div>",
        )


if __name__ == "__main__":
    unittest.main()
