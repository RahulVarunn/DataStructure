# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the 
# signed 32-bit integer range [-231, 231 - 1], then return 0.




def reverse(x):

    s = str(abs(x)) 
    reversed = int(s[::-1])

    if reversed > 2147483647:
        return 0
    
    elif x>0:
        return reversed

    else:
        return (reversed * -1)
    
print(reverse(-3245))

    
