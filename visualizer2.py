import pygame
import sys 
import random
import time

#GLOBAL VARIABLES 
# these are the dimensions of the pygame screen window
width = 1800
height = 600

# this are the varaibles for the bars we will sort : we have the number of  bars, the width of the bars and the space between the bars 
num_bars = random.randint(100,200)   # the number of bars are randomly generated 
bar_width = 5
space = 1
bars = []

#this sets the sorting to false, so we can control when we start sorting 
sorting = False

blue = (0,0,255) # defines a golbal varaible for a color 

#here we initialise the screen and color it 
pygame.init()
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))


#this is the quicksort function
#this is the partition function that divides the array 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    
    for j in range(low , high): 
        pygame.event.get()
        # here we are redrawing the bars as we sort 
        for k in range(num_bars):
            pygame.event.get()
            x = int((k* bar_width) +  (k*space)  + (width -(num_bars*bar_width+ num_bars*space))/2)
            height = bars[k]
            if bars[k] is bars[j] or bars[k] is  bars[i]:
                color = (255,130,80)
            else:
                color = blue
            drawBar(x,height,color)
        #we update the screen after we sort 
        pygame.display.update()
        time.sleep(.001)
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
        screen.fill((255,255,255))
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


#this is a button function that we click to sort the function
def button(msg,x_coordinate,y_coordinate,width,height,screen_color,hover_color):
    global sorting 

    #gets position of the mouse
    mouse = pygame.mouse.get_pos()
    # checks if mouse is being clicked
    clcik = pygame.mouse.get_pressed()
  

    # if the mouse is hovering over a bar it changes the color and sets sorting varaible to true 
    if x_coordinate + width > mouse[0] > x_coordinate and y_coordinate + height > mouse[1]> y_coordinate:
        pygame.draw.rect(screen, hover_color,(x_coordinate,y_coordinate,width,height),0)

        if clcik[0] == 1:
            sorting  = True

    else:
        pygame.draw.rect(screen, screen_color,(x_coordinate,y_coordinate,width,height),0)
    
    #displays a font on the button 
    font = pygame.font.SysFont("comicsansms", 10 )
    text = font.render(msg, True ,(0,0,0))
    screen.blit(text, (x_coordinate +10,y_coordinate+10))
        

#this is our function to draw a bar
def drawBar(x,height, color ):
    pygame.draw.rect(screen,color, (x,400,bar_width,height),0)
    bars.append(height)

#here we are drawing bars with differnt height 
for i in range(num_bars):
    height = random.randint(-100,-10)
    x = int((i* bar_width) +  (i*space)  + (width -(num_bars*bar_width+ num_bars*space))/2)
    drawBar(x, height,blue)



while True:
    #here we are updating the eventes on the screen 
    pygame.event.get()
    button('Sort' , int(200-75/2) , 200 -25 , 75, 50 ,(230,230,230), (200,200,200) )
    pygame.display.update()

    # if you click sort button this loop end 
    if sorting:
        break

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#here we sort the bars 
quickSort(bars,0,len(bars)-1)
while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

