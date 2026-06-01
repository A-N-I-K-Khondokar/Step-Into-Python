#conditional statement
num=int(input('Enter a number: '))
if num==0:
    print(f"Zero {num}")
elif num>0:    
    print(f"Positive {num}")
else:    
    print(f"Negative {num}")   

#for loop
# for index_Value  in iterator:
#     ->do something
print("First way....")
score=[23,45,34,56,787,77,345]
for i in [1,2,3,4]:
    print(f"Score is = {score[i]}")
print("\n")


#range() is a function
#range(start,end,stepsize)
#Another way:
print("Second way..")
for i in range(0,len(score), 2):
    print(f"Values : {score[i]}")
print('\n')

#Another way:
print("Third way..")
for num in score:
    print(num)

## iterator and iterable
print("\niterator and iterable..")
numbers=[12,34,56,78,45]
i=iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print("\n Enumerate in loops it needed in cross validation..")
for index,value in enumerate(numbers):
    print(index,value)


