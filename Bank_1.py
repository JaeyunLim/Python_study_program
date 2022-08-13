currentMoney = 100000
print("1: Deposit, 2: Withdraw, 3: CheckBalance 4: Exit")
option = int(input("Please Enter Your Choice "))


# 예금 업무
if option == 1 :
    deposit_money = int(input("How much? "))
    if deposit_money > 0 :
        currentMoney += deposit_money
    else :
        print("Wrong input")

# 출금 업무
elif option == 2 :
    withdraw_money = int(input("How much? "))
    if withdraw_money <= 0 :
        print("Wrong input")
    elif withdraw_money > currentMoney :
        print("Not enough money")
    else :
        currentMoney -= withdraw_money

    print(withdraw_money)
    print(currentMoney)

# 잔고 확인
elif option == 3 :
    print(currentMoney)
# 종료
elif option == 4 :
    print("Thank you for visiting our bank! Good Bye!")

else :
    print("Pick one from between one and four")
