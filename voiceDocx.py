from pydoc import doc
from xml.dom.minidom import Document
import speech_recognition as sr
import sys
from docx import Document
r = sr.Recognizer()
with sr.Microphone() as source:
        #to clear the background noise
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        print("speak now")
        #capture the audio
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # break
            #print("speak:", text)
            

            doc = Document()
            nomination = doc.add_paragraph(text)
            doc.save(text+'.docx')
            print(text)
            if text == 'quit':
                #break
                 sys.exit()
                
               #return 0
        except Exception as e:
            print("say again") 
        