import unittest

from textnode import TextNode, TextType
from images import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
            "and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is just regular text.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual([node], new_nodes)

    def test_image_at_beginning(self):
        node = TextNode(
            "![cat](https://example.com/cat.png) is cute.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
                TextNode(" is cute.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "Look at this: ![cat](https://example.com/cat.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Look at this: ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "![cat](https://example.com/cat.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
            ],
            new_nodes,
        )

    def test_multiple_images(self):
        node = TextNode(
            "![one](https://example.com/one.png) "
            "middle "
            "![two](https://example.com/two.png) "
            "end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("one", TextType.IMAGE, "https://example.com/one.png"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "https://example.com/two.png"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_non_text_node(self):
        node = TextNode(
            "already an image",
            TextType.IMAGE,
            "https://example.com/image.png",
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual([node], new_nodes)
