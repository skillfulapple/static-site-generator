import unittest

from htmlnode import HTMLNode


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

# come back to this later...

#	def test_props_to_html_empty(self):
#		node1 = HTMLNode()
#		self.assertEqual(node1.props_to_html, "")


if __name__ == "__main__":
	unittest.main()

