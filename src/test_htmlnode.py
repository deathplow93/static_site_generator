import unittest
from htmlnode import HtmlNode
from test_data import *



class TestTextNode(unittest.TestCase):
    
    def test_prop(self):
        prop_test = {"href": "https://www.google.com", "target": "_blank"}
        expected_prop = " href=\"https://www.google.com\" target=\"_blank\""
        hnode = HtmlNode(props=prop_test)
        prop_mod = hnode.props_to_html()
        self.assertEqual(prop_mod, expected_prop)

    def test_no_prop(self):
        prop_test = None
        expected_prop = None
        hnode = HtmlNode(props=prop_test)
        prop_mod = hnode.props_to_html()
        self.assertEqual(prop_mod, expected_prop)




if __name__ == "__main__":
    unittest.main()
