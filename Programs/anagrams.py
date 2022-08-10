def anagrams(str1,str2):
    if sorted(str1)==sorted(str2):
        return "It's Anagrams"
    else:
        return "It's Not a Anagrams" 

print(anagrams("HELLO","OLLEH"))
print(anagrams("HELO","OLLEH"))
print(anagrams("HELO","OLLEH"))

