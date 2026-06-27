import tkinter as t
import tkinter.font as font
from math import pi 

answer = ""

def press(num):
    global answer
    answer += str(num)
    final_answer.set(answer)


def equal():
    try:
        global answer
        total = str(eval(answer))
        final_answer.set(total)
        answer = ''
    except:
        final_answer.set('ERROR')
        answer = ''


def clear():
    global answer
    answer = ''
    final_answer.set(answer)


if __name__ == "__main__":
    cal = t.Tk()
    cal.title("calculater")
    cal.geometry("260x348")

    final_answer = t.StringVar()
    fontSize = font.Font(size=14)

    nums_entry = t.Entry(cal, textvariable=final_answer, width=10)
    nums_entry.grid(columnspan=90, ipadx=89, ipady=10)

    button1 = t.Button(cal, text='1', command=lambda: press(1),
                        fg='black', bg='light pink', height=2, width=5, font=fontSize)
    button1.grid(row=3, column=0)

    button2 = t.Button(cal, text='2', command=lambda: press(2),
                    fg='black', bg='light pink', height=2, width=5, font=fontSize)
    button2.grid(row=3, column=1)

    button3 = t.Button(cal, text='3', command=lambda: press(3),
                    fg='black', bg='light pink', height=2, width=5, font=fontSize)
    button3.grid(row=3, column=2)

    button4 = t.Button(cal, text='4', command=lambda: press(4),
                    fg='black', bg='powder blue', height=2, width=5, font=fontSize)
    button4.grid(row=4, column=0)

    button5 = t.Button(cal, text='5', command=lambda: press(5),
                    fg='black', bg='powder blue', height=2, width=5, font=fontSize)
    button5.grid(row=4, column=1)

    button6 = t.Button(cal, text='6', command=lambda: press(6),
                    fg='black', bg='powder blue', height=2, width=5, font=fontSize)
    button6.grid(row=4, column=2)

    button7 = t.Button(cal, text='7', command=lambda: press(7),
                    fg='black', bg='PaleGreen', height=2, width=5, font=fontSize)
    button7.grid(row=5, column=0)

    button8 = t.Button(cal, text='8', command=lambda: press(8),
                    fg='black', bg='PaleGreen', height=2, width=5, font=fontSize)
    button8.grid(row=5, column=1)

    button9 = t.Button(cal, text='9', command=lambda: press(9),
                    fg='black', bg='PaleGreen', height=2, width=5, font=fontSize)
    button9.grid(row=5, column=2)

    buttonC = t.Button(cal, text='Clear', command=lambda: clear(),           
                       fg='black', bg='IndianRed3', height=2, width=5, font=fontSize)
    buttonC.grid(row=7, column=0)
    
    button0 = t.Button(cal, text=0, command=lambda: press(0),
                       fg='black', bg='BlanchedAlmond', height=2, width=5, font=fontSize)
    button0.grid(row=6, column=1)

    buttonDot = t.Button(cal, text='.', command=lambda: press('.'),
                         fg='black', bg='wheat', height=2, width=5, font=fontSize)
    buttonDot.grid(row=6, column=2)

    buttonDivision = t.Button(cal, text='/', command=lambda: press('/'),
                         fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonDivision.grid(row=3, column=3)

    buttonMultiplication = t.Button(cal, text='*', command=lambda: press('*'),
                         fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonMultiplication.grid(row=4, column=3)

    buttonSubtraction = t.Button(cal, text='-', command=lambda: press('-'),
                         fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonSubtraction.grid(row=5, column=3)

    buttonAddition = t.Button(cal, text='+', command=lambda: press('+'),
                         fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonAddition.grid(row=6, column=3)

    buttonEqual = t.Button(cal, text='=', command=lambda: equal(),
                           fg='white', bg='black', height=2, width=5, font=fontSize)
    buttonEqual.grid(row=7, column=3)

    buttonPercent = t.Button(cal, text='%', command=lambda: press('%'),
                             fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonPercent.grid(row=7, column=2)

    buttonCaret = t.Button(cal, text='x²', command=lambda: press('**'),
                           fg='black', bg='LightSeaGreen', height=2, width=5, font=fontSize)
    buttonCaret.grid(row=7, column=1)

    buttonPi = t.Button(cal, text='pi', command=lambda: press(pi),
                           fg='black', bg='wheat', height=2, width=5, font=fontSize)
    buttonPi.grid(row=6, column=0)

    cal.mainloop()