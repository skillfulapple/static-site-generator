import re

from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        i = 0
        split_texts = old_node.text.split(delimiter)
        if len(split_texts) % 2 == 0:
            raise Exception("split_nodes_delimiter():\nunclosed markdown syntax")
        for split_text in split_texts:
            if not split_text:
                i += 1
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(split_text, TextType.TEXT))
            elif i % 2 == 1:
                new_nodes.append(TextNode(split_text, text_type))
            else:
                raise Exception("split_nodes_delimiter():\nsomething mysterious happened!")
            i += 1
            continue
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
