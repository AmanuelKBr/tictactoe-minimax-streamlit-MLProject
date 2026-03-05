
import streamlit as st
from minimax import best_move
from game_logic import check_winner, is_draw


# Page layout
st.set_page_config(layout="centered")

st.title("Tic Tac Toe - Minimax AI")
st.caption("Play against an unbeatable AI powered by the Minimax algorithm")


# Initialize board
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9


board = st.session_state.board


# Move function
def play_move(index):

    if board[index] == " ":

        board[index] = "X"

        if not check_winner(board,"X") and not is_draw(board):

            ai_move = best_move(board)

            board[ai_move] = "O"



# Add spacing
st.write("")


# Draw board
for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        i = row*3 + col

        label = board[i] if board[i] != " " else " "

        cols[col].button(
            label,
            key=i,
            on_click=play_move,
            args=(i,),
            use_container_width=True
        )


# Game result
st.write("")

if check_winner(board,"X"):
    st.success("You win!")

elif check_winner(board,"O"):
    st.error("AI wins!")

elif is_draw(board):
    st.warning("Draw!")


# Restart button
st.write("")

if st.button("Restart Game"):
    st.session_state.board = [" "] * 9
