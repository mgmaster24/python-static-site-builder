from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("ParentNodes must have a tag")
        if len(self.children) == 0:
            raise ValueError("ParentNodes must have children")
        
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"