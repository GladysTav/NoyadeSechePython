print("Exercice 18")

#EX18: Un crime a été commis dans le château d’Adéno. Tu as récupéré deux brins d’ADN, provenant de deux positions éloignées de l’ADN du coupable. Il y a quatre suspects, dont tu as séquencé l’ADN.
#Sauras-tu trouver qui est le coupable ?

#Premier code du coupable :CATA
#Second code du coupable :ATGC
#ADN du colonel Moutarde :CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN 
#de Mlle Rose :CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN 
#de Mme Pervenche :AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN 
#de M. Leblanc :CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG

def coupable(DNA):
    if("CATA" in DNA
    and "ATGC" in DNA
    and abs(DNA.find("CATA") - DNA.find("ATGC"))>4):
        return True
    else:
        return False
        
if coupable("CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"):
    print("Colonel Moutarde est coupable.")
if coupable("CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"):
    print("Mlle Rose est coupable.")
if coupable("AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN"):
    print("Mme Pervenche est coupable.")
if coupable("CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"):
    print ("Mr Leblanc est coupable.")

    
    
    