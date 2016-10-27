import sys 
import os 
import pygame as p 
import tkinter 
import tkinter.messagebox 
import tkinter.font 

# Issues 
# None, it's perfect 

def main(): 
    p.init() 
    # Event handlers 
    def quit(): 
        root.destroy() 
    def work_timer(): 
        try: 
            p.mixer.music.load(work_stop_audio) 
        except: 
            print("Can't load 'Nyeah Stop.mp3'")
        stopped.set(True) 
        seconds.set(0) 
        minutes.set(work_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def break_timer(): 
        try: 
            p.mixer.music.load(break_stop_audio) 
        except: 
            print("Can't load 'Back to Work.mp3'") 
        stopped.set(True) 
        seconds.set(0) 
        minutes.set(break_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def start(): 
        if stopped.get(): 
            stopped.set(False) 
            root.after(100, decrement_timer)  
    def stop(): 
        stopped.set(True) 
    def decrement_break_timer(): 
        if break_minutes.get() > 1: 
            break_minutes.set(break_minutes.get()-1) 
        break_timer() 
    def increment_break_timer(): 
        if break_minutes.get() < 60: 
            break_minutes.set(break_minutes.get()+1) 
        break_timer() 
    def decrement_work_timer(): 
        if work_minutes.get() > 1: 
            work_minutes.set(work_minutes.get()-1) 
        work_timer() 
    def increment_work_timer(): 
        if work_minutes.get() < 60: 
            work_minutes.set(work_minutes.get()+1) 
        work_timer() 
    def about(): 
        tkinter.messagebox.showinfo("About this application", "Pomodoro Timer\nBy Xaqiri\nVersion 1.0.1\nOct 8, 2016 - Oct 26, 2016\n\nWritten in Python\nVersion 3.5.1") 
    def info(): 
        tkinter.messagebox.showinfo("Pomodoro info", "A productivity timer.\nWork for some number of minutes, break for a shorter amount.\n\nFor more in-depth info, check Wikipedia.") 
    def issues(): 
        tkinter.messagebox.showwarning("Known Issues", "None, this application is perfect.")
    def decrement_timer(): 
        if not stopped.get(): 
            seconds.set(seconds.get()-1) 
            if minutes.get() >= 0 and seconds.get() < 0: 
                minutes.set(minutes.get()-1) 
                seconds.set(59) 
            time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
            time.set(time_var)
            if minutes.get() <= 0 and seconds.get() <= 0: 
                try: 
                    p.mixer.music.play() 
                except: 
                    print("Audio could not be played") 
            else: 
                root.after(1000, decrement_timer) 
    # Audio 
    try: 
        work_stop_audio = os.path.join('..', 'audio', 'Nyeah Stop.mp3') 
        break_stop_audio = os.path.join('..', 'audio', 'Back to Work.mp3') 
    except: 
        print("Can't load audio") 
    # Root window 
    root = tkinter.Tk() 
    root.title("Pomodoro Timer") 
    root.resizable(width=True, height=True) 
    root.minsize(width=400, height=600) 
    root.maxsize(width=1000, height=800) 
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight() 
    x_offset = (screen_width//2) - 200 
    y_offset = (screen_height//2) - 300 
    root.geometry("{}x{}+{}+{}".format(400, 600, x_offset, y_offset))
    # Variables 
    f1 = tkinter.font.Font(family="comicsansms", size=16) 
    f2 = tkinter.font.Font(family="comicsansms", size=64) 
    f3 = tkinter.font.Font(family="comicsansms", size=10) 
    work_minutes = tkinter.IntVar() 
    break_minutes = tkinter.IntVar() 
    minutes = tkinter.IntVar() 
    seconds = tkinter.IntVar() 
    time = tkinter.StringVar() 
    work_minutes.set(25) 
    break_minutes.set(5) 
    minutes.set(work_minutes.get()) 
    seconds.set(0) 
    time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
    time.set(time_var)
    stopped = tkinter.BooleanVar() 
    stopped.set(True) 
    # Frames 
    button_bar = tkinter.Frame(root, bg="black") 
    main_frame = tkinter.Frame(root, borderwidth=10, padx=5, pady=5, bg="black") 
    timer_frame = tkinter.Frame(main_frame, bg="black")
    break_timer_frame = tkinter.Frame(main_frame, bg="black") 
    work_timer_frame = tkinter.Frame(main_frame, bg="black") 
    # Menu bar 
    menu_bar = tkinter.Menu(root) 
    file_menu = tkinter.Menu(menu_bar, tearoff=0) 
    file_menu.add_command(label="Exit", command=quit) 
    help_menu = tkinter.Menu(menu_bar, tearoff=0) 
    help_menu.add_command(label="Info", command=info)
    help_menu.add_command(label="About", command=about) 
    help_menu.add_command(label="Issues", command=issues)
    menu_bar.add_cascade(label="File", menu=file_menu) 
    menu_bar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menu_bar) 
    # Timer area 
    t = tkinter.Label(timer_frame, text="Pomodoro Timer", bg="black", fg="white", font=f1)
    timer = tkinter.Label(timer_frame, textvariable=time, bg="black", fg="white", font=f2) 
    # Time change area 
    dec_break_label = tkinter.Label(break_timer_frame, text="Break Time", bg="black", fg="white", font=f3) 
    dec_work_label = tkinter.Label(work_timer_frame, text="Work Time", bg="black", fg="white", font=f3) 
    break_min_label = tkinter.Label(break_timer_frame, textvariable=break_minutes, bg="black", fg="white", font=f1) 
    work_min_label = tkinter.Label(work_timer_frame, textvariable=work_minutes, bg="black", fg="white", font=f1) 
    # Buttons 
    work_button = tkinter.Button(button_bar, text="Work Timer", command=work_timer) 
    rest_button = tkinter.Button(button_bar, text="Break Timer", command=break_timer) 
    start_button = tkinter.Button(button_bar, text="Start Timer", command=start)
    stop_button = tkinter.Button(button_bar, text="Stop Timer", command=stop) 
    decrement_break_timer_button = tkinter.Button(break_timer_frame, text="-", command=decrement_break_timer) 
    increment_break_timer_button = tkinter.Button(break_timer_frame, text="+", command=increment_break_timer) 
    decrement_work_timer_button = tkinter.Button(work_timer_frame, text="-", command=decrement_work_timer) 
    increment_work_timer_button = tkinter.Button(work_timer_frame, text="+", command=increment_work_timer) 

    button_bar.pack(side=tkinter.TOP, fill=tkinter.X) 
    main_frame.pack(fill=tkinter.BOTH, expand=True) 
    work_button.pack(side=tkinter.LEFT) 
    rest_button.pack(side=tkinter.LEFT) 
    start_button.pack(side=tkinter.LEFT)
    stop_button.pack(side=tkinter.RIGHT) 
    t.pack() 
    timer_frame.pack(expand=True) 
    timer.pack() 
    break_timer_frame.pack(side=tkinter.LEFT) 
    work_timer_frame.pack(side=tkinter.RIGHT) 
    dec_break_label.pack(side=tkinter.TOP) 
    decrement_break_timer_button.pack(side=tkinter.LEFT) 
    break_min_label.pack(side=tkinter.LEFT) 
    increment_break_timer_button.pack(side=tkinter.LEFT) 
    dec_work_label.pack(side=tkinter.TOP) 
    decrement_work_timer_button.pack(side=tkinter.LEFT) 
    work_min_label.pack(side=tkinter.LEFT) 
    increment_work_timer_button.pack(side=tkinter.LEFT) 

if __name__ == "__main__": 
    main() 
    tkinter.mainloop() 
