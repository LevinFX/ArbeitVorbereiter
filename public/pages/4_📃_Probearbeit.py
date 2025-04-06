import streamlit as st
from ollama import Client
from tika import parser
import json
import os

st.set_page_config(
    page_title="Probearbeit",
    page_icon="📃"
)

def load_settings():
    with open("settings.json", 'r') as f:
        loaded = json.load(f)
        return loaded

settings = load_settings()

client = Client(
    host=settings["ollama_url"],
)

with st.sidebar:
    Fach = st.text_input("Fach", key="fach_auswahl")
    klasse = st.number_input("Jahrgang",1,14,value=10, key="klasse_auswahl")
    Thema = st.text_input("Thema", key="thema_auswahl")
    files = st.file_uploader("Lade hier Pdf Dateien hoch, die mit dem Thema zu tun haben (optional)", key="file_auswahl",type="pdf")
    Prompt = st.text_area("Falls du noch mehr Informationen geben willst, schreibe sie hier rein (optional).", key="prompt_auswahl")

    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"

st.title("📃 Probearbeit")

if "messages" not in st.session_state:
    if not Fach:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    if not Thema:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    if not klasse:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    else:
        if files:
            raw = parser.from_file(files)
            texts = raw['content']
            st.session_state["messages"] = [{"role": "system", "content": 'Du bist der beste Nachhilfelehrer für das Fach '+Fach +'und einer deiner Schüler geht in die '+str(klasse)+'. Klasse eines Gymnasiums in Schleswig Holstein. Deshalb sollst du, falls es nicht vom Schüler anders verlangt wird, auf Deutsch reden (außer du bist Englischlehrer) Deine Aufgabe ist es nun, ihm eine Probearbeit zu erstellen, die über folgende Themen handelt: '+Thema+'.Hier villeicht noch ein paar Worte des Schülers zu dir: '+Prompt+'. Ende der Nachricht des Schülers, hier ist noch Text, welcher aus Dateien, die der Schüler dir gegeben hat, extrahiert wurde: '+texts}]
        else:
            st.session_state["messages"] = [{"role": "system", "content": 'Du bist der beste Nachhilfelehrer für das Fach '+Fach +'und einer deiner Schüler geht in die '+str(klasse)+'. Klasse eines Gymnasiums in Schleswig Holstein. Deshalb sollst du, falls es nicht vom Schüler anders verlangt wird, auf Deutsch reden (außer du bist Englischlehrer) Deine Aufgabe ist es nun, ihm eine Probearbeit zu erstellen, die über folgende Themen handelt: '+Thema+'. Hier villeicht noch ein paar Worte des Schülers zu dir: '+Prompt}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Bitte erkläre mir alles nochmal."):
    if not Fach:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    if not Thema:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    if not klasse:
        st.info("Bitte fülle die Infos Links aus.")
        st.stop()
    #client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    #response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    response = client.chat(model="llama3:8b", messages=st.session_state.messages, )
    msg = response['message']['content']#response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)