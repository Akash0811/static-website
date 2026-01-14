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