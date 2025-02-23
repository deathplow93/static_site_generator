from textnode import TextNode, TextType

def main():
    node = TextNode("hewwo", TextType.BOLD, "ass.com")
    print(node)

if __name__ == "__main__":
    main()