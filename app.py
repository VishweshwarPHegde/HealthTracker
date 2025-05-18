# Required Libraries
from flask import Flask, render_template, jsonify
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
import random
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
from email_sender import alert_sender
from chat import get_response
import csv
import os
# Initialize Flask App
app = Flask(__name__)

# Load Pre-trained Model
model = pickle.load(open("xgboost_model.pkl", "rb"))

import random
import string

# Generate three random alphabets
random_alphabets = ''.join(random.choices(string.ascii_uppercase, k=3))

# Generate three random integers
random_integers = ''.join(random.choices(string.digits, k=3))

# Combine alphabets and integers
random_combination = random_alphabets + random_integers

print(random_combination)



# render home page

# Function to initialize or load chat history
def load_chat_history():
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                chat_history.append({'random_combination':[0],'user_message': row[1], 'bot_response': row[2]})

    return chat_history

def load_chat_history2(target_combination):
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the 'random_combination' field is in the second column (index 1)
                if len(row) > 1 and row[0] == target_combination:
                    chat_history.append({'random_combination': [0], 'user_message': row[1], 'bot_response': row[2]})

    return chat_history

# Function to save a new message to the chat history
def save_to_chat_history(random_combination,user_message, bot_response):
    file_path = 'chat_history.csv'

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([random_combination,user_message, bot_response])
#@ app.route('/')
#def home():
#    title = 'Coalbot'
#    return render_template('index4.html', title=title)

# render crop recommendation form page





# Helper Function to Generate Random Data
def generate_random_data():
    condition = random.choice(["Good", "Bad"])
    if condition == "Good":
        data = {
            "Heart Rate (BPM)": np.random.randint(60, 101),
            "ECG Irregularity": 0,
            "Blood Oxygen Level (%)": np.random.uniform(95, 100),
            "Sleep Quality Score": np.random.uniform(70, 100),
            "Body Temperature (\u00b0C)": np.random.uniform(36.1, 37.2),
        }
    else:
        data = {
            "Heart Rate (BPM)": random.choice([np.random.randint(40, 60), np.random.randint(101, 180)]),
            "ECG Irregularity": 1,
            "Blood Oxygen Level (%)": np.random.uniform(85, 94.9),
            "Sleep Quality Score": np.random.uniform(0, 69.9),
            "Body Temperature (\u00b0C)": random.choice([np.random.uniform(35.0, 36.0), np.random.uniform(37.3, 39.0)]),
        }
    return data

@app.route('/')
def index():
    return render_template('login44.html')

@app.route('/mainp')
def mainp():
    return render_template('index.html')


@app.route('/mainp2')
def mainp2():
    return render_template('details.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


#@app.route('/')
#def index():
#    return render_template('index.html')
@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    # Save the text to a pickle file
    text = str(int_features3[0])
    with open('smartai_text.pkl', 'wb') as file:
        pickle.dump(text, file)


    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
  #  print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    #print(password_list)
    #print(gmail_list.index(logu))
    #print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index2.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})

@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')


@app.route('/get_data')
def get_data():
    # Generate Random Data
    data = generate_random_data()
    df = pd.DataFrame([data])

    # Predict using Model
    prediction = model.predict(df)[0]
    data["Prediction"] = "Good" if prediction == 0 else "Bad"

    # Example of random data generation, including longitude, latitude, and mobile number
    data['longitude'] = random.uniform(-180, 180)
    data['latitude'] = random.uniform(-90, 90)
    data['mobile_number'] = f"+1{random.randint(1000000000, 9999999999)}"

    # Convert data to DataFrame
    df2 = pd.DataFrame([data])


    if prediction == 0:
        print("Patient is healthy")
    else:
        print("Patient condition is bad, sending email alert.")
        # Send the full DataFrame as an email
        alert_sender(df2)

    return jsonify(data)
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # You can replace the next line with a call to an AI model for generating responses
    bot_response ,predicted_tag=get_response(user_message)

    #save_to_chat_history(random_combination,user_message, bot_response)

    #chat_history = load_chat_history2(random_combination)

  #  print("the random generated result is ",chat_history)





    # Extract 'bot_response' value
    #bot_response_value = chat_history[0]['bot_response']

    
    from gtts import gTTS
    from pydub import AudioSegment
    import pygame
    import os

    text = str(bot_response)
    language = 'en'

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio in a file
        tts.save("output.mp3")
        print("Audio file saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Play the saved audio file using pygame
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value as needed

        # Close the mixer
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error playing audio: {e}")
    

    from translate import Translator

    def translate_text(text, target_language):
        translator= Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
   
    text_to_translate =bot_response
    # Translate to Kannada
    english_translation=text_to_translate
    kannada_translation = translate_text(text_to_translate, "kn")
    print(f"Kannada: {kannada_translation}")

    # Translate to Hindi
    hindi_translation = translate_text(text_to_translate, "hi")
    print(f"Hindi: {hindi_translation}")

    # Translate to Tamil
    tamil_translation = translate_text(text_to_translate, "ta")
    print(f"Tamil: {tamil_translation}")

    # Translate to Malayalam
    malayalam_translation = translate_text(text_to_translate, "ml")
    print(f"Malayalam: {malayalam_translation}")


    marathi_translation = translate_text(text_to_translate, "mr")
    print(f"marathi: {marathi_translation}")

    # Print the result
    #print("this is the text response for present question",loaded_data_yield)
    #return render_template('index.html', user_message=user_message, bot_response=bot_response)
    save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

    chat_history = load_chat_history2(random_combination)

    #bot_response_value = chat_history[0]['bot_response']

    return render_template('chatbot.html', user_message=user_message, bot_response=text_to_translate, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)




if __name__ == "__main__":
    app.run(debug=True)
