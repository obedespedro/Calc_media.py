from tkinter import *

def calcular():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    result = (n1+n2) / 2

    if result >= 9:
        final.set(str("Aprovado! Conceito Final: A"))
    elif result >= 7.5 and result <= 9:
        final.set(str("Aprovado! Conceito Final: B"))
    elif result >= 6 and result <= 7.5:
        final.set(str('Aprovado! Conceito Final: C'))
    elif result >= 4 and result <= 6:
        final.set(str('Reprovado! Conceito Final: D'))
    else:
        final.set(str('Reprovado! Conceito Final: E'))

#__________________________________________________________________________________________

root = Tk()
root.title("Calcular Media ")
root.geometry("260x120+0+0")
root.resizable(False,False)
#root.iconbitmap("C:\\Users\\Diego\\Documents\\Curso ADS\\ads\\1.ico")
root['bg'] = "#505050"

#___________________________________________________________________________________________

final = StringVar()
label1 = Label(root,text="Nota 01: ", bg="#505050", fg="#fff", width=13, anchor=W)
label2 = Label(root,text="Nota 02: ", bg="#505050", fg="#fff", width=13, anchor=W)

nota1 = Entry(root, bg="#505050", fg="#fff")
nota2 = Entry(root, bg="#505050", fg="#fff")

ver = Button(root, text="Calcular", command=calcular, bg="#505050", fg="#fff", anchor=W)
media = Label(root, textvariable=final, bg="#505050", fg="#fff")

label3 = Label(root,text="Por: Obedes Pedro ",font="Arial 6", bg="#505050", fg="#fff", width=13, anchor=E)

#___________________________________________________________________________________________

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

nota1.grid(row=0, column=1)
nota2.grid(row=1, column=1 )

ver.grid(row=2,column=0)

media.grid(row=3,column=1)
label3.grid(row=6,column=1)

#___________________________________________________________________________________________

root.mainloop()