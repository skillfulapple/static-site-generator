from textnode import TextType, TextNode


def main():
	example_node = TextNode(
		"Example text.",
		TextType.BOLD,
		"https://example.example"
		)

	print(example_node)


main()
