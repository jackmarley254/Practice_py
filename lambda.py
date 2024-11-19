a = lambda x:x*2

print("Double of 10 is", a(10))

my_list = [1, 5, 4, 6, 8]
new_list = list(filter(lambda x: (x%2 ==0) , my_list))

print(new_list)