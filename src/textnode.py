from htmlnode import HTMLNode
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = 'link'
text_type_image = 'image' 

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value: object) -> bool:
        return (self.text == value.text and 
                self.text_type == value.text_type and
                self.url == value.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def to_html_node(self) -> HTMLNode:
        match self.text_type:
            case "text":
                return LeafNode(None, self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text, props={"href": self.url})
            case "image":
                return LeafNode("img", None, props={
                    "src": self.url,
                    "alt": self.text
                })
            case _:
                raise ValueError(f"Invalid text type: {self.text_type}")

