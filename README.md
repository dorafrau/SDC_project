# SDC project: Triple extraction for graph visualisation
*Author: Dora Frauscher*

## Overview:
* ML: Spacy model for named entity recognition and simple logic for realtion extraction.
* Rest API: Flask API to provide the model
* Transferability: Docker compose
* Tracking: W and B

## Descriptoin:
The goal of the project is the development and deployment of an application that allows a user to put in text and get information extracted in form of a graph. A streamlit app serves as userinterface and therefore as the frontend. In the backend there is a flask api providing the model and extraction methods. In the backend W and B is integrated for tracking. The architecture is divided into frontend and backend and is conveniently transferred using docker compose.
  
## Further improvements:
Improve model / try different models (interesting metrics to compare in wandb), focus was set on deployment techniques rather than the model. Also with more time I would have aestetically improved the streamlit app. Also adding multiple options for models or example texts would increase quality and usability.
