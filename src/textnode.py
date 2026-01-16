from enum import Enum

class TextType(Enum):
    TEXT = "plain text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            inbetween_text = node.text.split(delimiter)
            if len(inbetween_text) % 2 == 0 and len(inbetween_text) >= 1:
                raise Exception("Invalid Markdown.")
            for i, item in enumerate(inbetween_text):
                if i % 2 == 0:
                    new_nodes.append(
                        TextNode(
                            item,
                            TextType.TEXT
                        )
                    ) 
                else:
                    new_nodes.append(
                        TextNode(
                            item,
                            text_type
                        )
                    )
    return new_nodes
