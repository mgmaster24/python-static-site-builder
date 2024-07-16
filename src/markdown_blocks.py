import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split('\n\n')
    filtered = []
    for block in blocks:
        if block == "":
            continue
        
        block = block.strip()
        filtered.append(block)

    return filtered

def __get_block_type_or_paragraph(lines, character, ret_block_type):
    for line in lines:
        if not line.startswith(character):
            return block_type_paragraph
    return ret_block_type

def block_to_block_type(block: str)-> str:
    if (
        block.startswith('#') or
        block.startswith('##') or
        block.startswith('###') or
        block.startswith('####') or
        block.startswith('#####') or
        block.startswith('######') 
    ):
        return block_type_heading
    
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    
    lines = block.split('\n')
    if block.startswith(">"):
        return __get_block_type_or_paragraph(lines, ">", block_type_quote)
    if block.startswith("* "):
        return __get_block_type_or_paragraph(lines, "* ", block_type_unordered_list)
    if block.startswith("- "):
        return __get_block_type_or_paragraph(lines, "- ", block_type_unordered_list)
    if block.startswith("1. "):
        ordered_idx = 1
        for line in lines:
            if not line.startswith(f"{ordered_idx}. "):
                return block_type_paragraph
            ordered_idx += 1
        return block_type_ordered_list
   
    return block_type_paragraph