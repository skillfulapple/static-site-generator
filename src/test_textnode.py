import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node1, node2)

	def test_text_not_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is also a text node", TextType.BOLD)
		self.assertNotEqual(node1, node2)

	def test_texttype_not_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertNotEqual(node1, node2)

	def test_url_not_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD, "https://text.node")
		self.assertNotEqual(node1, node2)

	def test_def_url_is_None(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node1.url, None)


if __name__ == "__main__":
	unittest.main()
