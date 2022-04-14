from encodings import utf_8


def count_lines(name: str):
    with open(name, encoding='UTF-8') as file:
        # count = 0
        # for line in file.readlines():
        #     count += 1
        return len(file.readlines())

def count_chars(name: str):
    with open(name, encoding='UTF-8') as file:
    #     count = 1
    #     for char in file.read():
    #         count += 1
        return len(file.read())
 
def test(name: str):
    print(count_lines(name))
    print(count_chars(name))

print(__name__)
if __name__ == "__main__":
    test("popularne_slowa.txt")

# with open("popularne_slowa.txt", encoding='UTF-8') as file:
#     print(file.read())
