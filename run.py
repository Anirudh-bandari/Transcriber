from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import Scrollbar
from tkinter.filedialog import *
# from tkinter.tix import *

import pyttsx3
import requests
import time
import PyPDF2
import webbrowser
import os
import threading


# A basic tkinter window 
def window_defination(width,height):
    global w
    w=Tk()

    width_of_window = width#427
    height_of_window = height#250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    w.configure(bg='#249794')

# distroying a tkinter window
def window_destroy():
    w.destroy()

# hover effect 
def changeOnHover(button, colorOnHover, colorOnLeave):

    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

# this is first page which appears when program executes
def landing_page():
    window_defination(427,250)

    progress=Progressbar(w,style='red.Horizontal.TProgressbar',orient=HORIZONTAL,length=500)

    a='#249794'
    def bar():
        l4=Label(w,text='Loading...',fg='white',bg=a)
        lst4=('Calibri (Body)',10)
        l4.config(font=lst4)
        l4.place(x=18,y=210)
        
        import time
        r=0
        for i in range(100):
            progress['value']=r
            w.update_idletasks()
            time.sleep(0.03)
            r=r+1
        
        w.destroy()
        home_page()
            
        
    progress.place(x=-10,y=235)

    button = Button(w,width=10,height=1,text='Get Started',command=bar)
    button.place(x=170,y=200)

    label = Label(w,text='Welcome to Transcriber',font='Verdana 18 bold',fg='white',bg=a)
    label.place(x=60, y=100)
    # label.place(relx=0.35,rely=0.5)
    w.mainloop()

# home page leads to all other pages
def home_page():
    window_defination(427,250)

    btn1 = Button(w, text="Text to Speech", command=Text_to_speech)
    btn1.place(relx=0.15,rely=0.25)
    changeOnHover(btn1, "#77dad6", "white")
    # ToolTip(btn1, msg="This converts text to speech")
    
    btn2 = Button(w, text="PDF to Speech", command=Pdf_to_speech)
    btn2.place(relx=0.65,rely=0.25)
    changeOnHover(btn2, "#77dad6", "white")
    # ToolTip(btn2, msg="This converts text to speech")

    btn3 = Button(w, text="Audio/Video To Text", command=Audio_Video_to_text)
    btn3.place(relx=0.15,rely=0.60)
    changeOnHover(btn3, "#77dad6", "white")
    # ToolTip(btn3, msg="This converts text to speech")

    btn4 = Button(w, text="Video To SRT", command=Video_to_srt)
    btn4.place(relx=0.65,rely=0.60)
    changeOnHover(btn4, "#77dad6", "white")
    # ToolTip(btn4, msg="This converts text to speech")

    w.mainloop()

# returning back to home page
def back_to_home():
    w.destroy()

    home_page()

# converts text to speech
def Text_to_speech():
    w.destroy()
    window_defination(500,300)

    Label(w,text="Text To Speech", bg="#77dad6", font="Verdana 18 bold").place(x=30, y=10)
    Label(w,text="Enter Text", font="Verdana 10 bold", bg="#77dad6").place(x=30, y=75)

    text = StringVar()
    ch = StringVar()
    
    entry_field = Entry(w, textvariable=text, width='50')
    entry_field.place(x=30, y=110)

    engine = pyttsx3.init()
    #changing voice
    voices = engine.getProperty('voices')
    #selecting voice 0 male 1 female
    engine.setProperty('voice', voices[1].id) 


    # voices = engine.getProperty('voices')
    # if m.get() == 0:
    #     engine.setProperty('voice', voices[0].id)
    # elif f.get() == 1:
    #     engine.setProperty('voice', voices[1].id)


    # def Voice():
    #     voices = engine.getProperty('voices')
    #     if ch.get() == 0:
    #         return engine.setProperty('voice', voices[0].id)
    #     elif ch.get() == 1:
    #         return engine.setProperty('voice', voices[1].id)

    # Radiobutton(w,text="Male Voice",value=0,variable=ch).place(x=30, y=150)
    # Radiobutton(w,text="Female Voice",value=1,variable=ch).place(x=120, y=150)

    newVoiceRate=150#speed of speech
    engine.setProperty('rate', newVoiceRate)

    # Function to play
    def Play():
        text = entry_field.get()
        engine = pyttsx3.init() 
        # Voice()
        engine.say(text)
        engine.runAndWait()

    def Save():
        text = entry_field.get()
        engine = pyttsx3.init() 

        newVoiceRate=150#speed of speech
        engine.setProperty('rate', newVoiceRate)
        # Voice()
        engine.save_to_file(text, 'name.mp3')
        engine.runAndWait()

    # Function to Reset  
    def Reset():
        text.set("")


    Button(w, text = "PLAY" , font = 'Verdana 12 bold', command = threading.Thread(target=Play).start).place(x=30, y=180)
    Button(w,text = 'SAVE',font = 'Verdana 12 bold' , command = threading.Thread(target=Save).start, bg = '#77dad6').place(x=100,y=180)
    Button(w, text = 'RESET', font='Verdana 12 bold', command = Reset).place(x=170 , y =180)
    Button(w, text = 'Back', font='Verdana 8 bold', command = back_to_home).place(x=460 , y =0)

    w.mainloop()

# converts a pdf to speech
def Pdf_to_speech():
    w.destroy()
    window_defination(500,300)

    Label(w,text="PDF To Speech", bg="#77dad6", font="Verdana 18 bold").place(x=30, y=10)

    
    def Get_pdf():
        global pdfReader
        file = askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
        pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
        pathlabel.config(text="The file you selected is: "+file)

    engine = pyttsx3.init()
    #changing voice
    voices = engine.getProperty('voices')
    #selecting voice 0 male 1 female
    engine.setProperty('voice', voices[1].id)

    newVoiceRate=150#speed of speech
    engine.setProperty('rate', newVoiceRate)

    def save():
    
        for page_num in range(pdfReader.numPages):
            text =  pdfReader.getPage(page_num).extractText()
            # engine.say(text)
            engine.runAndWait()
        engine.stop()
    
        engine.save_to_file(text,'audio.mp3')
        engine.runAndWait()
        Label(w,text="The Audio File is Saved").place(x=30, y = 220)
    
    def Play():

        for page_num in range(pdfReader.numPages):
            text =  pdfReader.getPage(page_num).extractText()
            engine.say(text)
            engine.runAndWait()
        engine.stop()
        engine.runAndWait()
        # Label(w,text="The Audio File is Saved").place(x=30, y=120)

    Button(w,text="Browse File",bg='#77dad6',font="Verdana 10 bold", command=Get_pdf).place(x=30, y=80)
    # Label(w,text="The you selected is: ").place(x=30, y=100)
    pathlabel = Label(w,bg="#77dad6")
    pathlabel.place(x=30, y=120)

    Button(w,text="Play",command=threading.Thread(target=Play).start, font="Verdana 10 bold").place(x=30, y=170)

    Button(w,text="Save",command=threading.Thread(target=save).start, font="Verdana 10 bold").place(x=100, y=170)

    Button(w, text = 'Back', font='Verdana 8 bold', command = back_to_home).place(x=460 , y =0)

    w.mainloop()

# gives a text file when provided with a audio or video file
def Audio_Video_to_text():
    w.destroy()
    window_defination(500,300)

    
    def Get_file():
        global file
        file = askopenfilename(title="Select a PDF", filetype=(("Audio Files","*.mp4"),("All Files","*.*")))   
        # return file
        pathlabel.config(text="The file you selected is: "+file)

    def Assembly():
        webbrowser.open_new(r"https://www.assemblyai.com/")

    def display_text():
        # window_defination(500,300)
        d=Tk()

        width_of_window = 500
        height_of_window = 300
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        d.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        d.configure(bg='#249794')
        
        txtarea = Text(d, width=40, height=20)
        txtarea.pack(pady=20)

        def open_file():
            global loc
            loc = f"{os.getcwd()}\\text.txt" 
            tf = loc
            # pathh.insert(END, tf)
            tf = open(tf, 'r')  # or tf = open(tf, 'r')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()
        open_file()

        Button(d, text = 'Back', font='Verdana 8 bold', command = d.destroy).place(x=460 , y=0)

        w.mainloop()

        

    def Get_text():
        label = Label(w,text="Processing Please wait ...")
        label.place(x=30, y=210)
        api_key = entry_field.get()

        def read_file(file, chunk_size=5242880):
            with open(file, 'rb') as _file:
                while True:
                    data = _file.read(chunk_size)
                    if not data:
                        break
                    yield data
                
        headers = {'authorization': api_key}
        response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers,data=read_file(file))

        audio_url = response.json()['upload_url']
        print(audio_url)

        endpoint = 'https://api.assemblyai.com/v2/transcript'

        json = {'audio_url':audio_url}
        headers = {'authorization' : api_key, 'content-type' : 'application/json'}

        transcript_input_response = requests.post(endpoint, json=json, headers=headers)

        # print(transcript_input_response.json())

        transcript_id = transcript_input_response.json()['id']

        endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
        # https://api.assemblyai.com/v2/transcript/<your transcript id>/srt?chars_per_caption=32

        headers = {
            'authorization': api_key,
            'content-type': 'application/json'
        }

        while True:
            transcript_output_response = requests.get(endpoint, headers=headers)

            if transcript_output_response.json()['status']!='completed':
                print(transcript_output_response.json()['status'], end='')
                print("....")# print("Processing...")
                time.sleep(5)
            else:
                print("Competed")
                break

        with open('text.txt', 'w') as _file:
            _file.write(transcript_output_response.json()['text'])
        print("Created text file sucessfully")

        label.pack_forget()
        label = Label(w,text="your text file has been generated")
        label.place(x=30, y=210)
        # message_display.insert(END, transcript_output_response.json()['text'])

    Label(w,text="Audio/Video to Text", bg="#77dad6", font="Verdana 18 bold").place(x=30, y=10)

    Button(w,text="Browse File",bg='#77dad6',font="Verdana 10 bold", command=Get_file).place(x=30, y=50)

    pathlabel = Label(w,bg="#77dad6")
    pathlabel.place(x=30, y=90)


    api_key = StringVar()
    Label(w,text="Enter your api key ").place(x=30, y=120 )
    entry_field = Entry(w,textvariable=api_key,width='30')
    entry_field.place(x=150,y=120)
    Label(w,text="If you do not have an api key click here->").place(x=30, y=150)
    hyperlink = Button(w,text="Assembly AI",command=Assembly)
    hyperlink.place(x=270,y=150)
    changeOnHover(hyperlink, '#77dad6', 'white')
    # Button(w,text="test").place(x=100, y=180)

    Button(w,text="Get Text", font="Verdana 10 bold", command=threading.Thread(target=Get_text).start).place(x=30, y=180)
    
    # v.config(command=message_display.yview)
    
    Button(w,text="Open Text File", command=display_text).place(x=30, y=240)

    Button(w, text = 'Back', font='Verdana 8 bold', command = back_to_home).place(x=460 , y =0)

    w.mainloop()

# gives a subtitles file when provided with a audio or video file
def Video_to_srt():
    w.destroy()
    window_defination(500,300)
    
    def Get_file():
        global file
        file = askopenfilename(title="Select a Video", filetype=(("Audio Files","*.mp4"),("All Files","*.*")))   
        # return file
        pathlabel.config(text="The file you selected is: "+file)

    def Assembly():
        webbrowser.open_new(r"https://www.assemblyai.com/")

    def display_text():

        d=Tk()

        width_of_window = 500
        height_of_window = 300
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        d.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        d.configure(bg='#249794')

        txtarea = Text(d, width=40, height=20)
        txtarea.pack(pady=20)

        def open_file():
            global loc
            loc = f"{os.getcwd()}\\subtitles.srt" 
            tf = loc
            # pathh.insert(END, tf)
            tf = open(tf, 'r')  # or tf = open(tf, 'r')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()
        open_file()

        Button(d, text = 'Back', font='Verdana 8 bold', command =d.destroy).place(x=460 , y=0)

        w.mainloop()

        

    def Get_srt():

        label = Label(w,"Processing Please wait")
        label.place(x=30, y=210)

        api_key = entry_field.get()

        def read_file(file, chunk_size=5242880):
            with open(file, 'rb') as _file:
                while True:
                    data = _file.read(chunk_size)
                    if not data:
                        break
                    yield data
                
        headers = {'authorization': api_key}
        response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers,data=read_file(file))

        audio_url = response.json()['upload_url']
        print(audio_url)

        endpoint = 'https://api.assemblyai.com/v2/transcript'

        json = {'audio_url':audio_url}
        headers = {'authorization' : api_key, 'content-type' : 'application/json'}

        transcript_input_response = requests.post(endpoint, json=json, headers=headers)

        print(transcript_input_response.json())

        transcript_id = transcript_input_response.json()['id']

        endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
        # https://api.assemblyai.com/v2/transcript/<your transcript id>/srt?chars_per_caption=32

        headers = {
            'authorization': api_key,
            'content-type': 'application/json'
        }

        while True:
            transcript_output_response = requests.get(endpoint, headers=headers)

            if transcript_output_response.json()['status']!='completed':
                print(transcript_output_response.json()['status'], end='')
                print("....")# print("Processing...")
                time.sleep(5)
            else:
                print("Competed")
                break

        srt_endpoint = endpoint + "/srt"
        srt_response = requests.get(srt_endpoint, headers=headers)

        with open('subtitles.srt', 'w') as _file:
            _file.write(srt_response.text)
        print("created srt file sucessfully")

        label.pack_forget()
        label = Label(w, text="your subtitles has been created")
        label.place(x=30, y=210)

    Label(w,text="Generating subtitles of a video", bg="#77dad6", font="Verdana 18 bold").place(x=30, y=10)

    Button(w,text="Browse File",bg='#77dad6',font="Verdana 10 bold", command=Get_file).place(x=30, y=50)

    pathlabel = Label(w,bg="#77dad6")
    pathlabel.place(x=30, y=90)


    api_key = StringVar()
    Label(w,text="Enter your api key ").place(x=30, y=120 )
    entry_field = Entry(w,textvariable=api_key,width='30')
    entry_field.place(x=150,y=120)
    Label(w,text="If you do not have an api key click here->").place(x=30, y=150)
    hyperlink = Button(w,text="Assembly AI",command=Assembly)
    hyperlink.place(x=270,y=150)
    changeOnHover(hyperlink, '#77dad6', 'white')
    # Button(w,text="test").place(x=100, y=180)

    Button(w,text="Get srt", font="Verdana 10 bold", command=Get_srt).place(x=30, y=180)
    
    label = Label(w, text="Your subtitles has been generated")
    
    
    Button(w,text="Open srt File", command=display_text).place(x=30, y=240)

    Button(w, text = 'Back', font='Verdana 8 bold', command = back_to_home).place(x=460 , y =0)

    w.mainloop()


()
