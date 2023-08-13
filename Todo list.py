from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Todo List!')
root.geometry('500x500')

#Định nghĩa font chữ
my_font = Font(
    family = 'Iciel Nabila',
    size=14,
)

#Khung
my_frame = Frame(root)
my_frame.pack(pady=10)

#Listbox
my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg='SystemButtonFace',
    bd=0,
    fg='#464646',       
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)
my_list.pack(side=LEFT, fill=BOTH)


#Ds công việc
stuff = [
    # 'Learn Excel',
    # 'Learn SQL',
    # 'Learn Power BI',
    # 'Learn Python'
]

#Thêm danh sách công việc vào list box
for item in stuff:
    my_list.insert(END, item)


#Tạo thanh cuộn
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#Thêm thanh cuộn vào khung
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Tạo ô nhập
my_entry = Entry(root, font=('Helvetica', 14), width=26)
my_entry.pack(pady=5)

#Tạo khung nút
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions

#Xóa item
def deleteItem():
    my_list.delete(ANCHOR)

#Thêm item
def addItem():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

#Đánh dấu hoàn thành
def doneItem():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#dedede',)
    my_list.select_clear(0, END)

#Bỏ dấu hoàn thành
def unCrossItem():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#464646',)
    my_list.select_clear(0, END)

#Lưu danh sách
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir='/Users/meomongmerr/Documents/DA Project/Tkinter CRUD basic/',
        title='Save File',
        filetypes=(
        ('Dat Files', '*.dat'), 
        ('All Files', '*.*'))
    )
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

    #Lất tất cả công việc trong danh sách
    stuff = my_list.get(0, END)

    #Mở file
    output_file = open(file_name, 'wb')

    #Thêm công việc vào trong file
    pickle.dump(stuff, output_file)


#Mở danh sách
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir='/Users/meomongmerr/Documents/DA Project/Tkinter CRUD basic/',
        title='Open File',
        filetypes=(
        ('Dat Files', '*.dat'), 
        ('All Files', '*.*'))
    )
    if file_name:
        #Delete currently open list
        my_list.delete(0, END)
        #Open the file
        input_file = open(file_name, 'rb')

        #Load the data from the file
        stuff = pickle.load(input_file)

        #ouput stuff to the screen
        for item in stuff:
            my_list.insert(END, item)

#Xóa danh sách
def delete_list():
    my_list.delete(0, END)

#Tạo Menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
#Tạo danh sách menu con
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=delete_list)


#Tạo nút
delBtn = Button(button_frame, text='Delete Item', command=deleteItem)
addBtn = Button(button_frame, text='Add Item', command=addItem)
doneBtn = Button(button_frame, text='Done', command=doneItem)
unCrossBtn = Button(button_frame, text='Uncross Item', command=unCrossItem)

#Vị trí nút
delBtn.grid(row=0, column = 0)
addBtn.grid(row=0, column=1, padx=20)
doneBtn.grid(row=0, column=2)
unCrossBtn.grid(row=0, column=3, padx=20)


root.mainloop()