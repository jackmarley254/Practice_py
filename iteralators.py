our_list = [44, 77, 33, 49, 56]
#get an iteralator using iter() method
our_iter = iter(our_list)

print(next(our_iter))

print(next(our_iter))

print(next(our_iter))

print(our_iter.__next__())

print(next(our_iter))