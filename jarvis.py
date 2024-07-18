import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import music
from openai import OpenAI

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key="________________"
    )


    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "you are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
    ]
    )
    return(completion.choices[0].message.content)
    

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening " )

    speak("Jarvis here ,how can i help you")


def takeCommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
      print("Listening......")
      r.pause_threshold = 1
      audio=r.listen(source)

    try:
        
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e :
        print(e)

        print("Say that again ......")
        return"None"
    
    return query



      
        
    
    

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email',to,content)
    server.close
if __name__ == "__main__":
    wishMe()
    if 1:

        query=takeCommand().lower()

        # executing task based query

        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif takeCommand().lower().startswith("play"):
            song=takeCommand().lower().split(" ")[1]
            link=music.music[song]
            webbrowser.open(link)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'play classes' in query:
            classes_dir="________________"
            classes=os.listdir(classes_dir)
            print(classes)
            os.startfile(os.path.join(classes_dir,classes[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            codepath="________________"
            os.startfile(codepath)

        elif 'email to mukul' in query:
            try:
                speak("what shoul i say")
                content=takeCommand()
                to="________________"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak(" i am not able to send email")

        
        else:
            output=aiprocess(query)
            speak(output)
            
            
            
            

        
