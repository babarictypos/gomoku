def evaluate_board(gameboard):
    best = -100
    for row in range(15):
        for col in range(15):
            if gameboard.cells_attack[row][col] == True:
                if evaluate_cell(gameboard, row, col)[0] > best:
                    best = evaluate_cell(gameboard, row, col)
                    bestmove = row, col
    return bestmove

def evaluate_board_top(gameboard, x):
    best = -100
    moves_with_eval = []
    top_moves_with_eval = []
    for row in range(15):
        for col in range(15):
            if gameboard.cells_attack[row][col] == True:
                moves_with_eval.append([row, col, evaluate_cell(gameboard, row, col)[0]])
    moves_with_eval.sort(key=lambda x: x[2], reverse = True)
    for move in range(x):
        top_moves_with_eval.append(moves_with_eval[move])

    return top_moves_with_eval

def evaluate_cell(gameboard, row, col):

    #row 0,1,2,3,4,5
    player_chains = [0, 0, 0, 0, 0, 0]
    opp_chains = [0, 0, 0, 0, 0, 0]
    player = gameboard.turn
    for i in range(-4,1):
        player_counter = 0
        opp_counter = 0
        for x in range(0,5):
            if -1 < col + i + x < 15:
                if gameboard.read_cell(row, col + i + x) == player:
                    player_counter += 1
                if gameboard.read_cell(row, col + i + x) == -player:
                    opp_counter += 1
        
        if opp_counter == 0:
            player_chains[player_counter] += 1
            #if player_counter = 1:
                #player_chains[1] += 1
                #if gameboard.read_cell(row, col - 1) or gameboard.read_cell(row, col + 1) == player:
                    #add open 2 
            #if player_counter = 2:
                #player_chains[2] += 1

        else:
            if player_counter == 0:
                opp_chains[opp_counter] += 1
    #col
    for i in range(-4, 1):
        player_counter = 0
        opp_counter = 0
        for x in range(5):
            if -1 < row + i + x < 15:
                if gameboard.read_cell(row + i + x, col) == player:
                    player_counter += 1
                if gameboard.read_cell(row + i + x, col) == -player:
                    opp_counter += 1
        
        if opp_counter == 0:
            player_chains[player_counter] += 1

        else:
            if player_counter == 0:
                opp_chains[opp_counter] += 1
    #diag -> v
    for i in range(-4, 1):
        player_counter = 0
        opp_counter = 0
        for x in range(5):
            if -1 < row + i + x < 15 and -1 < col + i + x < 15:
                if gameboard.read_cell(row + i + x, col + i + x) == player:
                    player_counter += 1
                if gameboard.read_cell(row + i + x, col + i + x) == -player:
                    opp_counter += 1
        
        if opp_counter == 0:
            player_chains[player_counter] += 1

        else:
            if player_counter == 0:
                opp_chains[opp_counter] += 1
    #diag2 -> ^
    for i in range(-4, 1):
        player_counter = 0
        opp_counter = 0
        for x in range(5):
            if -1 < row - i - x < 15 and -1 < col + i + x < 15:
                if gameboard.read_cell(row - i - x, col + i + x) == player:
                    player_counter += 1
                if gameboard.read_cell(row - i - x, col + i + x) == -player:
                    opp_counter += 1
        
        if opp_counter == 0:
            player_chains[player_counter] += 1

        else:
            if player_counter == 0:
                opp_chains[opp_counter] += 1

    a, b, c, d, e, f = player_chains
    u, v, w, x, y, z = opp_chains
    #mine , theirs
    value = 1.1*(b + 7*c + 25*d + 10000*e) + v + 7*w + 25*x + 1000*y - abs(row - 7)*0.01 - abs(col - 7)*0.01
    if e == 0:
        return value, False
    else: 
        return value, True

def number_chains(gameboard, player):
    # 0   1   2   semi3   semi4   5   open 3   open 4
    joins = [0, 0, 0, 0, 0, 0, 0, 0]

    #row
    for row in range(15):
        col = 0
        while col < 11:
            counter = 0
            for x in range(5):
                
                if gameboard.read_cell(row, col + 4 - x) == player*(-1):
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row, col + 4 - x) == player:
                        counter += 1
            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row, col + 4) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    
                    if col + 5 < 15:
                        if gameboard.read_cell(row, col + 5) == 0:
                            counter += 3

                if gameboard.read_cell(row, col + 4) == 0:  
                    if col - 1 > -1:
                        if gameboard.read_cell(row, col - 1) == 0:
                            counter += 3                
            col += 1
            joins[counter] += 1

    #col
    for col in range(15):
        row = 0
        while row < 11:
            counter = 0
            for x in range(5):
                
                if gameboard.read_cell(row + 4 - x, col) == player*(-1):
                    row += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col) == player:
                        counter += 1

            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row + 4, col) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    if row + 5 < 15:
                        if gameboard.read_cell(row + 5, col) == 0:
                            counter += 3
                if gameboard.read_cell(row + 4, col) == 0:
                    if row - 1 > -1:
                        if gameboard.read_cell(row - 1, col) == 0:
                            counter += 3                
            row += 1
            joins[counter] += 1

    #diagonal1 ->, v
    for col1 in range(11):
        col = 0 + col1
        row = 0
        while col < 11:
            counter = 0
            for x in range(5):
                        
                if gameboard.read_cell(row + 4 - x, col + 4 - x) == -player:
                    row += 4 - x
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col + 4 - x) == player:
                        counter += 1

            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row + 4, col + 4) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    if col + 5 < 15:
                        if gameboard.read_cell(row + 5, col + 5) == 0:
                            counter += 3
                if gameboard.read_cell(row + 4, col + 4) == 0:
                    if row - 1 > -1:
                        if gameboard.read_cell(row - 1, col - 1) == 0:
                            counter += 3      

            row += 1
            col += 1              
            joins[counter] += 1

    for row1 in range(1, 11):
        row = 0 + row1
        col = 0
        while row < 11:
            counter = 0
            for x in range(5):
                if gameboard.read_cell(row + 4 - x, col + 4 - x) == -player:
                    row += 4 - x
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col + 4 - x) == player:
                        counter += 1

            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row + 4, col + 4) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    if row + 5 < 15:
                        if gameboard.read_cell(row + 5, col + 5) == 0:
                            counter += 3
                if gameboard.read_cell(row + 4, col + 4) == 0:
                    if col - 1 > -1:
                        
                        if gameboard.read_cell(row - 1, col - 1) == 0:
                            counter += 3 

            row += 1
            col += 1              
            joins[counter] += 1
    #diag2 -> ^
    for col1 in range(11):
        col = 0 + col1
        row = 14
        while col < 11:
            counter = 0
            for x in range(5):
                        
                if gameboard.read_cell(row + x - 4, col + 4 - x) == -player:
                    row += x - 4
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + x - 4, col + 4 - x) == player:
                        counter += 1

            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row - 4, col + 4) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    if row - 5 > -1 and col + 5 < 15:
                        if gameboard.read_cell(row - 5, col + 5) == 0:
                            counter += 3
                if gameboard.read_cell(row - 4, col + 4) == 0:
                    if row + 1 < 15:
                        if gameboard.read_cell(row + 1, col - 1) == 0:
                            counter += 3

            row -= 1
            col += 1              
            joins[counter] += 1

    for row1 in range(4, 15):
        row = 0 + row1
        col = 0
        while row > 3:
            counter = 0
            for x in range(5):
                if gameboard.read_cell(row + x - 4, col + 4 - x) == -player:
                    row += x - 4
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + x - 4, col + 4 - x) == player:
                        counter += 1

            if counter == 3:
                if gameboard.read_cell(row, col) == 0 and gameboard.read_cell(row - 4, col + 4) == 0:
                    counter += 3

            if counter == 4:
                if gameboard.read_cell(row, col) == 0:
                    if row - 5 > -1:
                        if gameboard.read_cell(row - 5, col + 5) == 0:
                            counter += 3
                if gameboard.read_cell(row - 4, col + 4) == 0:
                    if col - 1 > - 1:
                        if gameboard.read_cell(row + 1, col - 1) == 0:
                            counter += 3

            row -= 1
            col += 1              
            joins[counter] += 1

    return joins
def eval(gameboard):
    next_player = gameboard.turn
    playerzero, playerone, playertwo, playerthree, playerfour, playerfive, player_open_three, player_open_four = number_chains(gameboard, -next_player)
    opp_zero, opp_one, opp_two, opp_three, opp_four, opp_five, opp_open_three, opp_open_four = number_chains(gameboard, next_player)

    #join value
    one = opp_one*1.5 - playerone
    two = opp_two*2.5 - playertwo
    three = opp_three*5 - playerthree
    open_three =  opp_open_three*20 - player_open_three
    four = opp_four*20 - playerfour
    open_four = opp_open_four*5 - player_open_four
    five = opp_five*20 - playerfive
    total = next_player*(one*1.1 + two*4 + three*7 + four*50 + open_three*100 + open_four*500 + five*10000)

    return(total)