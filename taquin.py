#Benzina Amina, Lamand Christophe et Nezzari Khalil
#Projet rendu 1
#Lundi 21 Mars 2016



#COMMANDES={'H': haut, 'B': bas , 'G':gauche, 'D':droite, 'A' : abandonner}
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
      
def melanger_taquin(taq):
    """
             
            ::  A OPTIMISER!!!!!!!!!!!!!!!!!!!!!!!   ::
       
    """
    global liste_coup
    nb_coups= randint(50,150)
    coups='HBGD'
    for i in range (nb_coups):
        position_vide= position_case_vide(taq)
        n_action=randint(0,3)
        COMMANDES[coups[n_action]](taq)
        new_position_vide= position_case_vide(taq)
        while new_position_vide== position_vide:
            position_vide= position_case_vide(taq)
            n_action=randint(0,3)
            COMMANDES[coups[n_action]](taq)
            new_position_vide= position_case_vide(taq)
        liste_coup=liste_coup+[coups[n_action]]


    
##
##def imprimer_taquin(taq):
##




def est_resolu(taq):
    """
    """
    resolu=cree_taquin(len(taq))
    return resolu == taq
    
def haut(taq):
    case_vide= position_case_vide(taq)
    if case_vide[1]>0:
        echanger(taq, case_vide, (case_vide[0],case_vide[1]-1))
    

def bas(taq):
    case_vide= position_case_vide(taq)
    if case_vide[1]<len(taq)-1:
        echanger(taq, case_vide, (case_vide[0],case_vide[1]+1))
    

def droite(taq):
    case_vide= position_case_vide(taq)
    if case_vide[0]<len(taq)-1:
        echanger(taq, case_vide, (case_vide[0]+1,case_vide[1]))

def gauche(taq):
    case_vide= position_case_vide(taq)
    if case_vide[0]>0:
        echanger(taq, case_vide, (case_vide[0]-1,case_vide[1]))


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
