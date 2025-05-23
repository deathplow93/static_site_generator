from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be a TextType enum member")
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
        return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"
