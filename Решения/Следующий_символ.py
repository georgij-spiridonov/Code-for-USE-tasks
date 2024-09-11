file = open('task.txt')
text = file.read()
count = 0
max_count = 0
for i in range(len(text) - 1):
    if (text[i] in "ABC" and text[i+1] in '123') or (text[i] in "123" and text[i+1] in 'ABC'):
        count += 1
    else:
        max_count = max(max_count, count + 1)
        count = 0
print(max_count)