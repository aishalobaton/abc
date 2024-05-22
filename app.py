import paho.mqtt.client as paho
import time
import json
import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("LengManos")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker, port)

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

letters = ['A', 'B', 'C', 'D', 'I', 'K', 'L', 'N', 'O']
current_letter_index = 0

st.title("Básico: abecedario")
st.text("hola")

while True:
  letter = letters[current_letter_index]
  st.title(letter)

  # Generate a unique key for each camera_input instance
  camera_input_key = f"camera_input_{letter}"  

  img_file_buffer = st.camera_input(f"Toma una Foto de {letter}", key=camera_input_key)  

  if img_file_buffer is not None:
      # Preprocess image
      img = Image.open(img_file_buffer)
      newsize = (224, 224)
      img = img.resize(newsize)
      img_array = np.array(img)
      normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
      data[0] = normalized_image_array

      # Run inference
      prediction = model.predict(data)
      print(prediction)
      if prediction[0][letters.index(letter)] > 0.3:
          st.header(letter)
          client1.publish("LengSenas", {'abc': letter}, qos=0, retain=False)
          time.sleep(2)

          # Move to the next letter
          current_letter_index = (current_letter_index + 1) % len(letters)











   #if prediction[0][0]>0.3:
      #st.header('R')
      #client1.publish("LengSenas","{'abc': 'R'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('U')
      #client1.publish("LengSenas","{'abc': 'U'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('V')
      #client1.publish("LengSenas","{'abc': 'V'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('Y')
      #client1.publish("LengSenas","{'abc': 'Y'}",qos=0, retain=False)
      #time.sleep(0.2)
