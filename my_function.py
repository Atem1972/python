"""def hello():
    print("hello")
#hello() # this will print out the function hello above

def display_name(name):
    print(f"hello {name}")
#display_name('serge')    

def addition(a,b):
    sum = a + b
    print(sum)
#addition(2,4) or
x=addition(2,4) 
print(x)

  #another way to use print
def addition1(a,b):
    sum = a - b
    return sum
#addition(2,4) or
x=addition1(2,4) 
print(x)
# how to stop third party from executing a particula functiom
if __name__ == '__main__':
 my_value = addition1(2, 7)
print(my_value)


def command(cmd):
    import os
    os.system(cmd)

# Call separately for each command
command('ls')  # Lists files in the current directory
command('pwd')  # Prints the current working directory
# OR

def command(*cmds):
    
    
    
    import os
    for cmd in cmds:
        os.system(cmd)

# Call with multiple commands
command('ls', 'pwd')"""


def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))








  