from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Fatemeh Alimardani Project')

my_font = Font(family='Times',
               size=30,
               weight='normal')

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg='peach puff',
                  bd=5,
                  fg='gray11',
                  highlightthickness=2,
                  selectbackground='dark salmon',
                  selectforeground='maroon')

my_list.pack(side=LEFT, fill=BOTH)

# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create an entry box
my_entry = Entry(root, font=('helvetica', 24), width=20)
my_entry.pack(pady=20)

# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)


# Button FUNCTIONS
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def delete_item():
    my_list.delete(ANCHOR)


def cross_off_item():
    # cross off the item
    my_list.itemconfig(my_list.curselection(),
                       fg='dark salmon')
    # get rid of selection bar
    my_list.selection_clear(0, END)


def uncross_item():
    # uncross off the item
    my_list.itemconfig(my_list.curselection(),
                       fg='gray11')
    # get rid of selection bar
    my_list.selection_clear(0, END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, 'fg') == 'dark salmon':
            my_list.delete(my_list.index(count))
        else:
            count += 1


# Menu FUNCTIONS
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir='C:/todo',
        title='save file')
    if file_name:
        if file_name.endswith('.txt'):
            pass
        else:
            file_name = f'{file_name}.txt'

        # delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, 'fg') == 'dark salmon':
                my_list.delete(my_list.index(count))
            else:
                count += 1

        # grab all the stuff from the list
        stuff = my_list.get(0, END)

        # open the file
        output_file = open(file_name, 'wb')

        # actually add the stuff to the file
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir='C:/todo',
        title='open file')

    if file_name:

        # delete currently open list
        my_list.delete(0, END)

        # open the file
        input_file = open(file_name, 'rb')

        # load the data from the file
        stuff = pickle.load(input_file)

        # output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)


def clear_list():
    my_list.delete(0, END)


# create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add items to menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)

# add drop down items
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=clear_list)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

# add some buttons
add_button = Button(button_frame, text='add item', command=add_item)
delete_button = Button(button_frame, text='delete item', command=delete_item)
cross_off_button = Button(button_frame, text='cross off item', command=cross_off_item)
uncross_button = Button(button_frame, text='uncross item', command=uncross_item)
delete_crossed_button = Button(button_frame, text='delete crossed item', command=delete_crossed)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
