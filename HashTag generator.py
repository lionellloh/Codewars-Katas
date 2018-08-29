def generate_hashtag(s):
    print(s)
    if s.strip() == "":
        return False
    list_of_words = s.strip().split(" ")
    list_of_words = [word.lower() for word in list_of_words]
    for i in range(len(list_of_words)):
        try:
            list_of_words[i] = list_of_words[i][0].upper() + list_of_words[i][1:]

        except:
            pass

    output = "#" + "".join(list_of_words)
    if len(output) > 140:
        return False
    return output


print(generate_hashtag("Hello there thanks for trying my kata"))