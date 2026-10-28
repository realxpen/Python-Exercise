# numbers = input().split()

# num_list = []

# for n in numbers:
#     num_list.append(int(n))

# print(num_list)

# if not num_list:
#     print("The list is empty.")
# else:
#     target = int(input("Input your Target!: "))
#     found = False
#     for index in range(len(num_list)):
#         if num_list[index] == target:
#             print(f'Target {target} is found at {index}')
#             found = True
#             break

#     if not found:
#         print(f'Target {target} is not found')
    
name = 'Ayomide'
age = 18
if age >= 18:
    result = f'{name} is eligible to vote!'
else:
    result = f'{name} is not old enough to vote yet.'
print(result) 

if es