# #import packages
import numpy as np
import cv2
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
from crop_rectangle import ExampleApp
from custombutton import RoundedButton
from customlabel import RoundedLabel

window=tk.Tk()

#create user interference
class mywindow:
    #set up pop out windown
    def __init__(self, window):
        self.cropper = None
        self.detectimg = None
        self.dilfac = None
        self.window = window
        # Add left blue frame
        self.frameleft = tk.Frame(window, height = 900, width = 350, bg = '#71ABFF', bd =1)
        self.frameleft.place(x=0, y=0)
        # Add right white frame
        self.frameright = tk.Frame(window, height = 900, width = 1000, bg = 'white', bd =1)
        self.frameright.place(x=350, y=0)
        # Add topic
        self.topic = tk.Label(window, text="Automated", fg='white', bg = '#71ABFF',font=("Helvetica", 35, 'bold'))
        self.topic.place(x=40, y=150)
        self.topic = tk.Label(window, text="Cell Counter", fg='white', bg='#71ABFF', font=("Helvetica", 35, 'bold'))
        self.topic.place(x=40, y=200)
        # Add entry for dilution factor
        self.dill=tk.Label(window, text="Dilution factor:", fg='white', bg = '#71ABFF', font=("Helvetica", 10, 'bold'))
        self.dill.place(x=85, y=300)
        self.txtfld=tk.Entry(window, width= 10, bd=1)
        self.txtfld.place(x=185, y=302)
        # Design rounded corner buttons for upload and count
        self.imgb = RoundedButton(window, text="Upload",  border_radius=4, padding=4, color="white")
        self.imgb.place(x=80, y=350)
        self.imgb.bind('<Button-1>', self.uploadimg)
        self.countb=RoundedButton(window, text="Count",  border_radius=4, padding=4, color="white")
        self.countb.place(x=180, y=350)
        self.countb.bind('<Button-1>', self.count)
        # Add labels at the right frame
        # self.countb=RoundedLabel(window, color= "#71ABFF", text="Crop your image",  border_radius=4, padding=4)
        # self.countb.place(x=360, y=70)



    # Upload image
    def uploadimg(self, event):
        fn = tk.filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(
            ("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
        # When user cancel uploading, show "Please upload a image"
        if fn == '':
            self.upimgl = tk.Label(window, text="Please upload an image", fg='white',bg = '#71ABFF', font=("Helvetica", 8))
            self.upimgl.place(x=120, y=378)
            detectimg = None
        # When user finish uploading, call ExampleApp class to show and crop image
        else:
            self.cropper = ExampleApp(self.window, fn)
            self.cropper.pack(padx = 300, pady = 90, anchor='s')

    def count(self, _):
        # If no cropped image, do nothing until there is a cropped image
        if self.cropper is None:
            return
        self.dilfac = self.txtfld.get()
        #If no dilution factor in entry, print 'Please enter dilution factor' and do nothing until entry
        if self.dilfac is '':
            self.nonresult = tk.Label(window, text='Please enter dilution factor', fg='white',bg = '#71ABFF')
            self.nonresult.place(x=100, y=323)
            return
        # Get the cropped, resized image and show on canvas
        cropped = self.cropper.bigcropped
        # image proccesing to make circle detection more accurate
        newdetectimg = np.asarray(cropped)
        cv2.imshow("original", newdetectimg)
        blurimg = cv2.blur(newdetectimg, (2, 2))
        cv2.imshow("blur1", blurimg)
        cimg = cv2.cvtColor(blurimg, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", cimg)
        copycimg = newdetectimg.copy()
        canny = cv2.Canny(cimg, 80, 100)
        cv2.imshow("canny", canny)
        blurcanny = cv2.blur(cimg, (3,3))
        cv2.imshow("blur2", blurcanny)
        # count,draw and show numbers of circles
        circles = cv2.HoughCircles(blurcanny, cv2.HOUGH_GRADIENT, 1, 5,
                                   param1=118, param2=7, minRadius=1, maxRadius=3)
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            circledimg = cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 1)
        cv2.imshow('circled imge', circledimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # Calculate result according to diluent factor and show on right frame
        calculate = circles.shape[1] * int(self.dilfac) * 10000
        txt = "Cell concentration: " + str(calculate) +" cells/mL"
        self.result = tk.Label(window, text=txt, fg='black', font=("Helvetica", 16) , bg="white")
        self.result.place(x=370, y=570)
        
mywin = mywindow(window)
window.title('Automated cell counter')
window.geometry("1000x600+10+20")
window.mainloop()
