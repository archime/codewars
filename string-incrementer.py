"""
String Incrementer
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number the number 1 should be appended to the new string.
"""

def increment_string(string):
    if len(string) == 0 or string[-1] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        return string[:] + "1"
    else:
        append_list = []
        for letter in string:
            if letter in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                append_list.append(letter)
            else:
                append_list = []
    end_string = str(int("".join(append_list)) + 1)
    return string[:-len(append_list)] + "0" * (len(append_list) - len(end_string)) + end_string

# Tests
print(increment_string("123amb2")) # Expect "123amb3"
print(increment_string("123amb0")) # Expect "123amb1"
print(increment_string("123amb")) # Expect "123amb1"
print(increment_string("123amb09")) # Expect "123amb10"
print(increment_string("123amb9")) # Expect "123amb10"
print(increment_string("foobar001")) # Expect "foobar002"