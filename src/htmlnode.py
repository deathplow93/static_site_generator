class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        empty_list = []
        for key, value in self.props.items():
            html_convert = f"{key}" + "=" + f"\042{value}\042"
            empty_list.append(html_convert)
            html_out = " ".join(empty_list)
        return html_out

    def __repr__(self):
        return f"HtmlNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"


# Debug for checking if works
def main():
    stuff = {
        "href": "https://www.google.com",
        "target": "_blank",
    }

    h_node = HtmlNode(props=stuff)
    print(h_node)
    print_props = h_node.props_to_html()

    print(print_props)


if __name__ == "__main__":
    main()
