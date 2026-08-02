import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nodes", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_type_is_dif(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nodes", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_is_same(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nodes", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()