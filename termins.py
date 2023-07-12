from tkinter import *
from tkinter import ttk
#инициализируем глобальные переменные, так как код упакован в функции для распределения по файлам
questions = ['a','g']
trueAnswers = []
userAnswers = []

i = 0
#Methods
def getAnswer():
    global i
    global answer
    ans = answer.get()
    userAnswers.append(ans)
    i+=1
    print('a')

    

def termins():
    #инициализировали окно и задали его размеры
    window = Tk()
    window.title('Викторина по терминам')
    window.geometry("1020x800")
    #Заготовка

    for i in range(len(questions)):
        #Вопрос
        question= ttk.Label(window, 
                            text=f'Вопрос {i+1}. {questions[i]}',
                            font=("Courier", 20),
                            justify=LEFT,
                            wraplength=1000
                            )
        question.pack(anchor=W, pady=30, padx=40)        
    
        #Ответ
        answer = ttk.Entry(window,  
                        width=40, 
                        justify=LEFT, 
                        font=("Calibri", 20)
                        )
        answer.pack(anchor=W, padx=40, pady=20)
        
        #Кнопка отправки ответа
        btn = Button(text="Ответить", 
                        width=10, 
                        justify=CENTER,
                        font=('Courier',14),
                        command = getAnswer()
                        )
        btn.pack(anchor=W, pady=10, padx=40)

    #отображение окна
    window.mainloop()
termins()