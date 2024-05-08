#Importation des bibliothèques
from flask import Flask,render_template, request
import wikipedia
from keras.models import load_model
from PIL import Image
from keras.models import load_model
import numpy as np
from module import prediction, info






app=Flask(__name__)

#Page d'accueil
@app.route('/')
def home():
    return render_template("index.html")


#traitement
@app.route('/traitement', methods=["POST"])
def traitement():

    #recuperatio du fichier image
    file = request.files
    image= file.get('img_submit')
    image=Image.open(image)
    image.save("static\image\lol.jpg")


    #importation du modele
    model_path="best3_model.h5"
    model=load_model(model_path)

    #prediction
    modele_prediction=prediction(image, model)

    #info wiki
    info_wiki=info(modele_prediction)

    print(modele_prediction,"::: ", info_wiki)

    return render_template("traitement.html",modele_prediction=modele_prediction,info_wiki=info_wiki)
    #return "Reusssi"

   






if __name__=='__main__':
    app.run(debug=True)

