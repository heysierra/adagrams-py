# from adagrams.game import draw_letters
import random
# LETTER_POOL = {
#     'A': 9, 
#     'B': 2, 
#     'C': 2, 
#     'D': 4, 
#     'E': 12, 
#     'F': 2, 
#     'G': 3, 
#     'H': 2, 
#     'I': 9, 
#     'J': 1, 
#     'K': 1, 
#     'L': 4, 
#     'M': 2, 
#     'N': 6, 
#     'O': 8, 
#     'P': 2, 
#     'Q': 1, 
#     'R': 6, 
#     'S': 4, 
#     'T': 6, 
#     'U': 4, 
#     'V': 2, 
#     'W': 2, 
#     'X': 1, 
#     'Y': 2, 
#     'Z': 1
# }
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
freqs = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
word = "apple"
letter_bank = ["a","p","p","a","l","e","a","b","c","y","z"]
for letter in word :
    if letter in letter_bank:
        letter_bank.remove(letter)
print(letter_bank)

