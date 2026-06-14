import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import os

class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
    
    def predict(self):
        #load model
        model  = load_model(os.path.join('model' , 'model.keras'))

        imagename = self.filename
        test_image = image.load_img(imagename,target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image,axis = 0)
        test_image = preprocess_input(test_image)

        pred = model.predict(test_image)
        print(pred)
        result = np.argmax(pred,axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return {"prediction" : prediction}
        else:
            prediction = 'Normal'
            return {"prediction" : prediction}
