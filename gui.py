import tkinter as tk

class SpellingBeeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NYT Spelling Bee Cheater")

        self.mainLetterLabel = tk.Label(self.window, text="Center letter:")
        self.mainLetterLabel.pack()

        self.mainLetterEntry = tk.Entry(self.window)
        self.mainLetterEntry.pack()

        self.otherLettersLabel = tk.Label(self.window, text="Other letters:")
        self.otherLettersLabel.pack()

        self.otherLettersEntry = tk.Entry(self.window)
        self.otherLettersEntry.pack()

        self.button = tk.Button(self.window, text="Get Answers", command=self.displayAnswers)
        self.button.pack()

        self.resultLabel = tk.Label(self.window, text="Results:")
        self.resultLabel.pack()

    def displayAnswers(self):
        mainLetter = self.mainLetterEntry.get()
        otherLetters = self.otherLettersEntry.get()
        otherLetters = otherLetters.split(',')
        if len(otherLetters) == 1:
            otherLetters = otherLetters[0].split(' ')
        if len(otherLetters) == 1:
            otherLetters = list(otherLetters[0])
        self.resultLabel.config(text=f'Results: {mainLetter}, {otherLetters}')

    def run(self):
        self.window.mainloop()