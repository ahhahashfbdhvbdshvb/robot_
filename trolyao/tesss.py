import os
import speech_recognition as sr
from gtts import gTTS
#import playsound
#from firebase import firebase
import datetime
import serial
import openai

import config
from playsound import playsound

openai.api_key = config.API_KEY

ArduinoSerial=serial.Serial('COM7',2000000)


r = sr.Recognizer()

def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        #ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source, phrase_time_limit=4)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
        return text.lower()    
    
    except:
        text =""
        print(text)
        
    return text.lower()    
    
def speak(text):
   # ArduinoSerial.write('X1'.encode('utf-8'))
    print ("Robot: " + text)   
    output = gTTS(text,lang="vi", slow=False)
    output.save("output.mp3")
    playsound('output.mp3')
    os.remove('output.mp3') 




def main():
    with sr.Microphone() as source:
        
        while True:
            
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text1 = r.recognize_google(audio, language="vi-VN")
                text = text1.lower()
                print("Bạn: " + text)
                
                
            except:
                text = ""
                print("Bạn: " + text)
                
            if not text:
                khong_nghe()
           # elif "đây là gì" in text:
           
               # ArduinoSerial.write('X4'.encode('utf-8'))
               # playsound('tit.mp3')
              #  speak ("đây là: " + result)
            elif "chào" in text:
                ArduinoSerial.write('X1'.encode('utf-8'))
                chao()
            
            elif "mấy giờ " in text:
                
                get_time(text)
                #playsound('tit.mp3')
            elif "ngày" in text:
               # ArduinoSerial.write('X2'.encode('utf-8'))
                #playsound('tit.mp3')
                get_time(text)
           
              #  current_weather()
            elif "làm gì" in text:
              #  ArduinoSerial.write('X1'.encode('utf-8'))
                speak ("")
            elif "bạn tên " in text:
               # ArduinoSerial.write('X1'.encode('utf-8'))
                ten()
            elif "tâm trạng" in text:
                tam_trang()
            elif "sợ ma" in text:
                ArduinoSerial.write('X3'.encode('utf-8'))
                traloi()
               
            elif "biết tôi" in text:
                traloi2()
            elif "thích động vật" in text:
                ArduinoSerial.write('X4'.encode('utf-8'))
                traloi3()
            elif "thể nói tiếng anh" in text:
                traloi4()
            elif "thích trẻ con" in text:
                traloi5()
            elif "từ hà nội đến thành phố hồ chí minh" in text:
                traloi6()
            elif "bạn được tạo ra để làm gì" in text:
                traloi7()
            elif "đặt chân lên mặt" in text:
                traloi8()
            elif "con gì biết bơi" in text:
                traloi9()
            elif "loài gì chạy nhanh nhất" in text:
                traloi10()
            elif "con gì chạy chậm nhất" in text:
                traloi11()
            elif "bạn có yêu" in text:
              #  ArduinoSerial.write('X5'.encode('utf-8'))
                traloi12()
            elif "mở nhạc" in text:
                traloi15()
            elif "biết thêm" in text:
                traloi16()
            elif "đi thẳng" in text:
                traloi15()    
                ArduinoSerial.write('X2'.encode('utf-8'))
            elif "dừng" in text:
                traloi15()    
                ArduinoSerial.write('X6'.encode('utf-8'))
            elif "trái" in text:
                traloi15()    
                ArduinoSerial.write('X8'.encode('utf-8'))
            elif "phải" in text:
                traloi15()    
                ArduinoSerial.write('X7'.encode('utf-8'))
            elif "lùi" in text:
                traloi15()    
                ArduinoSerial.write('X5'.encode('utf-8'))
            


            elif "trường sa" in text:
                traloi16()    
                #ArduinoSerial.write('X2'.encode('utf-8'))
            elif "thủ đô" in text:
                traloi17()    
                #ArduinoSerial.write('X6'.encode('utf-8'))
            elif "tuyên ngôn" in text:
                traloi18()    
                #ArduinoSerial.write('X8'.encode('utf-8'))
            #elif "phải" in text:
                #traloi15()    
                #ArduinoSerial.write('X7'.encode('utf-8'))









            elif "tạm biệt" in text:
                traloi13()
                ok_google()
                break
            
                #print ("Robot:" + speak)
                #output = gTTS(speak,lang="vi", slow=False)
                #output.save("output.mp3")
                #playsound.playsound('output.mp3', True)
                #os.remove("output.mp3") 
                #ok_google()
                #break
            else:
                prompt = text
                 
                resp = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt, 
                    max_tokens=100
                )  
                
                text1 = (resp.choices [0].text) 
                
                speak(text1)
            
            #print ("Robot: " + speak)   
            #output = gTTS(speak,lang="vi", slow=False)
            #output.save("output.mp3")
            #playsound.playsound('output.mp3', True)
            #os.remove("output.mp3")       
def chao():
    speak("chào bạn")
    

def ten():
  #  ArduinoSerial.write('X1'.encode('utf-8'))
    speak ("tôi tên là momo")
def khong_nghe():
  #  ArduinoSerial.write('X1'.encode('utf-8'))
    speak ("Tôi không nghe gì cả")
def traloi():
    speak("tôi không những sợ ma, mà tôi còn sợ cả lòng người ")
def traloi2():
    speak("có chứ bạn là một con người tốt bụng ")
def traloi3():
    speak("có tôi thích mèo và cả chó nữa")    
def traloi4():
    speak("có chứ tôi có thể")
def traloi5():
    speak("tôi rất thích trẻ con, bởi vì những đứa trẻ thật đáng yêu")
def traloi6():
    speak("1723km và mất 2 giờ nếu bạn di chuyển bằng máy bay")
def traloi7():
    speak("tôi là một con robot với trí tuệ nhân tạo AI được tạo ra để làm bạn với những đứa trẻ")
def traloi8():
    speak("phạm tuân là người việt nam đầu tiên đặt chân lên mặt trăng nha")
def traloi9():
    speak("cá voi xanh, cá chuồn, lươn, hải ly và nhiều sinh vật khác có thể bơi dưới nước")
def traloi10():
    speak("báo là loài chạy nhanh nhất")
def traloi11():
    speak("ốc sên là loài di chuyển chậm nhất")
def traloi12():
    speak ("có chứ tôi yêu tất cả mọi người trên thế giới ")
def traloi13():
    speak("tạm biệt bạn")

def traloi15():
    speak ("ok bạn")

def traloi16():
    speak ("Hoàng Sa,Trường Sa là thuộc chủ quyền Việt Nam")

def traloi17():
    speak ("Hà Nội là thủ đô của Việt Nan ")

def traloi18():
    speak (" Ngày 2 tháng 9 năm 1945 là ngày Bác Hồ đọc bản tuyên ngôn độc lập ")

def traloi19():
    speak ("ok bạn")


def go():
    
    ArduinoSerial.write('x1'.encode('utf-8'))
    speak ("ok")
    print("x1")

def stop():
    
    ArduinoSerial.write('x3'.encode('utf-8'))
    print("x3")
    speak ("ok bạn ")

def traloi16():
    with sr.Microphone() as source:
        
        while True:
            
            audio = r.listen(source, phrase_time_limit=5)
            print("mời bạn nói")
            try:
                text1 = r.recognize_google(audio, language="vi-VN")
                text = text1.lower()
                print("Bạn: " + text)
                
                
            except:
                print("Bạn: " )
                continue
            
            
            if not text:
                print ("Robot:...... ") 
                continue
        #prompt = input ("Enter a prompt: ")
            elif "tạm biệt" in text:
                traloi13()
                ok_google()
                break
            
            
            else:
                
                prompt = text
                 
                resp = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt, 
                    max_tokens=100
                )  
                text1 = (resp.choices [0].text)   
                
                print ("Robot: " + text1)   
                output = gTTS(text1,lang="vi", slow=False)
                output.save("output.mp3")
                playsound('output.mp3')
                os.remove('output.mp3')
            
                
                


            
            

  
def tam_trang():
    speak ("hôm nay tôi rất vui vì được nói chuyện cùng bạn, bạn cũng vậy chứ") 
    ArduinoSerial.write('X4'.encode('utf-8'))   
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
            
def ok_google():
    while True:
        
    #    ArduinoSerial.write('X0'.encode('utf-8'))
        test = get_audio_2().lower()
        
        if "ok robot".lower() in test:
            
       #     ArduinoSerial.write('X1'.encode('utf-8'))
            #playsound.playsound('output.mp3', True)
            print("Bạn: " + test)
            playsound('goi.mp3')
            
            #speak("Hello")
            main()
            break
        if "momo".lower() in test:
            
        #    ArduinoSerial.write('X1'.encode('utf-8'))
            #playsound.playsound('output.mp3', True)
            print("Bạn: " + test)
            speak("Ơi")
            main()
            break
        if test == "":
            print("Bạn: " + test)
            continue
       
        
ok_google()
