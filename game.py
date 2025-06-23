import streamlit as st
import time
import random


if "loading_done" not in st.session_state:
    st.session_state.loading_done = False

if not st.session_state.loading_done:
    st.markdown("<h1 style='text-align: center;'>X-treme Math Run</h1>", unsafe_allow_html=True)
    my_bar = st.progress(0)

    for pct_complete in range(1, 101):
        time.sleep(0.01)
        my_bar.progress(pct_complete)

    time.sleep(2)
    my_bar.empty()
    st.session_state.loading_done = True 


forbidden_names = ["Saggin", "Nigger", "Nigga", "Reggin"]

player3 = ""
player4 = ""

num_players = st.number_input("How many players?", min_value=2, max_value=4, step=1)



player1 = st.text_input("Enter a name for player one:", key="player1")
player2 = st.text_input("Enter a name for player two:", key="player2")

if num_players >= 3:   
    player3 = st.text_input("Enter a name for player three:", key="player3")

if num_players >= 4:   
    player4 = st.text_input("Enter a name for player four:", key="player4")

Finish = player1 and player2 and (num_players < 3 or player3) and (num_players < 4 or player4)
if Finish:
    show_scoreboard = True
else:
    show_scoreboard = False
if player1 and player2 and (num_players < 3 or player3) and (num_players < 4 or player4):



    if num_players >=1:

        col1, col2 = st.columns(2)

        with col1:
            number1 = st.number_input(f"Score for {player1}", key="num1")
            st.write("Box 1 current number:", number1)

        with col2:
            number2 = st.number_input(f"Score for {player2}", key="num2")
            st.write("Box 2 current number:", number2)


    if num_players >=3:
        col1, col2 = st.columns(2)

        with col1:
                number3 = st.number_input(f"score for {player3}", key="num3")
                st.write("Box 1 current number:", number3)
    if num_players == 4:
        with col2:
            number4 = st.number_input(f"score for {player4}", key="num4")
            st.write("Box 2 current number:", number4)
else:
    st.warning("Please enter all players names to continue!")

st.title("🎲 Spin the Randomizer!")

good_options = ["Move forward 3", "Coin Flip!", "Swap Places", "Roll Again"]
bad_options = ["Go back 2", "Skip a Turn"]
all_options = bad_options + good_options

if "spin_result" not in st.session_state:
    st.session_state.spin_result = None

all_names_entered = (
    player1.strip() and player2.strip() and
    (num_players < 3 or player3.strip()) and
    (num_players < 4 or player4.strip())
)

if st.button("🎡 Spin the Wheel!", disabled=not all_names_entered):
    with st.spinner("Spinning..."):
        time.sleep(2)
    st.session_state.spin_result = random.choice(all_options)

result = st.session_state.spin_result
if result:
    if result in good_options:
        st.success(f"🎉 You landed on: **{result}**")
    elif result in bad_options:
        st.error(f"😬 You landed on: **{result}**")

    if result == "Coin Flip!":
        choice = st.radio("Choose:", ["Heads", "Tails"], horizontal=True, key="coin_choice")
        if st.button("Flip Coin 🪙"):
            with st.spinner("Flipping..."):
                time.sleep(2)
            coin_result = random.choice(["Heads", "Tails"])
            st.write(f"The coin landed on **{coin_result}**.")

            if choice == coin_result:
                st.success("You guessed right! Move forward 3 blocks.")
            else:
                st.error("Wrong guess! Move back 2 blocks.")
