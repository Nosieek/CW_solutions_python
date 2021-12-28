def data_reverse(data):
    y = len(data)
    x = y-8
    new_data = []
    for q in range(len(data)//8):
        for i in data[x:y]:
            new_data.append(i)
        y = x
        x -= 8
    return new_data




data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

print(data_reverse(data1) ==data2)

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
print(data_reverse(data3) == data4)