
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import serial as sr
from tkinter.messagebox import showwarning

root = Tk()
root.title("SMARTHOME APP")
root.geometry("700x800")  # Adjust the size to fit the content



# Serial connection
ser1 = None

def send_command(command):
    global ser1
    if ser1:
        try:
            ser1.write(command.encode())
            receive()
        except Exception as e:
            showwarning(title="WARNING!!!", message=f"Error sending command: {e}")
    else:
        showwarning(title="WARNING!!!", message="Arduino not connected!")

def connect_arduino():
    global ser1
    try:
        comport = CB1.get()
        ser1 = sr.Serial(comport, baudrate=9600, timeout=1)
    except Exception as e:
        showwarning(title="WARNING!!!", message=f"Error connecting Arduino: {e}")

def disconnect_arduino():
    global ser1
    if ser1:
        ser1.close()
    ser1 = None

def receive():
    global ser1
    try:
        if ser1:
            data = ser1.readline()
            if len(data) > 0:
                message = data.decode('utf-8').strip()
                lb1.config(text=message)
    except Exception as e:
        showwarning(title="WARNING!!!", message=f"Error receiving data: {e}")
lb1 = Label(root, font="Times 20")
lb1.grid(row=5, column=0, columnspan=3)
# Background image
image_path3 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\bb.jpg"
try:
    bg_image = Image.open(image_path3)
    bg_image = bg_image.resize((1000, 800))  # Adjust the background image size to fit the window
    bg_image = ImageTk.PhotoImage(bg_image)
    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError as e:
    print(f'Không tìm thấy tệp: {e.filename}')

CB1 = ttk.Combobox(root, values=["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"])
CB1.place(x=15, y=10)
CB1.set("Chọn cổng COM:")

Button(root, text="CONNECT", font="Times 14", command=connect_arduino, height = 1, width = 15).place(x=170, y=30)
Button(root, text="DISCONNECT", font="Times 14", command=disconnect_arduino, height= 1, width = 15).place(x=170, y=70)
lb1
# Control buttons and images
image_path1 = r"C:\Users\ADMIN\Downloads\bongden.jpg"
image_path2 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\tv.jpg"
image_path4 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\door.png"
image_path5 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\đèn ngủ.png"
image_path7 = r"C:\Users\ADMIN\Downloads\tvtat.jpeg"
image_path6 = r"C:\Users\ADMIN\Downloads\tvbat.jpeg"
image_path8 = r"C:\Users\ADMIN\Downloads\tvtat.jpeg"
image_path9 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\mocuaa.png"
image_path10 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\dongcuaa.jpg"
image_path11 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\denngubat.jpg"
image_path12  = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\denngutat.jpg"
image11 = r"C:\Users\ADMIN\Downloads\images.png"
image12 = r"C:\Users\ADMIN\Downloads\ngu.png"
logo1 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\LOGO.png"
# Variables to track states
light_on = False
tv_on = False
door_open = False

def update_light_image():
    global light_on, anh1_label, anh2_label
    if light_on:
        anh1_label.place_forget()
        anh2_label.place(x=350, y=250) # vị trí ảnh đèn bật
    else:
        anh2_label.place_forget()
        anh1_label.place(x=350, y=250)  # vị trí ảnh đèn tắt

def update_tv_image():
    global tv_on, tv1_label, tv2_label
    if tv_on:
        tv1_label.place_forget()
        tv2_label.place(x=350, y=250)
    else:
        tv2_label.place_forget()
        tv1_label.place(x=350, y=250)

def update_door_image():
    global door_open, door1_label, door2_label
    if door_open:
        door1_label.place_forget()
        door2_label.place(x=350, y=250)
    else:
        door2_label.place_forget()
        door1_label.place(x=350, y=250)

def toggle_light(state):
    global light_on
    if state == "on":
        light_on = True
        send_command("mở đèn")
    elif state == "off":
        light_on = False
        send_command("tắt đèn đi")
    update_light_image()

def toggle_tv(state):
    global tv_on
    if state == "on":
        tv_on = True
        send_command("mở ti vi")
    elif state == "off":
        tv_on = False
        send_command("tắt ti vi")
    update_tv_image()

def toggle_door(state):
    global door_open
    if state == "open":
        door_open = True
        send_command("servo 0 độ")
    elif state == "close":
        door_open = False
        send_command("servo 90 độ")
    update_door_image()
on_button = None
off_button = None

def nutden():
    global on_button, off_button
    # Destroy previously created buttons
    if on_button:
        on_button.destroy()
    if off_button:
        off_button.destroy()
    global anh1_label, anh2_label

    on_button = Button(root, text="Mở đèn", font="Times 20", command=lambda: toggle_light("on"))
    on_button.place(x=330, y=500)
    
    anh1 = Image.open(image_path12)
    resize_anh1 = anh1.resize((200, 200))
    anh1 = ImageTk.PhotoImage(resize_anh1)
    anh1_label = Label(root, image=anh1)
    anh1_label.image = anh1  # Keep a reference to ensure the image displays correctly

    anh2 = Image.open(image_path11)
    resize_anh2 = anh2.resize((200, 200))
    anh2 = ImageTk.PhotoImage(resize_anh2)
    anh2_label = Label(root, image=anh2)
    anh2_label.image = anh2  # Keep a reference to ensure the image displays correctly

    off_button = Button(root, text="Tắt đèn", font="Times 20", command=lambda: toggle_light("off"))
    off_button.place(x=470, y=500)

    # Initial display
    update_light_image()

def nuttv():
    global on_button, off_button
    # Destroy previously created buttons
    if on_button:
        on_button.destroy()
    if off_button:
        off_button.destroy()
    global tv1_label, tv2_label

    on_button = Button(root, text="Mở TV", font="Times 20", command=lambda: toggle_tv("on"))
    on_button.place(x=330, y=500)
    
    tv1 = Image.open(image_path8)
    resize_tv1 = tv1.resize((200, 200))
    tv1 = ImageTk.PhotoImage(resize_tv1)
    tv1_label = Label(root, image=tv1)
    tv1_label.image = tv1  # Keep a reference to ensure the image displays correctly

    tv2 = Image.open(image_path6)
    resize_tv2 = tv2.resize((200, 200))
    tv2 = ImageTk.PhotoImage(resize_tv2)
    tv2_label = Label(root, image=tv2)
    tv2_label.image = tv2  # Keep a reference to ensure the image displays correctly

    off_button = Button(root, text="Tắt TV", font="Times 20", command=lambda: toggle_tv("off"))
    off_button.place(x=470, y=500)

    # Initial display
    update_tv_image()

def nutcua():
    global on_button, off_button
    # Destroy previously created buttons
    if on_button:
        on_button.destroy()
    if off_button:
        off_button.destroy()
    global door1_label, door2_label

    on_button = Button(root, text="Mở cửa", font="Times 20", command=lambda: toggle_door("open"))
    on_button.place(x=330, y=500)
    
    door1 = Image.open(image_path10)
    resize_door1 = door1.resize((200, 200))
    door1 = ImageTk.PhotoImage(resize_door1)
    door1_label = Label(root, image=door1)
    door1_label.image = door1  # Keep a reference to ensure the image displays correctly

    door2 = Image.open(image_path9)
    resize_door2 = door2.resize((200, 200))
    door2 = ImageTk.PhotoImage(resize_door2)
    door2_label = Label(root, image=door2)
    door2_label.image = door2  # Keep a reference to ensure the image displays correctly

    off_button = Button(root, text="Đóng cửa", font="Times 20", command=lambda: toggle_door("close"))
    off_button.place(x=470, y=500)

    # Initial display
    update_door_image()
label11 = Label(root, text="SMARTHOME UEH", font=("Times", 30), height=1, fg="yellow", bg="black").place(x=260, y=130)
#logo11 = Image.open(logo1): 
# logo11 = bg_image.resize((1000, 800))  # Adjust the background image size to fit the window
 #bg_image11 = ImageTk.PhotoImage(bg_image11)
 #background_label11 = Label(root, image=bg_image11)
 #background_label.place(x=100, y=100)
logo1 = r"C:\Users\ADMIN\OneDrive\Hình ảnh\Ảnh chụp màn hình\LOGO.png"
logo11 = Image.open(logo1)
logo11 = logo11.resize((120,100))  # Điều chỉnh kích thước hình nền để phù hợp với cửa sổ
bg_image11 = ImageTk.PhotoImage(logo11)

# Tạo Label để hiển thị hình nền
background_label11 =Label(root, image=bg_image11)
background_label11.place(x=550, y=10)
# Load and place images for control buttons
def ngu():
    send_command('đi ngủ')
def phim():
    send_command('xem phim')

try:
    image = Image.open(image_path1)
    resized_image = image.resize((150, 150))
    image1 = ImageTk.PhotoImage(resized_image)
    b1light = Button(root, image=image1, command=nutden)
    b1light.place(x=10, y=200)

    image2 = Image.open(image_path2)
    resized_image2 = image2.resize((150, 150))
    image3 = ImageTk.PhotoImage(resized_image2)
    b2light = Button(root, image=image3, command=nuttv)
    b2light.place(x=10, y=400)

    image4 = Image.open(image_path4)
    resized_image3 = image4.resize((150, 150))
    image5 = ImageTk.PhotoImage(resized_image3)
    b3light = Button(root, image=image5, command=nutcua)
    b3light.place(x=10, y=600)

    image6 = Image.open(image11)
    resized_image4 = image6.resize((150, 150))
    image7 = ImageTk.PhotoImage(resized_image4)
    b4light = Button(root, image=image7, command=phim)
    b4light.place(x=250, y=600)

    image8 = Image.open(image12)
    resized_image5 = image8.resize((150, 150))
    image9 = ImageTk.PhotoImage(resized_image5)
    b5light = Button(root, image=image9, command=ngu)
    b5light.place(x=500, y=600)

except FileNotFoundError as e:
    print(f'Không tìm thấy tệp: {e.filename}')

root.mainloop()