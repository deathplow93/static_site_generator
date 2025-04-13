import unittest
from src.leafnode import LeafNode

# from src.htmlnode import HtmlNode


class TestTextNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        print("test_leaf_to_html_p")
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Hello, world!", props)
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Hello, world!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode(None, "Hello, world!", props)
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
