def anagram_check(str1, str2):
    if (len(str1)!=len(str2)):
        print ("The strings are not anagrams of each other.")
    else:
        num = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (i==j):
                    num=1
    if (num==1):
        print ("The strings are anagrams of each other.")
    else:
        print ("The strings are anagrams of each other.")
"""
dixitjimanas
giftbymandy01
hossenteelo
internshipmandy01
mohit8887mohit
mohitmohitmohit8887
rajatneon3




"""
str1 = 'listeki'
str2 = 'silent'
anagram_check(str1, str2)