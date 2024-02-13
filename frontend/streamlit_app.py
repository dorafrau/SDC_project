import streamlit as st
import requests
from pyvis.network import Network
import streamlit as st
import pandas as pd
import networkx as nx
import streamlit.components.v1

# UI für Texteingabe
st.title("NLP Tripel-Extraktion")
user_input = st.text_area("Text eingeben:")

# Button zum Senden des Textes an die Flask-API
if st.button("Extrahiere Tripel"):
    response = requests.post("http://flask_api:5000/extract", json={"text": user_input})
    if response.status_code == 200:
        triples = response.json()
        if triples:
            net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

            for ent1, relation, ent2 in triples:
                net.add_node(ent1, label=ent1)
                net.add_node(ent2, label=ent2)
                net.add_edge(ent1, ent2, label=relation)

            # Generiere das Netzwerk als HTML
            net.save_graph("graph.html")

            # HTML-Code zum Einbetten in Streamlit
            HtmlFile = open("graph.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            st.components.v1.html(source_code, height=800)
        else:
            st.write("Keine Beziehungen gefunden.")

            st.write("Gefundene Tripel:")
            for triple in triples:
                st.write(triple)
    else:
        st.write("Fehler beim Abrufen der Daten von der API")
