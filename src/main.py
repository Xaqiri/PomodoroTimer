import sys 
import tkinter 
import tkinter.messagebox 
import tkinter.font 

# Issues 
# Pressing the "Start Timer" button multiple times while the timer is running will 
# cause the timer to tick down much faster 

def main(): 
    # Event handlers 
    def quit(): 
        root.destroy() 
    def work_timer(): 
        seconds.set(0) 
        minutes.set(work_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def break_timer(): 
        seconds.set(0) 
        minutes.set(break_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def resume(): 
        stopped.set(False) 
        root.after(100, decrement_timer) 
    def stop(): 
        stopped.set(True) 
    def decrement_break_timer(): 
        seconds.set(0) 
        break_minutes.set(break_minutes.get()-1) 
        minutes.set(break_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def increment_break_timer(): 
        seconds.set(0) 
        break_minutes.set(break_minutes.get()+1) 
        minutes.set(break_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def decrement_work_timer(): 
        seconds.set(0) 
        work_minutes.set(work_minutes.get()-1) 
        minutes.set(work_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def increment_work_timer(): 
        seconds.set(0) 
        work_minutes.set(work_minutes.get()+1) 
        minutes.set(work_minutes.get()) 
        time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
        time.set(time_var) 
    def about(): 
        tkinter.messagebox.showinfo("About this application", "Pomodoro Timer\nBy Xaqiri\nVersion 1.0.0\nOct 8, 2016\n\nWritten in Python\nVersion 3.5.1") 
    def info(): 
        tkinter.messagebox.showinfo("Pomodoro info", "Placeholder.  Will update with info about what a Pomodoro timer is in the future.\n\nFor now, check Wikipedia.") 
    def decrement_timer(): 
        if not stopped.get(): 
            seconds.set(seconds.get()-1) 
            if minutes.get() >= 0 and seconds.get() < 0: 
                minutes.set(minutes.get()-1) 
                seconds.set(59) 
            time_var = "{}:{:02d}".format(minutes.get(), seconds.get())
            time.set(time_var)
            if minutes.get() <= 0 and seconds.get() <= 0: 
                tkinter.messagebox.showwarning("Ding!", "Time's up") 
            else: 
                root.after(1000, decrement_timer) 
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
    stopped.set(False) 
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
    start_button = tkinter.Button(button_bar, text="Work Timer", command=work_timer) 
    rest_button = tkinter.Button(button_bar, text="Break Timer", command=break_timer) 
    resume_button = tkinter.Button(button_bar, text="Start Timer", command=resume)
    stop_button = tkinter.Button(button_bar, text="Stop Timer", command=stop) 
    decrement_break_timer_button = tkinter.Button(break_timer_frame, text="-", command=decrement_break_timer) 
    increment_break_timer_button = tkinter.Button(break_timer_frame, text="+", command=increment_break_timer) 
    decrement_work_timer_button = tkinter.Button(work_timer_frame, text="-", command=decrement_work_timer) 
    increment_work_timer_button = tkinter.Button(work_timer_frame, text="+", command=increment_work_timer) 

    button_bar.pack(side=tkinter.TOP, fill=tkinter.X) 
    main_frame.pack(fill=tkinter.BOTH, expand=True) 
    start_button.pack(side=tkinter.LEFT) 
    rest_button.pack(side=tkinter.LEFT) 
    resume_button.pack(side=tkinter.LEFT)
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
