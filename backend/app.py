from flask import Flask, request, jsonify
import spacy
import wandb
import time  # Zeitmessung hinzufügen

app = Flask(__name__)

# NLP-Modell laden
nlp = spacy.load("en_core_web_sm")

# W&B initialisieren
wandb.init(project='graphlit')

def extract_triples(text):
    doc = nlp(text)
    triples = []
    for ent1 in doc.ents:
        for ent2 in doc.ents:
            if ent1 == ent2:
                continue
            common_ancestor = ent1.root.head
            if common_ancestor.pos_ == 'VERB' and common_ancestor in [ancestor for ancestor in ent2.root.ancestors]:
                triples.append((ent1.text, common_ancestor.lemma_, ent2.text))
    return triples, doc
#39fbd2c790b8bcf1bcb7a993e0ad9b8f4740c019
@app.route('/extract', methods=['POST'])
def extract():
    start_time = time.time()  # Startzeit messen
    data = request.json
    text = data['text']
    triples, doc = extract_triples(text)
    end_time = time.time()  # Endzeit messen
    processing_time = end_time - start_time  # Verarbeitungszeit berechnen
    
    # Metriken erfassen
    num_relations = len(triples)
    num_nodes = len(set([node for triple in triples for node in triple[:2]]))  # Eindeutige Knoten
    num_words = len([token for token in doc])
    num_sentences = len(list(doc.sents))
    
    # Metriken und Verarbeitungszeit loggen
    wandb.log({"num_relations": num_relations, 
               "num_nodes": num_nodes, 
               "num_words": num_words, 
               "num_sentences": num_sentences,
               "processing_time": processing_time})
    
    return jsonify(triples)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
