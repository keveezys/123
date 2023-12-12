while 1:
    N = input('Введите число N ')
    flag = True
    for i in N:
        if i in '1234567890':
            flag = False
            continue
        else:
            print(' ')
            break
    if int(N) <= 0:print("Введите N больше нуля")
    elif not flag and int(N) > 0:
        break
print(N)
while 1:
    K = input('Введите число K ')
    flag = True
    for i in K:
        if i in '1234567890':
            flag = False
            continue
        else:
            print(' ')
            break
    if int(N) < int(K):print('Введите K меньше, чем N')
    elif int(K) <= 0:print("Введите K больше нуля")
    elif not flag and 0 < int(K) <= int(N):
        break
print(K)
pupa = 1
lupa = 1
sorry = 1
for i in range(1, int(N)+1):
    pupa = pupa * i
for i in range(1, int(K)+1):
    lupa = lupa * i
for i in range(1, int(N)-int(K)+1):
    sorry = sorry * i
print(pupa/(lupa*sorry))