import unittest
import random
from src.textnode import TextNode, TextType
from src.textnode_html import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_random_types(self):
        base_text = "This is a text node"
        base_url = "http://example.com"
        all_types = list(TextType)
        random.seed(42)  # For reproducibility

        # Test equality with same values
        base_type = random.choice(all_types)
        base_node = TextNode(base_text, base_type, base_url)
        same_node = TextNode(base_text, base_type, base_url)
        self.assertEqual(base_node, same_node)

        # Test inequality with different types
        for t in all_types:
            if t != base_type:
                diff_node = TextNode(base_text, t, base_url)
                self.assertNotEqual(base_node, diff_node)

        # Test inequality with different text/url
        self.assertNotEqual(base_node, TextNode("Different text", base_type, base_url))
        self.assertNotEqual(
            base_node, TextNode(base_text, base_type, "http://different.com")
        )

    def test_repr_special_chars(self):
        test_cases = [
            (
                "hello",
                TextType.NORMAL,
                "bj.com",
                "TextNode('hello', 'normal', 'bj.com')",
            ),
            ("", TextType.BOLD, None, "TextNode('', 'bold', None)"),
            (
                "$$$$",
                TextType.CODE,
                "example.com",
                "TextNode('$$$$', 'code', 'example.com')",
            ),
        ]

        for text, text_type, url, expected in test_cases:
            with self.subTest(text=text, text_type=text_type, url=url):
                obj = TextNode(text, text_type, url)
                self.assertEqual(repr(obj), expected)

        def test_text_type_validation(self):
            with self.assertRaises(AttributeError):
                # This should fail because we're passing a string instead of TextType
                TextNode("test", "invalid_type", None)


if __name__ == "__main__":
    unittest.main()
