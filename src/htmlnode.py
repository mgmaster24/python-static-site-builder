class HTMLNode:
    def __init__(
            self, 
            tag: str = None, 
            value: str = None, 
            children = None, 
            props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        node = {
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "props": self.props
        }

        return f"HTMLNode: {node}"

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        
        to_html = ""
        for prop in self.props:
            to_html += f' {prop}="{self.props[prop]}"'
        return to_html