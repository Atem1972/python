
#****Number 
a= 20
b= 2.4
c= 3+7j

#Arithmetic operators are for number ( + , - , /, *. ** , %, //)
# ***String
s='serge'
la= "smith brown"
_s = """I am learning python"""

#String methods len(), .upper(), .lower(), .isdigit(), .isalpha(), .stip(), .title() and more 
#String indexing and slicing 
# String concatenation
# Membership operator  in, not in,
'a' in 'serge'
'@' not in 'kserge@gmail.com'

'ellys' in ['serge','john','smith','jude']
#Boolean
is_student=True
is_current=False

#List []
courses = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]

#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(), .count()

#Tuple () Tuples in Python are immutable sequences, which means their elements cannot be changed or modified after the tuple is created
t=(2,4,6,True)
#tuple methods .count(), index()

#set {} Sets in Python are unordered collections of unique elements
s_set={2 ,2 ,3 ,4 ,5 , True}

#set methods add(), update(), remove(), pop(), clear(), discard()

#Dictionary {} Dictionaries in Python are a collection of key-value pairs. They are highly flexible and WIDELY used for data manipulation
d={'name':'Serge', 'age': 30, 'profession': 'DevOps Engineer', 'courses':['aws','linux','terraform']}

#Dict methods .clear(), .copy(), .get() items(), keys(), values(), pop(), popitem(), update(dict), del(dict[key])

#give the list of string 'aws','terraform','python', write a program that will generate a list of this items upper letters

  #how to create virtual env in python
 #  pip install virtualenv # to install
# python -m venv myenv # to rename env
#source myenv/Scripts/activate # to activate in windows
 #source myenv/bin/activate # to activate in mac or linux

 
"""***Project: 
          1- AT work,we have many jenkins servers and there is a need to inventory those servers. it is a 
          Stedious task to manually go in jenkins and count the jobs, and the vcs link associated
          to each of them. go ahead and propose a solution for this.
          jenkins url: 'http://54.237.237.41:8080'
          jenkins username: 'devops'
          jenkins password: 'devops'"""