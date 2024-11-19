#creating a custom iterlator
class Pow_of_Two:
	'''class to implement an ierlator
	of powers of two'''
	def __init__(self, max = 0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
		else:
		    raise StopIteration

print(Pow_of_Two.__doc__)
a = Pow_of_Two(4)
i = iter(a)
print((i.__next__())) 
print(next(i))
print(next(i))