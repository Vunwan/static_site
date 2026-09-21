import unittest

from textnode import TextNode, TextType
from links import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode(
                    "to boot dev",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
            "This is just regular text.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual([node], new_nodes)

    def test_link_at_beginning(self):
        node = TextNode(
            "[Boot.dev](https://www.boot.dev) is great.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(
                    "Boot.dev",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
                TextNode(" is great.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "Visit [Boot.dev](https://www.boot.dev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode(
                    "Boot.dev",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "[Boot.dev](https://www.boot.dev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(
                    "Boot.dev",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
            ],
            new_nodes,
        )

    def test_multiple_links(self):
        node = TextNode(
            "[one](https://example.com/one) "
            "middle "
            "[two](https://example.com/two) "
            "end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("one", TextType.LINK, "https://example.com/one"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("two", TextType.LINK, "https://example.com/two"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_non_text_node(self):
        node = TextNode(
            "already a link",
            TextType.LINK,
            "https://example.com",
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual([node], new_nodes)
