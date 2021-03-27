import textwrap

# method 1
"""def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    return word_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for element in result:
        print(element)"""


# method 2
def wrap(strg, max_length):
    return textwrap.fill(strg, max_length)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

print("Successfully run")
