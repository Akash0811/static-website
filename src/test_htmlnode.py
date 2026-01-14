import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "blank link",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(node.props_to_html(), ''' href="https://www.google.com" target="_blank"''')

    def test_props_to_html_none(self):
        node = HTMLNode("p", "This is a paragraph.")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_attributes(self):
        node = HTMLNode("p", "This is a paragraph.", [], {})
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
