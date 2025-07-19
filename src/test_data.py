from textnode import TextNode, TextType
import random

//text
test_text = ["$!@#$@$", "peee", "doodoo", "-------------", "/////////"]

//text types
test_text_type = [
    TextType.BOLD,
    TextType.ITALIC,
    TextType.TEXT,
    TextType.IMAGE,
    TextType.LINK,
    TextType.CODE,
]
test_text_type_2 = [
    TextType.IMAGE,
    TextType.BOLD,
    TextType.CODE,
    TextType.ITALIC,
    TextType.LINK,
    TextType.TEXT,
]
//URLS
test_urls = ["https://bigdogwoof.com", "test.com", "letthebigdogshuntowww"]

none_list = [None]
rand_num = random.randint(1, 10)