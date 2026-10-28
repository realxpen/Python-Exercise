# d = {"name": "John", "age": 30, "city": "New York"}

# for x, y in d.items():
    
#     print(x, y)

# # print(d["name"])

# d = {"name": "John", "age": 30, "city": "New York"}

# # Slice the first two items (index 0 and 1)
# for x, y in list(d.items())[0:2]:
#     print(x, y)


# age = 18
# if age > 18:
#   print("Adult")
#   if age > 65:
#     print("Senior")
#   else:
#     print("Working age")



# networkResult = '200'
# match networkResult:
#     case '200':
#         print("Success")
#         if networkResult == '200':
#             print("Everything is OK")
#     case _:
#         print("Error")


# import random
# langs = ["French", "Spanish"]
# result = random.choices(
#     langs,
#     weights=[1, 4],
#     k=3
# )
# print(len(result))


# import random
# vowels = ["a", "e", "i", "o", "u"]
# consonants = ["b", "c", "d", "f"]
# v = random.choice(vowels)
# c = random.choices(consonants, k=2)

# word = v + ''.join(c)
# print(word)



try:
  print(hello)
except:
  print("hello is not a variable")
