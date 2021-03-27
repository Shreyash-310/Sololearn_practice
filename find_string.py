def count_substrings(strg, substrg):
    string_size = len(strg)
    substring_size = len(substrg)
    number = 0
    for i in range(0, string_size - substring_size + 1):
        if string[i:i + substring_size] == substrg:
            number += 1
    return number


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substrings(string, sub_string)
    print(count)
