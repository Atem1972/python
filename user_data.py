Name= input("what is your name?")
print(Name)

if len(Name) < 3:
    print("Name too short")
else:
    print("complete")    
Email= input("what is your email addres?")
print(Email)

if "@" in (Email):
    print("success")
else:
    print("in complete email")


    