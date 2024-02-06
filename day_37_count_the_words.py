# Day 37: Count the Vowels

def count_the_words(str):
    vowels = {"a": False, "e": False, "i": False, "o": False, "u": False}
    vowel_count = 0

    for char in str:
        if char.lower() in vowels and not vowels[char.lower()]:
            vowels[char.lower()] = True
            vowel_count += 1
            return vowel_count
        else:
            return "The string has no vowels"
    
print(count_the_words("sly"))