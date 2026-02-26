import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝")

st.title("🏝 Welcome to Treasure Island")
st.write("Your mission is to find the treasure.")

# Initialize stage
if "stage" not in st.session_state:
    st.session_state.stage = 1


# ------------------ STAGE 1 ------------------
if st.session_state.stage == 1:
    choice1 = st.radio(
        "You're at a crossroad. Where do you want to go?",
        ["left", "right"]
    )

    if st.button("Next"):
        if choice1 == "left":
            st.session_state.stage = 2
        else:
            st.error("🕳 You fell into a hole. Game Over.")
            st.session_state.stage = 5


# ------------------ STAGE 2 ------------------
elif st.session_state.stage == 2:
    choice2 = st.radio(
        "You've come to a lake. There is an island in the middle of the lake.",
        ["wait", "swim"]
    )

    if st.button("Next"):
        if choice2 == "wait":
            st.session_state.stage = 3
        else:
            st.error("🐟 You got attacked by an angry trout. Game Over.")
            st.session_state.stage = 5


# ------------------ STAGE 3 ------------------
elif st.session_state.stage == 3:
    choice3 = st.radio(
        "You arrive at the island unharmed. There is a house with 3 doors.",
        ["red", "yellow", "blue"]
    )

    if st.button("Open Door"):
        if choice3 == "red":
            st.error("🔥 It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            st.success("🎉 You found the treasure. You Win!")
        elif choice3 == "blue":
            st.error("🐺 You enter a room of beasts. Game Over.")
        else:
            st.error("❌ You chose a door that doesn't exist. Game Over.")

        st.session_state.stage = 5


# ------------------ RESTART ------------------
elif st.session_state.stage == 5:
    if st.button("Play Again"):
        st.session_state.stage = 1



