import re

def word_count(s):
    # Your code here
    cache = {}
    lower = s.lower() #lowercase the string
    #remove specified characters
    stringo = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&]', '', lower)

    words = stringo.split() #create an array of individual words

    for word in words:
        key = word
        if key not in cache:
            cache[key] = 1
        else:
            cache[key] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))