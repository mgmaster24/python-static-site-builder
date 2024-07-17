import unittest

from textnode import TextNode
from leafnode import LeafNode
from htmlnode import HTMLNode

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

    def test_to_raw_text_leafnode(self):
        node = TextNode("Some raw text", 'text')
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, "Some raw text")
        self.assertIsInstance(converted, LeafNode)
        self.assertIsNone(converted.tag)

    def test_to_bold_leafnode(self):
        node = TextNode("Some raw text", 'bold')
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, "Some raw text")
        self.assertIsInstance(converted, LeafNode)
        self.assertEqual(converted.tag, "b")
    
    def test_to_italic_htmlnode(self):
        node = TextNode("Some raw text", 'italic')
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, "Some raw text")
        self.assertIsInstance(converted, LeafNode)
        self.assertEqual(converted.tag, "i")
    
    def test_to_code_htmlnode(self):
        node = TextNode("Some raw text", 'code')
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, "Some raw text")
        self.assertIsInstance(converted, LeafNode)
        self.assertEqual(converted.tag, "code")

    def test_to_link_htmlnode(self):
        node = TextNode("Some raw text", 'link', "www.boot.dev")
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, "Some raw text")
        self.assertIsInstance(converted, LeafNode)
        self.assertEqual(converted.tag, "a")
        self.assertEqual(converted.props, {
            "href": "www.boot.dev"
        })
        self.assertEqual(converted.props_to_html(), ' href="www.boot.dev"')
        converted.to_html()

    def test_to_image_htmlnode(self):
        node = TextNode("some alt text", 'image', "./assets/cool.jpg")
        converted = node.to_htmlnode()
        self.assertEqual(converted.value, None)
        self.assertIsInstance(converted, LeafNode)
        self.assertEqual(converted.tag, "img")
        self.assertEqual(converted.props, {
            "src": "./assets/cool.jpg",
            "alt": "some alt text"
        })

        self.assertEqual(converted.props_to_html(), ' src="./assets/cool.jpg" alt="some alt text"')
    
    def test_raise_unsupported_text_type(self):
        node = TextNode("some alt text", 'unsupported', "./assets/cool.jpg")
        self.assertRaises(ValueError, node.to_htmlnode)
        

if __name__== "__main__":
    unittest.main()