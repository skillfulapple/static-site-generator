from textnode import TextType, TextNode


def main():
    bootdev_node = TextNode('boot.dev', TextType.LINK, 'https://www.boot.dev')
    print(bootdev_node)


main()
