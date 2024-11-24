text = 111 * '1'
while '11111' in text:
   text = text.replace('111', '2', 1)
   text = text.replace('222', '3', 1)
   text = text.replace('333', '1', 1)

print(text)