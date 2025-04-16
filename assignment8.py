def reverse_string(s):
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest and add the first character at the end
    return reverse_string(s[1:]) + s[0]

# Example 
word = "hello"
reversed_word = reverse_string(word)
print("Original:", word)
print("Reversed:", reversed_word)
