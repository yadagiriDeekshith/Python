import speech_recognition as sr
#from google_trans_new import google_translator
import translate
import pyttsx3
from playsound import playsound
recognizer=sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source: 
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for message..') 
    audio = recognizer.listen(source,timeout=5)
    print('Done recording..') 
try:
    print('Recognizing..')
    result = recognizer.recognize_google(audio,language='en')
    print(result)
except Exception as ex:
    print(ex)
    
def trans():
    langinput=input('Type the language you want to convert:')
    if(langinput == "fr" or langinput == "lan"):
        lan=input('Type the language you want to convert:')
        source_lang = 'en'  # English
        target_lang = lan  
        translator = translate.Translator(to_lang=target_lang, from_lang=source_lang)
        text = result
        translation = translator.translate(text)
        print(translation)
        #print(translate_text)
        engine.say(str(translation))
        engine.runAndWait()
    
    elif(langinput == "pra"):
        if(result == "good morning"):
                print("goood morning")
                import b
        elif(result == "how are you"):
                print("how are you")
                import c
        else:
                print("error")
    elif(langinput == "gov"):
        if(result == "good morning"):
            print("goood morning")
            import d
        elif(result == "how are you"):
            print("how are you")
            import e
        else:
            print("error")
    elif(langinput == "tel"):
        if(result == "good morning"):
            print("goood morning")
            import f
        elif(result == "how are you"):
            print("how are you")
            import g    
    else:
    
        print("error")
    
trans()
