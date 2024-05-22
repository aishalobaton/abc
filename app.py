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


st.title("Básico: el abecedario")
st.header("¡Aprende lenguaje de señas colombiano!")
st.subheader("¿Por qué es importante aprender LSC?")
st.markdown("""
Saber sobre el lenguaje de señas colombiano es crucial para fomentar una sociedad más inclusiva, accesible y respetuosa

de los derechos de todos sus miembros, además de enriquecer culturalmente a la comunidad en general.
""")

st.title("A")

camera_input_key = f"camera_input_A"  
img_file_buffer = st.camera_input(f"Toma una Foto de A", key=camera_input_key)  

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
    else: 
        st.text("Incorrecto")

st.title("B")
camera_input_key = f"camera_input_B"  
img_file_buffer = st.camera_input(f"Toma una Foto de B", key=camera_input_key)

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
    if prediction[0][1] > 0.3:
        st.header('B')
        client1.publish("LengSenas", {'abc': 'B'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("C")
camera_input_key = f"camera_input_C"  
img_file_buffer = st.camera_input(f"Toma una Foto de C", key=camera_input_key)

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
    if prediction[0][2] > 0.3:
        st.header('C')
        client1.publish("LengSenas", {'abc': 'C'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")
        
st.title("D")
camera_input_key = f"camera_input_D"  
img_file_buffer = st.camera_input(f"Toma una Foto de D", key=camera_input_key)

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
    if prediction[0][3] > 0.3:
        st.header('D')
        client1.publish("LengSenas", {'abc': 'D'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("I")
camera_input_key = f"camera_input_I"  
img_file_buffer = st.camera_input(f"Toma una Foto de I", key=camera_input_key)

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
    if prediction[0][4] > 0.3:
        st.header('I')
        client1.publish("LengSenas", {'abc': 'I'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("K")
camera_input_key = f"camera_input_K"  
img_file_buffer = st.camera_input(f"Toma una Foto de K", key=camera_input_key)

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
    if prediction[0][5] > 0.3:
        st.header('K')
        client1.publish("LengSenas", {'abc': 'K'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("L")
camera_input_key = f"camera_input_L"  
img_file_buffer = st.camera_input(f"Toma una Foto de L", key=camera_input_key)

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
    if prediction[0][6] > 0.3:
        st.header('L')
        client1.publish("LengSenas", {'abc': 'L'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("N")
camera_input_key = f"camera_input_N"  
img_file_buffer = st.camera_input(f"Toma una Foto de N", key=camera_input_key)

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
    if prediction[0][7] > 0.3:
        st.header('N')
        client1.publish("LengSenas", {'abc': 'N'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")

st.title("O")
camera_input_key = f"camera_input_O"  
img_file_buffer = st.camera_input(f"Toma una Foto de O", key=camera_input_key)

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
    if prediction[0][8] > 0.3:
        st.header('O')
        client1.publish("LengSenas", {'abc': 'O'}, qos=0, retain=False)
        time.sleep(0.2)
    else: 
        st.text("Incorrecto")




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
