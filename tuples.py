# Creating an empty tuple
tuple1 = ()
print(tuple1)

# Creating tuples with integer elements
tuple2 = (1, 2, 3)
print(tuple2)

# Tuples with mixed datatypes
tuple3 = (100, "airbnb", 200.00, "HR Dept")
print(tuple3)

# creation of nested Tuple
tuple4 = ("points", [1,3,4], (5,6,7))
print(tuple4)
print(tuple4[0][3])
print(tuple3[:-4])
print(tuple2.index(1))
print('a' not in tuple2)
print(reversed(tuple2))