from selenium import webdriver
from bs4 import BeautifulSoup
import re
import cv2
import bensCode

def suggest(pic,mode,type):
    
    pic = cv2.imread("./Trow.jpg")
    percentages = bensCode.bensCode(pic);


    whiteCounter = 100  - percentages[0]
    percentages[0] = 0
    for x in range(0,len(percentages)):
        percentages[x] = percentages[x] * (100/whiteCounter)
    print(percentages)
##    percentages = [5,3,6,2,54,32,14,15,1,1,1,1,1,1]
    colours = ["black","white","red","red-orange","orange","orange-yellow","yellow","yellow-green","green","green-blue","blue","blue-purple","purple","purple-red"]
    
    driver = webdriver.Chrome("./chromedriver")

    coloursDic = {"black": "deo","white":"df2","red":"df1","pink":"dez","orange":"dey","yellow":"df3","green":"det","blue":"dep","purple":"df0"}
    typesDic =  {"top":"qnv","jeans":"qnh","skirts":"qnr","leggings":"qnwZ26ke","bjeans":"r8qZqnh","shorts":"qnqZqoa","hjeans":"poaZqnh"}

    mainColours = []

    for x in range(0,14):
        if percentages[x]>20:
            if mode == "contrast":
                x +=6
                if x>14:
                    x=2+(x-14)
                if colours[x] == "yellow-green":
                    mainColours.append("yellow")
                    mainColours.append("green")
                elif colours[x] == "green-blue":
                    mainColours.append("yellow")
                    mainColours.append("green")
                elif colours[x] == "blue-purple":
                    mainColours.append("yellow")
                    mainColours.append("green")
                elif colours[x] == "purple-red":
                    mainColours.append("yellow")
                    mainColours.append("green")
                elif colours[x] == "orange-yellow":
                    mainColours.append("yellow")
                    mainColours.append("green")
                elif colours[x] == "red-orange":
                    mainColours.append("yellow")
                    mainColours.append("green")     
                else:
                    mainColours.append(colours[x])
                

    mainColours.append("black")
    if (mode != "plain" or (mode == "plain" and type != "jeans")):
        mainColours.append("white")

    if (type == "jeans"):
        mainColours.append("blue")
        
    startString = ("https://www.topshop.com/en/tsuk/category/clothing-427/")
     
    for y in mainColours:
         startString += y +"/"



    

    if (type == "turtleneck"):
        startString += "jeans"+"/"
        startString += "skirts"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["jeans"]
        startString += "Z"+typesDic["skirts"]
    if (type == "shirt"):
        startString += "jeans"+"/"
        startString += "shorts/high-waist"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["jeans"]
        startString += "Z"+typesDic["shorts"]
    if (type == "crop"):
        startString += "shorts/high-waist"+"/"
        startString += "jeans"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["shorts"]
        startString += "Z"+typesDic["jeans"]
    if (type == "polo"):
        startString += "skirts"+"/"
        startString += "jeans"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["skirts"]
        startString += "Z"+typesDic["jeans"]
    if (type == "t-shirt"):
        startString += "jeans"+"/"
        startString += "shorts/high-waist"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["jeans"]
        startString += "Z"+typesDic["shorts"]
    if (type == "tanktop"):
        startString += "trousers-leggings/leggings"+"/"
        startString +="N-82z"
        startString += "Z"+typesDic["leggings"]
        
    for z in mainColours:
         startString += "Z"+coloursDic[z]    
        
    
    startString +="Zdgl"     
    driver.get(startString)
    features="html.parser"
    content = driver.page_source
    soup = BeautifulSoup(content,features)
    counter=0
    outputImgs = []
    for a in soup.findAll('img'):
        a = str(a)
        indexes = [m.start() for m in re.finditer('"', a)]

        if (len(indexes)>8):
            imgString = a[indexes[8]+1:indexes[9]]
            index = imgString.find('_')

            stringList = list(imgString)

            stringList[index+1] = 'F'

            stringList.insert(0, 'http:')

            outputImgs.append(''.join(stringList))
            counter +=1
            if counter == 9:
                break
                
##            print(len(indexes))
    link = []
    disc  = []
    counter = 0
    for a in soup.findAll('a'):
        if a.parent.name == "header":
            a = str(a)
            indexes1 = [m.start() for m in re.finditer('"', a)]
            indexes2 = [m.start() for m in re.finditer('<', a)]
            linkText = "https://www.topshop.com" +  a[indexes1[2]+1:indexes1[3]]
            link.append(''.join(linkText))
            
            discText = a[indexes1[3]+2:indexes2[1]]
            disc.append(''.join(discText))

            counter +=1
            if counter == 9:
                break
    for x in range(0,9):
        print(outputImgs[x])
        print(link[x])
        print(disc[x])
        print()
        
    
            
            
            
        
