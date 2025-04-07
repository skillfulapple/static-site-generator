import unittest
from split_node_delimiter import *
from textnode import *


class TestSplitNodesDelimiter(unittest.TestCase):
	def test_delimiter_simple(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(
			new_nodes,
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.TEXT),
			])


if __name__ == "__main__":
	unittest.main()
