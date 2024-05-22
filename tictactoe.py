# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:26:31 2024

@author: Solal
"""
import ast
import random

# Quelques structures de données

Grid = tuple[tuple[int, ...], ...]
State = Grid
Action = tuple[int, int]
Player = int
Score = float
inf = float('inf')
Strategy = callable([[State, Player], Action])

# Quelques constantes
DRAW = 0
EMPTY = 0
X = 1
O = 2

def grid_tuple_to_grid_list(grid: Grid) -> list[list[int]]:
    lst = []
    for row in grid:
        lst.append(list(row))
    return lst

def grid_list_to_grid_tuple(grid: list[list[int]]) -> Grid:
    tup = []
    for row in grid:
        tup.append(tuple(row))
    return tuple(tup)

def legals(grid: State) -> list[Action]:
    act = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                act.append([i,j])
    return act

def line(grid: State, player: Player) -> bool:
    grid = grid_tuple_to_grid_list(grid)
    
    #rowcheck
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] == player:
            return True
    
    #colcheck
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] == player:
            return True
    
    #diacheck
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] == player:
        return True
    
    return False

def final(grid: State) -> bool:
    grid = grid_tuple_to_grid_list(grid)
    
    if line(grid, 1) == True:
        return True
    if line(grid, 2) == True:
        return True
    
    for row in grid:
        for col in row:
            if col == 0:
                return False
    return True
    
def score(grid: State) -> float:
    grid = grid_tuple_to_grid_list(grid)
    
    if line(grid, 1) == True:
        return 1
    if line(grid, 2) == True:
        return -1
    return 0
    
def pprint(grid: State):
    grid = grid_tuple_to_grid_list(grid)
    
    for row in grid:
        for col in row:
            if col == 0:
                print("0", end = " ")
            if col == 1:
                print("X", end = " ")
            if col == 2:
                print("O", end = " ")
        print()

def play(grid: State, player: Player, action: Action) -> State:
    grid = grid_tuple_to_grid_list(grid)
    grid[action[0]][action[1]] = player
    return grid_list_to_grid_tuple(grid)

def strategy_brain(grid: State, player: Player) -> Action:
    print("à vous de jouer(int,int): ", end="")
    s = input()
    t = ast.literal_eval(s)
    while (t not in grid_list_to_grid_tuple(legals(grid))):
        print("C'est invalid. Donner une autre action(int,int): ", end = "")
        s = input()
        t = ast.literal_eval(s)
    return t

def strategy_first_legal(grid: State, player: Player) -> Action:
    return legals(grid)[0]

def strategy_random(grid: State, player: Player) -> Action:
    return random.choice(legals(grid))

def tictactoe(strategy_X: Strategy, strategy_O: Strategy, debug: bool = False) -> Score:
    grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    player = X
    while final(grid) == False:
        print("--Player%d--" % player)
        winning_rate(player, minmax(grid, player))
        if player == X:
            grid = play(grid,player,strategy_X(grid, player))
            player = O
        elif player == O:
            grid = play(grid,player,strategy_O(grid, player))
            player = X
        pprint(grid)
    return score(grid)

def winning_rate(player: Player, score: Score):
    print("winning rate: ", end = "")
    if score == 0:
        print("50%")
    if player == X:
            if score == 1:
                print("100%")
            if score == -1:
                print("0%")            
    elif player == O:
            if score == 1:
                print("0%")
            if score == -1:
                print("100%") 

def player_inverse(player: Player) -> Player:
    if player == X:
            player = O
    else:
            player = X
    return player

def minmax(grid: State, player: Player) -> float: 
    if final(grid):
       return score(grid)

    if player == X:
         bestValue = -inf
         for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            bestValue = max(bestValue, v)
         return bestValue

    else: # minimizing player
        bestValue = inf
        for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            bestValue = min(bestValue, v)
        return bestValue

def minmax_action(grid: State, player: Player, depth: int = 0) -> tuple[float, Action]:
    bestAction = Action
    if player == X:
         bestValue = -inf
         for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            if v > bestValue:
                bestValue = v
                bestAction = action
         return tuple[bestValue,bestAction]

    else: # minimizing player
        bestValue = inf
        for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            if v < bestValue:
                bestValue = v
                bestAction = action
        return tuple[bestValue,bestAction]

def strategy_minmax(grid: State, player: Player) -> Action:
    bestAction = Action
    if player == X:
         bestValue = -inf
         for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            if v > bestValue:
                bestValue = v
                bestAction = action
         return bestAction

    else: # minimizing player
        bestValue = inf
        for action in legals(grid):
            newGrid = play(grid, player, action)
            v = minmax(newGrid, player_inverse(player))
            if v < bestValue:
                bestValue = v
                bestAction = action
        return bestAction

def main():
    tictactoe(strategy_minmax,strategy_random)
    
if __name__ == "__main__":
    main()