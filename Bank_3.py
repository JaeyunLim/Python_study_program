def runATM(name):
    if name in userList.keys():
        if name == 'admin':
            adminMode()
        else:
            customerMode()
    else:
        print("Invalid User!")


def deposit(moneyIn):
    if moneyIn > 0:
        userList[name] += moneyIn
        print("You just made deposit of %d, your current balance is %d" % (moneyIn, userList[name]))
    else:
        print("Wrong Input")


def withdraw(moneyOut):
    if moneyOut > 0:
        userList[name] -= moneyOut
        print("You just made withdraw of %d, your current balance is %d" % (moneyOut, userList[name]))
    else:
        print("Wrong input")


def checkBalance():
    print("%s's balance is %s" %(name, userList[name]))


def exit():
    print("Thank you")


def customerMode():
    print("1: Deposit, 2: Withdraw, 3: CheckBalance 4: Exit")
    while True:
        option = int(input("Please Enter Your Choice : "))
        if option == 1:
            moneyIn = int(input("enter money to deposit : "))
            deposit(moneyIn)


        elif option == 2:
            moneyOut = int(input("How much do you want to withdraw? : "))
            withdraw(moneyOut)


        elif option == 3:
            checkBalance()


        elif option == 4:
            exit()
            break
        else:
            print("Wrong input!")


def getCustomersInfo():
    print("================= CUSTOMER LIST =================")
    for user, balance in userList.items():
        print("********_******** CUSTOMER : %s, BALANCE : %s" % (user, balance))
    print("=================   LIST END    =================")


def adminMode():
    print("<<<<<<<<< YOU ENTERED ADMIN MODE >>>>>>>>>")
    Wrong_input = 0
    while True:
        Input_password = str(input("Enter the password : "))
        if Input_password == password:
            print("1: Get Customers Data, 0: Exit")
            option = int(input("Select your choice : "))

            if option == 1:
                getCustomersInfo()

            else:
                print("Exit Admin Mode")
                quit()


        else:
            Wrong_input += 1
            print("Wrong Password (Wrong_input(%d/3)" %Wrong_input)
            if Wrong_input == 3:
                print("You entered wrong password three times")
                quit()


password = "qwerty332065"
userList = {'Peter': 300000, 'David': 50000, 'Simon': 10000, 'admin': "N/A"}
name = input("Enter Your Name : ")
runATM(name)