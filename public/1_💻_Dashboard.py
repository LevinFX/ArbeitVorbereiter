import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="💻"
)


with st.sidebar:
    Fach = st.text_input("Fach", key="fach_auswahl")
    
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"

st.title("💻 Dashboard")

st.write(
    '''Wie benutzte ich die App am besten?
    ''')

st.write("Simpel.")
st.markdown('''
    1. Falls du das Thema erklärt haben willst, gehe auf Erklären und fülle die Infos Links aus.
    2. Falls du Feedback für z.B. eine Deutsch Analyse haben willst, gehe auf Feedback und fülle die Info Links aus.
    3. Falls du eine Probearbeit generieren willst, gehe auf Probearbeit und fülle die Infos Links aus. \n
    So einfach ist das. \n
    Die App ist noch sehr schlecht, wird noch besser. Am besten nicht neuladen / auf andere Seite der app gehen, wenn man gerade in einem chat ist. Es ist normal bis zu 2 Minuten wartezeit zu haben, bevor man eine Antwort bekommt.
    ''')