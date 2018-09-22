"""
Title: Simple pig latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
"""

def pig_it(text):
    sentence_list = [word[1:] + word[0] + "ay" if word not in [".", "?", "!"] else word for word in text.split(" ")]
    return " ".join(sentence_list)

# Tests

print(pig_it('Pig latin is cool')) # Expect 'igPay atinlay siay oolcay'
print(pig_it('This is my string')) # Expect 'hisTay siay ymay tringsay'
print(pig_it('Quis custodiet ipsos custodes ?')) # Expect 'uisQay ustodietcay psosiay ustodescay ?'