from tkinter import *
from random import choice

#==================================== GUI ====================================
win = Tk()
win.title("tic tac toe")
win.configure(bg="#546eff")
win.geometry("300x250")
win.resizable(0, 0)

#==================================== variables ====================================
players = ["x", "o"]
player = choice(players)
player_x_score = IntVar()
player_o_score = IntVar()

player_x_color = "#610c0d"
player_o_color = "#4100e6"
background_color = "#546eff"

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#==================================== functions ====================================
def next_turn(row, column):
    global player

    if player == players[0]:
        buttons[row][column]['fg'] = player_x_color
    elif player == players[1]:
        buttons[row][column]['fg'] = player_o_color

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                result_label.config(text=(f"player {players[1]}'s turn"))

            elif check_winner() is True:
                result_label.config(text=(f"player {players[0]} wins"))
                player_x_score_label.config(text=player_x_score.set(player_x_score.get() + 1))

            elif check_winner() == "tie":
                result_label.config(text="it's a tie")
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                result_label.config(text=(f"player {players[0]}'s turn"))

            elif check_winner() is True:
                result_label.config(text=(f"player {players[1]} wins"))
                player_o_score_label.config(text=player_o_score.set(player_o_score.get() + 1))

            elif check_winner() == "tie":
                result_label.config(text="it's a tie")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#52ff5d")
            buttons[row][1].config(bg="#52ff5d")
            buttons[row][2].config(bg="#52ff5d")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#52ff5d")
            buttons[1][column].config(bg="#52ff5d")
            buttons[2][column].config(bg="#52ff5d")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#52ff5d")
        buttons[1][1].config(bg="#52ff5d")
        buttons[2][2].config(bg="#52ff5d")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#52ff5d")
        buttons[1][1].config(bg="#52ff5d")
        buttons[2][0].config(bg="#52ff5d")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#fff152")
        return "tie"
    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def reset_game():
    global player
    player = choice(players)
    result_label.config(text=f"player {player}'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=background_color)


def reset_score():
    player_x_score_label.config(text=player_x_score.set("0"))
    player_o_score_label.config(text=player_o_score.set("0"))


def undo_move():
    for row in range(2):
        for column in range(2):
                buttons[row][column].config(text="", bg=background_color)

#==================================== buttons ====================================
reset_game_btn = Button(
    win, text="reset game", font=("Kokila", 10, "bold italic"), 
    fg="black", width=8, bg=background_color, command=reset_game)

reset_score_btn = Button(
    win, text="reset score", font=("Kokila", 10, "bold italic"), 
    fg="black", width=8, bg=background_color, command=reset_score)

undo_btn = Button(
    win, text="undo", font=("Kokila", 10, "bold italic"),
    fg="black", width=5, bg=background_color, command=undo_move)

quit_btn = Button(
    win, text="quit", font=("Kokila", 10, "bold italic"),
    fg="black", width=5, bg=background_color, command=win.destroy)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            win, text='', font=("Kokila", 10, "bold"), width=4, height=2,
            bg=background_color, command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

#==================================== labels ====================================
player_x_label = Label(
    win, text="player x", 
    font=("Kokila", 12, "bold"), fg=player_x_color, bg=background_color)

player_o_label = Label(
    win, text="player o", 
    font=("Kokila", 12, "bold"), fg=player_o_color, bg=background_color)

result_label = Label(
    win, text=f"player {player}'s turn", font=("Kokila", 14, "bold"), bg=background_color)

#==================================== score board ====================================
player_x_score_label = Entry(
    win, textvariable=player_x_score, font=("Kokila", 14, "bold"), 
    fg=player_x_color, width=2, bg=background_color)

player_o_score_label = Entry(
    win, textvariable=player_o_score, font=("Kokila", 14, "bold"), 
    fg=player_o_color, width=2, bg=background_color)

#==================================== coordinates ====================================
reset_game_btn.place(x=220, y=0)
reset_score_btn.place(x=220, y=50)
undo_btn.place(x=150, y=0)
quit_btn.place(x=150, y=50)

player_x_label.place(x=10, y=170)
player_o_label.place(x=230, y=170)

player_x_score_label.place(x=20, y=200)
player_o_score_label.place(x=240, y=200)
result_label.place(x=75, y=200)


if __name__ == "__main__":
    win.mainloop()