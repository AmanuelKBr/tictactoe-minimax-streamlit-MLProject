

import streamlit as st
from minimax import best_move
from game_logic import check_winner, is_draw

st.set_page_config(layout="centered")

st.title("Tic Tac Toe - Minimax AI")

st.caption("Play against an unbeatable Minimax AI")

if "board" not in st.session_state:

    st.session_state.board = [" "] * 9


board = st.session_state.board


def play_move(index):

    if board[index] == " ":

        board[index] = "X"

        if not check_winner(board,"X") and not is_draw(board):

            ai_move = best_move(board)

            board[ai_move] = "O"



for row in range(3):

    cols = st.columns([1,1,1])

    for col in range(3):

        i = row*3 + col

        cols[col].button(board[i], key=i, on_click=play_move, args=(i,))



if check_winner(board,"X"):

    st.success("Human Wins")


elif check_winner(board,"O"):

    st.error("AI Wins")


elif is_draw(board):

    st.warning("Draw")


if st.button("Restart Game"):

    st.session_state.board = [" "] * 9
