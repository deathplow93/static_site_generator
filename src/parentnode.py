from .htmlnode import HtmlNode

# from .leafnode import LeafNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.props = props
        self.children = children

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        props_html = ""

        if self.props:
            props_html = " " + self.props_to_html()
        if self.tag is None or self.tag == "" or self.tag == " ":
            raise ValueError("Missing Tag ParentNode.py")
        if self.children is None or self.children == "" or self.children == " ":
            raise ValueError("Missing Children Parentnode.py")
        else:
            children_html = ""
            for child_node in self.children:
                if hasattr(child_node, "to_html"):
                    # print(child_node)
                    children_html += child_node.to_html()
                    # print(f"printing children_html:{children_html}")
                else:
                    raise ValueError(f"Invalid child type: {type(child_node)}")
        return f"<{self.tag}>{props_html}{children_html}</{self.tag}>"


# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# p_node = node.to_html()
# print(p_node)
