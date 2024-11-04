'''
Lambda function = a smalll anonymous function fo a one time use (throw away function)

    They take any number of arguments, but have only 1 expression.
    Helps keep the namespace clean and is useful with higher order functions:

    'sort()', 'map()', 'filter()', 'reduce()' etc.
    lamda parameters: expression
'''

### SYNTAX:

def add(x,y):
    return(x+y)

print(add(2,3))

# powyższa funckcja, odpowiada poniższej:
add2 = lambda x,y: x+y
print(add2(2,3))

# inne zastosowanie:
print((lambda x,y: x+y)(4,5))


### inny przykład

double = lambda x: x*2

print(double(5))