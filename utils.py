def countSpaces(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count