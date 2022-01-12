import heapq # https://docs.python.org/3/library/heapq.html

             # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
             # https://www.google.ca/amp/s/www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/amp/

filename = "../Input_files/15.txt"

# Part 1 board

board_Pt1 = []

for lines in open(filename):

    row = " ".join(lines.replace("\n","")).split(" ")

    board_Pt1.append(row)


# Part 2 board

board_Pt2 = []

cpt = 0

board_width = 0

board_height = 0

row = []



for lines in open(filename):

    while board_width < 5:

        temp_row = [x + cpt if x + cpt <= 9 else ((x + cpt + 1) % 10) for x in list(map(int," ".join(lines.replace("\n","")).split(" ")))]

        row += temp_row

        board_width += 1

        cpt += 1

    board_Pt2.append(row)

    row = []

    board_width = 0

    cpt = 0



final_board_Pt2 = []

final_board_Pt2[:] = board_Pt2[:] # Création d'une copie

cpt = 1

row = []

while board_height < 4: # 4 puisque nous avons déjà 1/5 de complété lorsque nous avons fait la largeur ci-haut

    for rows in board_Pt2:

        row = [x + cpt if x + cpt <= 9 else ((x + cpt + 1) % 10) for x in rows] # si x + cpt > 9 -> x + cpt + 1 % 10 (ex. (9 + 2) -> 11 + 1 -> 12 % 10 -> 2)

        final_board_Pt2.append(row)                                             # (9 + 1) -> 10 + 1 -> 11 % 10 -> 1

    board_height += 1

    cpt += 1



def getAdjacent(i,j,riskLvl,board,visited):

    moves = [(i,j-1),(i,j+1),(i-1,j),(i+1,j)] #gauche,droite,haut,bas

    new_cells = []

    for possible_Moves in moves:

        row = possible_Moves[0]

        col = possible_Moves[1]



        if row >= 0 and row < len(board) and col >= 0 and col < len(board[i]) and (row,col) not in visited: # On veut pas reprendre des coords déjà visité

            new_cells.append([int(riskLvl) + int(board[row][col]),(row, col)]) # cell - > [riskLvl, (i coord, j coord)]

    return new_cells



def bestPath(board):

    height = len(board) - 1 # Va permettre de savoir si nous sommes à la dernière row de notre board

    width = len(board[0]) - 1 # Va permettre de savoir si nous sommes à la dernière col de notre row


    visited = []

    main_list = []


    main_list.append([0,(0,0)]) # risk level à 0 et coords (0,0) --> Start

    visited.append((0,0)) # Ajout du Start dans les visited pour ne pas y retourner


    while main_list:

        heapq.heapify(main_list)

        best_cell = heapq.heappop(main_list) # On va prendre la cellule ayant le plus petit risque


        # Check si on est à la fin i = len(board) - 1 et j = len(board[i]) - 1

        if best_cell[1][0] == height and best_cell[1][1] == width:

            print("Fin")

            print(best_cell[0]) # Affichage de son risque

            break

        else:

            #                                    i              j        risk lvl     board  visited

            adjacent_cells = getAdjacent(best_cell[1][0],best_cell[1][1],best_cell[0],board,visited) # getAdjacent va me retourner les cellules voisins de notre meilleur candidat


            for cells in adjacent_cells:

                visited += [cells[1]] # Ajout des nouvelles cellules dans la liste des visités (x,y)

                if cells not in main_list: # Si ils ne sont pas déjà dans la main liste, on les ajoutes

                    main_list += [cells]





# Part 1

bestPath(board_Pt1)

# Part 2

bestPath(final_board_Pt2)