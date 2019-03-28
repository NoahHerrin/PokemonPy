# adds padding to right of string until it is desired length
def add_padding_right(str,new_len):
    for counter in range(len(str), new_len):
        str += " "
    return str
# adds padding to left of string until it is desired length
def add_padding_left(str,new_len):
    for counter in range(len(str), new_len):
        str = " " + str
    return str
# given a list of words it will return the length of the longest
def get_max_len(words):
    if len(words) != 0:
        largest = len(words[0])
        for index in range(1, len(words)):
            if len(words[i]) > largest:
                largest = len(words[i])

        return largest + 1
