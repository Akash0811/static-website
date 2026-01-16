import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


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

    def test_simple_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_multiple_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word and **bold word**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes_2 = new_nodes[:-1] + split_nodes_delimiter([new_nodes[-1]], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes_2,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word and ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD),
                TextNode(".", TextType.TEXT),
            ]
        )

    def test_invalid_markdown(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertRaises(
            Exception,
            split_nodes_delimiter([node], "`", TextType.CODE)
        )



if __name__ == "__main__":
    unittest.main()
