import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
	def test_def_is_None(self):
		node1 = HTMLNode()
		self.assertEqual(
			(node1.tag, node1.value, node1.children, node1.props),
			(None, None, None, None)
			)

	def test_assignment(self):
		node1 = HTMLNode(
			tag="div",
			value="Hello",
			children=["child1"],
			props={"class": "greeting"}
			)
		self.assertEqual(
			(node1.tag, node1.value, node1.children, node1.props),
			("div", "Hello", ["child1"], {"class": "greeting"})
			)

	def test_repr(self):
		node1 = HTMLNode(
			tag="div",
			value="Hello",
			children=["child1"],
			props={"class": "greeting"}
		)
		self.assertEqual(
			repr(node1),
			"HTMLNode(div, Hello, ['child1'], {'class': 'greeting'})"
		)

	def test_props_to_html(self):
		node1 = HTMLNode(props={"href": "https://example.com", "class": "bold"})
		self.assertEqual(
			node1.props_to_html(),
			' href="https://example.com" class="bold"'
		)

	def test_props_to_html_empty(self):
		node1 = HTMLNode()
		self.assertEqual(node1.props_to_html(), "")


class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_b(self):
		node = LeafNode("b", "Hello, world!")
		self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

	def test_leaf_to_html_props(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

	def test_repr(self):
		node1 = LeafNode(
			tag="div",
			value="Hello",
			props={"class": "greeting"}
		)
		self.assertEqual(
			repr(node1),
			"LeafNode(div, Hello, {'class': 'greeting'})"
			)


class TestParentNode(unittest.TestCase):
	def test_simple_parent_to_html(self):
		node = ParentNode("p", [LeafNode("b", "Hello, world!")])
		self.assertEqual(
			node.to_html(),
			"<p><b>Hello, world!</b></p>"
			)

	def test_complex_parent_to_html(self):
		node = ParentNode("p", [
				ParentNode("p", [LeafNode("b", "Hello, world!")]),
				LeafNode("b", "Hello, again!")
				])
		self.assertEqual(
			node.to_html(),
			"<p><p><b>Hello, world!</b></p><b>Hello, again!</b></p>"
			)


# other tests to add:
# test all for errors
# test ParentNode for simple with props


if __name__ == "__main__":
	unittest.main()
