#Benzina Amina, Lamand Christophe et Nezzari Khalil
#Projet rendu 1
#Lundi 21 Mars 2016

#COMMANDES={'H': haut(), 'B': bas() , 'G':gauche() , 'D':droite()}
def cree_taquin (n=4):
    """
    
    """

    taq=[]
    for i in range (n):
        l=[]
        for j in range(n):
            l=l+[(n*i)+j+1]
        taq=taq+[l]
    return taq

taq=cree_taquin()
      
##def melanger_taquin(taq):
##
##def imprimer_taquin(taq):
##
##def est_resolu(taq):
##
##def haut():
##    """
##    """
##
##def bas():
##    """"""
##def gauche():
##
##def droite():
##
##def echanger(taq, c1, c2):
##
##def position_case_vide(taq):
##    
##def abandonner():
##
##def numero_piece(taq, x, y):
##    
