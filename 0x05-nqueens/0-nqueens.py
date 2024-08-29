#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri August 30 02:00:00 2024

@Author: Kenneth Kariuki
"""
import sys


def is_safe(board, row, col):
    """
    Checks if a queen can be placed on the board

    Args:
        board (list): Board to place the queen on
        row (int): Row of the queen to be placed
        col (int): Column of the queen to be placed

    Returns:
        bool: True if the queen can be placed on the
        board, False otherwise
    """
    # Check if the queen is already placed on the board
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Solves the N queens puzzle by placing the N queens
    on the board and returns the solutions.

    Args:
        board (list): Board to place the queens on
        col (int): Column of the queen to be placed
        n (int): Number of queens
        solutions (list): List to store the solutions

    Returns:
        None
    """
    if col >= n:
        # All queens have been placed, add the solution to the list
        solutions.append([i for i in board])
        return

    for i in range(n):
        if is_safe(board, i, col):
            # Place the queen at the current column
            board[col] = i

            # Recursively solve the rest of the board
            solve_nqueens(board, col + 1, n, solutions)

            # Remove the queen from the board (backtrack)
            board[col] = -1


def nqueens(N):
    """
    Solves the N queens puzzle by placing the N queens
    on the board and returns the solutions.

    Args:
        N (int): Number of queens

    Returns:
        list: Solutions to the N queens puzzle
    """
    # Validate the input N
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board of size N x N
    board = [-1 for _ in range(N)]

    # List to store the solutions
    solutions = []

    # Solve the N queens puzzle
    solve_nqueens(board, 0, N, solutions)

    return solutions


def format_solution(solution):
    """
    Formats the solution as a string.

    Args:
        solution (list): A list representing the solution.

    Returns:
        str: Formatted string representing the solution.
    """
    formatted_solution = "["
    for row, col in enumerate(solution):
        formatted_solution += f"[{row}, {col}], "
    formatted_solution = formatted_solution[:-2] + "]"
    return formatted_solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit()

    solutions = nqueens(sys.argv[1])
    for i, solution in enumerate(solutions):
        formatted_solution = format_solution(solution)
        print(formatted_solution)
