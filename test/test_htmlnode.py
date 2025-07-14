import unittest
from src.htmlnode import HtmlNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        stuff = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        correct_node = 'href="https://www.google.com" target="_blank"'
        h_node = HtmlNode(props=stuff)
        p_node = h_node.props_to_html()
        self.assertEqual(p_node, correct_node)

    def test_repr_special_chars(self):
        tag = "a"
        value = "Click me"
        children = "None"
        props = {"href": "https://google.com"}
        h_node = HtmlNode(tag, value, children, props)
        expected_repr = "HtmlNode(tag='a', value='Click me', children=None, props={'href': 'https://google.com'})"
        self.assertEqual(repr(h_node), expected_repr)


stuff = {
    "href": "https://www.google.com",
    "target": "_blank",
}
if __name__ == "__main__":
    unittest.main()
