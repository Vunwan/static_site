from textnode import TextNode, TextType
from regex import extract_markdown_images


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for image_alt, image_url in images:
            sections = remaining_text.split(
                f"![{image_alt}]({image_url})",
                1,
            )

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(
                TextNode(image_alt, TextType.IMAGE, image_url)
            )

            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
