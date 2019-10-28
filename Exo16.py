print("Exercice 16")

#EX16: Distance entre deux mots.
#La distance de Hamming entre deux mots de même longueur est 
#le nombre d’endroits où les lettres sont différentes.
#Par exemple : JAPON  SAVON
#La première lettre de JAPON est différente de la première 
#lettre de SAVON, les troisièmes aussi sont différentes. 
#La distance de Hamming entre JAPON et SAVON vaut donc 2.
#Écris une fonction distance_hamming()qui calcule la distance de 
#Hamming entre deux mots de même longueur.

def dist_hamming(A, B):
    d = 0
    for a,b in zip(A,B):
        if a != b :
            d += 1
    return d
    
print(dist_hamming("JAPON","SAVON"))
    
    
    