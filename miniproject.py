# hi

def word_score(word):
    letterPoints = {
    "a":  1,
    "b":  3,
    "c":  3,
    "d":  2,
    "e":  1,
    "f":  4,
    "g":  2,
    "h":  4,
    "i":  1,
    "j":  8,
    "k":  5,
    "l":  1,
    "m":  3,
    "n":  1,
    "o":  1,
    "p":  3,
    "q": 10,
    "r":  1,
    "s":  1,
    "t":  1,
    "u":  1,
    "v":  4,
    "w":  4,
    "x":  8,
    "y":  4,
    "z": 10
}

    word = word.lower()

    word_total = sum((letterPoints[letter] if letter in list(letterPoints) else 0) for letter in word)
        

    return word_total
    
def find_highest_score(text):
    max_word = ""
    max_score = 0
    for word in text:
        if word_score(word) >= max_score:
            max_word = word
            max_score = word_score(word)
    return max_score, max_word

while True:
    text_file_name = input("Enter a file name to find the highest scoring word: ")

    with open(text_file_name, "r") as fh:
        content = fh.read()
        all_words = content.split()

    print(find_highest_score(all_words))





