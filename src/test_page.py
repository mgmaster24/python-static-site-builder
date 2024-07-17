import unittest

from page import extract_title

class TestPage(unittest.TestCase):

    def test_extract_title(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        title = extract_title(md)
        self.assertEqual(title, "this is an h1")
