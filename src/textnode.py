from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"


# text_enum = TextType("text")
# test_1 = TextNode("trtrt", TextType.ITALIC, "http://wowow.com")
# test_2 = TextNode("wwrwrwr", TextType.ITALIC, "http://monkey.com")

# print(text_enum)
# print(test_1)

# print(test_1 == test_2)
