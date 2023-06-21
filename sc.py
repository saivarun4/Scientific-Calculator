import math
def add( num1 , num2 ):
  return num1 + num2

def subtract( num1 , num2 ):
  return num1 - num2

def multiply( num1 , num2 ):
  return num1 * num2

def decimal_division( num1 , num2 ):
  return num1 /  num2

def integer_division( num1 , num2 ):
  return num1 // num2

def remainder( num1 , num2 ):
  return num1 % num2

def square( num1 ):
  return num1 ** 2

def cube( num1 ):
  return num1 ** 3

def square_root( num1 ):
  return num1 ** 0.5

def cube_root( num1 ):
  return num1 ** 0.33

def power( num1  , power ):
  return math.pow( num1 , power )

def log( num1 ):
  return math.log( num1 )

def log_base( num1  , base ):
  return math.log( num1  , base )

def sin( num1 ):
  return math.sin( num1 )

def cos( num1 ):
  return math.cos( num1 )

def tan( num1 ):
  return math.tan( num1 )


while True:
    print( '***********************************************************************\n\n' )
    print( 'Enter the operation to perform\n',
                  '1. Add\n' ,
                  '2. Subtract\n' ,
                  '3. Multiply\n' ,
                  '4. Division\n' ,
                  '5. Interger Division\n' ,
                  '6. Remainder\n' ,
                  '7. Square\n'  ,
                  '8. Cube\n' ,
                  '9. Square Root\n' ,
                  '10. Cube Root\n' ,
                  '11. Power value\n'
                  ' 12. Log value\n'  ,
                  '13. Log with base value\n' ,
                  '14. Sin value\n' ,
                  '15. Cos value\n' ,
                  '16. Tan value\n' ,
                  '17. Exit\n\n\n')
    try:
        choice = int(input( 'Enter the operation no to perform:' ))
        print( '\n' )
    except ValueError:
        print( 'Invalid choice !!! \nType only integers !\n' )
        continue
    if choice == 1:
        num1 = float( input( 'Enter the number to be added: ' ) )
        num2 = float( input( 'Enter the number to be added: ' ) )
        print( 'Result: ' , add( num1 , num2 ) )
        print( '\n' )
    elif choice == 2:
        num1 = float( input( 'Enter the number to be subtracted: ' ) )
        num2 = float( input( 'Enter the number to be subtracted: ' ) )
        print( 'Result: ' , subtract( num1 , num2 ) )
        print( '\n' )
    elif choice == 3:
        num1 = float( input( 'Enter the number to be multiplied: ' ) )
        num2 = float( input( 'Enter the number to be multiplied: ' ) )
        print( 'Result: ' , multiply( num1 , num2 ) )
        print( '\n' )
    elif choice == 4:
        num1 = float( input( 'Enter the number to be divided: ' ) )
        num2 = float( input( 'Enter the number to be divided: ' ) )
        print( 'Result: ' , decimal_division( num1 , num2 ) )
        print( '\n' )
    elif choice == 5:
        num1 = float( input( 'Enter the number to be divided: ' ) )
        num2 = float( input( 'Enter the number to be divided: ' ) )
        print( 'Result: ' , integer_division( num1 , num2 ) )
        print( '\n' )
    elif choice == 6:
        num1 = float( input( 'Enter the number to be divided: ' ) )
        num2 = float( input( 'Enter the number to be divided: ' ) )
        print( 'Result: ' , remainder( num1 , num2 ) )
        print( '\n' )
    elif choice == 7:
        num1 = float( input( 'Enter the number to be squared: ' ) )
        print( 'Result: ' , square( num1 ) )
        print( '\n' )
    elif choice == 8:
        num1 = float( input( 'Enter the number to be powered: ' ) )
        print( 'Result: ' , cube( num1 ) )
        print( '\n' )
    elif choice == 9:
        num1 = float( input( 'Enter the number to have square root: ' ) )
        print( 'Result: ' , square_root( num1 ) )
        print( '\n' )
    elif choice == 10:
        num1 = float( input( 'Enter the number to have cube root: ' ) )
        print( 'Result: ' , cube_root( num1 ) )
        print( '\n' )
    elif choice == 11:
        num1 = float( input( 'Enter the number: ' ) )
        num2 = float( input( 'Enter the power: ' ) )
        print( 'Result: ' , power( num1  , num2  ) )
        print( '\n' )
    elif choice == 12:
        num1 = float( input( 'Enter the number: ' ) )
        print( 'Result: ' , log( num1  , num2  ) )
        print( '\n' )
    elif choice == 13:
        num1 = float( input( 'Enter the number: ' ) )
        num2 = float( input( 'Enter the base: ' ) )
        print( 'Result: ' , log_base( num1  , num2  ) )
        print( '\n' )
    elif choice == 14:
        num1 = float( input( 'Enter the angle( radians ): ' ) )
        print( 'Result: ' , sin( num1 ) )
        print( '\n' )
    elif choice == 15:
        num1 = float( input( 'Enter the angle( radians ): ' ) )
        print( 'Result: ' , cos( num1 ) )
        print( '\n' )
    elif choice == 16:
        num1 = float( input( 'Enter the angle( radians ): ' ) )
        print( 'Result: ' , tan( num1 ) )
        print( '\n' )
    elif choice == 17:
        print( '\n\n\nPOWER OFF !!!' )
        break
    else:
        print( 'Invalid choice !!!\nType btw 1 to 17 !' )
print( '\n\n*******************************************************************' )
