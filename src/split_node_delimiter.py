from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []

	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue

		processed_nodes = process_text_node(old_node, delimiter, text_type)
		new_nodes.extend(processed_nodes)

	return new_nodes


def process_text_node(text_node, delimiter, text_type):
	result_nodes = []
	text = text_node.text

	# find first delimiter (opening)
	opening_index = text.find(delimiter)
	if opening_index == -1:
		return [text_node]

	# find second delimiter (closing)
	closing_index = text.find(delimiter, opening_index + len(delimiter))
	if closing_index == -1:
		raise Exception(f"No closing delimiter \"{delimiter}\" found in text: {text}")

	before = text[:opening_index]
	middle = text[opening_index + len(delimiter):closing_index]
	after = text[closing_index + len(delimiter):]

	if before:
		result_nodes.append(TextNode(before, TextType.TEXT))

	if middle:
		result_nodes.append(TextNode(middle, text_type))

	# process "after" recursively if it exists
	if after:
		if after.find(delimiter) == -1:
			result_nodes.append(TextNode(after, TextType.TEXT))
		else:
			after_nodes = process_text_node(TextNode(after, TextType.TEXT), delimiter, text_type)
			result_nodes.extend(after_nodes)

	return result_nodes




#
# node = TextNode("This is text with a `code block` word.", TextType.TEXT)
# print(split_nodes_delimiter([node], "`", TextType.CODE))
