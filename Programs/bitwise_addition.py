def Add(num1, num2):

    while (num2 != 0):
        print("num2",num2)
        carrnum2 = num1 & num2 
        print(carrnum2)
        print("_____________________________________")
   
        num1 = num1 ^ num2
        num2 = carrnum2 << 1
     
    return num1

print(Add(27,5))