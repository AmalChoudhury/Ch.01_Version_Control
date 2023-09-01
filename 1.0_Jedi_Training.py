'''
1.0 Jedi Training (17pts)  Name:Amal


1. Define Forking (1pt): 
A fork is a new repository that shares code with the original “upstream” repository.
2. Define Cloning (1pt): 
making an exact copy of a program, or anything
3. Define Branching (1pt):
creating copies of programs or objects in development to work in parallel versions, keep the original code and make chnages, and experiment on the branch
4. Define Committing (1pt): 
an operation which sends the latest changes of the source code to the repository
5. Define Merging (1pt): 
merges 2 programs and keeps what works, and throws out what dosent
6. Define Pushing (1pt):
the act of sending, or uploading, code from a branch in your local source code repository to a branch in the remote repository
7. Define Pull Request (1pt):
 initiates the process of integrating new code changes into the main project repository

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,90) #right eye
yoda.pendown()
yoda.circle(20)
yoda.penup()
yoda.goto(88,145)
yoda.penup()
yoda.setpos(-50,90)  #left eye
yoda.pendown()
yoda.circle(20)
yoda.penup()

yoda.goto(-50,50)
yoda.pendown()
yoda.goto(50,50)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')


yoda.write('Amal',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
