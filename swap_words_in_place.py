def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))


print(reverse_string_words("The quick brown fox jumps over the lazy dog."))