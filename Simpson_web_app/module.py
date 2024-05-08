#Importation des bibliothèques
import wikipedia
from keras.models import load_model
#from skimage.io import imread
from PIL import Image
from keras.models import load_model
import numpy as np




#prediction
def prediction(image, model):

  #Redimensionnent de l'image
  resized_image=image.resize((224,224))
  

  #Normaliser l'image
  #normalized_img=resized_image/255.0



  #prediction
  prediction = model.predict(np.expand_dims(resized_image, axis=0))
  predicted_class = np.argmax(prediction, axis=1)



  #Affichage de la prédiction
  if predicted_class==0:
    return "Bart Simpson"

  elif predicted_class==1:
    return "Homer Simpson"

  elif predicted_class==2:
    return "Lisa Simpson"

  elif predicted_class==3:
    return "Marge Simpson"

  elif predicted_class==4:
    return "Milhouse Van Houten"

  elif predicted_class==5:
    return "Ned Flanders"

  else:
    return"Oups! Je ne connais pas ce personnage! Je vais mater mater d'autres épisodes des Simpson"





#Fonction de recherche
wikipedia.set_lang("fr")


def info(perso):

  if perso=="Je ne supporte pas ce format d'image. Essaie avec une autre image":
    return perso

  elif perso=="Oups! Je ne connais pas ce personnage! Je vais mater d'autres épisodes des Simpson":
    return perso

  else:
    result = wikipedia.summary(perso, sentences=15)
    return result

