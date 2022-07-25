import tkinter as tk
from tkinter import *

from Board import Board, number_chains
from Evaluation import evaluate_board, evaluate_board_top, evaluate_cell
from Depth import depth, depth_n, minimax_initial

#INITIALISATION ======================================
gameboard = Board()
widgetdict = {}
widgetdictcounter = 2

for row in range(0, 15):
    for col in range(0, 15):
        widgetdict[widgetdictcounter] = (col, row)
        widgetdictcounter += 1

window = tk.Tk()
canvas = tk.Canvas(width=904, height=904)
canvas.create_rectangle((0, 0, 905, 905), fill="black")

finish = False

#=====================================================

def quit(event):
    window.destroy()

def clickedon(t):
    counter = 0
    for row in range(0 ,15):
        for col in range(0, 15):
            if gameboard.read_cell(row, col) != 0:
                counter += 1

    if counter%2 == 0:
        turn = 1
    else:
        turn = -1
    number = t.widget.find_closest(t.x, t.y)[0]

    new = (widgetdict[number])

    if gameboard.read_cell(new[0], new[1]) == 0:
        if turn == 1:
            #new = evaluate_board(gameboard)
            #new = depth1(gameboard, evaluate_board, 10)

            canvas.create_oval(((new[1])*60+os+3, (new[0])*60+os+3, (new[1]+1)*60-3, (new[0]+1)*60-3), fill='white', tags = ks)
            gameboard.write_cell(new[0], new[1], 1)
            if number_chains(gameboard, 1)[5] > 0:
                canvas.update()
                canvas.after(1000)
                canvas.create_rectangle((0, 0, 905, 905), fill="white", tags= "whitewin")
                canvas.tag_bind("whitewin", "<1>", quit)
        if turn == -1:
            #computer = new
            computer = minimax_initial(gameboard, 2, 2)
            #computer = evaluate_board(gameboard)

            canvas.create_oval(((computer[1])*60+os+3, (computer[0])*60+os+3, (computer[1]+1)*60-3, (computer[0]+1)*60-3), fill='black', tags = ks)
            gameboard.write_cell(computer[0], computer[1], -1)
            if number_chains(gameboard, -1)[5] > 0:
                canvas.update()
                canvas.after(1000)
                canvas.create_rectangle((0, 0, 905, 905), fill="black", tags= "blackwin")
                canvas.tag_bind("blackwin", "<1>", quit)

for row in range(0, 15):
    for col in range(0, 15):
    
        os = 6
        ks = str(col) + "," + str(row)
        canvas.create_rectangle(((row)*60+os, (col)*60+os, (row+1)*60, (col+1)*60), fill='#ffcc99', tags = ks)
        canvas.tag_bind(ks, '<1>', clickedon)


canvas.pack()

window.mainloop()