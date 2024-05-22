"""
[IA02] TP SAT/Sudoku template python
author:  Sylvain Lagrue
version: 1.1.0
"""

from typing import List, Tuple
from itertools import combinations
import subprocess

# alias de types
Grid = List[List[int]] 
PropositionnalVariable = int
Literal = int
Clause = List[Literal]
ClauseBase = List[Clause]
Model = List[Literal]

example: Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


example2: Grid = [
    [0, 0, 0, 0, 2, 7, 5, 8, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 8, 1, 0, 0, 0, 0],
    [4, 0, 6, 3, 0, 1, 0, 0, 9],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 3, 1, 0],
]


empty_grid: Grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#### fonctions fournies


def write_dimacs_file(dimacs: str, filename: str):
    with open(filename, "w", newline="") as cnf:
        cnf.write(dimacs)


def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8"
) -> Tuple[bool, List[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:-2].split(" ")

    return True, [int(x) for x in model]


#### fonction principale

def cell_to_variable(i: int, j: int, val: int) -> PropositionnalVariable:
    return (i * 9 + j ) * 9 + val + 1

def variable_to_cell(var: PropositionnalVariable) -> Tuple[int, int, int]:
    if var % 9 :
        val = var % 9 - 1
    else:
        val = 8
    var = (var - val)// 9
    j = var % 9
    i = var // 9
    return(i, j, val)

def model_to_grid(model: Model, nb_vals: int = 9) -> Grid: 
    pass

def at_least_one(variables: List[PropositionnalVariable]) -> Clause:
    clause = [var for var in variables]
    return clause

def unique(variables: List[PropositionnalVariable]) -> ClauseBase:
    combination = list(combinations(variables, 2)) 
    clauseBase = [[-l1, -l2] for l1,l2 in combination]
    clauseBase.append(at_least_one(variables))
    return clauseBase

def create_cell_constraints() -> ClauseBase:
    clauseBase
    for i in range(0, 9):
        for j in range(0, 9):
            var = range(cell_to_variable(i,j,0)-1, cell_to_variable(i,j,8)-1)
            clauseBase.append(unique(var))
    return clauseBase


def create_line_constraints() -> ClauseBase:
    clauseBase
    for i in range(0, 9):
        var = range(cell_to_variable(i,0,0)-1, cell_to_variable(i,8,8)-1)
        clauseBase.append(unique(var))
    return clauseBase


def create_column_constraints() -> ClauseBase:
    clauseBase
    for i in range(0, 9):
        for j in range(0, 9):
            var = range(cell_to_variable(i,j,0)-1, cell_to_variable(i,j,9)-1)
            clauseBase.append(unique(var))
    return clauseBase

def create_box_constraints() -> ClauseBase:
    pass




def main():
    variables = [1, 3, 5]
    unique_result = unique(variables)
    print(unique_result)
    pass


if __name__ == "__main__":
    main()
