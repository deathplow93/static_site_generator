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
        if not self.props :
            return None
        else:
            for key, value in self.props.items():
                html_list.append(f' {key}="{value}"')
            appended_list = "".join(html_list)
            return appended_list

    def __repr__(self):
        return f"HtmlNode({self.tag},{self.value},{self.children},{self.props})"


# hnode_test = HtmlNode(props=prop_test)
# print(hnode_test.props_to_html())
