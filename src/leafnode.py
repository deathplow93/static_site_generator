from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self,value,tag=None,props=None):
        super().__init__(tag,props,value)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HtmlNode({self.value},{self.tag},{self.props})"
    
    def __eq__(self, other):
        if (
            self.tag == other.tag
            and self.props == other.props
            and self.value == other.value
        ):
            return True
        else:
            return False