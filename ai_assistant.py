import speech_recognition as sr 
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import keyboard

r = sr.Recognizer()

phone_numbers = {'ravi':'12345678','raja':'14445678','rio':'12345578'}
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(command)
    engine.runAndWait()
    
def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening.... Ask now...")
            audioin = r.listen(source) 
            my_text =  r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            
            # Ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak("Playing" + my_text)
                pywhatkit.playonyt(my_text)
                
            # Ask date 
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(str(today))
                
            # Ask time 
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)
                
            # Ask detail about any person 
            elif 'tell about' in my_text:
                person = my_text.replace('tell about','')
                info = wikipedia.summary(person,1)
                speak(info)
                
            elif "phone number" in my_text:
                names = list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name + " phone number is " + phone_numbers[name])
                        speak(name + " phone number is " + phone_numbers[name])
            else:
                speak("Please ask correct question")
            
    except Exception as e:
        print("Error in capturing Microphone...",e)
    

# while True:
#     commands()
