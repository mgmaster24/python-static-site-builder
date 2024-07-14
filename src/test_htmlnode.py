import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
        
    def test_to_string(self):
        node = HTMLNode("h1", "My Heading")
        str_rep = f"{node}"
        expected = "HTMLNode: {'tag': 'h1', 'value': 'My Heading', 'children': None, 'props': None}"
        self.assertEqual(str_rep, expected)

    def test_to_string2(self):
        node = HTMLNode("h1", "My Heading", [HTMLNode("p")], {"class: primary"})
        str_rep = f"{node}"
        expected = "HTMLNode: {'tag': 'h1', 'value': 'My Heading', 'children': [HTMLNode: {'tag': 'p', 'value': None, 'children': None, 'props': None}], 'props': {'class: primary'}}"
        self.assertEqual(str_rep, expected)


    def test_children(self):
        node = HTMLNode("h1", "My Heading", [HTMLNode("p"), HTMLNode("a")])
        expected = [HTMLNode("p"), HTMLNode("a")]

        for i in range(0, len(expected)) :
            self.assertEqual(node.children[i].tag, expected[i].tag)
        

    def test_props_to_html(self):
        node = HTMLNode("h1", "My Heading", props= {
            "href": "https://www.google.com", 
            "target": "_blank",
        })

        props = node.props_to_html()
        self.assertEqual(props,  " href=\"https://www.google.com\" target=\"_blank\"")
        
       
if __name__== "__main__":
    unittest.main()