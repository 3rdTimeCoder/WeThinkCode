
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """Coverts given text into a list, spliting on delimiters"""
    delimiters = ['.', ' ', ',', ';', '?']
    return [word.lower() for word in split(delimiters, text) if word]
    

def words_longer_than(length, text):
    """Returns a list of words in text that are longer than given length"""
    return [word for word in convert_to_word_list(text) if len(word) > length]


def words_lengths_map(text):
    """Returns a dictionary of words in texts and their number of occurrences."""
    l = convert_to_word_list(text)
    word_lengths = [len(word) for word in l]
    return {word_len : word_lengths.count(word_len) for word_len in word_lengths}
    

def letters_count_map(text):
    """Returns a dictionary of how many times each letter appears in text"""
    delimiters = ['.', ' ', ',', ';', '?']
    char_list = [char.lower() for char in list(text) if char not in delimiters]
    return {char : char_list.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'}


def most_used_character(text):
    """Returns the most used character in text"""
    if not text: return None
    letter_count = letters_count_map(text)
    leter_count_inversed = {value:key for key,value in letter_count.items()}
    return leter_count_inversed[max(letter_count.values())]


if __name__ == '__main__':
    print(convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(most_used_character('These are indeed interesting, an obvious understatement, times. What say you?'))


# This code is O(n2) complexity, figure out why and then try make it O(logn).