def count_substring(string, sub_string):
    c = 0
    # string = input().strip()
    # sub_string = input().strip()
    # print(string.find(sub_string))
    for i in range(len(string)):
        if string.startswith(sub_string, i) == True:
            c = c + 1

    return c