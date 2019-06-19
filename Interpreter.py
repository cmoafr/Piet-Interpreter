#Created by cmoa
#
#Check out http://www.dangermouse.net/esoteric/piet.html for more informations on this language


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import math
from time import sleep



filename = "Hello World.png"

debug = False



#Loading image
image = mpimg.imread(filename)
image = image[:,:,:3]
if(debug):
   plt.imshow(image)
   plt.show()
   print("imported version:")
   print(image)

height = image.shape[0]-1
width = image.shape[1]-1
image = (image*255).astype(int)
if(debug):
   print()
   print("integers values:")
   print(image)
img = np.tile(-999, [height+1, width+1])
for j in range(0,height+1):
   for i in range(0,width+1):
      c = image[j,i]
      if(np.array_equal(c,[0, 0, 0])): img[j,i]=-1
      if(np.array_equal(c,[255, 255, 255])): img[j,i]=0
      if(np.array_equal(c,[255, 192, 192])): img[j,i]=1
      if(np.array_equal(c,[255, 0, 0])): img[j,i]=2
      if(np.array_equal(c,[192, 0, 0])): img[j,i]=3
      if(np.array_equal(c,[255, 255, 192])): img[j,i]=4
      if(np.array_equal(c,[255, 255, 0])): img[j,i]=5
      if(np.array_equal(c,[192, 192, 0])): img[j,i]=6
      if(np.array_equal(c,[192, 255, 192])): img[j,i]=7
      if(np.array_equal(c,[0, 255, 0])): img[j,i]=8
      if(np.array_equal(c,[0, 192, 0])): img[j,i]=9
      if(np.array_equal(c,[192, 255, 255])): img[j,i]=10
      if(np.array_equal(c,[0, 255, 255])): img[j,i]=11
      if(np.array_equal(c,[0, 192, 192])): img[j,i]=12
      if(np.array_equal(c,[192, 192, 255])): img[j,i]=13
      if(np.array_equal(c,[0, 0, 255])): img[j,i]=14
      if(np.array_equal(c,[0, 0, 192])): img[j,i]=15
      if(np.array_equal(c,[255, 192, 255])): img[j,i]=16
      if(np.array_equal(c,[255, 0, 255])): img[j,i]=17
      if(np.array_equal(c,[192, 0, 192])): img[j,i]=18
if(debug):
   print()
   print("aliases numbes:")
   print(img)


#Error checking
if(-999 in img):
   print("\nUnidentified color detected")
   if(debug): print("\n\n",img,"\n")
   while(True): continue

#Start processing
for i in range(1,10): print()
x=0
y=0
old=img[0,0]
dir=0
orient=-1
stack=[]
if(debug):printedvalues=[]

for loops in range(1,1000000000000000000):
   oldx=x
   oldy=y
   old=img[oldy,oldx]
   attemps=0
   #Movement initialisation (Get current codel)
   check=np.tile(False, [height+1, width+1])
   check[oldy,oldx]=True
   edges=[[oldx,oldy]]
   listx=[oldx]
   listy=[oldy]
   while(len(listx)):
      loopx=listx.pop()
      loopy=listy.pop()
      for tempy in range(loopy-1,loopy+2):
         if(tempy>=0 and tempy<=height):
            for tempx in range(loopx-1,loopx+2):
               if(tempx>=0 and tempx<=width):
                  if((tempx==loopx) ^ (tempy==loopy)):
                     if(img[tempy,tempx]==old and not check[tempy,tempx]):
                        edges.append([tempx,tempy])
                        check[tempy,tempx]=True
                        listx.append(tempx)
                        listy.append(tempy)
   while "Hitting the wall or outside":
      #Get correct edge (sorting)
      if(orient==-1):
         if(dir==0): edges.sort(key = lambda x: (-x[0], x[1]))
         if(dir==1): edges.sort(key = lambda x: (x[1], x[0]))
         if(dir==2): edges.sort(key = lambda x: (x[0], -x[1]))
         if(dir==3): edges.sort(key = lambda x: (-x[1], -x[0]))
      else:
         if(dir==0): edges.sort(key = lambda x: (-x[0], -x[1]))
         if(dir==1): edges.sort(key = lambda x: (x[1], -x[0]))
         if(dir==2): edges.sort(key = lambda x: (x[0], x[1]))
         if(dir==3): edges.sort(key = lambda x: (-x[1], x[0]))
      x = edges[0][0]
      y = edges[0][1]
      x+=int(math.cos(0.5*dir*math.pi))
      y-=int(math.sin(0.5*dir*math.pi))
      #Get codel value
      new=-1
      if(x>=0 and y>=0 and x<=width and y<=height): new=img[y,x]
      if(debug):print("Debug|", oldx, oldy, old, "|", dir, orient)
      if(debug):print("Debug| -->", x, y, new)      
      #Execute function if necessary
      if(new==-1):
         attemps+=1
         if(attemps%2):
            orient*=-1
         else:
            dir=(dir-1)%4
         x=oldx
         y=oldy
         if(attemps==9):break #Stuck
      else:
         if(new==0): #Slide into the next color codel
            loop=[[-1,-1,-1]]
            attemps=0
            while "Not not going in a loop or on color codel":
               while "Not at the end of the line":
                  x+=int(math.cos(0.5*dir*math.pi))
                  y-=int(math.sin(0.5*dir*math.pi))
                  new=-1
                  if(x>=0 and y>=0 and x<=width and y<=height): new=img[y,x]
                  if(debug):print("Debug| -->", x, y, new, "|", dir, orient)
                  if(new): break
               if(new==-1): #If wall or outside
                  attemps+=1
                  x-=int(math.cos(0.5*dir*math.pi))
                  y+=int(math.sin(0.5*dir*math.pi))
                  if([x,y,dir] in loop): #Already there before: in a loop
                     attemps = 9
                     break
                  loop.append([x,y,dir])
                  orient*=-1
                  dir=(dir-1)%4
               else: #On color codel
                  attemps = 0
                  break
            old=new
         break
   
   #Start processing command
   if(attemps==9):break #Halt the program
   command=3*((math.floor((new-1)/3)-math.floor((old-1)/3))%6)+(new-old)%3
   if(debug):print("Debug| command value:",command)
   if(debug):print("Debug| action:",np.array(["noop","push","pop","add","sub","mult","div","mod","not","greater","pointer","switch","duplicate","roll","in num","in char","out num","out char"])[command])
   
   if(command==1):                                                   #Push
      size=1
      check=np.tile(False, [height+1, width+1])
      check[y,x]=True
      listx=[x]
      listy=[y]
      while(len(listx)):
         loopx=listx.pop()
         loopy=listy.pop()
         for tempy in range(loopy-1,loopy+2):
            if(tempy>=0 and tempy<=height):
               for tempx in range(loopx-1,loopx+2):
                  if(tempx>=0 and tempx<=width):
                     if((tempx==loopx) ^ (tempy==loopy)):
                        if(img[tempy,tempx]==new and not check[tempy,tempx]):
                           size+=1
                           check[tempy,tempx]=True
                           listx.append(tempx)
                           listy.append(tempy)
      if(debug):print("Debug| counted:",size,"tiles")
      stack.append(size)
   if(command==2 and len(stack)): stack.pop()                        #Pop
   if(command>=3 and command<=7 and len(stack)>1): #Calculations:
      result = 0
      a = stack[-2]
      b = stack[-1]
      if(command>=3): result = a+b                                   #Add
      if(command==4): result = a-b                                   #Substract
      if(command==5): result = a*b                                   #Multiply
      if(command==6): result = int(a/b)                              #Divide
      if(command==7): result = a%b                                   #Modulo
      stack.pop()
      stack[-1]=result
   if(command==8 and len(stack)):                                    #Not
      if(stack[-1]==0):
         stack[-1]=1
      else:
         stack[-1]=0
   if(command==9 and len(stack)>1):                                  #Greater
      result = 0
      if(stack[-2]>stack[-1]): result = 1
      stack.pop()
      stack[-1] = result
   if(command==10 and len(stack)): dir = (dir + stack.pop())%4       #Pointer
   if(command==11 and len(stack)):                                   #Switch
      temp = stack.pop()
      if(temp): orient*=-1*abs(temp)
   if(command==12 and len(stack)): stack.append(stack[-1])           #Duplicate
   if(command==13 and len(stack)>1):                                 #Roll
      nbrolls = stack.pop()
      depth = stack.pop()
      if(depth>0 and nbrolls):
         for i in range(1,nbrolls):
            if(nbrolls>0):
               stack.insert(-depth+1,stack.pop(-1))
            else:
               stack.append(stack.pop(-depth))
   if(command==14): stack.append(int(input("Input number: ")))       #In number
   if(command==15): stack.append(ord(input("Input char: ")))         #In char
   if(command==16 and len(stack)):                                   #Out number
      temp=stack.pop(-1)
      print(temp)
   if(command==17 and len(stack)):                                   #Out char
      temp=chr(stack.pop(-1))
      print(temp,end="")
   if((command==16 or command==17) and debug):
      printedvalues.append(temp)
      print()
   if(debug):print("Debug| stack:",stack,"\n\n")

   old=new

   if(debug): sleep(3)



print("\n\nProgram ended: Infinite loop with no action or trapped.\n")
if(debug): print("Debug| Pritend values:",printedvalues)
sleep(3)
