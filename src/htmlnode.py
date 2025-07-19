prop_test = {"href": "https://www.google.com", "target": "_blank"}


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_list = []
        for key, value in self.props.items():
            html_list.append(f' {key}="{value}"')
        appended_list = "".join(html_list)
        return appended_list


hnode_test = HtmlNode(props=prop_test)
print(hnode_test.props_to_html())
