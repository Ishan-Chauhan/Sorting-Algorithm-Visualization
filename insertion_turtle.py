import turtle as t
import time

x,y=-150,0

def bar(h,c="yellow",y1=0):
  global x
  t.pencolor("black")
  t.fillcolor("%s"%(c))
  t.begin_fill()
  t.penup()
  t.goto(x+20,y1)
  t.pendown()
  for _ in range(4):
    if _%2==0:
      t.forward(20)
      t.left(90)
    else:
      t.forward(h)
      t.left(90)
  t.end_fill()
  x=x+20

def reset():
  t.clear()
  global x
  x=-150
  t.penup()
  t.goto(x,y)
  t.pendown()

def insertion_sort(n=0.5):
  global x
  a=[198,230,142,163,173,110,194,143,172,134,104,193,175,130,142,164]
  t.hideturtle()
  t.tracer(0,0)
  t.clear()
  for i in a:
    bar(i)
  t.update()
  time.sleep(1)
  reset()

  for i in range(1,len(a)):
    key=a[i]
    for k in range(len(a)):
      if(a[k:] == a[i:]):
          bar(a[k],"red")
      else:
          bar(a[k])
    t.update()
    time.sleep(n)
    reset()

    for k in range(len(a)):
      if(a[k:] == a[i:]):
          bar(a[k],"red",-250)
      else:
          bar(a[k])
    t.update()
    time.sleep(n)
    reset()
    
    j=i-1
    while(j>=0 and key<a[j]):
        a[j+1]=a[j]
        a[j]=0
        j-=1
        for k in range(len(a)):
          if(a[k]!=0):
            bar(a[k])
          else:
            x=x+20
          if(k==i):
            x=x-20
            bar(key,"red",-250)   
        t.update()
        time.sleep(n)
        reset()
    a[j+1]=key

    for k in range(len(a)):
      if(k==j+1):
          bar(a[k],"red",-250)
      else:
          bar(a[k])
    t.update()
    time.sleep(n)
    reset()

    for k in range(len(a)):
      if(k==j+1):
          bar(a[k],"red")
      else:
          bar(a[k])
    t.update()
    time.sleep(n)
    reset()

    for k in range(len(a)):
      if(k<i+1):
          bar(a[k],"blue")
      else:
          bar(a[k])
    t.update()
    time.sleep(n)
    reset()
    
  for k in a:
    bar(k)
  t.update()
  time.sleep(2)
  reset()
  t.hideturtle()
  t.penup()
  t.goto(0,-70)
  t.pendown()
  t.write("Press\n1- Bubble sort\n2- Insertion sort\n3- Selection sort\n4- Merge sort\n5- Exit",align="center",font=("Times New Roman",20,"bold"))

#insertion_sort()

