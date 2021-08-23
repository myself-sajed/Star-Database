from tkinter import *
import tkinter.messagebox as tmsg


# TODO : Functions

# Function for submitting data into Text Area

def write_into_file():

    # Old method of Writing into files:
    # f = open("star.txt", "a")
    # f.write(f"1. Name   : {name_entry.get()}\n"
    #         f"2. Mobile  : {mobile_entry.get()}\n"
    #         f"3. Service : {service_entry.get()}\n__________________________"
    #         f"___________________")

    # New method of writing into files:

    # 1. Storing all the data into temp_file variable
    f = open("star.txt", "r")
    temp_file = f.read()
    f.close()

    f = open("star.txt", "w")

    if name_entry.get() == "":
        tmsg.showinfo("Error", "Please Enter the name")
        f.write(temp_file)
    elif mobile_entry.get() == "":
        tmsg.showinfo("Error", "Please Enter the mobile number")
        f.write(temp_file)
    elif service_entry.get() == "":
        tmsg.showinfo("Error", "Please Enter the service name")
        f.write(temp_file)
    elif date_entry.get() == "":
        tmsg.showinfo("Error", "Please Enter the date")
        f.write(temp_file)
    else:
        f.write(f"1. Name   : {name_entry.get()}\n"
                f"2. Mobile  : {mobile_entry.get()}\n"
                f"3. Service : {service_entry.get()}\n"
                f"4. Date     : {date_entry.get()}\n"
                f"_____________________________________________")
        f.write(temp_file)
        f.close()

        # New Member Added message box
        tmsg.showinfo("Star Xerox", "New Member Added Successfully ")
        mobile_entry.set("")
        name_entry.set("")
        service_entry.set("")
        


# Function For showing data on text Area


def show():
    t_area.delete(1.0, END)
    f = open("star.txt", "r")

    t_area.insert(1.0, f.read())

# Function for searching


def search():
    t_area.tag_remove('found', '1.0', END)
    s = search_me.get().capitalize()

    if s:
        idx = 1.0

        # code
        idx = t_area.search(s, idx, nocase=1, stopindex=END)

        try:
            if not idx:
                pass
                
            last_idx = '%s+%dc' % (idx, len(s))
            t_area.tag_add('found', str(idx), last_idx)

            idx = last_idx

            t_area.tag_config('found', foreground='red')

            t_area.see(idx)

            while 1:

                idx = t_area.search(s, idx, nocase=1, stopindex=END)

                if not idx:
                    break

                last_idx = '%s+%dc' % (idx, len(s))
                t_area.tag_add('found', idx, last_idx)

                idx = last_idx

                t_area.tag_config('found', foreground='red')

        except Exception:
            tmsg.showinfo("Star Search", f"Sorry! Couldn't find anything about : {s}")

    search_me.focus_set()


# TODO : Main Function


if __name__ == '__main__':
    ban = Tk()
    ban.geometry("1050x600")
    ban.title("Star Xerox Database                       - Designed by SHAIKH SAJED") 
    ban.wm_iconbitmap("star.ico")   
    ban.minsize(width=1050, height=600)

    # Adding Background Image

    try:
        pic = PhotoImage(file="pic.png")
        photo_label = Label(ban, image=pic)
        photo_label.pack()
    except Exception:
        ban.config(bg="powder blue")

    # Star Xerox Label

    Label(text="STAR XEROX DATABASE", font="timesnewroman 20 bold").place(relx=0.5, rely=0.018, width=500, height=30, anchor="n")

    # Frame 1 for Entry of name, mobile number and service

    frame1 = Frame(ban, bg="White")
    frame1.place(relx=0.25, rely=0.1, width=450, height=500, anchor="n")

    # Label for name and entry

    Label(frame1, text="Name", font="timesnewroman 15 bold", fg="black", bg="White").place(x=50, y=35)
    name_entry = StringVar()
    Entry(frame1, textvariable=name_entry, font="timesnewroman 15 ", borderwidth=3).place(x=150, y=35)

    # Label for phone and entry

    Label(frame1, text="Mobile", font="timesnewroman 15 bold", fg="black", bg="White").place(x=50, y=90)
    mobile_entry = StringVar()
    Entry(frame1, textvariable=mobile_entry, font="timesnewroman 15 ", borderwidth=3).place(x=150, y=90)

    # Label for service and entry

    Label(frame1, text="Service", font="timesnewroman 15 bold", fg="black", bg="White").place(x=50, y=140)
    service_entry = StringVar()
    Entry(frame1, textvariable=service_entry, font="timesnewroman 15 ", borderwidth=3).place(x=150, y=140)

    # label for date and entry
    Label(frame1, text="Date", font="timesnewroman 15 bold", fg="black", bg="White").place(x=50, y=190)
    date_entry = StringVar()
    Entry(frame1, textvariable=date_entry, font="timesnewroman 15 ", borderwidth=3).place(x=150, y=190)

    # Adding text frame and scroll bar

    scroll_bar = Scrollbar(ban)
    scroll_bar.place(relx=0.45, rely=0.1, width=25, height=500)
    t_area = Text(ban, font="Arial 15 ", bg="white", yscrollcommand=scroll_bar.set)
    t_area.place(relx=0.75, rely=0.1, width=500, height=500, anchor="n")

    scroll_bar.config(command=t_area.yview)

    # For adding submit button

    submit_button = Button(frame1, text="Add Member", bg="black", fg="White", command=write_into_file, font="timesnewroman 15")
    submit_button.place(x=150, y=250)

    # Display List
    display_button = Button(frame1, text="Display List", bg="black", fg="White", command=show, font="timesnewroman 15")
    display_button.place(x=150, y=300)

    # Search Button

    search_button = Button(frame1, text="Search", bg="black", fg="White", command=search, font="timesnewroman 15")
    search_button.place(x=150, y=450)

    search_me = Entry(frame1, font="timesnewroman 15 ", borderwidth=3)
    search_me.place(x=150, y=400)
    search_me.focus_set()

    Label(frame1, text="Enter Text", font="calibri 15 ", fg="black", bg="White").place(x=50, y=400)
    
    print("Success!")

    ban.mainloop()
