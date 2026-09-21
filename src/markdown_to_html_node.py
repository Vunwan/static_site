from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    return [
        text_node_to_html_node(text_node)
        for text_node in text_nodes
    ]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            children = text_to_children(text)

            block_nodes.append(
                ParentNode("p", children)
            )

        elif block_type == BlockType.HEADING:
            heading_level = len(block.split(" ")[0])
            text = block[heading_level + 1:]

            children = text_to_children(text)

            block_nodes.append(
                ParentNode(f"h{heading_level}", children)
            )

        elif block_type == BlockType.CODE:
            code_text = block[4:-3]

            code_node = text_node_to_html_node(
                TextNode(code_text, TextType.CODE)
            )

            block_nodes.append(
                ParentNode("pre", [code_node])
            )

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")

            quote_text = "\n".join(
                line[1:].lstrip()
                for line in lines
            )

            children = text_to_children(quote_text)

            block_nodes.append(
                ParentNode("blockquote", children)
            )

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")

            list_items = []

            for line in lines:
                item_text = line[2:]
                children = text_to_children(item_text)

                list_items.append(
                    ParentNode("li", children)
                )

            block_nodes.append(
                ParentNode("ul", list_items)
            )

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")

            list_items = []

            for line in lines:
                item_text = line.split(". ", 1)[1]
                children = text_to_children(item_text)

                list_items.append(
                    ParentNode("li", children)
                )

            block_nodes.append(
                ParentNode("ol", list_items)
            )

    return ParentNode("div", block_nodes)
