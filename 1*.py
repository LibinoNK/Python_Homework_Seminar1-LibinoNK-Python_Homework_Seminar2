# *** (1)У вас есть массив чисел, составьте из них максимальное число. Например:
# [61, 228, 9] -> 961228

list = [61, 228, 9]

def make_max_number(list):
    for i in range(0, len(list)):
        list[i] = str(list[i])
print(list)

for j in range(0, len(list)-1):
    for x in range(1, len(list)):
        if int(list[j][0]) < int(list[x][0]):
            temp = list[j]
            list[j] = list[x]
            list[x] = temp
print(list)

result = ""
for k in range(0, len(list)):
    result = result + list[k]
print(result)

make_max_number(list)
