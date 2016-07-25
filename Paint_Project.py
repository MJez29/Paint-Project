#Paint_Project.py
#Theme: Star Wars
#By Michal Jez

from pygame import*
from random import*
from math import*
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import*
from datetime import*
import os

root = Tk() 
root.withdraw()

os.environ['SDL_VIDEO_WINDOW_POS'] = '100,25' #where the program shows up onscreen

screen=display.set_mode((1200,700))
display.set_caption("Star Wars Paint")

font.init() #loading the font to be used
comicFont28 = font.SysFont("Comic Sans MS", 28)
comicFont14 = font.SysFont("Comic Sans MS", 14)
comicFont16 = font.SysFont("Comic Sans MS", 16)
comicFont16.set_underline(True)
tbFont = font.SysFont("Comic Sans MS", 15) #text box font
comicFont19 = font.SysFont("Comic Sans MS", 19)
comicFont10 = font.SysFont("Comic Sans MS", 10)
impactFont30=font.SysFont("impact", 30)
mouseposFont=font.SysFont("impact", 25)

#---loading background images---
background=image.load("space.jpg") #background of the program
background=transform.scale(background,(1200,800)) #fixes the pic to fit the screen
logo=image.load("Logo-Star Wars.png") #star wars logo
logo=transform.scale(logo,(300,140)) #fits it to size
pencil_img=image.load("pencil.png")
pencil_img=transform.scale(pencil_img,(60,60))
eraser_img=image.load("eraser.png") #image of eraser
eraser_img=transform.scale(eraser_img,(60,60)) #adjusting size
mouse_img=image.load("mouse icon.png")
mouse_img=transform.scale(mouse_img,(40,40))
spraycan_img=image.load("spray can.png")
spraycan_img=transform.scale(spraycan_img,(60,60))
selectcol_img=image.load("colour selector icon.png") #tool icon for selecting the col onscreen
selectcol_img=transform.scale(selectcol_img,(60,60))
marker_img=image.load("marker.png")
marker_img=transform.scale(marker_img,(38,60))
colpick_img=image.load("colour picker.jpg")
colpick_img=transform.scale(colpick_img,(300,129)) #the actual colour picker image that goes above the canvas
clear_img=image.load("clear icon.png")
clear_img=transform.scale(clear_img,(60,60)) #image for the clear icon
pen_img=image.load("pen icon.png") #image for pen
pen_img=transform.scale(pen_img,(60,60))
loadimage_img=image.load("insert image icon.png")
loadimage_img=transform.scale(loadimage_img,(60,60))
bucket_img=image.load("paint bucket icon.png")
bucket_img=transform.scale(bucket_img,(60,60))
#---tools above canvas---
save_img=image.load("save icon.png")
save_img=transform.scale(save_img,(40,40))
openfile_img=image.load("open file icon.png")
openfile_img=transform.scale(openfile_img,(40,40))
undo_img=image.load("undo icon.png")
undo_img=transform.scale(undo_img,(40,40))
redo_img=image.load("redo icon.png")
redo_img=transform.scale(redo_img,(40,40))
#img_filenames_pg1=["pencil.png","eraser.png","spray can.png","colour selector icon.png",
#               "marker.png","colour picker.jpg","clear icon.png","pen icon.png","insert image icon.png","paint bucket icon.png"]
#img_names_pg1=[pencil_img,eraser_img,spraycan_img,selectcol_img,marker_img,clear_img,pen_img,loadimage_img,bucket_img]
#for i in range(len(img_filenames_pg1)):
#    img_file

#---star wars images---
#  n_orig ->  original size of image
#
luke_orig=image.load("Luke Skywalker.png")
luke_img=transform.scale(luke_orig,(52,80)) #new size of image while keeping aspect ratio
obiwan_orig=image.load("Obi-Wan Kenobi.png")
obiwan_img=transform.scale(obiwan_orig,(67,80))
r2d2_orig=image.load("R2D2.png")
r2d2_img=transform.scale(r2d2_orig,(80,80))
c3po_orig=image.load("C-3PO.png")
c3po_img=transform.scale(c3po_orig,(42,80))
darthvader_orig=image.load("Darth Vader.png")
darthvader_img=transform.scale(darthvader_orig,(80,71))
anakin_orig=image.load("Anakin Skywalker.png")
anakin_img=transform.scale(anakin_orig,(50,80))
leia_orig=image.load("Princess Leia.png")
leia_img=transform.scale(leia_orig,(45,80))
clone_orig=image.load("Clone Trooper.png")
clone_img=transform.scale(clone_orig,(58,80))
storm_orig=image.load("Storm Trooper.png")
storm_img=transform.scale(storm_orig,(74,80))
han_orig=image.load("Han Solo.png")
han_img=transform.scale(han_orig,(50,80))
chewbacca_orig=image.load("Chewbacca.png")
chewbacca_img=transform.scale(chewbacca_orig,(41,80))
droid_orig=image.load("Battle Droid.png")
droid_img=transform.scale(droid_orig,(51,80))
#---images for the third page---
atats_img_orig=image.load("at-ats.jpg")
death_star_img_orig=image.load("death star.jpg")
star_destroyers_img_orig=image.load("star destroyers.jpg")
stormtroopers_img_orig=image.load("stormtroopers.jpg")
grayscale_img_orig=image.load("grayscale.jpg")
sepia_img_orig=image.load("sepia.jpg")
invert_img_orig=image.load("flowers.jpg")
pixelated_img_orig=image.load("pixelated.png")
orig_imgs_pg3=[atats_img_orig,death_star_img_orig,star_destroyers_img_orig,stormtroopers_img_orig,grayscale_img_orig,sepia_img_orig,
               invert_img_orig,pixelated_img_orig]

#---Initiated the music player so that my program can have sounds---
mixer.init()
saber_snd=mixer.Sound("sw4-lightsabre.wav")
saber_hits=["lasrhit1.wav","lasrhit2.wav","lasrhit3.wav","lasrhit4.wav"]
star_wars_theme=mixer.Sound("Star Wars Theme-WAV.wav")
star_wars_theme.play(-1)

#---drawing background up on screen---
screen.blit(background,(0,0))
screen.blit(logo,(0,0))
painttxtP=comicFont28.render("P",True,(255,255,0)) #word "PAINT" that goes after
painttxtA=comicFont28.render("A",True,(255,255,0)) #the Star Wars logo
painttxtI=comicFont28.render("I",True,(255,255,0))
painttxtN=comicFont28.render("N",True,(255,255,0))
painttxtT=comicFont28.render("T",True,(255,255,0))
screen.blit(painttxtP,(300,0))
screen.blit(painttxtA,(310,28))
screen.blit(painttxtI,(320,56))
screen.blit(painttxtN,(330,84))
screen.blit(painttxtT,(340,112))
comicFont10=comicFont10.render("By Michal Jez",True,(255,255,255)) #shows who
screen.blit(comicFont10,(1100,687)) #made the program
draw.rect(screen,(0,0,0),(373,3,305,135))
screen.blit(colpick_img,(375,5)) #the actual colour picker

#---preview box---
draw.rect(screen,(255,255,0),(700,10,490,120),0)
draw.rect(screen,(0,0,0),(705,15,480,110),2)
draw.rect(screen,(255,255,255),(840,30,80,80),0) #the preview box
draw.rect(screen,(0,0,0),(840,30,80,80),2) #preview box outline
draw.rect(screen,(0,0,0),(940,30,240,80)) #box for info about mouse and date


#---drawing canvas---
canvas=Rect(300,140,890,550) #the dimensions of the canvas
draw.rect(screen,(255,255,255),(canvas))


#---positions of tools (PAGE 1)---
pencil=Rect(40,160,60,60) #position of the pencil tool
pen=Rect(120,160,60,60)
eraser=Rect(200,160,60,60) #position of eraser tool
marker=Rect(40,240,60,60)
selectcol=Rect(120,240,60,60) #pos of the tool that gets the colour of a certain pixel on the canvas
spraycan=Rect(200,240,60,60) #pos of spray can
oval=Rect(40,320,60,60)
connectpoints=Rect(120,320,60,60) #pos of the connect the dots drawing tool
rectangle=Rect(200,320,60,60)
nofilloval=Rect(40,400,60,60) #pos of oval without fill
lineseg=Rect(120,400,60,60) #position of the line segment drawing tool
nofillrect=Rect(200,400,60,60) #pos of the rectangle without fill
clear=Rect(40,480,60,60) #turns the canvas white
bucket=Rect(120,480,60,60)
loadimage=Rect(200,480,60,60) #loads an image that the user can scale
textbox=Rect(50,555,200,40)
#---positions of characters (PAGE 2)---
luke=Rect(10,160,80,80)
obiwan=Rect(115,160,80,80)
r2d2=Rect(210,160,80,80)
c3po=Rect(10,250,80,80)
darthvader=Rect(115,250,80,80)
anakin=Rect(210,250,80,80)
leia=Rect(10,340,80,80)
clone=Rect(115,340,80,80)
storm=Rect(210,340,80,80)
han=Rect(10,430,80,80)
chewbacca=Rect(115,430,80,80)
droid=Rect(210,430,80,80)
r_saber=Rect(10,519,280,42)
g_saber=Rect(10,561,280,42)
b_saber=Rect(10,619,280,42)
#---positions of background modifiers (PAGE 3)---
atats=Rect(20,160,125,77)
deathstar=Rect(155,160,125,77)
stardestroyers=Rect(20,250,125,77)
stormtroopers=Rect(155,250,125,77)
grayscale=Rect(20,340,125,77)
sepia=Rect(155,340,125,77)
invert=Rect(20,430,125,77)
pixelated=Rect(155,430,125,77)
toolnames_pg3=[atats,stardestroyers,stormtroopers,grayscale,sepia,invert,pixelated]

#---tools above canvas---
save=Rect(720,25,40,40)
openfile=Rect(720,75,40,40) #loads an image that will fill the entire canvas
undo=Rect(780,25,40,40)
redo=Rect(780,75,40,40)
preview=Rect(840,30,80,80)
colourpicker=Rect(375,5,300,129)

#---page1 - Descriptions---
toolnames_pg1=[pencil,pen,eraser,marker,selectcol,spraycan,oval,connectpoints,rectangle,nofilloval,lineseg,nofillrect,clear,bucket,loadimage] #list of tool positions
toolnames_str_pg1=["pencil","pen","eraser","marker","selectcol","spraycan","oval","connectpoints","rectangle","nofilloval","lineseg","nofillrect","clear",
                   "bucket","load image","textbox"] #string version of tool names
firstline_pg1=["PENCIL","PEN","ERASER","MARKER","SELECT COLOUR","SPRAY CAN","OVAL","CONNECT THE DOTS","RECTANGLE","NO FILL OVAL","LINE SEGMENT","NO FILL RECTANGLE",
               "CLEAR SCREEN","FILL BUCKET","LOAD IMAGE","TEXT BOX"]
secondline_pg1=["Draw a line","Thickness decreases as","Everyone makes","Same as pencil but is","Get the colour of a certain","Vandalize your work",
            "Draw a filled","Left click to place a vertex","Draw a filled","Draw the outline of","Draw a line","Draw the outline of",
            "Clear your screen","Fills the area with a","Load an image of your own","Type text where you click"]
thirdline_pg1=["","you draw faster","mistakes","partially transparent","pixel on the canvas","","oval","right click to draw the polygon","rectangle","an oval",
               "","a rectangle","","certain colour","",""]

#---page2 - Descriptions---
toolnames_pg2=[luke,obiwan,r2d2,c3po,darthvader,anakin,leia,clone,storm,han,chewbacca,droid]
imagenames=[luke_img,obiwan_img,r2d2_img,c3po_img,darthvader_img,anakin_img,leia_img,clone_img,storm_img,han_img,chewbacca_img,droid_img] #filenames for images
#that go on the toolbar
imagenames_orig=[luke_orig,obiwan_orig,r2d2_orig,c3po_orig,darthvader_orig,anakin_orig,leia_orig,clone_orig,storm_orig,han_orig,chewbacca_orig,droid_orig]
#filenames for the original sizes of the images
toolnames_str_pg2=["luke","obiwan","r2d2","c3po","darth vader","anakin","leia","clone","storm","han","chewbacca","droid"]
firstline_pg2=["LUKE SKYWALKER","OBI-WAN KENOBI","R2 D2","C-3PO","DARTH VADER","ANAKIN SKYWALKER","PRINCESS LEIA","CLONE TROOPERS","STORM TROOPER","HAN SOLO","CHEWBACCA",
               "BATTLE DROID"]
secondline_pg2=["Drag to draw","Drag to draw","Drag to draw","Drag to draw","Drag to draw","Drag to draw","Drag to draw","Drag to draw","Drag to draw",
               "Drag to draw","Drag to draw","Drag to draw"]


#---positions of page selector buttons---
pg1=Rect(10,670,80,20) #page 1: standard paint tools
pg2=Rect(110,670,80,20) #page 2: star wars features
pg3=Rect(210,670,80,20) #page 3: background modifiers, effects and miscellaneous stuff

#---drawing tool icons---
toolbackground=screen.subsurface(0,140,300,559).copy() #space background for where the tools are supposed to go
#---background for page 2---
screen.blit(toolbackground,(0,140))#making it blank again
draw.rect(screen,(255,255,255),(10,160,280,350))
draw.rect(screen,(111,111,111),(10,160,280,350),2)
screen.blit(luke_img,(10+(40-luke_img.get_width()//2),160))
screen.blit(obiwan_img,(115+(40-obiwan_img.get_width()//2),160))
screen.blit(r2d2_img,(210+(40-r2d2_img.get_width()//2),160))
screen.blit(c3po_img,(10+(40-luke_img.get_width()//2),250))
screen.blit(darthvader_img,(115+(40-darthvader_img.get_width()//2),250))
screen.blit(anakin_img,(210+(40-anakin_img.get_width()//2),250))
screen.blit(leia_img,(10+(40-leia_img.get_width()//2),340))
screen.blit(clone_img,(115+(40-clone_img.get_width()//2),340))
screen.blit(storm_img,(210+(40-storm_img.get_width()//2),340))
screen.blit(han_img,(10+(40-han_img.get_width()//2),430))
screen.blit(chewbacca_img,(115+(40-chewbacca_img.get_width()//2),430))
screen.blit(droid_img,(210+(40-droid_img.get_width()//2),430))
for c in range(11): #red lightsaber
    for i in range(238): #draws outer circles, colour becomes more white the smaller the circles get
        draw.circle(screen,(255,5*c,5*c),(i+31,540),(21-c))
for b in range(10):
    for i in range(238): #inner circles, colour becomes whiter 11X as fast as the outer circles so that it goes from red to white quickly
        draw.circle(screen,(255,55+b*20,55+b*20),(i+31,540),10-b)
for c in range(11): #green lightsaber
    for i in range(238):
        draw.circle(screen,(5*c,255,5*c),(i+31,590),(21-c))
for b in range(10):
    for i in range(238):
        draw.circle(screen,(55+b*20,255,55+b*20),(i+31,590),10-b)
for c in range(11): #blue lightsaber
    for i in range(238):
        draw.circle(screen,(5*c,5*c,255),(i+31,640),(21-c))
for b in range(10):
    for i in range(238):
        draw.circle(screen,(55+b*20,55+b*20,255),(i+31,640),10-b)

draw.rect(screen,(100,100,255),pg1)#page 1 button
page1text=comicFont19.render("PAGE 1",True,(255,255,255))
screen.blit(page1text,(16,667))
draw.rect(screen,(255,255,255),pg1,1)
draw.rect(screen,(100,100,255),pg2)#page 2 button
page2text=comicFont19.render("PAGE 2",True,(255,255,255))
screen.blit(page2text,(116,667))
draw.rect(screen,(255,255,255),pg2,1)
draw.rect(screen,(100,100,255),pg3)#page 3 button
page1text=comicFont19.render("PAGE 3",True,(255,255,255))
screen.blit(page1text,(216,667))
draw.rect(screen,(255,255,255),pg3,1)
page2=screen.subsurface(0,140,300,559).copy() #dimensions are 1 pixel greater so that the outlines for which tool is seleted will be completely
                                        #erased when you switch tools

#---background for page 3---
screen.blit(toolbackground,(0,140))#making it blank again
draw.rect(screen,(0,0,0),(5,145,290,380))
draw.rect(screen,(255,255,255),(10,150,280,370))
for i in range(len(orig_imgs_pg3)):
    screen.blit(transform.scale(orig_imgs_pg3[i],(125,77)),(20+(135*((i+2)%2)),160+(90*(i//2))))
draw.rect(screen,(100,100,255),pg1)#page 1 button
page1text=comicFont19.render("PAGE 1",True,(255,255,255))
screen.blit(page1text,(16,667))
draw.rect(screen,(255,255,255),pg1,1)
draw.rect(screen,(100,100,255),pg2)#page 2 button
page2text=comicFont19.render("PAGE 2",True,(255,255,255))
screen.blit(page2text,(116,667))
draw.rect(screen,(255,255,255),pg2,1)
draw.rect(screen,(100,100,255),pg3)#page 3 button
page1text=comicFont19.render("PAGE 3",True,(255,255,255))
screen.blit(page1text,(216,667))
draw.rect(screen,(255,255,255),pg3,1)
page3=screen.subsurface(0,140,300,559).copy()

#---background for page 1---
screen.blit(toolbackground,(0,140))#making it blank again
for i in range(260):
    draw.circle(screen,(111,111,111),(20+i,160),10)
    draw.circle(screen,(111,111,111),(20+i,600),10)
for i in range(440):
    draw.circle(screen,(111,111,111),(20,160+i),10)
    draw.circle(screen,(111,111,111),(280,160+i),10)
for i in range(250):
    draw.circle(screen,(255,255,255),(25+i,165),10)
    draw.circle(screen,(255,255,255),(25+i,595),10)
for i in range(430):
    draw.circle(screen,(255,255,255),(25,165+i),10)
    draw.circle(screen,(255,255,255),(275,165+i),10)
draw.rect(screen,(255,255,255),(15,165,270,430))
screen.blit(pencil_img,(pencil)) #pencil image
screen.blit(eraser_img,(eraser)) #eraser image
draw.line(screen,(0,0,0),(125,460),(175,400),15) #line segment image
draw.circle(screen,(0,0,0),(145,325),5) #connect the dots
draw.circle(screen,(0,0,0),(120,350),5) #         |
draw.circle(screen,(0,0,0),(150,375),5) #         |
draw.circle(screen,(0,0,0),(175,360),5) #         | all
draw.line(screen,(0,0,0),(145,325),(120,350),5) # |
draw.line(screen,(0,0,0),(120,350),(150,375),5) # | this
draw.line(screen,(0,0,0),(150,375),(175,360),5) # |
screen.blit(mouse_img,(160,350)) #----------------|
screen.blit(spraycan_img,(spraycan)) #spraycan image
draw.ellipse(screen,(255,0,255),(oval),0) #oval image, I use oval instead of ellipse,
    #I find that it is easier to type and there is less chance of making a typo,
    #it is also the term that I would use to describe that figure
draw.rect(screen,(0,255,255),(rectangle))
draw.ellipse(screen,(255,0,0),(nofilloval),5) #draws an ellipse outline
draw.rect(screen,(0,255,0),(nofillrect),2)
screen.blit(selectcol_img,(selectcol))
screen.blit(marker_img,(marker))
screen.blit(clear_img,(clear))
screen.blit(pen_img,(pen))
screen.blit(bucket_img,(bucket))
screen.blit(loadimage_img,(loadimage))
draw.rect(screen,(0,0,0),(50,555,200,40),1) #text box
textboxtext=comicFont19.render("Enter text...",True,(0,0,0))
screen.blit(textboxtext,(55,558))

draw.rect(screen,(100,100,255),pg1)#page 1 button
page1text=comicFont19.render("PAGE 1",True,(255,255,255))
screen.blit(page1text,(16,667))
draw.rect(screen,(255,255,255),pg1,1)
draw.rect(screen,(100,100,255),pg2)#page 2 button
page2text=comicFont19.render("PAGE 2",True,(255,255,255))
screen.blit(page2text,(116,667))
draw.rect(screen,(255,255,255),pg2,1)
draw.rect(screen,(100,100,255),pg3)#page 3 button
page1text=comicFont19.render("PAGE 3",True,(255,255,255))
screen.blit(page1text,(216,667))
draw.rect(screen,(255,255,255),pg3,1)
for i in range(len(toolnames_pg1)):
    draw.rect(screen,(0,0,0),toolnames_pg1[i],2)


page1=screen.subsurface(0,140,300,559).copy() #dimensions are 1 pixel greater so that the outlines for which tool is seleted will be completely
                                        #erased when you switch tools
#---tools above canvas---
screen.blit(save_img,(720,25))
screen.blit(openfile_img,(720,75))
screen.blit(undo_img,(780,25))
screen.blit(redo_img,(780,75))
#---lists---
pointpos=[] #positions of points in the connectpoints tool
redolist=[] #the lists for the undo and redo tools
undolist=[screen.subsurface(canvas).copy()] #starts off with the blank canvas in the list

#---presets---
tool="pencil"
colour=(0,0,0)
size=1
prev="circle"
timeflag=True
page=1
timecount=0
mx,my=0,0
realsize=1 #realsize is the actual size with decimals, size is int(realsize) and is the size used
#throughout the program

markercover=screen.subsurface(canvas).copy() #marker
markercover.set_alpha(51)
markercover.set_colorkey((255,255,255))
markercover.fill((255,255,255))
markercopy=screen.subsurface(canvas).copy()



#---flags---
pencildesc=True #flag for the pencil description
eraserdesc=True #flag for the eraser description
markerflag=True
drawing=False #the flag for undo/redo, when set to True, it means that the canvas has been changed
name=Rect(0,0,0,0)

descflag=True

#---Text box presets---
curkey=0
tx,ty=-500,-500
textflag=False
text=[]


running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        
        
        #---if the icon is pressed, the tool is activated---
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            if page==1:
                if pencil.collidepoint(mx,my):
                    tool="pencil"
                    prev="circle"
                elif oval.collidepoint(mx,my):
                    tool="oval"
                    ovalflag=True #flag for oval
                    prev="circle"
                elif eraser.collidepoint(mx,my):
                    tool="eraser"
                    prev="circle"
                elif lineseg.collidepoint(mx,my):
                    tool="lineseg"
                    lsegflag=True #flag for line segment
                    prev="line"
                elif rectangle.collidepoint(mx,my):
                    tool="rectangle"
                    rectflag=True
                elif spraycan.collidepoint(mx,my):
                    tool="spraycan"
                    prev="circle"
                elif nofilloval.collidepoint(mx,my):
                    tool="nofilloval"
                    nofillovalflag=True
                    prev="line"
                elif connectpoints.collidepoint(mx,my):
                    tool="connectpoints"
                    prev="line"
                elif nofillrect.collidepoint(mx,my):
                    tool="nofillrect"
                    nofillrectflag=True
                    prev="line"
                elif selectcol.collidepoint(mx,my):
                    tool="selectcol"
                    prev="circle"
                elif pen.collidepoint(mx,my):
                    tool="pen"
                    prev="circle"
                elif marker.collidepoint(mx,my):
                    tool="marker"
                    prev="circle"
                elif clear.collidepoint(mx,my):
                    ans=askokcancel("Do you really want to clear the canvas?","All of your work will be erased")
                    if ans==True:
                        draw.rect(screen,(255,255,255),(canvas))
                        screen.blit(page1,(0,140))
                        desccopy=screen.copy()
                elif bucket.collidepoint(mx,my):
                    tool="bucket"
                elif loadimage.collidepoint(mx,my):
                    tool="load image"
                    fileName=askopenfilename(parent=root,title="Open Image:")
                    if fileName!="":
                        loadedimage=image.load(fileName)
                        loadimageflag=True
                    
                elif textbox.collidepoint(mx,my):
                    tool="textbox"
                
            elif page==2:
                for i in range(len(toolnames_pg2)):
                    if toolnames_pg2[i].collidepoint(mx,my):
                        tool=toolnames_str_pg2[i]
                        imageflag=True
                if r_saber.collidepoint(mx,my):
                    tool="red saber"
                    #mixer.music.load("sw4-lightsabre.wav")
                    saber_snd.play()
                elif g_saber.collidepoint(mx,my):
                    tool="green saber"
                    #mixer.music.load("sw4-lightsabre.wav")
                    saber_snd.play()
                elif b_saber.collidepoint(mx,my):
                    tool="blue saber"
                    #mixer.music.load("sw4-lightsabre.wav")
                    saber_snd.play()
            
            elif page==3:
                if atats.collidepoint(mx,my):
                    atats_img=transform.scale(atats_img_orig,(890,550))
                    screen.blit(atats_img,(canvas))
                elif deathstar.collidepoint(mx,my):
                    death_star_img=transform.scale(death_star_img_orig,(890,550))
                    screen.blit(death_star_img,(canvas))
                elif stardestroyers.collidepoint(mx,my):
                    star_destroyers_img=transform.scale(star_destroyers_img_orig,(890,550))
                    screen.blit(star_destroyers_img,(canvas))
                elif stormtroopers.collidepoint(mx,my):
                    stormtroopers_img=transform.scale(stormtroopers_img_orig,(890,550))
                    screen.blit(stormtroopers_img,(canvas))
                elif grayscale.collidepoint(mx,my):
                    for x in range(890):
                        for y in range(550):
                            pixcol=screen.get_at((x+300,y+140))
                            ave=(pixcol[0]+pixcol[1]+pixcol[2])//3 #gets the average of the red, green and blue values
                            screen.set_at((x+300,y+140),(ave,ave,ave)) #sets the screen to that colour
                elif sepia.collidepoint(mx,my):
                    for x in range(890):
                        for y in range(550):
                            pixcol=screen.get_at((x+300,y+140))
                            r=int((pixcol[0]*0.393)+(pixcol[1]*0.769)+(pixcol[2]*0.189))
                            if r>255:
                                r=255
                            g=int((pixcol[0]*0.349)+(pixcol[1]*0.686)+(pixcol[2]*0.168))
                            if g>255:
                                g=255
                            b=int((pixcol[0]*0.272)+(pixcol[1]*0.534)+(pixcol[2]*0.131))
                            if b>255:
                                b=255
                            #values were found at: http://www.techrepublic.com/blog/how-do-i/how-do-i-convert-images-to-grayscale-and-sepia-tone-using-c/
                            screen.set_at((x+300,y+140),(r,g,b))
                elif invert.collidepoint(mx,my):
                    for x in range(890):
                        for y in range(550):
                            pixcol=screen.get_at((x+300,y+140))
                            r=255-pixcol[0]
                            g=255-pixcol[1]
                            b=255-pixcol[2]
                            screen.set_at((x+300,y+140),(r,g,b))
                elif pixelated.collidepoint(mx,my):
                    for x in range(177):
                        for y in range(109):
                            col=transform.average_color(screen.subsurface(300+(x*5),140+(y*5),5,5))
                            for a in range(5):
                                for b in range(5):
                                    screen.set_at((300+(x*5)+a,140+(y*5)+b),col)
                                    
                for i in range(len(toolnames_pg3)):
                    if toolnames_pg3[i].collidepoint(mx,my):
                        drawing=True
                        redolist=[] #nothing can be redone if something is just drawn
                


            
            
                
                
        #---what happens to the undo list after the canvas is drawn on---
        if e.type==MOUSEBUTTONUP and drawing==True:
            undolist.append(screen.subsurface(canvas).copy())
            drawing=False #so that it only copies the canvas once

        #---what happens when one of the tools above the canvas is pressed---
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            if save.collidepoint(mx,my):
                fileName=asksaveasfilename(parent=root,title="Save Image As:") #gets the filename and save location
                if fileName!="":
                    image.save(screen.subsurface(canvas),"%s.png"%(fileName)) #saves image
            elif undo.collidepoint(mx,my):
                if len(undolist)>1: #if there is anything besides the blank canvas in the list
                    screen.blit(undolist[-2],(canvas)) #[-1] is the current screen so it needs to be the one before, hence the [-2]
                    last=undolist.pop()
                    redolist.append(last) #adds the last item to the redo list
            elif redo.collidepoint(mx,my):
                if len(redolist)>0:
                    screen.blit(redolist[-1],(canvas))
                    del redolist[-1]
                    drawing=True #because the screen is changed
            elif openfile.collidepoint(mx,my):
                fileName=askopenfilename(parent=root,title="Open Image:") #gets the filename
                if fileName!="":
                    load_img=image.load(fileName) #loads it
                    load_img=transform.scale(load_img,(890,550)) #scales it to fit the canvas
                    screen.blit(load_img,(300,140)) #blits it up on screen
                    drawing=True
                    redolist=[] #nothing can be redone if something is just drawn

        
        #---when the mouse is pressed while on the colour picker---
        if e.type==MOUSEBUTTONDOWN and colourpicker.collidepoint(mx,my) and e.button==1:
            colour=screen.get_at((mx,my))

        #---the textbox tool---
        if tool=="textbox" and canvas.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:
            if "".join(text)!="": #if you click the mouse on the canvas to set a new textbox position
                drawing=True
                redolist=[] #nothing can be redone if something is just drawn
            text=[] #all previous text is erased from the list
            textcopy=screen.copy()
            tx,ty=mouse.get_pos() #start position of the textbox
            textflag=True
        if e.type==KEYDOWN and tool=="textbox":
            curkey=e.key
            if key.get_mods() & KMOD_SHIFT: #if a shift key is pressed
                for i in range(26): #changes lowercase letters
                    if e.key==i+97: #to uppercase
                        curkey=i+65
                if e.key==44: #if "," is pressed
                    curkey=60 #"<"
                elif e.key==46: #"."
                    curkey=62 #">"
                elif e.key==47: #"/"
                    curkey=63 #"?"
                elif e.key==59: #if ";" is pressed
                    curkey=58 #":"
                elif e.key==39: #"'"
                    curkey=34 #'"'
                elif e.key==92: #"\"
                    curkey=124 #"|"
                elif e.key==91: #"["
                    curkey=123 #"{"
                elif e.key==93: #"]"
                    curkey=125 #"}"
                elif e.key==96: #"`"
                    curkey=126 #"~"
                elif e.key==49: #"1"
                    curkey=33
                elif e.key==50: #"2"
                    curkey=64 #"@"
                elif e.key==51: #"3"
                    curkey=35 #"#"
                elif e.key==52: #"4"
                    curkey=36 #"$"
                elif e.key==53: #"5"
                    curkey=37 #"%"
                elif e.key==54: #"6"
                    curkey=94 #"^"
                elif e.key==55: #"7"
                    curkey=38 #"&"
                elif e.key==56: #"8"
                    curkey=42 #"*"
                elif e.key==57: #"9"
                    curkey=40 #"("
                elif e.key==48: #"0"
                    curkey=41 #")"
                elif e.key==45: #"-"
                    curkey=95 #"_"
                elif e.key==61: #"="
                    curkey=43 #"+"
            if e.key>=32 and e.key<127: #if the key is one of the standard keys pressed on the keyboard
                text.append(chr(curkey))
            elif e.key==8: #backspace
                if len(text)>0:
                    del text[-1]
            if textflag==True:
                screen.set_clip(canvas)
                screen.blit(textcopy,(0,0))
                screen.blit(tbFont.render("".join(text), 1, (colour)),
                        (tx,ty))
                screen.set_clip(None)
                
            if curkey==13 :
                screen.set_clip(canvas)
                try :
                    if "".join(text)!="":
                        screen.blit(textcopy,(0,0))
                        screen.blit(tbFont.render("".join(text), 1, (colour)),
                                (tx,ty))
                        text=[]
                        textflag=False
                        redolist=[]
                        drawing=True
                        redolist=[] #nothing can be redone if something is just drawn
                except NameError:
                    pass
                screen.set_clip(None)
                
                
        
             
        #---if one of the page buttons are pressed---
        if e.type==MOUSEBUTTONDOWN and pg1.collidepoint(mx,my) and e.button==1:
            page=1
            tool="pencil"
            prev="circle"
            screen.blit(page1,(0,140))
            draw.rect(screen,(0,255,255),pg1,2)
        elif e.type==MOUSEBUTTONDOWN and pg2.collidepoint(mx,my) and e.button==1:
            page=2
            tool="luke"
            screen.blit(page2,(0,140))
            draw.rect(screen,(0,255,255),pg2,2)
        elif e.type==MOUSEBUTTONDOWN and pg3.collidepoint(mx,my) and e.button==1:
            page=3
            tool=""
            screen.blit(page3,(0,140))
            draw.rect(screen,(0,255,255),pg3,2)
            
        #---mousewheel actions---
        if e.type==MOUSEBUTTONDOWN:
            if e.button==4: #if the mousewheel is scrolled,
                realsize+=0.5
                size=int(realsize)
            if e.button==5: #either the size increases or decreases
                realsize-=0.5
                if realsize<1:
                    realsize=1
                size=int(realsize)
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            
            if page==1:
                if tool=="lineseg":
                    linesegcopy=screen.subsurface(canvas).copy()
                elif tool=="oval":
                    ovalcopy=screen.subsurface(canvas).copy()
                elif tool=="rectangle":
                    rectcopy=screen.subsurface(canvas).copy()
                elif tool=="nofilloval":
                    nofillovalcopy=screen.subsurface(canvas).copy()
                elif tool=="nofillrect":
                    nofillrectcopy=screen.subsurface(canvas).copy()
                elif tool=="marker":
                    markercover=screen.subsurface(canvas).copy() #marker
                    markercover.set_alpha(51)
                    markercover.set_colorkey((255,255,255))
                    markercover.fill((255,255,255))
                    markercopy=screen.subsurface(canvas).copy()
                elif tool=="load image":
                    loadimagecopy=screen.subsurface(canvas).copy()
            elif page==2:
                for i in range(len(toolnames_str_pg2)):
                    if tool==toolnames_str_pg2[i]:
                        imagecopy=screen.subsurface(canvas).copy()
                if tool=="red saber":
                    saberflag=True
                    sabercopy=screen.subsurface(canvas).copy()
                if tool=="green saber":
                    saberflag=True
                    sabercopy=screen.subsurface(canvas).copy()
                if tool=="blue saber":
                    saberflag=True
                    sabercopy=screen.subsurface(canvas).copy()
        
    
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    

    #---drawing tool icons to show which is selected (selected has light blue box around it)---
    if page==1:
        for i in range(len(toolnames_str_pg1)-1):
            if tool==toolnames_str_pg1[i]:
                screen.blit(page1,(0,140))
                draw.rect(screen,(0,255,255),(toolnames_pg1[i]),2)
        if tool=="textbox":
            screen.blit(page1,(0,140))
            draw.rect(screen,(0,255,255),(textbox),1)
        
            
        draw.rect(screen,(0,255,255),pg1,2) #box that goes around the selected page
        
    elif page==2:
        for i in range(len(toolnames_str_pg2)):
            if tool==toolnames_str_pg2[i]:
                screen.blit(page2,(0,140))
                draw.rect(screen,(0,255,255),(toolnames_pg2[i]),2)
        if tool=="red saber" or tool=="green saber" or tool=="blue saber":
            screen.blit(page2,(0,140)) #the lightsabers dont get an outline
        draw.rect(screen,(0,255,255),pg2,2) #box that goes around the selected page
        

    #---The descriptions for tools---
    if page==1:
        for i in range(len(toolnames_pg1)):
            if toolnames_pg1[i].collidepoint(mx,my):
                if descflag==True:
                    desccopy=screen.copy() #copies the screen before it draws the polygon
                    
                    descflag=False
                    name=toolnames_pg1[i]
                screen.blit(desccopy,(0,0))
                if i%3==0: #if it is in the first column
                    draw.polygon(screen,(255,255,255),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(100,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(100,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))),1)
                    line1=comicFont16.render(firstline_pg1[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+80*(i//3)))
                    line2=comicFont14.render(secondline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+80*(i//3)))
                    line3=comicFont14.render(thirdline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line3,(71,96+80*(i//3)))
                elif i%3==1: #second column
                    draw.polygon(screen,(255,255,255),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(150,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(150,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))),1)
                    line1=comicFont16.render(firstline_pg1[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+80*(i//3)))
                    line2=comicFont14.render(secondline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+80*(i//3)))
                    line3=comicFont14.render(thirdline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line3,(71,96+80*(i//3)))
                elif i%3==2: #third column
                    draw.polygon(screen,(255,255,255),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(200,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+80*(i//3)),(280,60+80*(i//3)),(280,120+80*(i//3)),(180,120+80*(i//3)),(200,160+80*(i//3)),
                                                       (120,120+80*(i//3)),(70,120+80*(i//3))),1)
                    line1=comicFont16.render(firstline_pg1[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+80*(i//3)))
                    line2=comicFont14.render(secondline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+80*(i//3)))
                    line3=comicFont14.render(thirdline_pg1[i],True,(0,0,0)) #second line of text
                    screen.blit(line3,(71,96+80*(i//3)))
                
            elif name.collidepoint(mx,my)==False and descflag==False:
                screen.blit(desccopy,(0,0))
                descflag=True #so that it only blits the copied background once
    elif page==2:
        for i in range(len(toolnames_pg2)):
            if toolnames_pg2[i].collidepoint(mx,my):
                if descflag==True:
                    desccopy=screen.copy() #copies the screen before it draws the polygon
                    
                    descflag=False
                    name=toolnames_pg2[i]
                screen.blit(desccopy,(0,0))
                if i%3==0: #if it is in the first column
                    draw.polygon(screen,(255,255,255),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(90,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(90,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))),1)
                    line1=comicFont16.render(firstline_pg2[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+90*(i//3)))
                    line2=comicFont14.render(secondline_pg2[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+90*(i//3)))
                elif i%3==1: #second column
                    draw.polygon(screen,(255,255,255),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(155,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(155,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))),1)
                    line1=comicFont16.render(firstline_pg2[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+90*(i//3)))
                    line2=comicFont14.render(secondline_pg2[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+90*(i//3)))
                elif i%3==2: #third column
                    draw.polygon(screen,(255,255,255),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(210,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))))
                    draw.polygon(screen,(0,0,0),((70,60+90*(i//3)),(280,60+90*(i//3)),(280,120+90*(i//3)),(180,120+90*(i//3)),(210,160+90*(i//3)),
                                                       (120,120+90*(i//3)),(70,120+90*(i//3))),1)
                    line1=comicFont16.render(firstline_pg2[i],True,(0,0,0)) #first line of text
                    screen.blit(line1,(71,60+90*(i//3)))
                    line2=comicFont14.render(secondline_pg2[i],True,(0,0,0)) #second line of text
                    screen.blit(line2,(71,80+90*(i//3)))
                
            elif name.collidepoint(mx,my)==False and descflag==False:
                screen.blit(desccopy,(0,0))
                descflag=True #so that it only blits the copied background once
    
    
    #---what happens when the mouse is pressed and the cursor is on the canvas
    if canvas.collidepoint(mx,my) and mb[0]==1: #if the cursor is over the screen and is clicked
        if page==1:
            screen.set_clip(canvas)
            if tool=="pencil": #if the tool selected is the pencil
                if size==1:
                    draw.line(screen,(colour),(mx,my),(lx,ly),size) #thinner line than if drawn with circles
                else :
                    dist=hypot(mx-lx,my-ly) #distance between the 2 last point and the current point
                    dist=int(dist) #makes it into an integer
                    for i in range(dist):
                        sx=i*(mx-lx)//dist #the distance from the original position
                        sy=i*(my-ly)//dist #distance from the original position
                        draw.circle(screen,(colour),(lx+sx,ly+sy),size)

            elif tool=="oval":
                try:
                    screen.blit(ovalcopy,(300,140))
                    if ovalflag==True:
                        ox,oy=mx,my #first position where the mouse is pressed to draw oval
                        ovalflag=False
                    else :
                        if mx<ox and my<oy: #if mouse is to the top-left of the start pos
                            rect=Rect(mx,my,ox-mx,oy-my)
                        elif mx>ox and my<oy: #if the mouse is to the top-right of the start pos
                            rect=Rect(ox,my,mx-ox,oy-my)
                        elif mx<ox and my>oy: #if the mouse is to the bottom-left of the starting pos
                            rect=Rect(mx,oy,ox-mx,my-oy)
                        elif mx>ox and my>oy: #if the mouse is to the bottom-right of the starting pos
                            rect=Rect(ox,oy,mx-ox,my-oy)
                        else :
                            rect=Rect(mx,my,0,0) #if the mouse is at the same position as the start pos
                        draw.ellipse(screen,colour,rect,0)
                except NameError:
                    pass
            elif tool=="eraser":
                dist=hypot(mx-lx,my-ly) #distance between the 2 last point and the current point
                dist=int(dist) #makes it into an integer
                for i in range(dist):
                    sx=i*(mx-lx)//dist #the distance from the original position
                    sy=i*(my-ly)//dist #distance from the original position
                    draw.circle(screen,(255,255,255),(lx+sx,ly+sy),size)
                
            elif tool=="lineseg":
                try:
                    screen.blit(linesegcopy,(300,140))
                    if lsegflag==True: #line segment flag - if true, it gets the first point pressed
                        fx,fy=mx,my #coordinates of the point where the mouse is first pressed
                        lsegflag=False #on the canvas
                    
                    else :
                        draw.line(screen,(colour),(fx,fy),(mx,my),size) #draws line but only stays once mouse button is released
                except NameError:
                    pass

            elif tool=="rectangle":
                try :
                    screen.blit(rectcopy,(300,140))
                    if rectflag==True:
                        rx,ry=mx,my #initial position of mx,my when the mouse is left-clicked on the canvas
                        rectflag=False
                    else :
                        if mx<rx and my<ry: #if mouse is to the top-left of the start pos
                            rect=Rect(mx,my,rx-mx,ry-my)
                        elif mx>rx and my<ry: #if the mouse is to the top-right of the start pos
                            rect=Rect(rx,my,mx-rx,ry-my)
                        elif mx<rx and my>ry: #if the mouse is to the bottom-left of the starting pos
                            rect=Rect(mx,ry,rx-mx,my-ry)
                        elif mx>rx and my>ry: #if the mouse is to the bottom-right of the starting pos
                            rect=Rect(rx,ry,mx-rx,my-ry)
                        else :
                            rect=Rect(mx,my,0,0) #if the mouse is at the same position as the start pos
                        draw.rect(screen,colour,rect,0)
                except NameError:
                    pass

            elif tool=="spraycan":
                for i in range(2):
                    x=randint(size*(-1),size) #random x position in a square where the center is the cursor 
                    y=randint(size*(-1),size) #random y position in a square where the center is the cursor
                    dist=int(((mx-(x+mx))**2+(my-(y+my))**2)**0.5) #the tool spray can creates a circle, not a square
                    dist=max(dist,1)
                    if dist<=size: #only if the point (x,y) lies in the circle with radius being size will the 
                        screen.set_at((mx+x,my+y),colour) #pixel actually be coloured
                    else :
                       pass
            elif tool=="nofilloval":
                try :
                    screen.blit(nofillovalcopy,(300,140))
                    if nofillovalflag==True:
                        nfox,nfoy=mx,my #first position where the mouse is pressed to draw oval
                        nofillovalflag=False
                    else :
                        if mx<nfox and my<nfoy: #if mouse is to the top-left of the start pos
                            rect=Rect(mx,my,nfox-mx,nfoy-my)
                        elif mx>nfox and my<nfoy: #if the mouse is to the top-right of the start pos
                            rect=Rect(nfox,my,mx-nfox,nfoy-my)
                        elif mx<nfox and my>nfoy: #if the mouse is to the bottom-left of the starting pos
                            rect=Rect(mx,nfoy,nfox-mx,my-nfoy)
                        elif mx>nfox and my>nfoy: #if the mouse is to the bottom-right of the starting pos
                            rect=Rect(nfox,nfoy,mx-nfox,my-nfoy)
                        else :
                            rect=Rect(mx,my,0,0) #if the mouse is at the same position as the start pos
                        outline=size
                        if outline>rect[2]/2: #if the outline size is bigger than any of the radii, the 
                            outline=0 #oval will be filled
                        if outline>rect[3]/2:
                            outline=0
                        draw.ellipse(screen,colour,rect,outline)
                except NameError:
                    pass

            elif tool=="connectpoints":
                pointpos.append((mx,my)) #adds to the list of points
            elif tool=="nofillrect":
                try :
                    screen.blit(nofillrectcopy,(300,140))
                    if nofillrectflag==True:
                        nfrx,nfry=mx,my #first position where the mouse is pressed to draw rect
                        nofillrectflag=False
                    else :
                        if mx<nfrx and my<nfry: #if mouse is to the top-left of the start pos
                            rect=Rect(mx,my,nfrx-mx,nfry-my)
                        elif mx>nfrx and my<nfry: #if the mouse is to the top-right of the start pos
                            rect=Rect(nfrx,my,mx-nfrx,nfry-my)
                        elif mx<nfrx and my>nfry: #if the mouse is to the bottom-left of the starting pos
                            rect=Rect(mx,nfry,nfrx-mx,my-nfry)
                        elif mx>nfrx and my>nfry: #if the mouse is to the bottom-right of the starting pos
                            rect=Rect(nfrx,nfry,mx-nfrx,my-nfry)
                        else :
                            rect=Rect(mx,my,0,0) #if the mouse is at the same position as the start pos
                        outline=size
                        if outline>rect[2]/2: #if the outline size is bigger than the distance to the closest side, the 
                            outline=0 #rect will be filled
                        if outline>rect[3]/2:
                            outline=0
                        draw.rect(screen,colour,rect,outline)
                        if outline!=0:
                            if outline/2==outline//2:
                                num=outline//2-1
                            else :
                                num=outline//2
                            draw.rect(screen,colour,(rect[0]-num,rect[1]-num,outline,outline),0) #fixes the bad corners when
                            draw.rect(screen,colour,(rect[0]+rect[2]-num-1,rect[1]-num,outline,outline),0) #it draws an outline
                            draw.rect(screen,colour,(rect[0]+rect[2]-num-1,rect[1]+rect[3]-num-1,outline,outline),0) #of a 
                            draw.rect(screen,colour,(rect[0]-num,rect[1]+rect[3]-num-1,outline,outline),0) #rectangle
                except NameError:
                    pass
                
            elif tool=="selectcol":
                colour=screen.get_at((mx,my)) #gets the colour of the pixel where the cursor is pressed
            elif tool=="pen": #allows you to draw like your using a pen
                          #the faster the mouse is being move, the smaller the size of the trail of ink (or circles)
                if mx==lx and my==ly: #no need to draw extra circles if they arent going to be seen anyhow
                    pass
                elif size<=5: #if the size is less than 5, the faster you draw, the size becomes smaller than what the size variable is
                    dist=hypot((mx-lx),(my-ly))
                    if dist<=5:
                        pensize=size+5 #variable for the size of the pen, varies depending on the speed of the cursor moving around the screen
                    elif dist<=10:
                        pensize=size+4
                    elif dist<=15:
                        pensize=size+3
                    elif dist<=20:
                        pensize=size+2
                    elif dist<=25:
                        pensize=size+1
                    else :
                        pensize=size
                    dist=int(dist) #makes it into an integer
                    for i in range(dist):
                        sx=i*(mx-lx)//dist #the distance from the original position
                        sy=i*(my-ly)//dist #distance from the original position
                        draw.circle(screen,(colour),(lx+sx,ly+sy),pensize)
                else : #if the size is greater than 5, the slower you draw, the larger the size becomes, it becomes larger than the size variable
                    dist=hypot((mx-lx),(my-ly))
                    if dist<=5:
                        pensize=size
                    elif dist<=10:
                        pensize=size-1
                    elif dist<=15:
                        pensize=size-2
                    elif dist<=20:
                        pensize=size-3
                    elif dist<=25:
                        pensize=size-4
                    else :
                        pensize=size-5
                    dist=int(dist) #makes it into an integer
                    for i in range(dist):
                        sx=i*(mx-lx)//dist #the distance from the original position
                        sy=i*(my-ly)//dist #distance from the original position
                        draw.circle(screen,(colour),(lx+sx,ly+sy),pensize)
            elif tool=="marker": #draws a mostly transparent circle, when you draw over an already drawn circle, that circle becomes darker                
                draw.circle(markercover,colour,(mx-300,my-140),size) #draws onto the marker cover
                screen.blit(markercopy,(300,140)) #blits the current surface
                screen.blit(markercover,(300,140)) #blits the surface where the circles are drawn
            elif tool=="bucket": #the flood fill AKA bucket AKA fill tool
                p_list=[] #the point list
                col=screen.get_at((mx,my)) #the current colour at the mouse pos,
                    #the colour that fill feature is replacing
                p_list.append((mx,my)) #adds the current pizel pos. to the list
                if col!=colour: #if the selected colour is not the current colour on the screen
                    while len(p_list)>0: #the loop that the fill tool is run in
                        px,py=p_list.pop() #px,py becomes the last tuple in the list and is removed from it
                        if screen.get_at((px,py))==col: #if it is the same colour as where the mouse was pressed
                            screen.set_at((px,py),colour) #sets the pixel to the new colour
                            p_list.append((px+1,py)) #adds the pixels to the top, right, bottom, and left of px,py to the list
                            p_list.append((px-1,py))
                            p_list.append((px,py+1))
                            p_list.append((px,py-1))
                        
                        
            elif tool=="load image":
                screen.blit(loadimagecopy,(300,140))
                if loadimageflag==True:
                    lix,liy=mx,my #first position where the mouse is pressed to draw image
                    loadimageflag=False
                else :
                    if lix>=mx and liy>my:
                        newimage=transform.scale(loadedimage,(max(lix-mx,mx-lix),max(liy-my,my-liy))) #the dimensions of the image
                            #are the change in x and change in y from the starting position to the mouse position
                        #new image is the image with new dimensions, loaded image is the image with original dimensions
                        newimage=transform.flip(newimage,True,True)
                        screen.blit(newimage,(mx,my))
                    elif lix<mx and liy>=my:
                        newimage=transform.scale(loadedimage,(max(lix-mx,mx-lix),max(liy-my,my-liy))) #chooses the positive change
                        newimage=transform.flip(newimage,False,True)
                        screen.blit(newimage,(lix,my))
                    elif lix>mx and liy<=my:
                        newimage=transform.scale(loadedimage,(max(lix-mx,mx-lix),max(liy-my,my-liy))) #chooses the positive change
                        newimage=transform.flip(newimage,True,False)
                        screen.blit(newimage,(mx,liy))
                    elif lix<=mx and liy<my:
                        newimage=transform.scale(loadedimage,(max(lix-mx,mx-lix),max(liy-my,my-liy))) #chooses the positive change
                        screen.blit(newimage,(lix,liy))

            screen.set_clip(None)
        elif page==2:
            screen.set_clip(canvas)
            for i in range(len(toolnames_str_pg2)):
                if tool==toolnames_str_pg2[i]:
                    try :
                        screen.blit(imagecopy,(300,140))
                        if imageflag==True:
                            ix,iy=mx,my #first position where the mouse is pressed to draw image
                            imageflag=False
                        else :
                            if ix>=mx and iy>my:
                                newimage=transform.scale(imagenames_orig[i],(max(ix-mx,mx-ix),max(iy-my,my-iy))) #the dimensions of the image
                                #are the change in x and change in y from the starting position to the mouse position
                                #new image is the image with new dimensions, loaded image is the image with original dimensions
                                screen.blit(newimage,(mx,my))
                            elif ix<mx and iy>=my:
                                newimage=transform.scale(imagenames_orig[i],(max(ix-mx,mx-ix),max(iy-my,my-iy))) #chooses the positive change
                                screen.blit(newimage,(ix,my))
                            elif ix>mx and iy<=my:
                                newimage=transform.scale(imagenames_orig[i],(max(ix-mx,mx-ix),max(iy-my,my-iy))) #chooses the positive change
                                screen.blit(newimage,(mx,iy))
                            elif ix<=mx and iy<my:
                                newimage=transform.scale(imagenames_orig[i],(max(ix-mx,mx-ix),max(iy-my,my-iy))) #chooses the positive change
                                screen.blit(newimage,(ix,iy))
                    except NameError :
                        pass
            if tool=="red saber":
                try :
                    screen.blit(sabercopy,(canvas)) #the copy of the canvas taken just before the mouse was pressed on the canvas
                    if saberflag==True:
                        fx,fy=mx,my #the first position where the mouse was pressed on the canvas
                        saberflag=False
                    else:
                        dist=hypot(mx-fx,my-fy) #distance from the current mouse pos to the starting pos
                        dist=int(dist)
                        #the lightsaber tool is really just circles being layered overtop one another, each a pixel smaller than the last
                        #while turning closer and closer to white
                        for c in range(11): #the outer circles
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(255,5*c,5*c),(fx+sx,fy+sy),(21-c)) #the b and g colour values gradually increase, but slower than
                                #when you are nearing the middle of the beam of the lightsaber
                        for b in range(10):
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(255,55+b*20,55+b*20),(fx+sx,fy+sy),10-b)
                    #---the sound effects---
                    #the framerate is too fast to have a new sound effect being played at every frame
                    #to solve this issue, 2 numbers from 1-15 inclusive are generated every frame
                    #if they are the same, they produce a a randomly chosen sound
                    n1=randint(1,15)
                    n2=randint(1,15)
                    if n1==n2:
                        a=randint(0,len(saber_hits)-1)
                        sound=mixer.Sound(saber_hits[a])
                        sound.play()
                except NameError:
                    pass
            elif tool=="green saber": #refer to the section above for comments
                try :
                    screen.blit(sabercopy,(canvas))
                    if saberflag==True:
                        fx,fy=mx,my
                        saberflag=False
                    else:
                        dist=hypot(mx-fx,my-fy)
                        dist=int(dist)
                        for c in range(11):
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(5*c,255,5*c),(fx+sx,fy+sy),(21-c))
                        for b in range(10):
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(55+b*20,255,55+b*20),(fx+sx,fy+sy),10-b)
                    n1=randint(1,15)
                    n2=randint(1,15)
                    if n1==n2:
                        a=randint(0,len(saber_hits)-1)
                        sound=mixer.Sound(saber_hits[a])
                        sound.play()
                except NameError:
                    pass
                
            elif tool=="blue saber": #refer to red saber, comments apply almost entirely to this as well
                try:
                    screen.blit(sabercopy,(canvas))
                    if saberflag==True:
                        fx,fy=mx,my
                        saberflag=False
                    else:
                        dist=hypot(mx-fx,my-fy)
                        dist=int(dist)
                        for c in range(11):
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(5*c,5*c,255),(fx+sx,fy+sy),(21-c))
                        for b in range(10):
                            for i in range(dist):
                                sx=i*(mx-fx)//dist
                                sy=i*(my-fy)//dist
                                draw.circle(screen,(55+b*20,55+b*20,255),(fx+sx,fy+sy),10-b)
                    n1=randint(1,15)
                    n2=randint(1,15)
                    if n1==n2:
                        a=randint(0,len(saber_hits)-1)
                        sound=mixer.Sound(saber_hits[a])
                        sound.play()
                except NameError:
                    pass
        screen.set_clip(None)
        drawing=True
        redolist=[] #nothing can be redone if something is just drawn
        
    #---when mouse is right-clicked---
    elif mb[2]==1: 
        if tool=="connectpoints" and len(pointpos)!=0: #only runs if there are points in pointpos
            screen.set_clip(canvas)
            draw.lines(screen,(colour),True,(pointpos),size)
            pointpos=[] #erases list so that when the tool is used again, it doesn't have
            #the previous points in the drawing as well
            screen.set_clip(None)
        drawing=True
        redolist=[] #nothing can be redone if something is just drawn
    elif mb[0]==0:
        lsegflag=True #if mouse is no longer being left-clicked,
        ovalflag=True #flags get reset for the next time that the mouse is left-clicked on the screen
        rectflag=True
        nofillovalflag=True
        nofillrectflag=True
        loadimageflag=True
        imageflag=True
        saberflag=True

    

    
    

    #---cursor icons---
    if canvas.collidepoint(mx,my):
        #---cursor icon for pencil
        if tool=="pencil":
            thickarrow_string=(         #sized 24x24
                    "    XXXXXXXXXXXXXXXXX   ",
                    "   XXX............X..XX ",
                    "XXXXXX..XXXXXXXX..X....X",
                    "   XXX............X..XX ",
                    "    XXXXXXXXXXXXXXXXX   ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ")
            datatuple, masktuple=cursors.compile( thickarrow_string,
                                  black=".", white="X", xor="o") #for some reason, X is actually black and . is actually white
            mouse.set_cursor( (24,24), (0,2), datatuple, masktuple )
           #---cursor icon for eraser---
        elif tool=="eraser":
            thickarrow_string=(         #sized 24x24
                    "XXXXXX                  ",
                    "XX....X                 ",
                    "X.X....X                ",
                    "X..X....X               ",
                    "X...X....X              ",
                    "X....X....X             ",
                    " X....X....X            ",
                    "  X....X....X           ",
                    "   X....X....X          ",
                    "    X....X....X         ",
                    "     X....X....X        ",
                    "      X....XXXXXX       ",
                    "       X...X....X       ",
                    "        X..X....X       ",
                    "         X.X....X       ",
                    "          XX....X       ",
                    "           XXXXXX       ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ")
            datatuple, masktuple=cursors.compile( thickarrow_string,
                                  black=".", white="X", xor="o" )
            mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )
        elif tool=="textbox":
            thickarrow_string=(         #sized 24x24
                    "XXXX XXXX               ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "    X                   ",
                    "XXXX XXXX               ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ",
                    "                        ")
            datatuple, masktuple=cursors.compile( thickarrow_string,
                                  black=".", white="X", xor="o")
            mouse.set_cursor( (24,24), (5,0), datatuple, masktuple )
        
    else : #cursor resets to standard when it is not a specific tool or over the canvas
        mouse.set_cursor(*cursors.arrow)
        
    #---drawing the preview---
    draw.rect(screen,(255,255,255),(840,30,80,80),0) #the preview box
    if prev=="line": #if the tool uses lines, such as the draw a line tool, the preview will be a line
        screen.set_clip(preview)
        draw.line(screen,colour,(880,30),(880,110),size)
        screen.set_clip(None)
    elif prev=="circle": #if the tool uses circles, such as the pencil tool, the preview will be a circle
        screen.set_clip(preview)
        draw.circle(screen,colour,(880,70),size)
        screen.set_clip(None)
    draw.rect(screen,(0,0,0),(840,30,80,80),2) #preview box outline

    #---Stuff onscreen that may be helpful to user (mouse pos, date, time)---
    draw.rect(screen,(0,0,0),(940,30,240,80)) #box for info about mouse and date
    #---blitting time---
    screen.set_clip(1065,35,110,30)
    draw.rect(screen,(0,0,0),(1065,35,110,30),0)
    currenttime=datetime.now().strftime("%I:%M:%S")
    time=impactFont30.render(currenttime,True,(255,0,0))
    screen.blit(time,(1120-time.get_width()/2,32))
    draw.rect(screen,(255,255,0),(1065,35,110,30),2) #time box
    screen.set_clip(None)
    #---blitting date---
    #in DD/MM/YY
    screen.set_clip(1065,75,110,30)
    draw.rect(screen,(0,0,0),(1065,75,110,30),0)
    currentdate=datetime.now().strftime("%d/%m/%y")
    date=impactFont30.render(currentdate,True,(255,0,0))
    screen.blit(date,(1120-date.get_width()/2,72))
    draw.rect(screen,(255,255,0),(1065,75,110,30),2) #date box
    screen.set_clip(None)
    #---mouse position---
    mousetext=mouseposFont.render("Mouse:",True,(255,0,0)) #the word "mouse"
    screen.blit(mousetext,(1000-mousetext.get_width()/2,32))
    if canvas.collidepoint(mx,my): #if mouse is on canvas
        postext=mouseposFont.render("%d,%d"%(mx-300,my-140),True,(255,0,0)) #for this, the top left
        screen.blit(postext,(1000-postext.get_width()/2,72)) #pixel on the canvas is (0,0)
    else: #if it isnt
        postext=mouseposFont.render("Off Canvas",True,(255,0,0))
        screen.blit(postext,(1000-postext.get_width()/2,72))
    
        
    
    lx,ly=mx,my #"l" means "last" so lx,ly will be the last position of mx,my the next time the loop runs




    display.flip()
font.quit()
quit()
