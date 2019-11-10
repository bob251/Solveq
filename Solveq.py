from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import *
import pyglet
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import sys
import base64
import requests
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import re
#uuuj8hhhhhhhhujh8from splash import SplashScreen
#from anic import anicy
import os
import time

global pics
pics=[]

# Functions
def split(text) :
    length = len(text)
    temp = 0
    for i in range(len(text)) :
        if text[i] == '=' :
            temp = i
            break
    print(temp)
    return text[0:temp],text[temp+1:]


def donothing():
   filewin = Toplevel(app)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def confirm_exit():
   result = messagebox.askokcancel("Exit Confirmation","Are you sure you want to exit?")
   if result==1:
    app.destroy()
    exit()

   

# Frame Class
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.iconbitmap('./icon.xbm')
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login_Page, Result_Page, Input_Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        #global g_status
        #g_status = StringVar()
        #status = Label(self, textvariable=g_status, relief=SUNKEN, anchor=W, bd=1)
        #status.pack(side=BOTTOM, fill=X)
        #g_status.set("Running...")


        self.show_frame("Login_Page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#232323")
        path = "logo.png"

        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')

        frame0 = Frame(self,bg="#232323")
        frame0.pack(fill=X)
        #lbl = ImageLabel(self)
        #lbl.pack()
        #anicy.load_ani(self,'animate')
        

        #giflist = os.listdir('animate')
        ##print(giflist[1])
        ##temp = "animate/"+giflist[1]
        #photo = PhotoImage(file=temp)
        #width = photo.width()
        #height = photo.height()
        #canvas1 = Canvas(self,width=width, height=height)
        #canvas1.pack()
        # create a list of image objects
        #for imagefile in imagelist:
         #   photo = PhotoImage(file=imagefile)
          #  giflist.append(photo)
        # loop through the gif image objects for a while
        #for k in range(0, 1000):
         #   for gif in giflist:
          #      canvas1.delete(ALL)
           #     print('here ,',gif)
            #    temp = "animate/"+gif
             #   photo = PhotoImage(file=temp)
              #  canvas1.create_image(width/2.0, height/2.0, image=photo)
               # canvas1.update()
                #time.sleep(0.1)

        #img = ImageTk.PhotoImage(Image.open(path))
        #panel = Label(self, image = img, bg="black")
        #panel.image = img
        #panel.place(x=0,y=0)

        #logo = PhotoImage(file="./index.png")
        #logo_label = Label(frame0, image=logo)
        #logo_label.pack(side=TOP)

        frame0 = Frame(self,bg="#232323")
        frame0.pack(fill=X,padx=100,pady=30) #username and password distance


        frame1 = Frame(self,bg="#232323")
        frame1.pack(fill=X,padx=100,pady=0) #username and password distance
        lbl1 = Label(frame1, text="Username",font=" Helvetica",fg="#FFFFFF", width=10,bg="#232323")
        lbl1.pack(side=LEFT,padx=100,pady=0)
       
        self.entry1 = Entry(frame1)
        self.entry1.pack(padx=1, pady=0,expand=False)


        

        frame2 = Frame(self,bg="#232323")
        frame2.pack(fill=X,padx=100,pady=0)
        lbl2 = Label(frame2, text="Password",font=" Helvetica",fg="#FFFFFF", width=10,bg="#232323")
        lbl2.pack(side=LEFT, padx=100, pady=0)        

        self.entry2 = Entry(frame2,show="*")
        self.entry2.pack(padx=1, pady=0, expand=False)


        frame4 = Frame(self,bg="#232323")
        frame4.pack(fill=X)
        
        self.var = StringVar()
        self.var.set('')

        
        lbl2 = Label(frame4, textvariable=self.var, width=300 , bg="#232323", fg="red")
        lbl2.pack(side=LEFT, padx=20, pady=10) 


        frame3 = Frame(self,bg="#232323")
        frame3.pack(fill=X)

        login_button = tk.Button(frame3, text="Login", command=self.accept,width=10, bg="#4A4A4A", fg="white")
        login_button.pack(side=BOTTOM, ipadx=17, ipady=5)





    def accept(self):
        input_username=self.entry1.get()
        input_password=self.entry2.get()
        if(input_username=='1' and input_password=="1") :
            print('True')
            self.var.set('You have successfully logged out')
            self.controller.show_frame("Input_Page")
            self.entry1.delete(0,END)
            self.entry2.delete(0,END)
            #g_status.set("Logged in..")

        else :
            self.entry1.delete(0,END)
            self.entry2.delete(0,END)
            self.var.set('The Username or Password is incorrect')
            

class Input_Page(tk.Frame):

    def __init__(self, parent, controller,video_source=0):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#232323")
        frame1 = Frame(self,background="#232323")
        frame1.pack(fill=X)

        cap = cv2.VideoCapture('Comp_6.gif')
        
   
# Check if camera opened successfully 
        if (cap.isOpened()== False):  
          print("Error opening video  file") 
   
# Read until video is completed 
        while(cap.isOpened()): 
      
  # Capture frame-by-frame 
          ret, frame = cap.read() 
          if ret == True: 
   
    # Display the resulting frame 
            cv2.imshow('Frame', frame) 
   
    # Press Q on keyboard to  exit 
            if cv2.waitKey(25) & 0xFF == ord('q'): 
              break
   
  # Break the loop 
          else:  
            break
   
# When everything done, release  
# the video capture object 
        cap.release() 
   
# Closes all the frames 
        cv2.destroyAllWindows() 

       
        button = ttk.Button(frame1, text="Sign Out", command=lambda: controller.show_frame("Login_Page"))
        button.pack(side="right")
        temp_name = "Welcome onboard"
        label = tk.Label(frame1, text=temp_name, font=tkfont.Font(family='Helvetica', size=12,weight="bold"),fg="#FFFFFF", bg="#232323")
        label.pack(side="left", fill="x", pady=10)
        #user_name = Canvas(frame1,width = 200,height=20)
        #user_name.pack(side="left")
        #user_name.create_text(0,0,text="Welcome, "+temp_name+"!")

        path = "logo.png"
        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')
        
        self.frame12 = Frame(self,background="#232323")
        self.frame12.pack(fill=X)
        self.loadimage1 = tk.PhotoImage(file="capt.png")
        capture_image = tk.Button(self.frame12,image=self.loadimage1,command = self.capture,bg="#232323")
        capture_image["border"]="0"
        capture_image.pack(side="left", pady=40,padx=120)


        self.loadimage2 = tk.PhotoImage(file="select.png")
        file_opener = tk.Button(self.frame12, image=self.loadimage2,command = self.open_file,bg="#232323")
        file_opener["border"] = "0"
        file_opener.pack(side="left",pady=40,padx=80)
        
        self.frame_a = Frame(self,background="#232323")
        self.frame_a.pack(fill=X)
        self.frame_com = Frame(self,background="#232323")
        self.frame_com.pack(fill=X)

      

    def res(self):
        self.controller.show_frame("Result_Page")

    def open_file(self):
        result = filedialog.askopenfile(initialdir=".",title="Select File", filetypes=(("JPEG files",".jpg"),("PNG files",".png"),("all files",".*")))
        if result != None :
            print(result)
            
            
            print(result.name)
            #g_status.set("Opened FIle..")
            self.convert(result.name)

    def capture(self):
        cap = cv2.VideoCapture(0)

        font = cv2.FONT_HERSHEY_SIMPLEX

        while(True):
            ret, frame_cam = cap.read()
            rgb = cv2.cvtColor(frame_cam, cv2.COLOR_BGR2BGRA)


            cv2.imshow('framej', rgb)  
            cv2.putText(frame_cam, "Type q to Quit:",(50,700), font, 1,(255,255,255),2,cv2.LINE_AA)
            if not ret:
                break
            # Monitor keystrokes
            k = cv2.waitKey(1)

            if k & 0xFF == ord('q'):
                # q key pressed so quit
                print("Quitting...")
                break
            elif k & 0xFF == ord(' '):
                print("Captured")
                out = cv2.imwrite('capture.png', frame_cam)
                break


        cap.release()
        cv2.destroyAllWindows()
        #g_status.set("Caaptured..")
        #self.cap.set("Captured")
        print("1")
        self.convert('capture.png')

    def convert(self,loc):
        #self.math.set('Mathpix')
        self.mathpix(loc)
        print("convert 1")

    def mathpix(self,loc):
        file_path = loc
        print(loc)
        """
        try :
            image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
            r = requests.post("https://api.mathpix.com/v3/latex",
                data=json.dumps({'src': image_uri}),
                headers={"app_id": "ap496_snu_edu_in", "app_key": "3e9cd05d1dc494ad50f9",
                        "Content-type": "application/json"})
            temp = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
            resp = json.loads(temp)
            self.confidence = resp['latex_confidence']
            part1,part2=split(resp['latex'])
            params = {part1:part2}
            if (resp['latex_confidence']==0):
                messagebox.showerror(title='Invalid Image', message='The Image can not be converted. Please try once again.')
            else :
                if os.path.exists('capture.png'):
                    os.remove('capture.png')
                url_params = urllib.parse.urlencode(params)
                self.string = "http://api.wolframalpha.com/v2/query?appid=HXXYQR-4L4QR4A4PW&input=solve+"+url_params
                self.wolf(self.string)
        except :
            print(Exception)
            print(sys.exc_info()[0])
            messagebox.showerror(title='Poor Internet Connection', message='Please check your internet connection and try again.')
        """
        image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
        r = requests.post("https://api.mathpix.com/v3/latex",
            data=json.dumps({'src': image_uri}),
                headers={"app_id": "aa362_snu_edu_in", "app_key": "b8091e128ab0db6830cf",
                        "Content-type": "application/json"})
        temp = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
        resp = json.loads(temp)
        self.confidence = resp['latex_confidence']
        part1,part2=split(resp['latex'])
        params = {part1:part2}
        if (resp['latex_confidence']==0):
            messagebox.showerror(title='Invalid Image', message='The Image can not be converted. Please try once again.')
        else :
            if os.path.exists('capture.png'):
                os.remove('capture.png')
            url_params = urllib.parse.urlencode(params)
            print(url_params)
            self.string = "http://api.wolframalpha.com/v2/query?appid=G76QL9-AVQWHUV65G&input=solve+"+url_params
            self.wolf(self.string)    

        
    def wolf(self,string) :
        print(string)
        req = Request(string)
        html_page = urlopen(req)
        count = 0
        soup = BeautifulSoup(html_page, "lxml")
        img_links = []
        txt_links = []

        print(soup)

        for links in soup:
            s = str(links)

        tmp_text = [m.start() for m in re.finditer('false" id=',s)]
        tmp_image = [m.start() for m in re.finditer('src=',s)]


        for link in soup.findAll('img') :
            name = "pic"+str(count)+".gif"
            urllib.request.urlretrieve(link.get('src'), name)
            test = "Done" + str(count)
            img_links.append(name)
            print(test)
            count = count + 1
        print('Image Lonks',img_links)
            
        for link in soup.findAll('pod') :
            txt_links.append(link.get('title'))

        print('Text Lonks',txt_links)
            
        global pics

        ta=0
        tb=0
        for i in range(len(tmp_text)+len(tmp_image)) :  
            if tmp_text[ta]<tmp_image[tb] :
                pics.append(txt_links[ta])
                ta+=1
            else :
                pics.append(img_links[tb])
                tb+=1
            if ta==len(tmp_text) :
                for j in range(len(tmp_image)-tb) :
                    pics.append(img_links[tb])
                    tb+=1
                break
            elif tb==len(tmp_image) :
                for j in range(len(tmp_text)-ta) :
                    pics.append(txt_links[ta])
                    ta+=1
                break
                
        print("Pics",pics)
        
        """
        #self.frame_sol = Frame(self,background="#9cd5fc")
        #self.frame_sol.pack(fill=X)
        #label = tk.Label(self.frame_sol, text="Got the solution", font=self.controller.title_font)
        #label.pack(side="top", fill="x", pady=2)

        result = Image.new("RGB", (200,200))
        x=10
        y=0
        for i in range(len(pics)) :
            if pics[i].find('.gif') == -1 :
                img = Image.open("template.png")
                draw = ImageDraw.Draw(img)                # font = ImageFont.truetype(<font-file>, <font-size>)
                font = ImageFont.truetype("bboron.ttf", 20)
                # draw.text((x, y),"Sample Text",(r,g,b))
                #draw.text((1, 9),pics[i],(0,0,0),font=font)
                #pics[i] = pics[i]+'.gif'
                img.save(pics[i])

                """

        # result = Image.new(mode='RGBA',size=(400, 400),color=(255,255,255,0))
        # for index, file in enumerate(pics):
        #     path = os.path.expanduser(file)
        #     img = Image.open(path)
        #     img.thumbnail((400, 400), Image.ANTIALIAS)  
        #     w, h = img.size
        #     result.paste(img, (x, y, x + w, y + h))  
        #     y = y+img.height+10

        # result.save(os.path.expanduser('pic1.gif'))
        print("Saved")

        self.frame_com = Frame(self,background="#232323")
        self.frame_com.pack(fill=X)
        self.con = StringVar()
        self.con.set('Confidence Level = '+str('%.2f' % self.confidence))
        label = tk.Label(self.frame_com, textvariable=self.con, font=tkfont.Font(family='Helvetica', size=12, slant="italic"),fg="#FFFFFF",bg="#232323")
        label.pack(side="left", fill="x", pady=0)

        self.frame_but = Frame(self,background="#232323")
        self.frame_but.pack(fill=X)

        temp_button = tk.Button(self.frame_but, text = "Results",command = self.destroy,height=3,width=10)
        temp_button.pack(side="top")

    def destroy(self) :
        try :
            self.frame_but.pack_forget()
            self.frame_com.pack_forget()
            self.frame_mathpix.pack_forget()
            self.frame_sol.pack_forget()
            self.controller.show_frame("Result_Page")
            for files in pics :
                if os.path.exists(files):
                    os.remove(files)
                else :
                    print(files,' Not found')
        except :
            print(Exception)
            pass
        self.res()



class Result_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#232323")
        #label = tk.Label(self, text="This is the Result Page", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)

        frame1 = Frame(self,background="#232323")
        frame1.pack(fill=X)
        button = ttk.Button(frame1, text="Sign Out", command=lambda: controller.show_frame("Login_Page"))
        button.pack(side="right")
        temp_name = "Welcome on-board"
        label = tk.Label(frame1, text=temp_name, font=tkfont.Font(family='Helvetica', size=12, weight="bold"), bg="#232323")
        label.pack(side="left", fill="x", pady=10)

        path = "logo.png"
        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')
        self.frame = Frame(self,background="#232323")
        self.frame.pack(fill=X)
        self.button = ttk.Button(self.frame, text="Answer", command=self.show)
        self.button.pack(side="left",padx=50,pady=100)
        #canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
        #vbar=Scrollbar(frame,orient=VERTICAL)
        #vbar.pack(side=RIGHT,fill=Y)
        #vbar.config(command=canvas.yview)
        #canvas.config(width=300,height=300)
        #canvas.config(yscrollcommand=vbar.set)
        #canvas.pack(side=LEFT,expand=True,fill=BOTH)
        ht = 200
        width = 10
            


    def show(self):   
        
        #myframe_outer = ttk.Frame(self)
        #mycanvas = tk.Canvas(myframe_outer, height=300, width=300)
        #myframe_inner = ttk.Frame(mycanvas)
        #myscroll = ttk.Scrollbar(myframe_outer, orient='vertical', command=mycanvas.yview)
        #mycanvas.configure(yscrollcommand=myscroll.set)

        #myframe_outer.pack()
        #mycanvas.pack()
        #myscroll.pack()
        #result_image = PhotoImage(file = 'result.gif')
        #mycanvas.create_window(0, 0, window=myframe_inner, anchor='nw')
        #ttk.Label(myframe_inner, image=result_image).grid(sticky='w')
        self.button2 = ttk.Button(self.frame, text="New", command=self.destroy)        
        self.button2.pack(side="left",padx=50,pady=100)
        
        try :            
            #result_image = PhotoImage(file = 'result.gif')
            result_image = PhotoImage(file = 'pic1.gif')
            #canvas.create_image(width,ht,image=result_image,anchor='w')
            w = Label(self.frame, image=result_image)
            w.photo = result_image
            w.pack(padx=70,pady=100)

            self.button.pack_forget()
        except :
            print("Error")
            pass

        if os.path.exists("result.gif"):
            os.remove("result.gif")
        
        #button3 = tk.Button(self.frame, text="Save", command=self.save)
        #button3.pack()

    def destroy(self) :
        pics.clear()
        try :
            self.frame.pack_forget()
            self.controller.show_frame("Input_Page")
        except :
            pass


    #def save(self) :
    #    f = filedialog.asksaveasfile(mode='w',defaultextension=".gif")
    #    print('F',f)
    #    if f is None:
    #        return#

    #    f.imwrite('result.gif')
    #    f.close()
    

# main 
if __name__ == "__main__":
    #SplashScreen()
    app = SampleApp()
    app.geometry("800x600+600+200")
    app.resizable(0,0)
    app.title('Solveq')

    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=confirm_exit)
    menubar.add_cascade(label="File", menu=filemenu)

    #app.config(menu=menubar)
    app.mainloop()
