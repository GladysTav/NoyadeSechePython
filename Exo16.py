print("Exercice 16")

#EX16: Distance entre deux mots.
#La distance de Hamming entre deux mots de mÃªme longueur est 
#le nombre dâ€™endroits oÃ¹ les lettres sont diffÃ©rentes.
#Par exemple : JAPON  SAVON
#La premiÃ¨re lettre de JAPON est diffÃ©rente de la premiÃ¨re 
#lettre de SAVON, les troisiÃ¨mes aussi sont diffÃ©rentes. 
#La distance de Hamming entre JAPON et SAVON vaut donc 2.
#Ã‰cris une fonction distance_hamming()qui calcule la distance de 
#Hamming entre deux mots de mÃªme longueur.

def dist_hamming(A, B):
    d = 0
    for a,b in zip(A,B):
        if (a != b) :
            d = d+ 1
    return d
    
print(dist_hamming("JAPON","SAVON"))
