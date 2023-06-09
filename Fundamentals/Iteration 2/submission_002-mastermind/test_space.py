import random

# sample = [num for num in range(1, 9)]
# code = random.sample(sample, 4)
# print(code)

# t = [(num) for num in range(1,9)]
# print(t)
# print("2456" in t)
# def r():
#     code = []
#     while len(code) != 4:
#         random_num = str(random.randint(1,8))
#         if random_num not in code:
#             code.append(random_num)
#     # print(code)
#     return code
        

# for i in range(100):
#     print(r())
    
# while True:
#     l = input("enter number: ")
    
#     if l == '4':
#         print("u guessed correct: ")
#         break

x = '12345678'
code = input("Enter code: ")
if code[0] in x and code[1] in x and code[2] in x and code[3] in x:
    print('correct')
else:
    print('incorrect')