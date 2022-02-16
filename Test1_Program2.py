#str = "PA-DXA-7781"
#str = "NJ-QUE-3818"
str = "NY-ZVV-5927"

P_1 = ord(str[3])
P_2 = ord(str[4])
P_3 = ord(str[5])
Price_A = (P_1 + P_2 + P_3)

Price_B = 35.0 * (ord(str[-2]) - 48)
pre_price = (Price_A + Price_B)

Total_price = 0
if str[:2] == "PA":
    Total_price = pre_price * 1.06
elif str[:2] == "NJ":
    Total_price = pre_price * 1.07
elif str[:2] == "NY":
    Total_price = pre_price * 1.16
print("Total_price is %.2f"%Total_price)