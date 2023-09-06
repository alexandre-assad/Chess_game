from Materials.Echequier import Echequier
from Coup import Coup

def main():
    Echequier_1 = Echequier()
    run = True
    player = "player"
    while run:
        print(Echequier_1.display())
        if player == "player":
            li = int(input("Rentrer la ligne de la piece que vous voulez !"))
            col = int(input("Rentrer la colonne de la piece que vous voulez !"))
            pos = [li,col]
            if Echequier_1.pointer(pos,"w"):
                print(Echequier_1.board[pos[0]-1][pos[1]-1].generate_moves(Echequier_1))
                li_arr = int(input("Rentrer la ligne d'arrivée que vous voulez !"))
                col_arr = int(input("Rentrer la colonne d'arrivée que vous voulez !"))
                try:
                    Echequier_1.play_move(Coup((Echequier_1.board[pos[0]-1][pos[1]-1]),li_arr,col_arr))
                    player = "ia"
                except:
                    print("erreur lors du chargement du coup")
        elif player == "ia":
            li = int(input("Rentrer la ligne de la piece que vous voulez !"))
            col = int(input("Rentrer la colonne de la piece que vous voulez !"))
            pos = [li,col]
            if Echequier_1.pointer(pos,"b"):
                print(Echequier_1.board[pos[0]-1][pos[1]-1].generate_moves(Echequier_1))
                li_arr = int(input("Rentrer la ligne d'arrivée que vous voulez !"))
                col_arr = int(input("Rentrer la colonne d'arrivée que vous voulez !"))
                try:
                    Echequier_1.play_move(Coup((Echequier_1.board[pos[0]-1][pos[1]-1]),li_arr,col_arr))
                    player = "player"
                except:
                    print("erreur lors du chargement du coup")

if  __name__ == "__main__" :
    main()