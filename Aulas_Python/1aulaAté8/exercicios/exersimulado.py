# numero = 5
# for n in range(0,10):
#     print(numero,'X',n, '=',numero*n)

x = 9

def func_1(y):
    x = 3 + y
    return x

def func_2(y):
    global x
    x -= y

x = func_1(2)
func_2(5)
print(x)