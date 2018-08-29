# https://www.codewars.com/kata/simple-pig-latin/train/python


def pig_it(sentence):
    new_sentence = []
    for word in sentence.split(" "):
        if word.isalpha():

            new_word = word[1:] + word[0] + "ay"
            new_sentence.append(new_word)

        # punctuation
        else:
            new_sentence.append(word)
    output = " ".join(new_sentence)

    return output



print(pig_it("Hello world !"))