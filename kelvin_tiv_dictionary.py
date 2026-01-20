import streamlit as st


st.title("Tiv Dictionary")

languages = {
    "hello":"M sugh",
    "goodbye": "kwase",
    "thank you": "A vo",
    "yes": "Ee",
    "no": "Ao",
    "water": "minger",
    "food": "ishima",
    "man": "or",
    "woman": "mba",
    "child": "wan",
    "house": "ya",
    "road": "tar",
    "sun": "ushar",
    "moon": "ikyo",
    "fire": "kure",
    "love": "hemen",
    "friend": "manger",
    "school": "kwagh u ishim",
    "book": "ityo",
    "money": "kpen"
}

user_word = st.text_input("Enter a word you would like to translate").strip().lower()
if  st.button("Translate"):
    if user_word:
        #check if the word exists in the dictionary
        if user_word in languages:
            translation = languages[user_word]
            st.success(f"**translation:** {translation}")
        else:
            st.warning("sorry,word not in dictionary")
    else:
        st.warning("Please enter a word first")



