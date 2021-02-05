import smtplib
import speech_recognition as sr 
import pyttsx3
from email.message import EmailMessage
engine = pyttsx3.init()
listener = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass 

def send_email(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('shailashila8856@gmail.com','shaila_1603073')
    email = EmailMessage()
    email['From'] = 'shailashila8856@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email) 

email_list = {
    "blue" :"shailacse16@gmail.com",
    "white" : "shailaruet16@gmail.com",
    "black" : "1603073@student.ruet.ac.bd"
}

def get_email():
    speak('whom do u want to send the mail?')
    name = get_info()
    receiver = email_list.get(name)
    print(receiver)
    speak('what is the subject of your mail?')
    subject = get_info()
    speak('what is the email content?')
    content = get_info()
    send_email(receiver,subject,content)
          
get_email()
