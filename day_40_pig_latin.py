# Day 40: Pig Latin

def translate(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    new_words = []

    for word in words:
        if word[0] in vowels:
            new_word = f"{word}yay"
        else:
            first_letter = word[0]
            rest_of_word = word[1:]
            new_word = f"{rest_of_word}{first_letter}ay"
        
        new_words.append(new_word)
    
    return ' '.join(new_words)

my_string = 'i love python'

print(translate(my_string))
