import streamlit as st
from transformers import pipeline

# Use the gpt2 model for text generation
chatbot = pipeline("text-generation", model="gpt2")

def Healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult a doctor."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "Use prescribed medication as directed by a doctor. If you have any concerns, please contact a doctor."
    else:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant chatbot")
    user_input = st.text_input("how can i assist you today")
    if st.button("Submit"):
        if user_input:
            st.write("user :", user_input)
            with st.spinner("processing your request ... please wait."):
                response = Healthcare_chatbot(user_input)
            st.write("Healthcare assistant :", response)
        else:
            st.write("please enter the message to get a response")

if __name__ == "__main__":
    main()