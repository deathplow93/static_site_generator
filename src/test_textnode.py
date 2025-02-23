import unittest
import random
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_random_types(self):
        base_text = "This is a text node"
        base_url = "http://example.com"
        all_types = list(TextType)
        # Optionally set a seed for reproducibility:
        random.seed(42)
        
        # Choose a random base type
        base_type = random.choice(all_types)
        base_node = TextNode(base_text, base_type, base_url)
        
        # Check equality or inequality based on the text type
        for t in all_types:
            node = TextNode(base_text, t, base_url)
            if t == base_type:
                self.assertEqual(base_node, node,
                                 f"Nodes with type {t} should be equal")
            else:
                self.assertNotEqual(base_node, node,
                                    f"Nodes with type {t} should not be equal")
    def test_repr_special_chars(self):
        test_list = ["hello", "", "$$$$"]
        for test in test_list:
            with self.subTest(test_case=test):
                obj = TextNode(test,TextType("normal"),"bj.com")
                expected = f"TextNode({test}, normal, bj.com)"
                self.assertEqual(repr(obj),expected)


if __name__ == "__main__":
    unittest.main()
