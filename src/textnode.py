from htmlnode import HTMLNode
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = 'link'
text_type_image = 'image' 

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value: object) -> bool:
        return (self.text == value.text and 
                self.text_type == value.text_type and
                self.url == value.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def to_htmlnode(self) -> HTMLNode:
            if self.text_type == text_type_text:
                return LeafNode(None, self.text)
            if self.text_type == text_type_bold:
                return LeafNode("b", self.text)
            if self.text_type == text_type_italic:
                return LeafNode("i", self.text)
            if self.text_type == text_type_code:
                return LeafNode("code", self.text)
            if self.text_type == text_type_link:
                return LeafNode("a", self.text, props={"href": self.url})
            if self.text_type == text_type_image:
                return LeafNode("img", None, props={
                    "src": self.url,
                    "alt": self.text
                })
            
            raise ValueError(f"Invalid text type: {self.text_type}")
