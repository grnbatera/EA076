import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# retirando a notificação
np.set_printoptions(suppress=True)

# carregando o modelo para transfer leraning
model = tensorflow.keras.models.load_model('keras_model.h5')

#criando o dataset
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Abrindo as imagens salvas pela webcam
image = Image.open('webcam.jpg')

#fazendo resize e antialias da imagem
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#convertendo a imagem em array numérico
image_array = np.asarray(image)

# mostrando a imagem
image.show()

# normalizando a imagem
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# carregando a imagem normalizada
data[0] = normalized_image_array

# fazendo a predição
prediction = model.predict(data)
print(prediction)