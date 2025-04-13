# from .textnode import TextNode, TextType
from .parentnode import ParentNode

# from .htmlnode import HtmlNode
from .leafnode import LeafNode


def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    node.to_html()


if __name__ == "__main__":
    main()
