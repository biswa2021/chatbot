from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
bot=ChatBot("my bot")
convo=['hi',
      '......hi there.....robota',
      'ur name?',
      '....my name is chinti2.0,created by Biswa the data scienstist...robota',
      'ur config detail',
       '...I am advanced robo creted using Keras Deep learning...robota',
       'what do you like ?',
      '...hmmmm movies,parties & lot more..robota']
trainer=ListTrainer(bot)
trainer.train(convo) 
def ask_bot():
    query=textF.get()
    answer=bot.get_response(query)
    msg.insert(END,"you:" + query)
    msg.insert(END,"bot :"+ str(answer))
    textF.delete(0,END)   
gui=Tk()
gui.geometry("500x600")
gui.title('my chat bot')
img=PhotoImage(file="/Users/biswaranjantripathy/Desktop/myproject/bot.png")
phot=Label(gui,image=img)
phot.pack(pady=5)
frame=Frame(gui)
sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
textF=Entry(gui,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(gui,text='ask from bot',font=("Verdana",20),command=ask_bot)
btn.pack()
gui.mainloop()

