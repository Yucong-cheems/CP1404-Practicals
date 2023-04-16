"""
word_occurrences
Estimate: 10 minutes
Actual:   15 minutes
"""
# thing, width, other_thing = "first", 13, "second"
# print(f"{thing:{width}} = {other_thing}")

text = input("Text: ")
while text != " ":
    words = text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(word, ":", count)

    text = input("Text: ")



