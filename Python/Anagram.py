# function to check if two strings are
# anagram or not
def check(s1, s2):
     
    # the sorted strings are checked
    s1= s1.replace(' ','').lower()
    s2= s2.lower().replace(' ','')
    print(s1)
    print(s2)
    print(sorted(s1))
    print(sorted(s2))
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen"
s2 ="silent"
"""check(s1, s2)
check("faiq" , "car")"""
check("Hitler Woman" , "Mother In Law")