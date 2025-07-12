import math
import random
import os
import time
import tkinter as tk

# FIRST TASK
def Prompted_Calculator():

    num1=float(input("First number: "))
    op=input("Operator: ")
    num2=float(input("Second number: "))

    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op =="*":
        result=num1/num2
    elif op=="/":
        if num2 !=0:
         result=num1/num2
        else:
         result="Error: cannot divide by zero"
    else:
        result="Invalid operation"

    print("Result: ",result)
    input("Press enter to exit")
#Prompted_Calculator() 

# SECOND TASK
def Number_Guessing_Game():
    correct_num=random.randint(0,100)
    guess_num=None
    
    while guess_num!=correct_num:
        guess_num=(int(input("Guess: ")))
        if guess_num>correct_num:
            print("To high")
        elif guess_num<correct_num:
            print("To low")
        elif guess_num==correct_num:
            print("Correct")
        else: 
            print("Invalid ")
#Number_Guessing_Game()

# THIRD TASK
def os_test():
    # Print current working directory
    print("Current folder:", os.getcwd())

    # Check if a file exists
    if os.path.exists("tasks.txt"):
        print("✅ 'tasks.txt' exists!")
    else:
        print("❌ 'tasks.txt' not found.")

     # List all files and folders in the current directory
    print("Contents of the folder:")
    
    for item in os.listdir():
        print("-", item)
#os_test()

# FOURTH TASK
def Dice_Rolling():
    history=[]
    while True:
        print("Choose an option")
        choice=input(" 1. Roll Dice \n 2. View History \n 3. Clear History \n 4. Quit \n ")
        if choice=="1":
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            history.append((die1,die2))
            print("You rolled", die1, "and", die2)
            input("Press enter to go back to menu")
        elif choice==("2"):
            print(history)
            input("Press enter to go back to menu")
        elif choice==("3"):
            history.clear()
            print("History Cleared")
            input("Press enter to go back to menu")
        elif choice==("4"):
            print("quiting in 3 sec...")
            time.sleep(1)
            print("quiting in 2 sec...")
            time.sleep(1)
            print("quiting in 1 sec...")
            time.sleep(1)
            break
#Dice_Rolling()

# FIFTH TASK
def clear_screen():
    os.system('cls')

def Dice_Rolling_With_File():
    while True:
        print("Choose an option")
        choice=input(" 1. Roll Dice \n 2. View History \n 3. Clear History \n 4. Quit \n ")
        if choice=="1":
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            with open("roll_history", "a") as file:
                    file.write(f"({die1},{die2})")
            print("You rolled", die1, "and", die2)
            input("Press enter to go back to menu")
            clear_screen()
        elif choice==("2"):
            with open("roll_history","r") as file:
                history=file.read()
                print("Roll History")
                print(history)
            input("Press enter to go back to menu")
            clear_screen()
        elif choice==("3"):
            with open("roll_history","w") as file:
                pass
            print("History Cleared")
            input("Press enter to go back to menu")
            clear_screen()
        elif choice==("4"):
            print("quiting in 3 sec...")
            time.sleep(1)
            print("quiting in 2 sec...")
            time.sleep(1)
            print("quiting in 1 sec...")
            time.sleep(1)
            break
#Dice_Rolling_With_File()


# SIXTH TASK
def Dice_Rolling_GUI():
    window=tk.Tk()
    window.geometry("500x700")


    def roll_dice():
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        result_label.config(text=f"You rolled: {die1} and {die2}")
        with open("roll_history","a") as file:
            file.write((f"({die1},{die2}) \n"))

    def show_history():
        with open("roll_history","r") as file:
            history=file.read()
            result_label.config(text=f"Your history \n {history}")

    def clear_history():
        with open("roll_history","w") as file:
            pass

    label=tk.Label(
        text="Dice Rolling Tool",
        fg="white",
        bg="grey2", 
        width=100,
        height=2,   
        font=("Arial",30)  
    )
    label.pack()

    result_label = tk.Label(
        text="Click 'Roll Dice' to begin.",
        fg="black",
        bg="white",
        font=("Arial", 14)
    )
    result_label.pack(pady=10)

    buttons=tk.Frame(window)
    buttons.pack()
    
    roll_dice=tk.Button(
        master=buttons,
        text="Roll Dice",
        command=roll_dice,
        fg="white",
        bg="grey2",
        width=20,
        height=2, 
    )
    roll_dice.pack(padx=20, pady=(200,0))

    view_history=tk.Button(
        master=buttons,
        text="View History",
        command=show_history,
        fg="white",
        bg="grey2",
        width=20,
        height=2, 
    )
    view_history.pack(padx=20, pady=(10,0))

    clear_history=tk.Button(
        master=buttons,
        text="Clear History",
        fg="white",
        command=clear_history,
        bg="grey2",
        width=20,
        height=2, 
    )
    clear_history.pack(padx=20, pady=(10,0))

    quit=tk.Button(
        master=buttons,
        text="Quit",
        fg="white",
        command=window.quit,
        bg="grey2",
        width=20,
        height=2, 
    )
    quit.pack(padx=20, pady=(10,0))

    window.mainloop()
Dice_Rolling_GUI()