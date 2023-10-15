from tkinter import *
import csv
import random

with open("eng_quiz_data.csv", "r", encoding="cp949") as file:
    quiz = list(csv.reader(file))



def next_question():
    global answer
    global cnt

    for i in range(4):
        buttons[i].config(bg="#F0F0F0")

    multi_choice = random.sample(quiz, 4)
    answer = random.randint(0, 3)
    cur_question = multi_choice[answer][0]

    question_label.config(text=cur_question)

    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])

    cnt += 1
    count = Label(window, text='문제 수 : ' + str(cnt), font=("나눔바른펜"), bg='#F1D00A')
    count.place(x=0, y=0)



def check_answer(idx):
    global cnt
    global wrong
    global correct

    idx = int(idx)
    if answer == idx:
        buttons[idx].config(bg="green")
        window.after(50,next_question())
        correct += 1
        correct_cnt = Label(window, text='맞춘 개수 : ' + str(correct), font=("나눔바른펜"), bg='#F1D00A')
        correct_cnt.place(x=220, y=0)

    else:
        buttons[idx].config(bg="red")
        wrong += 1
        wrong_cnt = Label(window, text='틀린 개수 : ' + str(wrong), font=("나눔바른펜"), bg='#F1D00A')
        wrong_cnt.place(x=100, y=0)
        window.after(50,next_question())




window = Tk()
window.title('English Quiz')
window.config(padx=30,pady=10,bg="#21325E")

question_label = Label(window, width=20, height=2, text="test", font=("나눔바른펜", 25, "bold"),bg="#21325E",fg="white")
question_label.pack(pady=30)

buttons = []
for i in range(4):
    btn = Button(window,text=f"{i}",width=35, height=2, font=("나눔바른펜",15,"bold"),bg="#F0F0F0",command=lambda idx=i:check_answer(idx))
    btn.pack()
    buttons.append(btn)

next_btn = Button(window,text='Next',width=15,height=2,command = next_question,font=("나눔바른펜"),bg='#F1D00A')
cnt = 0
wrong = 0
correct = 0
next_btn.pack(pady=10)



next_question()


window.mainloop()