import unittest

from regex import extract_markdown_images, extract_markdown_links


class TestMarkdownParser(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        text = (
            "This is text with a "
            "![rick roll](https://i.imgur.com/aKaOqIh.gif) and "
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        matches = extract_markdown_images(text)

        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches
        )

    def test_extract_no_images(self):
        matches = extract_markdown_images(
            "This text has no images."
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link "
            "[to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            matches
        )

    def test_extract_multiple_links(self):
        text = (
            "This is text with a link "
            "[to boot dev](https://www.boot.dev) and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )

        matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches
        )

    def test_extract_no_links(self):
        matches = extract_markdown_links(
            "This text has no links."
        )
        self.assertListEqual([], matches)

    def test_links_do_not_extract_images(self):
        matches = extract_markdown_links(
            "![image](https://example.com/image.png)"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()