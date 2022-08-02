from numpy import prod

x = max(5, 8, 9, 10, 50)
print(x)



l = sum([10, 20, 30, 40, 50])
print(l)



m = prod([4, 8])
print(m)



range_1 = range(0, 20, 1)
number = int(input('Enter a number : '))
 
if number in range_1 :
    print(number, 'is present in the range.')
else :
    print(number, 'is not present in the range.')



def my_outer_function():
    print("Hello from my outer function")

    def my_inner_function():
        print("Hi there from my inner function!")



my_outer_function()

