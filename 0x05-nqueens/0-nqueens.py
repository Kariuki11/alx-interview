#!/usr/bin/python3
"""N-Queens Algorithm with Backtracking (Recursion inside loop)"""
import sys


class NQueenSolver:
    """Class for solving the N-Queens problem"""

    def __init__(self, n):
        """Initialize the solver with a given board size"""
        self.n = n
        self.positions = [0] * n
        self.solutions = []

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe"""
        for r in range(row):
            c = self.positions[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve_n_queens(self, row):
        """Place queens recursively and find all solutions"""
        if row == self.n:
            self.solutions.append([[r, c] for r, c in enumerate(self.positions)])
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.positions[row] = col
                    self.solve_n_queens(row + 1)

    def get_solutions(self):
        """Start the solving process and return the solutions"""
        self.solve_n_queens(0)
        return self.solutions


# Main program
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solver = NQueenSolver(N)
solutions = solver.get_solutions()

for solution in solutions:
    print(solution)
