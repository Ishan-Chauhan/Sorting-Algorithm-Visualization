import turtle as t
import time

x,y=-150,0

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

def barm(h,c="yellow",y1=-250,i=0):
    global x
    x=-150+20*i
    t.pencolor("black")
    t.fillcolor("%s"%(c))
    t.begin_fill()
    t.penup()
    t.goto(x,y1)
    t.pendown()
    for _ in range(4):
        if _%2==0:
            t.forward(20)
            t.left(90)
        else:
            t.forward(h)
            t.left(90)
    t.end_fill()

def reset():
    t.clear()
    global x,y
    x,y=-150,0
    t.penup()
    t.goto(x,y)
    t.pendown()

def merge(v,w,a,b,x,y,n):
    reset()
    i,j, k = a,x,a
    while(i<=b and j<=y):
        if v[i] < v[j]:
            w[k],i = v[i], i+1
        else:
            w[k], j = v[j], j+1
        for q in range(len(v)):
            if(q==i):
                bar(v[q],"red")
            elif(q==j):
                bar(v[q],"blue")
            else:
                bar(v[q])
        for q in range(len(w)):
            if(w[q]==0):
                break
            barm(w[q],"yellow",-250,q)
        t.update()
        time.sleep(n)
        reset()
        k += 1
    while(i<=b):
        w[k],i,k = v[i],i+1,k+1
        for q in range(len(v)):
            if(q==i):
                bar(v[q],"red")
            elif(q==j):
                bar(v[q],"blue")
            else:
                bar(v[q])
        for q in range(len(w)):
            if(w[q]==0):
                break
            barm(w[q],"yellow",-250,q)
        t.update()
        time.sleep(n)
        reset()
    while(j<=y):
        w[k],j,k = v[j],j+1,k+1
        for q in range(len(v)):
            if(q==i):
                bar(v[q],"red")
            elif(q==j):
                bar(v[q],"blue")
            else:
                bar(v[q])
        for q in range(len(w)):
            if(w[q]==0):
                break
            barm(w[q],"yellow",-250,q)
        t.update()
        time.sleep(n)
        reset()
    for i in range(a,y+1):
        v[i] = w[i]
        for q in range(len(v)):
            if(q==i):
                bar(v[q],"red")
            elif(q==j):
                bar(v[q],"blue")
            else:
                bar(v[q])
        for q in range(len(w)):
            if(w[q]==0):
                break
            barm(w[q],"yellow",-250,q)
        t.update()
        time.sleep(n)
        reset()
    
def merge_sort(x,y,a,w,n):
    if x < y: 
        m = (x+y)//2
        merge_sort(x,m,a,w,n)
        merge_sort(m+1,y,a,w,n)
        merge(a,w,x,m,m+1,y,n)

def merge_call(n=0.5):
    t.clear()
    t.hideturtle()
    t.tracer(0,0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    a=[198,230,142,163,173,110,194,143,172,134,104,193,175,130,142,164]
    w=[0]*len(a)
    for i in a:
        bar(i)
    t.update()
    time.sleep(n)
    reset()
    merge_sort(0,len(a)-1,a,w,n)
    t.penup()
    t.goto(0,-70)
    t.pendown()
    t.write("Press\n1- Bubble sort\n2- Insertion sort\n3- Selection sort\n4- Merge sort\n5- Exit",align="center",font=("Times New Roman",20,"bold"))



#merge_call()
    
