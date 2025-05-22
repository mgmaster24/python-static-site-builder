from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_code,
    text_type_italic,
)

import re


# TODO - Consider handling nested markdown
def split_nodes_delimiter(
    nodes: list[TextNode], delimeter: str, text_type: str
) -> list[TextNode]:
    transformed_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            transformed_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        transformed_nodes.extend(split_nodes)

    return transformed_nodes


def extract_markdown_images(text: str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(nodes: list[TextNode]):
    return __split_nodes(nodes, True, extract_markdown_images)


def split_nodes_link(nodes: list[TextNode]):
    return __split_nodes(nodes)


def __split_nodes(
    nodes: list[TextNode], is_image=False, extract=extract_markdown_links
) -> list[TextNode]:
    transformed_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            transformed_nodes.append(node)
            continue
        node_text = node.text
        results = extract(node_text)
        if len(results) == 0:
            transformed_nodes.append(node)
            continue
        for res in results:
            split_text = f"[{res[0]}]({res[1]})"
            if is_image:
                split_text = f"![{res[0]}]({res[1]})"
            sections = node_text.split(split_text)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, section not closed")
            if sections[0] != "":
                transformed_nodes.append(TextNode(sections[0], text_type_text))

            if is_image:
                transformed_nodes.append(TextNode(res[0], text_type_image, res[1]))
            else:
                transformed_nodes.append(TextNode(res[0], text_type_link, res[1]))
            node_text = sections[1]
        if node_text != "":
            transformed_nodes.append(TextNode(node_text, text_type_text))
    return transformed_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = split_nodes_delimiter(
        [TextNode(text, text_type_text)], "**", text_type_bold
    )
    nodes = split_nodes_delimiter(nodes, "_", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes
