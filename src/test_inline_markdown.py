import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_node_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], '`', TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ])

    def test_bold_node(self):
        node = TextNode("**This text is bold.**", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node], '**', TextType.BOLD),
            [node]
        )

    def test_multiple_nodes(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("**This text is bold.**", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node1, node2], '`', TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                node2,
            ])

    def test_unclosed_delimiter(self):
        node = TextNode("This is `unclosed code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], '`', TextType.CODE)
