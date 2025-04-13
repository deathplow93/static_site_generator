from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, others):
        return (
            self.text == others.text
            and self.text_type == others.text_type
            and self.url == others.url
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"


Test1 = TextNode("hewwo", "bold", "ass.com")
print(Test1)


def text_node_to_html_node(text_node):
    pass


# LeafNode(tag, value, props)

# Debug for checking if works
# Test1 = TestNode("hewwo", "bold", "ass.com")
# # Test2 = TestNode("hewwo", "bold", "ass.com")
# print(Test1)
# print(Test1==Test2)
