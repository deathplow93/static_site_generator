from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self,value,tag=None,props=None):
        super().__init__(tag,props,value)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag == None:
            return self.value