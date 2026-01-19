from enum import Enum
import re

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
                if item:
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

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            all_links = extract_markdown_links(node.text)
            current_text = node.text
            for link in all_links:
                splitter = f"[{link[0]}]({link[1]})"
                before_text, after_text = current_text.split(splitter, maxsplit=1)
                if before_text:
                    new_nodes.append(
                        TextNode(
                            before_text,
                            TextType.TEXT
                        )
                    )
                new_nodes.append(
                    TextNode(
                        link[0],
                        TextType.LINK,
                        link[1]
                    )
                )
                current_text = after_text
            if current_text:
                new_nodes.append(
                    TextNode(
                        current_text,
                        TextType.TEXT
                    )
                )
            return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            all_images = extract_markdown_images(node.text)
            current_text = node.text
            for image in all_images:
                splitter = f"![{image[0]}]({image[1]})"
                before_text, after_text = current_text.split(splitter, maxsplit=1)
                if before_text:
                    new_nodes.append(
                        TextNode(
                            before_text,
                            TextType.TEXT
                        )
                    )
                new_nodes.append(
                    TextNode(
                        image[0],
                        TextType.IMAGE,
                        image[1]
                    )
                )
                current_text = after_text
            if current_text:
                new_nodes.append(
                    TextNode(
                        current_text,
                        TextType.TEXT
                    )
                )
            return new_nodes
        


    