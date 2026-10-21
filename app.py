import random
import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

st.title("🎮 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Start a new game when the app first opens
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = "Make your first guess!"

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Check My Guess", disabled=st.session_state.finished):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.session_state.message = "⬆️ Too low! Try a higher number."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "⬇️ Too high! Try a lower number."
    else:
        st.session_state.message = (
            f"🎉 Correct! You won in "
            f"{st.session_state.attempts} attempts!"
        )
        st.session_state.finished = True

st.info(st.session_state.message)
st.write(f"Attempts: {st.session_state.attempts}")

if st.session_state.finished:
    if st.button("🔄 Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.finished = False
        st.session_state.message = "New game! Make your first guess."
        st.rerun()