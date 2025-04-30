useraction = "_"

def main():
    global useraction
    print("Hello! What would you like to do?")
    print("> LOGIN")
    print("> REGISTER")
    print("> QUIT")
    useraction = input("").lower()
    userinput = "_"
    pwdinput = "_"

    def userlogin():
        global userinput
        global pwdinput
        global useraction
        userlist = []
        pwdlist = []
        numuser = int(0)
        numpwd = int(0)

        with open("plaintext.csv") as file:
            for line in file:
                numuser = int(numuser + 1)
                numpwd = int(numpwd + 1)
                row = line.rstrip().split(",")
                userlist.append(row[0])
                pwdlist.append(row[1])

            userinput = input("Username: ")
            userno = int(0)
            for username in userlist:
                if username == userinput:
                    pwdinput = input("password: ")
                    pwdno = int(0)
                    for password in pwdlist:
                        if password == pwdinput:
                            if pwdno == userno:
                                print("you have successfully been logged in!")
                                loginscreen()
                                break
                            elif pwdno == int(numpwd + 1):
                                print("incorrect password. please try again.")
                                break
                            else:
                                pwdno = int(pwdno + 1)
                        else:
                            pwdno = int(pwdno + 1)
                elif userno == int(numuser + 1):
                    if useraction =="quit":
                        break
                    else:
                        print("incorrect username. please try again")
                        userlogin()
                        break
                else:
                    userno = int(userno + 1)

    def passwordchanger():
        global pwdinput
        currentpwd = input("enter your current password: ")
        if currentpwd == pwdinput:
            newpwd = input("enter your new password (must be more than 4 characters): ")
            newpwdlength = int(0)
            for letter in newpwd:
                newpwdlength = int(newpwdlength + 1)
            if newpwdlength < 4:
                print("This password is too short. please try again")
                passwordchanger()
            else:
                print("your password has been changed")
                print("(except it actually hasn't. yet. have some patience please.)")
                print(f"your new password is {newpwd}")
                print("")
                #open passwords document
                #find current password
                #replace that line with {userinput}, {newpwd}
                main()
        else:
            print("incorrect password. please try again")
            passwordchanger()

    def loginscreen():
        global userinput
        global pwdinput
        print(f"Welcome, {userinput}")
        print("> CHANGE PASSWORD")
        print("> LOGOUT")
        loginaction = input("").lower()

        if loginaction == "change password":
            passwordchanger()
        elif loginaction == "logout":
            main()
        else:
            loginscreen()

    def registeruser():
        global userinput
        print("Welcome to hell- i mean our lovely site with no coding errors whatsoever!")
        print("please input your new username and password")
        newuser = input("username: ")
        newpwd = input("password: ")
        # with open("plaintext.csv") as file:
        # for line in file: 
        #         row = line.rstrip().split(",")
        #         if row[0] == newuser:
        #             print("sorry! this user already exists.")
        #             registeruser()
        #             dupeuser = yes
        #             break
        #         else:
        #             dupeuser = no
        with open("plaintext.csv", "a") as file:
            # if dupeuser == no:
            file.write(f"\n")
            file.write(f"{newuser},{newpwd}")
            # else:
            #     registeruser()
            #was going to add a thing that checks to see if the user already exists
            #but i didnt have time
        userinput = newuser
        loginscreen()



    if useraction == "login":
        useraction = "login"
        userlogin()
    elif useraction == "register":
        registeruser()
    elif useraction == "quit":
        useraction = "quit"
        print("quitting...")

    else:
        main()

main()