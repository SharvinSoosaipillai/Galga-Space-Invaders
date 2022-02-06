import pygame, sys, random, time #imports all of the different modules that I will use throughout this code
pygame.init() #initializes the surface of my pygame screen

width = 800 #determines the width of my pygame screen
height = 600#determine the height of my pygame screen
windowsize = (width,height) #scores the width and the height in a variable in order to be easier to understand

gamewindow = pygame.display.set_mode(windowsize) #Defining a variable that serves as the game winodw while setting the dementions with the width and height
pygame.display.set_caption("Galaga") #displaying the name of the pygame window


#Colours that are used throughout this pygame
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

background = pygame.image.load("images/background.png") #from the image folder, it takes out the image named background.png and stores it into this variable


#each element of the pygame is made through a function and does a certain thing in the pygame
def introduction (): #the introudction function is the introduction screen to the code
  intro = True #This variable is used for a while loop to constantly update the instructions screen, thus allowing the code to continuously run and see what will happen
  while intro:

    gamewindow.blit(background, (0,0)) #uses the variable background which is an image and shows it on the screen at a certain position 

    mouseposition = pygame.mouse.get_pos() #creating a variable to get the position of the mouse
    x, y = mouseposition #creating 2 more variable to understand the x and y position of the mouse, will be used later on when help tracking if the mouse is touching certain objects 
    
    font = pygame.font.SysFont("Courier New" , 40) #To create a font in python I first must establish that there is a font, thus using the pygame module, i import a font in a specific size to use for my introduction screen

    title = font.render("Welcome to Galga!", 1 , (white)) #creating a variable to use for the title screen, this displays the message "welcome to galga" in a white font
    titlesize = title.get_size() #this variable is assigned to get the size of the of the pervious variable (title) in order to determine the length and the height of the title
    gamewindow.blit(title, (width/2-titlesize[0]/2 , 0)) #the title is then put onto the screen by bliting the text to a certain position using the dementions of the text

    #this same concept is applied for all of the other text to show the start text, how to play text, highscore text, powerup text and the quit text. The only difference is that there is a variable assiened to each piece of text when it is blited onto the screen, which is used to check if the mouse button actually clicks on these pieces of text. 
    start = font.render("Start" , 3, (white))
    startsize = start.get_size()
    showstart = gamewindow.blit(start, (width/2-startsize[0]/2-125, height/4))


    howtoplay = font.render("How to play" , 3, (white))
    howtoplaysize = howtoplay.get_size()
    showhowtoplay = gamewindow.blit(howtoplay, (width/2-howtoplaysize[0]/2+125, height/4))


    highscore = font.render("Highscore" , 3, (white))
    highscoresize = highscore.get_size()
    showhighscore = gamewindow.blit(highscore, (width/2-highscoresize[0]/2-140, 2.2*(height/4)))


    powerup = font.render("Powerups" , 3, (white))
    showpowerup = gamewindow.blit(powerup, (width/2+20, 2.2*(height/4)))

    quit = font.render("Quit", 1 , (white))
    quitsize = quit.get_size()
    showquit = gamewindow.blit(quit, (width/2-quitsize[0]/2 , 400))

    pygame.display.update() #this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
    for event in pygame.event.get(): #use of a for loop to see if any event occurs in the pygame window. 
      if event.type == pygame.QUIT:#if one of the events is quitting the pygame (clicking on the x button at the top right), it goes into this if statement
        sys.exit() #exits the game
    
      if event.type == pygame.MOUSEBUTTONDOWN: #if the event is when the mouse button is pressed, it will go into this if statement 

        if showstart.collidepoint(mouseposition): #if the mouse position colides with the start text block, it will go into this if statement
          intro = False #sets the intro to false since they clicked start
          loading()#preforms all o the code in the instructions function
      
        if showhowtoplay.collidepoint(mouseposition): #if the mouse position collides with the how to play text block, it will go into this if statement 
          instructions() #preforms all of the code in the instructions function 
      
        if showhighscore.collidepoint(mouseposition):#if the mouse position collides with the high score text block, it will go into this if statement
          thehighscore() #preforms all of the code in the highscore function
      
        if showpowerup.collidepoint(mouseposition): #if the mouse position collides with the powerup text block, it will go into this if statement
          powerups() #preforms all of the code in the powerup function
      
        if showquit.collidepoint(mouseposition):#if the mouse position collides with the quit text block, it will go into this if statement
          sys.exit("Thank you for playing! ") #tells the user thank you for playing in the console and quits the pygame
    
    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place




def instructions(): #this is the instructions function and is called when the player clicks on the instructions piece of text on the introudction game screen (in the introduction function)
  gamebasics = True #creating a variable to use in a while loop to constantly update the screen for the user during the instructions function 
  while gamebasics:
    gamewindow.blit(background, (0,0)) #blits the background onto the pygame screen 
    mouseposition = pygame.mouse.get_pos() #this variable gets the mouse position using the pygame function
    x, y = mouseposition #the mouseposition is then assigned an x and y coordinate to determine where the mouse is on the screen at all times
    
    font = pygame.font.SysFont("Courier New" , 40)#To create a font in python I first must establish that there is a font, thus using the pygame module, i import a font in a specific size to use for my introduction screen

    instruction1 = font.render("Move using the A D Keys", 1 , (white))#creating a variable to assigne what kind of text I want to display at what size and colour
    instruction1size = instruction1.get_size() #this variable gets the length and width of the text
    gamewindow.blit(instruction1, (width/2-instruction1size[0]/2 , 0))#the text is then shown at a certain part at the screen using the blit function

    #this process is then repeated a couple of times in order to show all of the instructions on how to play the pygame, galaga

    instruction2 = font.render("Shoot with the spacebar", 1 , (white))
    instruction2size = instruction2.get_size()
    gamewindow.blit(instruction2, (width/2-instruction2size[0]/2 , 100))

    instruction4 = font.render("Avoid Getting hit by the enemies", 1 , (white))
    instruction4size = instruction4.get_size()
    gamewindow.blit(instruction4, (width/2-instruction4size[0]/2 , 200))

    instruction5 = font.render("Collect powerups to help you win", 1 , (white))
    instruction5size = instruction5.get_size()
    gamewindow.blit(instruction5, (width/2-instruction5size[0]/2 , 300))

    instruction7 = font.render("Lose 3 lives and you are dead!", 1 , (white))
    instruction7size = instruction7.get_size()
    gamewindow.blit(instruction7, (width/2-instruction7size[0]/2 , 400))

    back = font.render("back", 1 , (white))#in order to display a back button for the user to go back I create a back button by setting a bariable using the font from the beginning to show a piece of text called back
    backsize = back.get_size()#I then get the size of this piece of text in order to put the text in a certain position 
    backing = gamewindow.blit(back, (0 , height-backsize[1]))#this variable the blits the piece of text to the game window at a certain position (bottom left of the screen) and can be clicked on in order to go back to the introduction screen

    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
    for event in pygame.event.get(): #use of a for loop to get all of the events that can be preformed in pygame using the pygame.event.get() Function 
      
      if event.type == pygame.QUIT: #if the player clicks on the X button at the top right, it will go into this if statement
        sys.exit() #exits the pygame
      
      if event.type == pygame.MOUSEBUTTONDOWN: #If the type of event is when the mouse button is pressed down it will go into this if statement 
        if backing.collidepoint(mouseposition): #on this screen, there is a back button at the bottom left of the screen, when that button is clicked it will go into this function
          gamebasics = False #sets the value of gamebasics to false, breaking he game basics loop
          introduction() #goes back to the home screen by using the code in the introduction function

    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place



def thehighscore(): #if the player clicked on the highscore button on the home screen, it will go into this function to display the high score. 
  gamewindow.blit(background,(0,0)) #The background shown on the home screen is blitted onto the pygame screen and shown to the player
  onscreen = True #creating a variable to use in a while loop to continuously show the pygame screen 
  while onscreen:

    mouseposition = pygame.mouse.get_pos() #variable used to find the mouse position by using the built in pygame function 
    x, y = mouseposition #sets the mouse position to 2 variable, x and y to get the x and y position of the mouse

    highscore = open("HighScore.txt", "r") #this variable opens up an internal text file called highscore text, once the file is opened, the computer only reads the score
    highscore = highscore.read()#variable used to read the highscore stored in the text file


    font = pygame.font.SysFont("Courier New" , 40) #in order to get the font to show on the screen, I use the pygame font function which generates a font and a size 
    #this is a similar procedure to the start and how to play where I use the font variable to create a desired piece of text, get the size and blit it onto the pygame screen, the only difference is that I am concantonating a string onto the screen, thus making me use a plus sign to make the whole thing blit onto the screen
    highhscore = font.render("Current Highscore: " + highscore, 1 , (white))
    highscoresize = highhscore.get_size()
    gamewindow.blit(highhscore, (width/2-highscoresize[0]/2 , height/2 - highscoresize[1]/2))

    back = font.render("back", 1 , (white)) #in order to display a back button for the user to go back I create a back button by setting a bariable using the font from the beginning to show a piece of text called back
    backsize = back.get_size() #I then get the size of this piece of text in order to put the text in a certain position 
    backing = gamewindow.blit(back, (0 , height-backsize[1])) #this variable the blits the piece of text to the game window at a certain position (bottom left of the screen) and can be clicked on in order to go back to the introduction screen

    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
    for event in pygame.event.get():#use of a for loop to get all of the events that can be preformed in pygame using the pygame.event.get() Function 
      if event.type == pygame.QUIT: #if the player clicks on the X button at the top right, it will go into this if statement
        sys.exit()#exits the pygame
      if event.type == pygame.MOUSEBUTTONDOWN:#If the type of event is when the mouse button is pressed down it will go into this if statement 
        if backing.collidepoint(mouseposition):#on this screen, there is a back button at the bottom left of the screen, when that button is clicked it will go into this function
          onscreen = False #sets the value of onscreen to false, breaking he game basics loop
          introduction()#goes back to the home screen by using the code in the introduction function



def powerups():
  gamewindow.blit(background,(0,0)) #at the beginning of the code, the background is blited in order to be shown onto the screen
  powerupscreen = True #sets the value of powerupscreen to true so that this true value can be used in a while loop
  while powerupscreen:

    #the same procedure is used to establish a font, and get the mouses x and y position from the previous functions
    font = pygame.font.SysFont("Courier New" , 40)
    mouseposition = pygame.mouse.get_pos()
    x, y = mouseposition

    #the same procedue is used to show different pieces of text, in this case it is displaying the title of the screen using ther powerup text, getting the size and putting that piece of text at a specific position using the blit function 
    title = font.render("Powerups!", 1 , (white))
    titlesize = title.get_size()
    gamewindow.blit(title, (width/2-titlesize[0]/2 , 0))


    powerup1 = font.render("Rapid Fire: Bullet is faster", 1 , (white))
    powerup1size = powerup1.get_size()
    gamewindow.blit(powerup1, (width/2-powerup1size[0]/2 , 100))

    #the first powerup is a white circle and that is a rapid fire bullet function, what this powerup does is it make the bullets fire faster, to show an image of what the powerup looks like, I draw a circle using the pygame.draw feature to draw a circle onto the game window at a specific position with a specific radius
    pygame.draw.circle(gamewindow, white, (width/2, 175) , 10)

    #the same procedue is used to show different pieces of text, in this case it is displaying the title of the screen using ther powerup text, getting the size and putting that piece of text at a specific position using the blit function 
    powerup2 = font.render("Another Chance: Extra Life ", 1 , (white))
    powerup2size = powerup2.get_size()
    gamewindow.blit(powerup2, (width/2-powerup2size[0]/2 , 300))


    extralife = pygame.image.load("images/extralife.png") #the extra life powerup is a heart, in order to get that picture I use the pygame image load function and take the heart image that I have stored in my image files
    extralifesize = pygame.transform.scale(extralife, (50,50)) #since the heart is not the desired size that I want, I use this other function called the pygame transfrom scale function, which transforms the length and with of the image to my liking
    gamewindow.blit(extralifesize, (width/2 - 25 , 350)) #I then blit this image of the heart onto the game window 


    #similar to the piece of code above, these 3 lines create a back button using the font and place the back button on the bottom left of the screen
    back = font.render("back", 1 , (white))
    backsize = back.get_size()
    backing = gamewindow.blit(back, (0 , height-backsize[1]))

    for event in pygame.event.get():#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
      if event.type == pygame.QUIT:#if the player clicks on the X button at the top right, it will go into this if statement
        sys.exit()#exits the pygame
      if event.type == pygame.MOUSEBUTTONDOWN:#If the type of event is when the mouse button is pressed down it will go into this if statement
        if backing.collidepoint(mouseposition):#on this screen, there is a back button at the bottom left of the screen, when that button is clicked it will go into this function
          powerupscreen = False #sets the value of of powerup screen to false breaking the power up screen display loop
          introduction()#goes back to the home screen by using the code in the introduction function
    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place




def loading(): #once the player clicks on the start button on the introduction screen it will go into this function 
  gamewindow.fill(black) #fills the entire screen with a black colour
  count1 = 0 #variable used for an accumulator in order to create an effect of a loading screen 
  #this is a similar prodecure to the previous while loops used, instead of having a variable change, this loop is just using a true value as this is a loading screen
  while True:

    #these 4 lines of code create the font, render my desired text, get the size of the text and put in onto my game window at a certain position
    font = pygame.font.SysFont("Courier New" , 40)
    load = font.render("Loading..." , 1 , (white))
    loadsize = load.get_size()
    gamewindow.blit(load, (width/2-loadsize[0]/2 , height/2 - loadsize[1]/2))

    pygame.display.update() #constantly updating the display window 
    #since this is a loading screen (to create the effect that the game is getting ready), to create this effect I made it so the loading screen stays on the screen for 5 seconds and then appears it is done by the lines of code below 
    time.sleep(1) #waits for one second before continuing the next code 
    count1 += 1 #adds 1 to the counter set at the beginning (counter was originally zero)

    if count1 == 5:#each time this while loop runs it will wait 1 second before adding 1 to count, therefore once this if statement becomes true, that means 5 seconds have passed
      gameloop()#goes into the game loop function to preform the game
      break#breaks out of this while loop

    pygame.display.update() #contsantly updating the screen



def score(count):#there is a score in this game and is constantly updated whenever an action happens in the game. This function takes on 1 perameter and that is the current score (constantly updated in the game)
  font = pygame.font.SysFont("Courier New", 30) #making a font that will be used to show the score
  score = font.render("Score: " + str(count) , 1 , (white)) #creating a variable to show the desired text and score. the peramater (count), at the beginning of this code is the actual score that will be displayed to the player
  gamewindow.blit(score, (0,0))#puts the score at a specific position (top left of the screen)



def lives(count):#there is a lives feature in this game and is constantly updated whenever an action happens in the main game. This function takes on 1 perameter and that is the amount of lives you start off with 
  font = pygame.font.SysFont("Courier New", 30)#making a font that will be used to show the amount of lives
  lives = font.render("Lives: " + str(count) , 1 , (white))# creating a variable to show the desired text and lives. The perameter (count), at the beginning of this code is the amount of lives and is shown throughout the code
  livessize = lives.get_size()#gets the size of the text so that it can be displayed properly 
  gamewindow.blit(lives, (width-livessize[0],0))#puts the amount og lives at a specific position (top right of the screen)using the size of the text



def gameloop(): #this function is the main game loop and where the game takes place, it is called after the loading screen

  galgaship = pygame.image.load("images/boi.png") #before getting into the actual function, I need to first load in all of the objects/ sprites that I am going to use. All of the objects move on the screen, meaning that I would need to import all of them from my image files. This variable loads the image of the player ship
  shipx = width/2 #this is the starting x position of the ship and constantly changes throughout the code 
  shipy = height - 100#this is the starting y position of the ship and remain fairly constant throughout the code
  shipW = 100 #the width of the ship
  shipH = 100 #the height of the ship

  shipsize = pygame.transform.scale(galgaship, (shipW,shipH)) #since the ship is initally to big, I need to make the image smaller to it can fit onto the screen, by using the transform scale function in pygame I am able to tranfrom the width and the height of the image (which is a rectangle) to what I desire
  #in these next lines of code, I preform a similar procedure of getting the image from the image file and resizing it using the transform scale function. I do this for the playerbullet, enemy bullet all of the enemies, and the extra life powerup. 
  bullet = pygame.image.load("images/boi2.png")
  bulletsize = pygame.transform.scale(bullet, (50,50))
  
  enemy01 = pygame.image.load("images/Enemy1.png")
  enemy01size = pygame.transform.scale(enemy01, (100,100))

  enemy02 = pygame.image.load("images/Enemy2.png")
  enemy02size = pygame.transform.scale(enemy02, (100,100))
  
  enemy03 = pygame.image.load("images/Enemy3.png")
  enemy03size = pygame.transform.scale(enemy03, (100,100))

  enemy04 = pygame.image.load("images/Enemy4.png")
  enemy04size = pygame.transform.scale(enemy04, (100,100))

  bullet2 = pygame.image.load("images/bullet2.png")
  bullet2size = pygame.transform.scale(bullet2, (50,50))

  extralife = pygame.image.load("images/extralife.png")
  extralifesize = pygame.transform.scale(extralife, (50,50))
  

  background2 = pygame.image.load("images/background3.jpg") #I import the background and store it in this variable, because this is the background I will not change the size since I need this image to cover the entire screen (which it already does)
  backgroundy = 0 #the background is a relative moving background, meaning it moves on its own on the verticle axis. This variable is set at the beginning to the initial Y position of the background but constantly changes due to the relative movement

  #enemy fire abilities
  enemyfire = False #the bullet can only fire under a specific condition, so when the game starts, this condition is false
  enemybulletx = 0 #the x position of the enemy bullet
  enemybullety = 0 #the y position of the enemy bullet
  enemybulletspeed = 5 #the speed of the enemy bullet
  bullet2Vy = 0 #the velocity of the enemy bullet (constantly changed throughout the game)

  #player fire abilities
  bulletspeed = -6 #speed of the player bullet
  speed = 6  #sets the speed of other objects
  shipVx = 0 #ships x velocity (initially set to zero but constantly changed throughout the game)
  currentbulletx = shipx + 25 #the current player bullet x position initialized at the beginning of the game (which is in the middle of the ship)
  bullety = shipy+50 #the current player y position initilized at the beginning of the game (which is in the middle of the ship)
  bulletVy = 0 #The velocity of the bullets y position which is constantly updated throughout the code
  fire = False #sets the player bullet fire to false, meaning that the player can only fire the bullet under specific conditions, meaning when the game starts, this condition is false

  #sets the x and y position of the rapid fire powerup (setting it to a random x position and a set  y position)
  powerupx = random.randint(0,width-10)
  powerupy = -2000

  poweruptimer = False #in the game you can only use the rapid fire power up for a certain time, however when you don't have this powerup, you fire at a slower rate, this initializes at the beginning so that you fire at a slower rate until you get the powerup 

  #sets the x and y position of the extra life powerup (settting it to a random x position and a set Y position)
  extralifex = random.randint(0,width-50)
  extralifey = -3000

  count = 0 #count represents the score and is an accumulator constantly updated throughout the code
  lives_left = 3 #lives left represents the number of lives the player has left and represents an accumulator which is constantly updated throughout the code
  
  Xdirection = 1 #there is only 1 enemy that shoots and he moves on the x axis when this happens, this variable stores the direction he moves in, whether it is positive or negative 
  start_time = 0 #to create a timer within the code (for the rapid fire powerup), this variable holds the start time to when you first get the powrerup 
  enemyspeed = 1.1#this sets the enemy speed for all of the enemies moving down on the Y axis
  
  #Since there are 4 enemies these variables represent the X and y position of the enemies when the first start into the game (where each enemy has a random x position with a set y position)
  x1 = random.randint(0, width-100)
  y1 = -100
  x2 = random.randint(0,width-100)
  y2 = -240
  x3 = random.randint(0, width-100)
  y3 = -320
  x4 = random.randint(0, width-100)
  y4 = -520

  clock = pygame.time.Clock() #used to constantly update the fps (frames per second) in the game 

  while lives_left != 0: #this loop repeats until the player has zero lives left (since he starts off with 3 this loop begins right away)

    rely = backgroundy % background2.get_rect().height #This variable gets the remaining height from when the background moves down and devides it by the height of the actual background. It represents the relative y position and how much remainder does the background have when it is moving down (that way both of the images can move at the same rate )
    gamewindow.blit(background2, (0,rely - background2.get_rect().height )) #blits an image onto the screen of the background, in this case, this background is always moving down as the y position is changing making the relative y position change 
    if rely < height:#if the relative y position is bigger than the height it goes into this if statement (meaning if there is a bigger height than remainder of image left it goes into this if statement )
      gamewindow.blit(background2, (0, rely)) #blits an image of the same background at a different y position but using the same relative y. Making this image apear ontop of the the alreay moving down image to make it look like it is moving 
    backgroundy += 1 #changes the backgrounds Y position to constantly make it seem like it is moving 
    
    #these lines of code blit / draw all of the images on the screen, including the ship, enemies, extra life and rapid fire powerup. It draws them at a psecific x and y position on the screen that is constantly updated 
    gamewindow.blit(shipsize , (shipx, shipy))
    gamewindow.blit(enemy01size , (x1, y1))
    gamewindow.blit(enemy02size , (x2, y2))
    gamewindow.blit(enemy03size , (x3, y3))
    gamewindow.blit(enemy04size , (x4, y4))
    gamewindow.blit(extralifesize, (extralifex, extralifey))
    pygame.draw.circle(gamewindow, white, (powerupx, powerupy) , 10)


    powerupy += 3.5 #changes the height of the powerup to make it look like it slowly coming down from the top of the screen. 
    if powerupy > height: #if the powerups y position is bigger than the height of the screen it will go into this if statement 
      powerupy = -2000 #sets the y position of the powerup so that it is off the screen
      powerupx = random.randint(0,width-100) #sets the x position of the powerup to a random x position
    
    extralifey += 2.5 #changes the height of the extra life at a certain speed to make it look like it is solwly coming down
    if extralifey > height:  #if the extra life powerup y position is bigger than the height of the screen it will go into this if statement 
      extralifex = random.randint(0,width-100) #sets the x position of the powerup to a random x position 
      extralifey = -3000 #sets the Y position of the powerup so that it is very high above the screen 


    pygame.event.get()#this module gets all the possible events that could happen in pygame 
    keys = pygame.key.get_pressed() #variable is used to see if a key is pressed in python
    if keys[pygame.K_ESCAPE]: #if the key pressed down is the escape key it will go into this if sttemenet 
       sys.exit() #Exits the game 
    
    if keys[pygame.K_SPACE]: #if the space key is pressed it will go into this game
      fire = True #sets the value of fire to true
    if keys[pygame.K_a]:#if the a key is pressed it goes into this if statement 
      shipVx = -speed #changes the velocity of the ship by the negative value of speed
    elif keys[pygame.K_d]: #on the other hand if the d key is pressed it will go into this elif statement, the reason why this is elif is because the ship has to stay in place in no key is pressed (nither the d or a key)
      shipVx = speed #changes the horisontal velocity of the ship by positive speed
    else: #this else statement only runs if the d or a key is not pressed, meaning the ship is not in motion 
      shipVx = 0 #changes the horisontal velocity of the ship to zero 
      
    #ship boundries
    if shipx + 100 > width: #if the ship and its width are bigger than the width of the sceen it will go into this if statement (if the ship tries to pass the right side of the screen) 
      shipx = width - 100 #sets the x postion of the ship so that it touches the edge of the screen, but doesn't go past it

    if shipx < 0: #If the ships s postion is less that zero (the left side of the screen) it will go into this if statement 
      shipx = 0 #sets the ships x postion to zero which is the very left side of the screen

    score(count) #uses the function score and takes on the accumulator count (which is the score)
    lives(lives_left) #uses the function lives and takes on the accumlator lives_left(which is how many lives the player has left)


    #Player bullet firing 
    if not fire: #if the bullet has not been fired (or the space key has alreay been pressed) it will go into this if statement 
      currentbulletx = shipx + 25 #sets the player bullets z position the the shipsx x postion + 25 (to make it look like it is being fired from the middle of the ship)
      bulletVy = 0 #sets the ships verticle velocity to zero 
      bullety = shipy + 50 #sets the y postion of the ship to the ships y position plus 50 (that way it is inside of the ship)

    if fire == True: #once the player presses the spacebar, fire will be true and this if statement will run 
      gamewindow.blit(bulletsize, (currentbulletx, bullety)) #generates a bullet image using the bullets x and y position 
      bulletVy = bulletspeed#changes the bullets velocity by the bullet speed 


    shipx = shipx + shipVx #changes the ships x position by the velocity 

    #these 4 lines make it so that the enemy ships y position is constantly updated to make it look like it is moving down and a certain speed 
    y1 += enemyspeed
    y2 += enemyspeed
    y3 += enemyspeed
    y4 += enemyspeed

    #one of the enemy ships move from right to left at a certain height, this code does that 
    if y4 >= 100: #if the y position of the ship is bigger than or equal to 100 it will go into this if statement 
      y4 = 100 #changes the y position of the ship to equal 100
      x4 += 3* Xdirection #changes it so that the enemy ship can move right using the direction x variable

    #x cordinate boundries of moving enemy ship 
    if x4 + 100 > width: #if the x position plus the width of the enemy ship is bigger than the width of the screen it will go into this if statement 
      Xdirection = -1 #changes the x direction to -1 causing the ship to move in the opposite direction (left)
    
    if x4 < 0: #if the x position of the ship is less than zero it will go into this if statement 
      Xdirection = 1 #changes the x direction to positive 1 causing the ship to move in the right direction 


    #enemy ship fire
    if (x4 == shipx and y4 == 100) or (x4 + 1 == shipx and y4 == 100) or (x4 + 1 == shipx and y4 == 100) or (x4 + 3 == shipx and y4 == 100) or (x4 + 5 == shipx and y4 == 100) or (x4 -1 == shipx and y4 == 100)or (x4 -3 == shipx and y4 == 100) or (x4 -5 == shipx and y4 == 100): #this if statement checkts to see if the x position of the enemy ship moving left to right has the same or a similar x position to the player ship if that is true, it will go into this if statement 
      enemyfire = True #sets the enemy fire to true, allowing the enemy ship to shoot back at the player


    if not enemyfire: #if the enemy ship has not fired the bullet, this if statement will be true and the code will go into here
      enemybulletx = x4 + 50 #sets the x position of the bullet 
      enemybullety = y4 + 100 #sets the y position of the bullet 
      bullet2Vy = 0 #sets the verticle velocity of the bullet 

    if enemyfire == True: #once enemy fire is true, that means the ships have a similar or same x position, making the code go into this if statement 
      gamewindow.blit(bullet2size, (enemybulletx, enemybullety)) #blits an enemy bullet onto the screen at a specific x and y position
      bullet2Vy = enemybulletspeed #changes the bullets verticle velocity by the enemy bullet speed defined prior to the game loop 

    #if the enemy bullet misses the the player and goes of the screen, it goes into this if statement 
    if enemybullety > height:
      bullet2Vy = 0#changes the bullets verticle velocity to zero 
      enemybullety = y4 #changes the bullets x position 
      enemybulletx = x4 #changes the bullets y position 
      enemyfire = False #makes the enemy fire false that way it doesn't constantly fire all the time 


    #since the remaining 3 enemy ships are always moving down, if they get to the end of the player screen, it will go into this if statement 
    if y1 + 100 > height: #if the y position of the enemy ship is about the same as the width of the screen it will go into this if statement 
      y1 = -200 #changes the y position so the ship goes back to the top of the screen
      x1 = random.randint(0, width-100) #changes the x position so that the enemy can go to a different left and right position 
      lives_left-=1 #since the ship passed the player, that means they have lost a life, so in this line of code I subtract the lives left by one 
    if y2 + 100 > height: #the same concept is applied for the next 2 ships 
      y2 = -440
      x2 = random.randint(0, width-100)
      lives_left-=1
    if y3 + 100 > height:
      y3 = -320
      x3 = random.randint(0, width-100)
      lives_left-=1


    bullety = bullety + bulletVy #changes the bullets y position so that it is constantly updated 
    enemybullety = enemybullety + bullet2Vy #changes the enemy bullets y position so that it is constantly updated 

    #creates a rectangle for all of the objects that are used on the screen, including all of the powerups, player ships, enemy ships and bullets 
    shiprect = pygame.Rect(shipx,shipy,100,100)
    bulletrect = pygame.Rect(currentbulletx, bullety, 50,50)
    enemy1rect = pygame.Rect(x1, y1, 100,100)
    enemy2rect = pygame.Rect(x2, y2, 100,100)
    enemy3rect = pygame.Rect(x3, y3, 100,100)
    enemy4rect = pygame.Rect(x4, y4, 100,100)
    bullet2rect = pygame.Rect(enemybulletx, enemybullety, 50,50)
    poweruprect = pygame.Rect(powerupx - 10, powerupy - 10, 20, 20) #since the circle is not a rectangle, I used fidderent properties, since the x position of a rectangle starts at the top left of the image, I subtracted the circles radius by the x position to get the top left corner, from there I got the width and height of the rectangle from the diamater of the circle 
    extraliferect = pygame.Rect(extralifex, extralifey, 50,50)


    #collision detection 
    if bulletrect.colliderect(enemy1rect): #if the player bullets rectangle collides with the enemy ship rectangle it goes into this if statement 
      count += 1 #changes the count accumlator (score) and increases it by 1 
      y1 = -200 #sets the x position of the rectangle so that it is off the screen
      x1 = random.randint(0, width-100) #sets the x position of the rectangle so it is at a random left and right position 
      fire = False #sets the value of the playerfire to false that way when they click spacebar again, they will be able to shoot their projectile again 
    if bulletrect.colliderect(enemy2rect): #this same concept is applied for all of the enemy ships (enemy2, enemy 3 and enemy 4)
      count += 1
      y2 = -440
      x2 = random.randint(0, width-100)  
      fire = False
    if bulletrect.colliderect(enemy3rect):
      count += 1
      y3 = -320
      x3 = random.randint(0, width-100)  
      fire = False
    if bulletrect.colliderect(enemy4rect):
      count += 1
      y4 = -220
      x4 = random.randint(0, width-100)
      fire = False
    if bullet2rect.colliderect(shiprect):# if the enemy bullets rectangle colides with the player rectangle then it goes into this if statement 
      lives_left -= 1 #subtracts the lives left by 1 
      enemyfire = False #sets the enemy fire to false that way they will be able to fire again 
    if shiprect.colliderect(extraliferect):#if the player rectangle collides with the extra life rectangle, then it goes into this if statement 
      extralifex = random.randint(0,width-100) #changes the x position of the extralife rectangle to a random x position 
      extralifey = -3000 #changes the y position of the extra life 
      lives_left += 1 #increases the lives the player has by 1 

    if shiprect.colliderect(poweruprect):#if the player ship collides with one of the rapid fire powerup, it goes into this if statement 
      bulletspeed = -24 #changes the player bullet speed to -24 making it faster 
      powerupy = -3000 #changes the powerups y position so that it is very high off the screen 
      print ("You got a powerup") #prints in the console that the player got a powerup 
      start_time =pygame.time.get_ticks() #creates a start timer to get the current time when the player got the powerup 
      poweruptimer = True #sets the poweruptimer variable to true, 

    
    #powerup timer 
    if poweruptimer == True: #if the player got the rapid fire powerup, that means that this statement is true and will go into this if statement 
      seconds = (pygame.time.get_ticks() - start_time)/1000 #in order to get the amount of seconfs that he has the powerup for, this variable takes the current time and subtracts the original time he had gottent the powerup (from the if statement above) it then divides the result by 1000 as it is measured in milliseconds 
      if seconds >= 5: #if 5 seconds have passed (using the seconds variable) it goes into this if statement 
        bulletspeed = -6 #changes the bullet speed back to the original speed of -6
        print ("Powerup timer is over") #prints in the console to tell the user the powerup timer is over 
        poweruptimer = False #sets the value of the powerup timer to false that way when the player gets another powerup then this code can be reused 
    elif poweruptimer == False: #if the powerup timer is set to false (such as at the beginning of the game or after the player powerup is over) then it will go into this elif statement 
      bulletspeed = - 6 #sets the bullet speed back to -6


    if shiprect.colliderect(enemy1rect) or shiprect.colliderect(enemy2rect) or shiprect.colliderect(enemy3rect) or shiprect.colliderect(enemy4rect):#if any of the enemy ships collide with the player ship then it goes into this if statement 
      lives_left = 0 #sets the lives left to zero causing the game to be over 


    #increasing the enmy speed 
    if count != 0: #if the score is not zero it will go to this if statement (as at the beginning of the game the code underneath could run on its own )
      if count%10 == 0: #if the remainder of the player score divided by 10 is equal to zero then it will go into this if statement 
        enemyspeed += 0.005 #increases the speed of the player by a set amount, the reason why this number is very small is because this will continue to run until the player hits another enemy ship, if the number was larger then the enemies would move much faster too quickly 
        
    if bullety < 0: #if the y position of the players bullet is less than zero (off the screen, it will go into this if statement) 
      fire = False #sets the fire to false, allowing the player to fire again once they click on the spacebar
      bulletVy = 0 #sets the verticle velocity to zero 
      bullety = shipy + 50 #sets the bullets y position back the to the current y position of the ship 
      currentbulletx = shipx #sets the bullets x position to the current x position of the ship 

    clock.tick(60) #constantly updating the game to run at 60 frames per second in order for the game to run smoothly 
    pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place

  #this statement is outside of the while loop and will only run when the while loop is complete (when the player has no lives)
  if lives_left == 0: #confirms the player has zero lives before preforming the code 
    gameoverscreen = True #creates a varaible to act as the game over screen to be constantly updated 
    while gameoverscreen: #while the gameover screen variable is still true this code will run 
      gamewindow.fill(black) #fills the screen in a black colour 

      font = pygame.font.SysFont("Courier New" , 40) #gets a bult in font and generates it 
      gameover = font.render("Game Over!", 1 , (red)) #generates a game over text
      gameoversize = gameover.get_size() #gets the size of the game over text
      gamewindow.blit(gameover, (width/2-gameoversize[0]/2 , 100)) #puts the game over text at a specific spot on the screen 
      pygame.display.update() #this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
      highscore = open("HighScore.txt", "r") #opens up the highscore file and reads the number 
      highscore = highscore.read() #remaking the highscore variable to read the value of the highscore in the highscore text file 
      if int(highscore) > count: #if the integer showed in the highscore text file is bigger than the count (score) value, it will go into this if statement 

        score1 = font.render("You didn't get a highscore", 1 , (white)) #creates a piece of text to show they did not get a high score 
        score1size = score1.get_size() #gets the size of that piece of text 
        gamewindow.blit(score1, (width/2-score1size[0]/2 , height/2-score1size[1])) #puts the piece of text on a specific part of the screen 
        pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
        time.sleep(5) #Waits 5 seconds before moving to the next piece of code 
        introduction() #goes back to the introduction function to run the game from the beginning 
      
      elif count > int(highscore): #if the player score set at the end of the game is bigger than the current high score it goes into this if statement as they got a new highscore 
        score1 = font.render("New highscore: " + str(count), 1 , (green)) #generates a font to tell them they got a new highscore with the score they got from the previous game 
        score1size = score1.get_size() #gets the size of the piece of text 
        gamewindow.blit(score1, (width/2-score1size[0]/2 , height/2-score1size[1])) #puts the text onto a specific part on the screen 
        pygame.display.update()#this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
        time.sleep(5) #waits 5 seconds before preforming the next piece of code 
        my_file=open("HighScore.txt", "w") #opens the highscore text file with the write function 
        my_file.write(str(count)) #writes a new string in the highscore text file which is the new highscore 
        my_file.close() #closes the highscore text file 
        pygame.display.update()     #this piece of code constantly updates the screen each time it goes through the while loop, allowing for any kind of movement or motion on the screen to take place
        introduction() #goes back to the introduction function to run the game from the beginning 

introduction() #since all of the code up until this point has been functions the game wouldn't actually start if no function was called upon, thus this line of code calls upon the introuduction function to get the game started, since all of the function after relate to the introduction function, this is the only function required to get the game started. 