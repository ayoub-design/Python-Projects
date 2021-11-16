
# declarations des functions des operations
def add (x,y):
    result = x + y
    return result

def sub (x,y):
    result = x - y
    return result

def mult (x,y):
    result = x * y
    return  result

def div (x,y):
    result = x / y
    return  result

# la saisie des variables
while True:
 x = int(input('enter the first number = '))
 y = int(input('enter the second number = '))
 print('this are the following operator : ADD , SUB  , MULT , DIV ')

 operator = str(input('choose your operator : '))

# les conditions
 if operator == "ADD" or operator == "add":
         print(add(x,y))

 elif operator == 'SUB' or operator == 'sub':
          print(sub(x,y))

 elif operator == 'MULT' or operator == 'mult':
           print(mult(x,y))

 elif operator == 'DIV' or operator == 'div':
           print(div(x,y))
 else:
            print(" please choose the correct form of operator")
 
 answer = str(input('you wanna start new operation? '))
 if answer == 'no' or answer == 'NO':
     break

