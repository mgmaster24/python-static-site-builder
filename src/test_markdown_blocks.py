import unittest
from markdown_blocks import (
    markdown_to_blocks, 
    block_to_block_type,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_quote,
    block_type_ordered_list,
    block_type_unordered_list
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_type_is_heading(self):
        block = "# This is an H1 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)

        block = "## This is an H2 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)

        block = "### This is an H3 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)

        block = "#### This is an H4 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)

        block = "##### This is an H5 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)

        block = "###### This is an H6 heading"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_heading)
    
    def test_block_type_is_code(self):
        block = "``` This is some code ```"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_code)

        block = """```
        This is some multi
        line code
        ```"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_code)

    def test_block_type_is_quote(self):
        block = ">This is a quote"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_quote)

        block = ">This is a multi\n>line quote"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_quote)

        block = """>This is a multi
>line quote
>Using multi line
>strings"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_quote)

    def test_block_type_should_default_to_paragraph(self):
        block = ">This is a quote\n* Some text"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_paragraph)

        block = ">This is a multi\n1. line quote"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_paragraph)

        block = """>This is a multi
>line quote
>Using multi line
- strings"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_paragraph)

    def test_block_type_ordered_list(self):
        block = "1. This is an\n2. ordered list"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_ordered_list)

        block = "1. This is a multi"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_ordered_list)

        block = """1. This is a multi
2. line ordered
3. list
4. of strings"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_ordered_list)
    
    def test_block_type_unordered_list(self):
        block = "* This is an\n* ordered list"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_unordered_list)

        block = "- This is a multi"
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_unordered_list)

        block = """* This is a multi
* line ordered
* list
* of strings"""
        bt = block_to_block_type(block)
        self.assertEqual(bt, block_type_unordered_list)

if __name__ == "__main__":
    unittest.main()
