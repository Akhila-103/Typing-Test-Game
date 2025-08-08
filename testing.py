from english_words import get_english_words_set
from tkinter import *
import tkinter.font as font
import random
score = 0
missed = 0
time_elapsed = 0
count = 0
words = list(get_english_words_set(['web2'], lower=True))
# Start Game Function
def startGame():
    welcome.destroy()  # Close the welcome window
    start_typing_game()

def start_typing_game():
    global score, missed, time_elapsed, count, words

    def timeFunc():
        global time_elapsed, score, missed, count
        if count <= 10:
            time_elapsed += 1
            timer.configure(text=time_elapsed)
            timer.after(1000, timeFunc)
        else:
            result = Label(game, text='', font=('arial', 20, 'italic bold'), fg='grey')
            result.place(x=180, y=250)
            result.configure(text='Time taken = {} \n Score = {} \n Missed = {}'.format(
                time_elapsed, score, count - score))
            nextWord.destroy()
            userInput.destroy()
            scorelabel.destroy()
            scoreboard.destroy()
            timerlabel.destroy()
            timer.destroy()

    def mainGame(event):
        global score, missed, count
        if time_elapsed == 0:
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)
            timeFunc()

        if userInput.get() == nextWord['text']:
            score += 1
            scoreboard.configure(text=score)

        count += 1
        if count <= 10:
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)

    # Game Window
    game = Toplevel()
    game.geometry('700x600')
    game.title('Typing Speed Challenge')
    game.config(bg='honeydew2')

    label = Label(game, text='Typing Speed Challenge', font=('arial', 25, 'italic bold'), fg='gray', width=40)
    label.place(x=10, y=10)

    global nextWord, scorelabel, scoreboard, timerlabel, timer, userInput

    nextWord = Label(game, text='Hit Enter to Start', font=('arial', 20, 'italic bold'), fg='black')
    nextWord.place(x=30, y=240)

    scorelabel = Label(game, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
    scorelabel.place(x=10, y=100)

    scoreboard = Label(game, text=score, font=('arial', 25, 'italic bold'), fg='blue')
    scoreboard.place(x=100, y=180)

    timerlabel = Label(game, text='Time Elapsed:', font=('arial', 25, 'italic bold'), fg='red')
    timerlabel.place(x=500, y=100)

    timer = Label(game, text=time_elapsed, font=('arial', 25, 'italic bold'), fg='blue')
    timer.place(x=560, y=180)

    userInput = Entry(game, font=('arial', 25, 'italic bold'), bd=10, justify='center')
    userInput.place(x=150, y=330)
    userInput.focus_set()

    game.bind('<Return>', mainGame)

# Welcome Window
welcome = Tk()
welcome.geometry('600x600')
welcome.title("Typing Speed Challenge")
welcome.config(bg='LightBlue1')

headingFrame1 = Frame(welcome, bg="snow3", bd=5)
headingFrame1.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Typing Speed Challenge",
                     bg='azure2', fg='black', font=('Courier', 15, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(welcome, text="Start", bg='old lace', fg='black', width=20, height=2, command=startGame)
btn['font'] = font.Font(size=12)
btn.place(x=200, y=300)

welcome.mainloop()
