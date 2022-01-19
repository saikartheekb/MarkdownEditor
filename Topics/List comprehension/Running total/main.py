user = input()

user_list = [int(i) for i in user]

count = 0
new_list = []
for i in user_list:
    count += i
    new_list.append(count)
print(new_list)
#

