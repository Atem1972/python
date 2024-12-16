"""try:
    print(a)
except:
    print("error")"""

    #error message and explanation

"""try:
    print(a)
except Exception as e:
    print(f'Error: {e}') """


try:
    print('a')
except NameError:
    print('Error: variable a not define')    
else:
    print("no error")    
finally:  
    print('always')  
