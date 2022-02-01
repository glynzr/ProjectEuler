#sum square difference
a=sum(x for x in range(1,101))**2
print(a)
b=sum(x**2 for x in range(1,101))
print(b)
print(a-b)

#self power
a=lambda x : x**x
summ=0
for x in range(1,11):
      summ+=a(x)
print(summ)
