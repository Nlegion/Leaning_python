fruits1 = ['apple','banana','orange','kiwi','pear']
fruits2 = ['banana','kiwi','tangerine']

result = []

for fruits in fruits1:
   if fruits in fruits2:
       result.append(fruits)
print(result)

result = [fruits for fruits in fruits1 if fruits in fruits2]
print(result)