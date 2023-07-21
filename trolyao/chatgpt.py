import openai

import config
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

openai.api_key = config.API_KEY
r = sr.Recognizer()

    
with sr.Microphone() as source:
        
    while True:
        
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text1 = r.recognize_google(audio, language="vi-VN")
            text = text1.lower()
            print("Bạn: " + text)
            
            
        except:
            print("Bạn: " )
            continue
    #prompt = input ("Enter a prompt: ")
        prompt = text



        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt, 
            max_tokens=100
        )

        print ("Robot: " + (resp.choices [0].text)) 
        output = gTTS((resp.choices [0].text),lang="vi", slow=False)
        output.save("output.mp3")
        playsound('output.mp3')
        os.remove('output.mp3') 