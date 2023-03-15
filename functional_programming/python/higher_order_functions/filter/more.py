"""removes vowels from a string """

string = "the quick brown fox over the lazy dog"
vowel = ["a", "e", "i", "o", "u"]
def disemvowel(s):
    return filter(lambda x: x not in vowel, s)
print("".join(disemvowel(string)))