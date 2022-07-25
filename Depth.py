import tkinter as tk
from tkinter import *

from Board import Board, number_chains
from Evaluation import evaluate_board, evaluate_board_top, evaluate_cell, number_chains, eval


def depth(gameboard, x, original_player, total_value, counter):
    candidate_moves_evals2 = []
    if counter == 0:
        print("hai")
        pass
    else:
        for move in evaluate_board_top(gameboard, x):

            if evaluate_cell(gameboard, move[0], move[1])[1] == True:
                total_value = -100000
                candidate_moves_evals2.append([move[0], move[1], total_value])
                break

            player = gameboard.turn
            gameboard.write_cell(move[0], move[1], player)
            if player == original_player:
                total_value += move[2]
            else:
                total_value -= move[2]

            depth(gameboard, x, original_player, total_value, counter - 1)


            gameboard.write_cell(move[0], move[1], 0)


def depth_n(gameboard, evaluate_board, x, depth):

    original_player = gameboard.turn

    candidate_moves_evals = []
    #move[2] is the value of the move
    for move1 in evaluate_board_top(gameboard, x):


        total_value = 0
        player = gameboard.turn
        candidate_moves_evals2 = []

        if evaluate_cell(gameboard, move1[0], move1[1])[1] == True:
            return [move1[0], move1[1]]

        gameboard.write_cell(move1[0], move1[1], player)
        total_value += move1[2]
        player = gameboard.turn
        
        depth(gameboard, x, original_player, total_value, depth)


        candidate_moves_evals2.sort(key=lambda x: x[2])
        candidate_moves_evals.append([move1[0], move1[1], candidate_moves_evals2[0][2]])

        gameboard.write_cell(move1[0], move1[1], 0)

    candidate_moves_evals.sort(key=lambda x: x[2], reverse = True)
    bestmove = [candidate_moves_evals[0][0], candidate_moves_evals[0][1]]
    return bestmove


def minimax(gameboard, x, depth):

    #mini
    lowest_value_list = []
    for move in evaluate_board_top(gameboard, x):
        print("---------------------------")
        print(move)
        total_value = 0
        if evaluate_cell(gameboard, move[0], move[1])[1] == True:
            total_value = -100000
            lowest_value_list.append(total_value)
            break


        else:
            player = gameboard.turn
            gameboard.write_cell(move[0], move[1], player)

            #max
            highest_value_list = []
            for move1 in evaluate_board_top(gameboard, x):
                total_value = -move[2]
                if evaluate_cell(gameboard, move1[0], move1[1])[1] == True:
                    total_value = 100000
                    highest_value_list.append(total_value)
                    break

                
                else:
                    player = gameboard.turn
                    gameboard.write_cell(move1[0], move1[1], player)
                    total_value += move1[2]

                    if depth > 0:
                        total_value += minimax(gameboard, x, depth - 1)
                    

                    highest_value_list.append(total_value)

                    gameboard.write_cell(move1[0], move1[1], 0)

            highest_value_list.sort(reverse = True)

            gameboard.write_cell(move[0], move[1], 0)


        lowest_value_list.append(highest_value_list[0])
    lowest_value_list.sort()
    print(lowest_value_list)
    return lowest_value_list[0]

def minimax_initial(gameboard, x, depth):


    candidate_moves_evals = []
    #move[2] is the value of the move
    candidate_moves_evals = []
    for move in evaluate_board_top(gameboard, x):

        if evaluate_cell(gameboard, move[0], move[1])[1] == True:
            return [move[0], move[1]]

        player = gameboard.turn
        gameboard.write_cell(move[0], move[1], player)
        total_value = move[2]
        total_value += minimax_with_static(gameboard, x, depth - 1)

        candidate_moves_evals.append([move[0], move[1], total_value])
        gameboard.write_cell(move[0], move[1], 0)

    candidate_moves_evals.sort(key=lambda x: x[2], reverse = True)
    bestmove = candidate_moves_evals[0]
    
    return bestmove

def minimax_with_static(gameboard, x, depth):

    #mini
    lowest_value_list = []
    for move in evaluate_board_top(gameboard, x):

        if evaluate_cell(gameboard, move[0], move[1])[1] == True:
            total_value = -100000
            lowest_value_list.append(total_value)
            break
        else:
            player = gameboard.turn
            gameboard.write_cell(move[0], move[1], player)

            #max
            highest_value_list = []
            for move1 in evaluate_board_top(gameboard, x):
                total_value = -move[2]
                if evaluate_cell(gameboard, move1[0], move1[1])[1] == True:
                    total_value = 100000
                    highest_value_list.append(total_value)
                    break


                else:
                    player = gameboard.turn
                    gameboard.write_cell(move1[0], move1[1], player)

                    if depth > 0:
                        minimax_with_static(gameboard, x, depth - 1)
                    
                    else:
                        total_value = eval(gameboard)

                    highest_value_list.append(total_value)

                    gameboard.write_cell(move1[0], move1[1], 0)

            highest_value_list.sort(reverse = True)

            gameboard.write_cell(move[0], move[1], 0)


        lowest_value_list.append(highest_value_list[0])
    lowest_value_list.sort()

    return lowest_value_list[0]