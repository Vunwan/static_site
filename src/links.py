from textnode import TextNode, TextType
from regex import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for link_text, link_url in links:
            sections = remaining_text.split(
                f"[{link_text}]({link_url})",
                1,
            )

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(
                TextNode(link_text, TextType.LINK, link_url)
            )

            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
