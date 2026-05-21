def convert(text):
    return text.replace(":)" , "🙂").replace(":(" , "🙁")


def main():
    name = input()
    result = convert(name)
    print(result)




main()
