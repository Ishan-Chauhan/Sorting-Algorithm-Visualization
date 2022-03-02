import turtle as t
import time

x,y=-150,-100

def bar(h,c="yellow"):
  global x,y
  t.pencolor("black")
  t.fillcolor("%s"%(c))
  t.begin_fill()
  for _ in range(4):
    if _%2==0:
      t.forward(20)
      t.left(90)
    else:
      t.forward(h)
      t.left(90)
  t.end_fill()
  t.penup()
  t.goto(x+20,y)
  t.pendown()
  x=x+20

def reset():
  t.clear()
  global x,y
  x,y=-150,-100
  t.penup()
  t.goto(x,y)
  t.pendown()
  

def bubble_sort(n=0.5):
  a=[198,230,142,163,173,110,194,143,172,134,104,193,175,130,142,164]
  t.clear()
  t.hideturtle()
  t.tracer(0,0)
  t.penup()
  t.goto(x,y)
  t.pendown()
  for i in a:
    bar(i)
  t.update()
  time.sleep(n)
  reset()
    
  for i in a:
    if(a.index(i)==0 or a.index(i)==1):
      bar(i,"red")
    else:
      bar(i)
  t.update()
  time.sleep(n)


  for i in range(len(a)-1):
      for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
              a[j],a[j+1]=a[j+1],a[j]
        reset()
        for k in range(len(a)):
          if(k==j or k==j+1):
            bar(a[k],"red")
          else:
            bar(a[k])
        t.update()
        time.sleep(n)
      reset()
      for k in range(len(a)):
        if(k>=len(a)-i-1):
          bar(a[k],"blue")
        else:
          bar(a[k])
      t.update()
      time.sleep(n)
  reset()    
  for i in a:
    bar(i)
  t.update()
  time.sleep(2)
  reset()
  t.hideturtle()
  t.penup()
  t.goto(0,-70)
  t.pendown()
  t.write("Press\n1- Bubble sort\n2- Insertion sort\n3- Selection sort\n4- Merge sort\n5- Exit",align="center",font=("Times New Roman",20,"bold"))


#bubble_sort()
