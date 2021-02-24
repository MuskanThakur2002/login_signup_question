user=input("You wants to 1.signup or 2.login")
if user=="1":
    user_name=input("enter user name")
    import json
    j=open("userdetails.json","r")
    j.seek(0)
    n=j.read()
    if user_name in n:
        print("user_name already exists")
    else:
        password_1=input("enter password")
        if "#" in password_1 or "@" in password_1 :
            password_2=input("enter password again")
            if password_1==password_2:
                #k={"user": [{user_name : password_1}]}
                # import json
                # f=open("userdetails.json", "a")
                # m=json.dumps(k)
                # f.write(m)
                # f.close()
                print("Congrats", user_name, "you are signed up success fully")
                Discription=input("Discription : ")
                DOB=input("Date of Birth : ")
                Hobbie=input("Hobbie : ")
                Gender=input("Gender Male/Female : ")
                t={"User" : {"username" : user_name, "Password": password_1, "Profile" : {"Discription" : Discription , "DOB":DOB, "Hobbie": Hobbie , "Gender": Gender}}}
                import json
                f=open("userdetails.json", "a")
                a=json.dumps(t)
                f.write(a)
                print()
                print(a)
                f.close()
            else:
                print("wrong password")
        else:
            print("Atleast Password should contain one special character and one number")
            print("Write answer properly")
elif user=="2":
    user_name=input("enter user name")
    password=input("enter password")
    import json
    m=open("userdetails.json","r")
    m.seek(0)
    l=m.read()
    if user_name in l:
        if password in l:
            print("login successfully")
            import json
            with open("userdetails.json") as data_file:    
                data = json.load(data_file)
                users = data['User']
                for user in users:
                    count=0
                    print ("users full name and password is ", users["username"] , users["Password"])
                while count<1:
                    print("profile")
                    print("Discription : ", users["Profile"]["Discription"])
                    print("DOB : ", users["Profile"]["DOB"])
                    print("Hobbie : ", users["Profile"]["Hobbie"])
                    print("Gender : ", users["Profile"]["Gender"])
                    count+=1
        else:
            print("password is incorrect")
    else:
        print("invalid User_Name")




definations
variable
conversion
operator
if/else
nested if 
while Loop
nested while Loop
list
tuple
array
dictionary
set
function
json
file
hangman
