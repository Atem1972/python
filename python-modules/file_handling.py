# how to open a file using python
#1 method
"""f = open('filename', 'w')   #w, r appen, t b

f.close()"""    #OR
                               
 # create file/write a message                              #  #when use W becarefull blc it can over write o text for new text , use A instead to add tex
"""with open('text.txt','w') as f:  # this will create a file called text.txt
    f.write("hello world")  

    # how to add appen on a file, adding a text to a file
with open('text.txt', 'a') as f:
    f.write("\nhello val\n")


with open('text.txt','r') as f:  # read the above content
    content = f.read()  #or f.readline()  or f.readlines()
    print(content)"""

#modules  to manipulate csv file
import csv

with open('jenkins.csv', 'w', newline='') as j:
    pen = csv.writer(j)
    pen.writerow(['USER_NAME', 'PHONE_NUMBER', 'INSTANCE_TYPE', 'REGION'])  # Header row
    pen.writerows([
        ['Alice', '1234567890', 't2.micro', 'us-east-1'],
        ['Bob', '9876543210', 't2.medium', 'us-west-2']
    ])
