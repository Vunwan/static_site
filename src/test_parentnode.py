import unittest

from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "Hello")
        child2 = LeafNode("span", "World")

        parent_node = ParentNode("div", [child1, child2])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>Hello</span><span>World</span></div>",
        )

    def test_to_html_with_text_and_element_children(self):
        child1 = LeafNode(None, "Hello ")
        child2 = LeafNode("b", "world")
        child3 = LeafNode(None, "!")

        parent_node = ParentNode("p", [child1, child2, child3])

        self.assertEqual(
            parent_node.to_html(),
            "<p>Hello <b>world</b>!</p>",
        )

    def test_to_html_with_multiple_nested_parent_nodes(self):
        child1 = ParentNode(
            "span",
            [LeafNode("b", "bold")],
        )

        child2 = ParentNode(
            "span",
            [LeafNode("i", "italic")],
        )

        parent_node = ParentNode("div", [child1, child2])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>bold</b></span><span><i>italic</i></span></div>",
        )

    def test_to_html_with_deeply_nested_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [
                                LeafNode("b", "deeply nested"),
                            ],
                        )
                    ],
                )
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<div><section><p><b>deeply nested</b></p></section></div>",
        )

    def test_to_html_with_no_tag(self):
        node = ParentNode(
            None,
            [LeafNode("span", "child")],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_children(self):
        node = ParentNode("div", None)

        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()