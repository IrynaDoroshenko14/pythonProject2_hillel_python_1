import random

figures = ["stone", "scissors", "paper"]


def user_select_figure():
    figure = ""
    while figure not in figures:
        figure = input(f"User, please, select a figure - {figures}: ")
    print(f"User selected {figure}")
    return figure


def comp_select_figure():
    figure = random.choice(figures)
    print(f"Comp selected {figure}")
    return figure


def define_winner(user_figure, comp_figure):
    if user_figure == comp_figure:
        return "draw"
    elif (user_figure == "scissors" and comp_figure == "paper") or \
            (user_figure == "paper" and comp_figure == "stone") or \
            (user_figure == "stone" and comp_figure == "scissors"):
        return "user"
    else:
        return "comp"


def show_result(winner):
    print(f"The winner is {winner}!")


def ask_continue():
    start = input("Enter 'y' to continue: ")
    return start
