from .htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props

        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        props_html = ""

        if self.props:
            props_html = " " + self.props_to_html()
        if self.tag is None or self.tag == "" or self.tag == " ":
            return self.value

        if self.value is None:
            raise ValueError("Value is empty")

        if self.props is None or self.tag == "" or self.tag == " ":
            if self.tag == "a":
                return f"<{self.tag}{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            if self.tag == "a":
                return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{props_html}{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HtmlNode(tag='{self.tag}',value='{self.value}', props={self.props})"


# Debug for checking if works
def main():
    # Debug for checking if works
    tag = "a"
    value = "Click me!"
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    h_node = LeafNode(tag, value, props)
    # print(h_node)
    print_to_html = h_node.to_html()

    print(print_to_html)


if __name__ == "__main__":
    main()
