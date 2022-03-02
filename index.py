from bubble_turtle import bubble_sort
from insertion_turtle import insertion_sort
from selection_turtle import selection_sort
from merge_turtle import merge_call
import turtle,time

sc=turtle.Screen()
sc.setup(800,600)
sc.bgcolor("cyan")
turtle.title("Visualizing Sorting Algorithm")

def f():
    turtle.clear()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write("Thank You",align="center",font=("Times New Roman",50,"bold"))
    time.sleep(1)
    turtle.bye()
    
turtle.hideturtle()
turtle.penup()
turtle.goto(0,-70)
turtle.pendown()
turtle.write("Press\n1- Bubble sort\n2- Insertion sort\n3- Selection sort\n4- Merge sort\n5- Exit",align="center",font=("Times New Roman",20,"bold"))
turtle.onkey(bubble_sort,'1')
turtle.onkey(insertion_sort,'2')
turtle.onkey(selection_sort,'3')
turtle.onkey(merge_call,'4')
turtle.onkey(f,'5')
turtle.listen()
turtle.mainloop()
    

    
