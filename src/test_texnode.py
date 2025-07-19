import unittest
import random
from textnode import TextNode, TextType

test_text = ["$!@#$@$", "peee", "doodoo", "-------------", "/////////"]
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
test_urls = ["https://bigdogwoof.com", "test.com", "letthebigdogshuntowww"]
none_list = [None]
rand_num = random.randint(1, 10)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        for item in test_text:
            for type in test_text_type:
                for url in test_urls:
                    node = TextNode(item, type, url)
                    node2 = TextNode(item, type, url)
                    self.assertEqual(node, node2)

    def test_neq(self):
        for item in test_text:
            random_item = random.choice(test_text)
            for type in test_text_type_2:
                random_type = random.choice(test_text)
                node = TextNode(random_item, random_type)
                node2 = TextNode(item, type)
                self.assertNotEqual(node, node2)

    def test_url(self):
        url = "helloworld.com"
        node = TextNode("peee", TextType.BOLD, url)
        test_node = TextNode("peee", TextType.BOLD, url)
        self.assertEqual(node, test_node)

    def test_ne_url(self):
        test_url = "helloworld.com"
        node = TextNode("peee", TextType.BOLD, test_url)
        test_node = TextNode("peee", TextType.BOLD, None)
        self.assertNotEqual(node, test_node)


if __name__ == "__main__":
    unittest.main()
