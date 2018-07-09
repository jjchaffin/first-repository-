def isDigit(string):
    for character in string:
        character.isdigit()
        # print(character + ": " + str(character.isdigit()))

        if character.isdigit() or character==" " or character=="-" or character==".":
            return True

    return False

tests = [
    "0",
    "3",
    "   3   ",
    "-3.23"
]

for test in tests:
    print("result for " + test + ": " + str(isDigit(test)))
