def reverse_string(text):
    if len(text) <= 1:
        return text
    # if len(text)>= 2:
    return reverse_string(text[1:]) + text[0]
text = 'catttttedede'
result = reverse_string(text)
print(result)