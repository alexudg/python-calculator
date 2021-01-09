from tkinter import *
import parser

root = Tk()
root.title('Calculadora')

# display de resultados
display = Entry(root)
display.grid(row=0, columnspan=5, sticky=W+E)

#botones superiores
Button(root, text='←', command=lambda:backSpace() ).grid(row=1,column=0, sticky=W+E)
Button(root, text="CE").grid(row=1,column=1, sticky=W+E)
Button(root, text='C', command=lambda:clearDisplay() ).grid(row=1,column=2, sticky=W+E)
Button(root, text="+/-").grid(row=1,column=3, sticky=W+E)
Button(root, text='√', command=lambda:showOperator('√') ).grid(row=1,column=4, sticky=W+E)

#botones numericos y a la derecha de operacion
Button(root, text="7", command=lambda:showNumber(7) ).grid(row=2,column=0, sticky=W+E)
Button(root, text="8", command=lambda:showNumber(8) ).grid(row=2,column=1, sticky=W+E)
Button(root, text="9", command=lambda:showNumber(9) ).grid(row=2,column=2, sticky=W+E)
Button(root, text="/", command=lambda:showOperator('/') ).grid(row=2,column=3, sticky=W+E)
Button(root, text="%").grid(row=2,column=4, sticky=W+E)

Button(root, text="4", command=lambda:showNumber(4) ).grid(row=3,column=0, sticky=W+E)
Button(root, text="5", command=lambda:showNumber(5) ).grid(row=3,column=1, sticky=W+E)
Button(root, text="6", command=lambda:showNumber(6) ).grid(row=3,column=2, sticky=W+E)
Button(root, text="*", command=lambda:showOperator('*') ).grid(row=3,column=3, sticky=W+E)
Button(root, text="1/x").grid(row=3,column=4, sticky=W+E)

Button(root, text="1", command=lambda:showNumber(1) ).grid(row=4,column=0, sticky=W+E)
Button(root, text="2", command=lambda:showNumber(2) ).grid(row=4,column=1, sticky=W+E)
Button(root, text="3", command=lambda:showNumber(3) ).grid(row=4,column=2, sticky=W+E)
Button(root, text="-", command=lambda:showOperator('-') ).grid(row=4,column=3, sticky=W+E)
Button(root, text='=', command=lambda:calculate() ).grid(row=4,column=4, rowspan=2, sticky=N+E+S+W) #expandir en todas las direcciones

#botones inferiores a los numericos
Button(root, text="0", command=lambda:showNumber(0) ).grid(row=5, column=0,columnspan=2, sticky=W+E)
Button(root, text=".", command=lambda:showNumber('.') ).grid(row=5,column=2, sticky=W+E)
Button(root, text="+", command=lambda:showOperator('+')).grid(row=5,column=3, sticky=W+E)

i = 0
def showNumber(n):
    #global i # tomar la variable global y no generar una interna
    display.insert(len( display.get() ), n)
    #i+=1

def showOperator(o):
    #global i
    display.insert(len( display.get() ), o)
    #i+=1

def clearDisplay():
    display.delete(0, END)

def backSpace():
    cont = display.get()
    if len(cont): # si existe algo
        cont = cont[:-1] # quitar ultimo caracter
        clearDisplay() # 1ro limpiar
        display.insert(0, cont)
        #global i
        #i = len(cont)

def calculate():
    cont = display.get()
    clearDisplay()
    try:
        expr = parser.expr( cont ).compile() # import parser       
        result = eval(expr)
        display.insert(0, result)
    except expresion as identifier:
        display.insert(0, 'ERROR')
    

root.mainloop()