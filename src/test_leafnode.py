import unittest
from leafnode import LeafNode
from test_data import *

value_text = test_text

class TestLeafNode(unittest.TestCase):
    
    def test_eq(self):
        for item in test_text:
            for type in test_text_type:
                for url in test_urls:
                    node = LeafNode(item, type, url)
                    node2 = LeafNode(item, type, url)
                    self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
