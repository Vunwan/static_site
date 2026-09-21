import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_all_markdown_types(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_plain_text(self):
        text = "This is just plain text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is just plain text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_bold(self):
        text = "This is **bold** text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_italic(self):
        text = "This is _italic_ text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_code(self):
        text = "This is `code` text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_link(self):
        text = "Visit [Boot.dev](https://boot.dev) today."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode(
                    "Boot.dev",
                    TextType.LINK,
                    "https://boot.dev",
                ),
                TextNode(" today.", TextType.TEXT),
            ],
            nodes,
        )

    def test_image(self):
        text = "Here is an ![image](https://example.com/image.png)."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )

    def test_multiple_styles(self):
        text = "**bold** and _italic_ and `code`"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            nodes,
        )

    def test_multiple_links_and_images(self):
        text = (
            "[one](https://one.com) "
            "![image](https://image.com/a.png) "
            "[two](https://two.com)"
        )

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("one", TextType.LINK, "https://one.com"),
                TextNode(" ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://image.com/a.png",
                ),
                TextNode(" ", TextType.TEXT),
                TextNode("two", TextType.LINK, "https://two.com"),
            ],
            nodes,
        )

    def test_empty_text(self):
        text = ""

        nodes = text_to_textnodes(text)

        self.assertListEqual([], nodes)
