print("Exercice 17")

#EX17: Palindrome.
#Ecris une fonction qui teste si un mot est un palindrome ou pas. 
#Un palindrome est un mot qui s’écrit indifféremment de gauche à droite 
#ou de droite à gauche ; par exemple RADAR est un palindrome.


def palindrome(mot):
    i= 0
    longueur = len(mot)
 
    while i < longueur:
        if (mot[i] != mot[-i - 1]):
              return False
        i = i+ 1
 
    return True
 
 
 
if (palindrome("RADAR")):
    print("Palindrome.")
else:
    print("Pas palindrome.")
    
    
    