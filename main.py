# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
       word = input("Enter the first word:  ")
       anagram = input("Enter the second word:  ")
       str_1 = word.lower()
       str_2 = anagram.lower()
       if len(str_1) == len(str_2): 
           sort_str_1 = sorted(str_1)
           sort_str_2 = sorted(str_2)

           if sort_str_1 == sort_str_2: 
               return True 

           else:
                return False

       else:         
           return False

print(find_anagram('players', 'parsley'))


