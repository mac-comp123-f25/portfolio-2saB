import tkinter as tk

"""
This example asks you to create a GUI program to reverse an input string and display it.  
To do this, you will need at least 3 GUI widgets: a Label to give instructions, 
an Entry widget for the user to type in the phrase to be reversed, and a Label to display the reversed phrase.
"""

class ReverseGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("String Reverser")

        # Instruction label
        instructionLabel = tk.Label(self.mainWin, text="Type a phrase and press Enter:")
        instructionLabel.grid(row=0, column=0, columnspan=2, pady=5)

        # Entry widget (store as object variable since we’ll access it later)
        self.entryBox = tk.Entry(self.mainWin, width=40)
        self.entryBox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Display label (to show the reversed string)
        self.outputLabel = tk.Label(self.mainWin, text="", fg="yellow")
        self.outputLabel.grid(row=2, column=0, columnspan=2, pady=5)

        # Optional quit button
        quitButton = tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)
        quitButton.grid(row=3, column=0, columnspan=2, pady=5)

        # Bind the Enter key to trigger the reversal
        self.entryBox.bind("<Return>", self.entry_response)

    def entry_response(self, event):
        # Get text from entry box
        user_input = self.entryBox.get()

        # Reverse the string
        reversed_text = user_input[::-1]

        # Display it in the output label
        self.outputLabel.config(text=reversed_text)

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = ReverseGui()
myGui.run()
