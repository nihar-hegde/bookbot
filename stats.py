def count_wrords(text):
    words = text.split()
    return len(words)

def no_of_charecters(text):
    chars = list(text)
    char_dict = {}
    for char in chars:
        word = char.lower()
        if word in char_dict:
            char_dict[word] += 1
        else:
            char_dict[word] = 1
    return char_dict


def sort_dir(char_dict):
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict