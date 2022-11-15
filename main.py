from linear_algebra import Vector

foo = Vector([1,2,3])
bar = Vector([4,5,6])
baz = foo + bar
#baz.scale(3)
print(baz)
print(baz - bar)

boom = Vector.vector_sum([Vector([1,2,3]),Vector([1,2,3]),Vector([1,2,3])])
print(boom)

