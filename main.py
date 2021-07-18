from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from PIL import ImageTk
import PIL.Image
import pyttsx3 as pp
import threading
import speech_recognition as s
engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
def speak(word):
    engine.say(word)
    engine.runAndWait()

from tkinter import *
bot = ChatBot("Olive")
trainer =ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train("chatterbot.corpus.english")


main=Tk()



main.geometry("600x450")

main.title("My chat bot")
img =ImageTk.PhotoImage(PIL.Image.open("image.png"))
photoL=Label(main, image=img)
photoL.pack(side=LEFT,pady=5)


def takeQuery():
    sr=s.Recognizer()
    print("bot is listening")
    with s.Microphone() as m:
       try:
           audio = sr.listen(m)
           query = sr.recognize_google(audio)
           print(query)
           textF.delete(0, END)
           textF.insert(0, query)
           ask_from_bot()
       except Exception as e:
           print(e)
           print("not recognized")

def ask_from_bot():
    query=textF.get()
    if query == 'What is your name?':
         answer= 'My name is olive'

    elif query == 'Bye':
        answer = 'Bye'

    elif (query == 'hi' or query == 'hii' or query == 'hello'):
        answer = 'hi'

    elif query == 'How are you':
        answer = 'I am fine.How are you?'

    elif query == 'what is the virus called which causes the corona virus':
        answer = 'SARS-CoV-2'

    elif query == 'what does SARS-CoV-2 stands for':
        answer = 'severe acute respiratory syndrome coronavirus 2'

    elif query == 'who is most at risk for covid-19':
        answer = '60+ yrs or with health conditions like lung or heart disease, diabetes or condition that affect immune system'

    elif query == 'how many types of human corona virus are there':
        answer = '6'

    elif query == 'can COVID-19 cause severe disease':
        answer = 'While COVID-19 is spreading rapidly, most people will experience only mild or moderate symptoms. That said, this coronavirus can cause severe disease in some people.'

    elif query == 'where did the first case of coronavirus disease originate':
        answer = 'The virus was first reported in humans in Wuhan,China in December 2019'

    elif query == 'will climate change make the COVID-19 pandemic worse':
        answer = 'There is no evidence of a direct connection between climate change and the emergence or transmission of COVID-19 disease.'

    elif query == 'can the COVID-19 survive in drinking water':
        answer = 'Currently, there is no evidence about the survival of the COVID-19 virus in drinking-water or sewage.'

    elif query == 'are COVID-19 Vaccine Side effects a good sign':
        answer = 'The vaccines can cause side effects, like tiredness, achiness, and fever, but the vast majority last only a day or two and are not serious or dangerous. Side effects are actually normal signs that the vaccine is working and your body is building protection.'

    elif query == 'what are the possible modes of transmission of COVID-19':
        answer = 'Transmission of SARS-CoV-2 can occur through direct, indirect, or close contact with infected people through infected secretions such as saliva and respiratory secretions or their respiratory droplets, which are expelled when an infected person coughs, sneezes, talks or sings.'

    elif query == 'how long does the virus that causes COVID-19 last on surfaces':
        answer = '72 hours on plastic and stainless steel, up to four hours on copper, and up to 24 hours on cardboard'

    elif query == 'what is double mutant virus':
        answer = 'The B.1.617 or “double mutant” Indian variant carries two mutations including the L452R and E484Q which have been seen separately before in other variants but never together in one variant.'

    elif query == 'who issued the official name of COVID-19':
        answer = 'The official names COVID-19 and SARS-CoV-2 were issued by the WHO on 11 February 2020.'

    elif query == 'what are the ingredients of the covid-19 vaccines':
        answer = 'messenger ribonucleic acid (mRNA), lipids (SM-102, polyethylene glycol [PEG] 2000 dimyristoyl glycerol [DMG], cholesterol, and 1,2-distearoyl-sn-glycero-3-phosphocholine [DSPC]), tromethamine, tromethamine hydrochloride, acetic acid, sodium acetate, and sucrose '

    elif query == 'what is the role of each ingredient in the vaccine':
        answer = 'mRNA: Like the Pfzer BioNTech vaccine, Moderna’s also uses mRNA technology to build antibodies against COVID-19.Lipids: Nanolipids help deliver the mRNA to the vaccine recipient’s cells. Nanolipid components of the Moderna vaccine include: (SM-102, 1,2-dimyristoyl-rac-glycero3-methoxypolyethylene glycol-2000 [PEG2000-DMG], cholesterol, and 1,2-distearoyl-snglycero-3-phosphocholine [DSPC]).The remaining ingredients, including acids (acetic acid), acid stabilizers (tromethamine and tromethamine hydrochloride), salt (sodium acetate), and sugar (sucrose) all work together to maintain the stability of the vaccine after it’s produced'

    elif query =='What are side effects of Covid vaccine':
        answer ='The most common side effects following COVID-19 vaccines are fatigue, a fever, headaches, body aches, chills, nausea, diarrhea, and pain at the site of injection, according to the World Health Organization'

    elif query == 'can a person get vaccinated against covid while the person is currently sick with covid':
        answer = 'No. People with COVID-19 who have symptoms should wait to be vaccinated until they have recovered from their illness and have met the criteria for discontinuing isolation; those without symptoms should also wait until they meet the criteria before getting vaccinated.'

    elif query =='is it good to have side effects of covid vaccine':
        answer ='While the symptoms show your immune system is responding to the vaccine in a way that will protect against disease, evidence from clinical trials showed that people with few or no symptoms were also protected.'
    else:
         answer=bot.get_response(query)
    msgs.insert(END,"user:" + query)
    msgs.insert(END,"bot:" + str(answer))
    pp.speak(answer)
    textF.delete(0, END)
    msgs.yview(END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT ,fill=Y)
msgs.pack(side=RIGHT ,fill= BOTH,pady=10)
frame.pack()
textF=Entry(main,font=("verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("verdana",20),command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


main.bind('<Return>',enter_function)

def repeat():
    while True:
        takeQuery()



t=threading.Thread(target=repeat)
t.start()
main.mainloop()
