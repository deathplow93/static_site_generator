


class HtmlNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_self(self):
        raise NotImplementedError
    def props_to_html(self):
        for key, value in prop_dict.items():
            html_string =
            print(f"{key} {value}")
        # for value in self.props:
             
        return "you did its"
        
    def __repr__(self):
        # return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"
        pass
# Debug for checking if works
prop_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}
node = HtmlNode(props=prop_dict)

Test1 = node.props_to_html()
# Test2 = HtmlNode()
print(Test1)
# print(Test1==Test2)
