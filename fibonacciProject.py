from tkinter import *

root = Tk()

root.title = "Fibonacci"
root.geometry = "1000x1000"

root.mainloop()

label_series = Label(root, text = "Fibonnaci Series")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    
    num = 10
    
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        
    label_flower["text"] = "The Flower Has Been Fully Bloomed"
    label_spiral["text"] = "The spirals in the left direction are: " + str(first_no) + ". " + "The spirals in the right direction are: " + str(second_no) + ". " + "Adding them together, we get " + str(sum) + " number of spirals in total."
        
btn = Button(root, text = "Show the Fibonacci Series", command = Fibbonaci)
        
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
