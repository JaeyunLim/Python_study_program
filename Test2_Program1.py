#아스키코드 사용해서 대/소문자 변환
alpha = "aPPLEaNDgRAPE"
for letter in alpha:
    if letter >= chr(65) and letter <= chr(90) :
        print(chr(ord(letter)+32))
    elif letter >= chr(97) and letter <= chr(122) :
        print(chr(ord(letter)-32))

