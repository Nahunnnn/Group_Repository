import streamlit as st

st.title("language Dictionary")

languages = {
    "yoruba": {"how": "Bawo", "good morning": "Ekaaro", "please": "Ejo", "wait": "Duro",
               "thanks": "Ope","house": "Ile","water": "Omi","food": "Onje","father": "Baba",
               "mother": "Iya","child": "Omode","soap": "Aro","market": "Oja","road": "Ona",
               "character": "Iwa","forgiveness": "Efun","joy": "Ayo","twins": "Ibeji","oracle": "Ifa",
               "chapter": "Odu"},
    "tiv": {"hello": "M sugh","goodbye": "kwase","thank you": "A vo","yes": "Ee","no": "Ao",
            "water": "minger","food": "ishima","man": "or","woman": "mba","child": "wan",
            "house": "ya","road": "tar","sun": "ushar", "moon": "ikyo","fire": "kure",
            "love": "hemen","friend": "manger","school": "kwagh u ishim","book": "ityo",
            "money": "kpen"},
    "edo": {"food": "Ẹghẹn", "Water": "Ami", "house": "Ẹvbu","person": "Edo","child": "Ọmọ",
        "mother": "Iyẹn","father": "Baba","king": "Oba","work": "Ise","hand": "Ovbẹ","ear": "Oto",
        "eye": "Egho","sun": "Ọwan","world": "Uwa","time": "Ẹghe","year": "Ọghe","happiness": "Uyi",
        "fire": "Ina","stone": "Ẹdo","soup": "Ẹkhọ", },
    "igbo": {"food": "abinci","water": "ruwa","house": "gida","person": "mutum","child": "yaro",
        "mother": "uwa","father": "uba","king": "sarki","work": "aiki","hand": "hannu","ear": "kunne",
        "eye": "ido","sun": "rana","world": "duniya","time": "lokaci","year": "shekara","happiness": "farin ciki",
        "fire": "wuta","stone": "dutse","soup": "miya"},
    "hausa": {"food": "abinci","water": "ruwa","house": "gida","person": "mutum","child": "yaro",
              "mother": "uwa","father": "uba","king": "sarki","work": "aiki","hand": "hannu","ear": "kunne",
              "eye": "ido","sun": "rana","world": "duniya","time": "lokaci","year": "shekara","happiness": "farin ciki",
               "fire": "wuta","stone": "dutse","soup": "miya" }

}
option = st.selectbox("what language would you like to you?",
                      ("yoruba", "tiv", "edo","igbo", "hausa")
)

word = st.text_input(f"enter a word to translate in {option.capitalize()}").strip()

if word:

    translator = languages.get(option, {}).get(word.lower()) or languages.get(option, {}).get(word.capitalize())

    if translator:
        st.success(f"**{word}** in {option.capitalize()} is **{translator}**")
    else:
        st.error("word not found in this dictionary")