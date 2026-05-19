
import streamlit as st
from chatbot import chatagent
from memory import get_memory

# Page config
st.set_page_config(
    page_title="FoodHub AI Chatbot",
    page_icon="🍔",
    layout="centered"
)

# Title
st.title(" FoodHub AI Customer Support Chatbot")

st.markdown(
    "Welcome to FoodHub customer support. "
    "Ask questions related to your orders."
)

# Session state
if "user_id" not in st.session_state:
    st.session_state.user_id = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# User login
user_id = st.text_input(
    "Enter User ID",
    value=st.session_state.user_id
)

if user_id:
    st.session_state.user_id = user_id


# User query input
user_query = st.text_input(
    "Enter your query"
)


# Submit button
if st.button("Send"):

    if not st.session_state.user_id:

        st.warning("Please enter User ID.")

    elif not user_query.strip():

        st.warning("Please enter a valid query.")

    else:

        # Generate chatbot response
        response = chatagent(
            st.session_state.user_id,
            user_query
        )

        # Save chat history
        st.session_state.chat_history.append(
            ("User", user_query)
        )

        st.session_state.chat_history.append(
            ("Bot", response)
        )


# Display conversation
st.subheader("Conversation History")

for sender, message in st.session_state.chat_history:

    if sender == "User":
        st.markdown(f" **You:** {message}")

    else:
        st.markdown(f" **Bot:** {message}")


# Memory display
if st.session_state.user_id:

    st.subheader("Memory")

    memory = get_memory(st.session_state.user_id)

    if memory:

        for item in memory:

            st.markdown(
                f"**Q:** {item['query']}"
            )

            st.markdown(
                f"**A:** {item['response']}"
            )

            st.markdown("---")
