import threading
import time
import tkinter as Tkinter


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Step Two")
        time.sleep(20)

class MyApp(Tkinter.Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)

        self.my_widgets()

    def my_widgets(self):
        self.grid()

        self.my_button = Tkinter.Button(self, text="Start my function",
                                          command=self.my_function)
        self.my_button.grid(row=0, column=0)

    def my_function(self):
        print("Step One")

        mt = MyThread()
        mt.start()

        while mt.isAlive():
            self.update()

        print("Step Three")

        print("end")

def main():
    my_app = MyApp()
    my_app.mainloop()

if __name__ == "__main__":
    main()