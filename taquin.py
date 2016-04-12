#Benzina Amina, Lamand Christophe et Nezzari Khalil
#Projet rendu 1
#Lundi 21 Mars 2016



#COMMANDES={'H': haut(), 'B': bas() , 'G':gauche() , 'D':droite(), 'A' : abandonner()}
def cree_taquin (n=4):
    """
    
    """

    taq=[]
    for i in range (n):
        l=[]
        for j in range(n):
            l=l+[(n*i)+j+1]
        taq=taq+[l]
    taq[n-1][n-1]=''
    return taq




def position_case_vide(taq):
    '''
    '''
    n=len(taq)
    for i in range(n):
        for j in range(n):
            if taq[i][j]=='':
                return (j,i)
      
##def melanger_taquin(taq):
##
    


    
##
##def imprimer_taquin(taq):
##




def est_resolu(taq):
    """
    """
    resolu=cree_taquin(len(taq))
    return resolu == taq
    
##
##def haut(taq):
##    """"""

##def bas(taq):
##    """"""

##def gauche(taq):

##def droite(taq):


def echanger(taq, c1, c2):
    """"""
    taq[c1[1]][c1[0]],taq[c2[1]][c2[0]]=taq[c2[1]][c2[0]],taq[c1[1]][c1[0]]
    
##def abandonner():
##

    
def numero_piece(taq, x, y):
    """"""
    piece=taq[y][x]
    if piece=='':
        return (len(taq))**2
    return piece
