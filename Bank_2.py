userList = {'Peter': 300000, 'David': 50000, 'Simon': 10000}

# 고객 이름 입력 받기
name = input("Enter Your Name : ")

if name in userList.keys():

    print("1: Deposit, 2: Withdraw, 3: CheckBalance 4: Exit")

    # 실제로 동작하는 코드 작성
    while True:
        option = int(input("Please Enter Your Choice "))
        # 예금 업무
        if option == 1:
            # 입금하려는 금액 입력받기
            moneyIn = int(input("How much? "))

            if moneyIn <= 0 :
                print("Wrong Input")
                continue

            else :
            # 고객의 돈에 더하기
                userList[name] += moneyIn

            # 고객의 계좌에 넣기

            # 성공적으로 예금이 되었는지 출력하기
            print("You just made deposit of %d, your current balance is %d" % (moneyIn, userList[name]))
        # 출금 업무
        elif option == 2:
            # 출금하려는 금액 입력 받기
            moneyOut = int(input("How much? "))
            if moneyOut > 0:
                if moneyOut <= userList[name]:
                    userList[name] -= moneyOut
                    print("You just made withdraw of %d, your current balance is %d" % (moneyOut, userList[name]))
                else:
                    print("No money")
            else:
                print("Wrong Input")

        # 잔고 확인
        elif option == 3:
            # 고객의 잔액 확인하기
            print("==========================")
            print("Hello " + name + "! your balance is %d" % userList[name])
            print("==========================")

        # 종료
        elif option == 4:
            print("Thank you for using our bank")
            break
        else:
            print("Wrong input!")
else:
    print("Invalid User!")