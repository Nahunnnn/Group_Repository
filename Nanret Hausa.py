import streamlit as st


st.title("hausa Dictionary")

languages = {
"food": "abinci",
"water": "ruwa",
"house": "gida",
"person": "mutum",
"child": "yaro",
"mother": "uwa",
"father": "uba",
"king": "sarki",
"work": "aiki",
"hand": "hannu",
"ear": "kunne",
"eye": "ido",
"sun": "rana",
"world": "duniya",
"time": "lokaci",
"year": "shekara",
"happiness": "farin ciki",
"fire": "wuta",
"stone": "dutse",
"soup": "miya"
}

user_word = st.text_input("Enter a word you would like to translate").strip().lower()
if st.button("Translate"):
if user_word:
#check if the word exists in the dictionary
if user_word in languages:
translation = languages[user_word]
st.success(f"**translation:** {translation}")
else:
st.warning("sorry,word not in dictionary")
else:
st.warning("Please enter a word first")
