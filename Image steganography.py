from tkinter import * 
from tkinter import ttk 
import tkinter.filedialog 
from PIL import ImageTk 
from PIL import Image from tkinter import messagebox 
from io import BytesIO 
import os
class Stegno:
output_image_size = 0
def main(self, root):
root.title('ImageSteganography')
root.geometry(600×600')
root.resizable(width=False, height-False)
f = Frame(root)
title = Label(f, text='Image Steganography')
title.config(font=('courier', 33)) title.grid(pady=10)
b_encode = Button(f, text-"Encode",
command=lambda: self. framel_encode(f), padx=14) b_encode.config(font=('courier', 14))
b_decode = Button(f, text-"Decode", padx-14,
command=lambda: self.frame1_decode(f))
_decode.config(font=('courier', 14)) b_decode.grid(pady=12)
root.grid_rowconfigure(1, weight=1) root.grid_columnconfigure(0, weight-1)
f.gridO title.grid(row=1)
b_encode.grid(row=2)
_decode.grid(row=3)
def home(self, frame):
frame.destroy0 self.main(root)

def framel_decode(self, f):
f.destroy0
d f2 = Frame(root)
l1 = Label(d_f2, text-'Select Image with Hidden text:')
l1.config(font=('courier', 18)) l1.grido
bws_button = Button(d_f2, text 'Select',
command-lambda: self.frame2_decode(d_f2))
bws_button.config(font=('courier', 18)) bws_button.grid0
back button = Button(d_f2, text='Cancel',
command=lambda: Stegno.home(self, d_f2)) back_button.config(font=('courier', 18)) back_button.grid(pady=15) back_button.grid() d_f2.gridO
def frame2_decode(self, d_f2):
d_f3 = Frame(root)
myfile = tkinter.filedialog.askopenfilename(filetypes=(
[(png', "* png'), ('jpeg', "* jpeg'), ('jpg', "*jpg'), (All Files', '* **])) if not myfile:
messagebox.showerror("Error", "You have selected nothing!") else:
myimg = Image.open(myfile, 'r')
myimage = myimg. resize ((300, 200))
img = ImageTk.Photolmage(myimage)
14 = Label(d_f3, text-'Selected Image :')
14.config(font=('courier', 18))
14.gridO
panel = Label(d_f3, image=img)
panel.image = img
panel.grid(
hidden_data = self.decode (myimg)
12 = Label(d_f3, text='Hidden data is :')
12.config(font=(courier', 18)) l2.grid (pady=10)
text_area = Text(d_f3, width=50, height-10)
text_area.insert (INSERT, hidden_data) text_area.configure(state='disabled')
text_area.grid()
back button = Button(d_f3, text='Cancel',
command=lambda: self.page3(d_f3))
back_button.config(font=('courier', 11)) back button.grid(pady=15) back_button.grid0 d_f3.grid(row=1) d_f2.destroy0

def decode(self, image):
data="
imgdata = iter (image.getdata())
while (True):
pixels = [value for value in imgdata.__next_()[:3] +
imgdata.__next_0[:3] + imgdata. _next_0[:3]]
binstr = "
for i in pixels[:8]:
if i % 2 == 0: binstr += '0' else:
binstr += '1'
data += chr(int (binstr, 2)) if pixels[-11 % 2 != 0 return data
def framel encode(self, f):
f.destroy0
f2 = Frame(root)
labeLart = Label(f2, text="\°0°)/\") label_art.config(font=('courier', 70)) label_art.grid (row=1, pady=50)
11 = Label(f2, text-'Select the Image in which \you want to hide text:')
l1.config(font=('courier', 18)) l1.grid0
bws_button = Button(f2, text='Select',
command-lambda: self.frame2_ encode (f2))
bws_button.config(font=('courier', 18)) bws_button.grid0
back button = Button(
f2, text='Cancel', command lambda: Stegno.home(self, f2)) back_button.config(font=('courier', 18)) back_button.grid(pady=15) back_button.grid() f2.grid0

def frame2 encode(self. f2):
ep = Frame(root)
myfile = kinter.filedialog.askopenfilename(filetypes=(
[(png', "* png'), ('jpeg', "* jpeg'), (jpg', "* jpg'), ('All Files', "***])) if not myfile:
messagebox.showerror("Error", "You have selected nothing !") else:
myimg = Image.open(myfile)
myimage = myimg.resize ((300, 200))
img = ImageTk.Photolmage(myimage)
(3 = Label(ep, text='Selected Image')
13.config(font=('courier', 18))
13.grid0
panel = Label(ep, image=img)
panel.image = img
self.output_image_size = os.stat (myfile)
self.o_image_w, self.o_image_h = myimg.size
panel.grid(
(2 = Label(ep, text='Enter the message")
12.config(font=('courier', 18))
12.grid(pady=15)
text_area = Text(ep, width-50, height=10)
text_area.gridO
encode_button = Button
ep, text='Cancel', command-lambda: Stegno.home(self, ep)) encode_button.config(font=('courier', 11))
data = text_area.get("1.0", "end-1c")
back_button = Button(ep, text='Encode', command=lambda: [
self.enc_fun(text_area, myimg), Stegno.home(self, ep)]) back_button.config(font=('courier', 11)) back_button.grid(pady=15) encode_button.grid0 ep.grid(row=1) f2.destroy0
def genData(self, data):
newd = D
for i in data:
newd.append(format(ord(i), '08b')) return newd

def modPix(self, pix, data):
datalist = self.genData(data)
lendata = len(datalist)
imdata = iter(pix)
for i in range(lendata):
# Extracting 3 pixels at a time
pix = [value for value in imdata. _next_0[:3] +
imdata._next__0[:3] + imdata. next_0[:311
# Pixel value should be made
# odd for 1 and even for 0
for j in range (0, 8):
if (datalistifil== 'O') and (pix[il % 2 != 0):
if (pix[il % 2 != 0):
pix[i] -= 1
elif (datalist[i] [i] == '1') and (pix[il % 2 == 0): pix[i] -= 1
# Eighth pixel of every set tells
# whether to stop or read further.
# O means keep reading; 1 means the
# message is over.
if (i == lendata - 1): if (pix[-1] % 2 == 0): pix[-1] -= 1 else:
if (pix[-1] % 2 != 0): pix[-1] -= 1
pix = tuple(pix)
yield pix[0:3]
yield pix[3:6]
yield pix[6:9]
def encode_enc(self, newimg, data):
W = newimg.size[0]
(x, y) = (0, 0)
for pixel in self.modPix(newimg-getdata0, data):
# Putting modified pixels in the new image
newimg.putpixel((x, y), pixel) if (x == w - 1):
x= 0
y += 1 else:
x+=1

def
def enc_fun(self, text_area, myimg):
data = text_area.get("1.0", "end-1c")
if (len(data) == 0):
messagebox.showinfo("Alert", "Kindly enter text in TextBox") else:
newimg = myimg.copy0
self.encode_enc(newimg, data)
my_file = Bytesl00
temp = os.path.splitext(os.path.basename(myimg.filename))[0]
newimg.save(tkinter.filedialog.asksaveasfilename(
initialfile=temp, filetypes=(L('png', * png']), defaultextension=".png"))
self.d_image_size = my_file.tello
self.d_image_w, self.d_image_h = newimg.size
messagebox.showinfol
"Success", "Encoding Successful\File is saved as Image_with_hiddentext.png in the same directory")
def page3(self, frame):
frame.destroy)
self.main(root)
root = Tk0
0 = Stegnol)
o.main(root)
root.mainloop()