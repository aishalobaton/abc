import paho.mqtt.client as paho
import time
import json
import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("LengManos")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker,port)

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


st.title("Básico: abecedario")
st.h1("hola")


st.title("A")
img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0] > 0.3:
        st.header('A')
        client1.publish("LengSenas", {'abc': 'A'}, qos=0, retain=False)
        time.sleep(0.2)


st.title("B")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][1] > 0.3:
    st.header('B')
    client1.publish("LengSenas", {'abc': 'B'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("C")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][2] > 0.3:
    st.header('C')
    client1.publish("LengSenas", {'abc': 'C'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("D")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][3] > 0.3:
    st.header('D')
    client1.publish("LengSenas", {'abc': 'D'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("I")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][4] > 0.3:
    st.header('I')
    client1.publish("LengSenas", {'abc': 'I'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("K")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][5] > 0.3:
    st.header('K')
    client1.publish("LengSenas", {'abc': 'K'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("L")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][6] > 0.3:
    st.header('L')
    client1.publish("LengSenas", {'abc': 'L'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("N")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][7] > 0.3:
    st.header('N')
    client1.publish("LengSenas", {'abc': 'N'}, qos=0, retain=False)
    time.sleep(0.2)

st.title("O")
img_file_buffer = st.camera_input("Toma una Foto")

if prediction[0][8] > 0.3:
    st.header('O')
    client1.publish("LengSenas", {'abc': 'O'}, qos=0, retain=False)
    time.sleep(0.2)

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
