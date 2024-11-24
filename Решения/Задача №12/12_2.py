text = 65 * '5'
while '333' in text or '555' in text:
    if '555' in text:
        text = text.replace('555', '3', 1)
    else:
        text = text.replace('333', '5', 1)

print(text)