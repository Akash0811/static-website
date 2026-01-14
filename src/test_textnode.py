import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is another node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.BOLD)
        self.assertIsNotNone(node.url)
        self.assertIsNone(node2.url)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
