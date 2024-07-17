from htmlnode import HTMLNode
from textnode import TextNode
from parentnode import ParentNode
from inline_markdown import text_to_textnodes

from markdown_blocks import (
    markdown_to_blocks, 
    block_to_block_type,
    block_type_code,
    block_type_heading,
    block_type_quote,
    block_type_paragraph,
    block_type_ordered_list,
    block_type_unordered_list
)

def markdown_to_htmlnode(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []
    for block in blocks:
        htmlnode = block_to_htmlnode(block)
        children.append(htmlnode)
    return ParentNode("div", children, None)

def block_to_htmlnode(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_htmlnode(block)
    if block_type == block_type_heading:
        return heading_to_htmlnode(block)
    if block_type == block_type_code:
        return code_to_htmlnode(block)
    if block_type == block_type_ordered_list:
        return list_to_htmlnode(block)
    if block_type == block_type_unordered_list:
        return list_to_htmlnode(block, block_type_unordered_list)
    if block_type == block_type_quote:
        return quote_to_htmlnode(block)
    raise ValueError("Invalid block type") 

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    children: list[HTMLNode] = []
    for text_node in text_nodes:
        html_node = text_node.to_htmlnode()
        children.append(html_node)
    return children


def paragraph_to_htmlnode(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))

def heading_to_htmlnode(block: str) -> ParentNode:
    heading_num = 0
    for char in block:
        if char == "#":
            heading_num += 1
        else:
            break
    if heading_num + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {heading_num}")
    children = text_to_children(block[heading_num + 1 :])
    return ParentNode(f"h{heading_num}", children)

def code_to_htmlnode(block: str) -> ParentNode:
    code = ParentNode("code", text_to_children(block[4:-3]))
    return ParentNode("pre", [code])

def list_to_htmlnode(block: str, list_block_type: str = block_type_ordered_list) -> ParentNode:
    items = block.split("\n")
    html_items = []
    num_chars = 2
    tag = "ul"
    if list_block_type == block_type_ordered_list:
        num_chars = 3
        tag = "ol"

    for item in items:
        text = item[num_chars:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode(tag, html_items)

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    return ParentNode("blockquote", text_to_children(content))