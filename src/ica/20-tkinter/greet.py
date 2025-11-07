import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        # Create three buttons
        quitButton = tk.Button(self.mainWin, text="Quit", command=self.quit_callback)
        quitButton.grid(row=0, column=0)

        helloButton = tk.Button(self.mainWin, text="Hello", command=self.hello_callback)
        helloButton.grid(row=1, column=0)

        goodbyeButton = tk.Button(self.mainWin, text="Goodbye", command=self.goodbye_callback)
        goodbyeButton.grid(row=2, column=0)

        self.welcomeLabel = tk.Label(self.mainWin, text="Welcome", fg="yellow")
        self.welcomeLabel.grid(row=1, column=1)



    def run(self):
        self.mainWin.mainloop()

    def quit_callback(self):
        self.mainWin.destroy()

    def hello_callback(self):
        # Change the label text to "Hello"
        self.welcomeLabel.config(text="Hello")

    def goodbye_callback(self):
        self.welcomeLabel.config(text="Goodbye")


# ----- Main program -----
myGui = BasicGui()
myGui.run()