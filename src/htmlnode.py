class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        else:
            final_str = ""
            for key, value in self.props.items():
                final_str += f' {key}="{value}"'
            return final_str
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {[repr(x) for x in self.children] if self.children else None}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Node must have value.")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have tag.")
        if self.children is None:
            raise ValueError("Parent Node cannot have optional children.")
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {[repr(x) for x in self.children] if self.children else None}, {self.props})"
