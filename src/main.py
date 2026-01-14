from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

    html_node = HTMLNode(
            "a",
            "blank link",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
    print(html_node)

if __name__ == "__main__":
    main()
