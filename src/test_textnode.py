import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_to_string(self):
        node = TextNode("This is a text node", "bold", "some.coolsite.me")
        str_rep = f"{node}"
        self.assertEqual(str_rep, "TextNode(This is a text node, bold, some.coolsite.me)")

    def test_url_is_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

if __name__== "__main__":
    unittest.main()