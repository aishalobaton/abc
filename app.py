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
st.text("Conocer el lenguaje de señas colombiano (LSC) es importante para la inclusión social y el enriquecimiento cultural. Aprender el LSC permite a las personas oyentes comunicarse con la comunidad sorda, promoviendo una sociedad más inclusiva y accesible. Esto reduce barreras de comunicación y facilita la integración de las personas sordas en diferentes ámbitos de la vida cotidiana, como la educación, el trabajo y los servicios públicos. El conocimiento y uso del LSC apoya el cumplimiento de los derechos humanos, específicamente los derechos de las personas con discapacidad. Facilita el acceso a la información y servicios en igualdad de condiciones, como lo establece la Convención sobre los Derechos de las Personas con Discapacidad de la ONU. El LSC es una parte integral de la cultura y la identidad de la comunidad sorda en Colombia. Aprender este lenguaje ayuda a valorar y preservar esta cultura, contribuyendo a la diversidad cultural del país. En el ámbito educativo, la enseñanza y el uso del LSC permiten que los estudiantes sordos accedan a la educación en condiciones equitativas. Los educadores que conocen LSC pueden ofrecer una mejor experiencia educativa y adaptar sus métodos de enseñanza para incluir a todos los estudiantes. Saber LSC facilita la comunicación con familiares, amigos o colegas que son sordos, fortaleciendo las relaciones personales y profesionales. Esto también puede mejorar la empatía y la comprensión hacia las experiencias de las personas sordas. El conocimiento del LSC puede abrir oportunidades laborales en áreas como la interpretación, la enseñanza de personas sordas, el trabajo social y la salud, donde la habilidad de comunicarse en LSC es un activo valioso. El LSC es un idioma con su propia gramática y estructura, diferente del español hablado. Conocerlo promueve la diversidad lingüística y reconoce el valor de los diferentes modos de comunicación.")


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
