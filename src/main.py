from textnode import TextNode, TextType


def main():
    text_test_1 = TextNode("trtrt", TextType.ITALIC, "http://wowow.com")
    text_test_2 = TextNode("wwrwrwr", TextType.ITALIC, "http://monkey.com")
    print(text_test_1)


if __name__ == "__main__":
    main()
