from turtle import *
from statistics import mode
import math
import matplotlib

Screen().title("Baxter Grapher - Not branched")

t = Turtle()


SPEED = 0

def AwaitInputForNextGraph():
    input("press ENTER to print next graph")
    print()

def Tabbing(Word, Space = 20, charToUse = " ", includesWord = True):
    Word = str(Word)
    WordLen = len(Word)
    phrase = ""

    for x in range(0, Space-WordLen):
        phrase = phrase + charToUse
    
    if includesWord:
        phrase = Word + phrase

    return phrase

def SetTrutleSpeed(typo):
    t.speed(typo)
    SPEED = typo

def Write(message, posX = 0, posY = 0, fontSize = 8, alignMent = "center", TextColor = "black"):
    t.penup()
    t.goto(posX, posY)
    t.color(TextColor)
    t.write(arg = message, font= ("Arial", fontSize, "normal"), align= alignMent)

def drawCakeGraph(size, percentage, posX, posY, color, WantsBorder = False, BackGroundColor = "Sfound", text = ""):
    t.penup()

    if BackGroundColor != "Sfound":
        t.color(BackGroundColor)
        t.goto(posX, posY)
        t.color(BackGroundColor)
        t.begin_fill()
        t.setheading(90)
        t.forward(size/2)
        t.left(90)
        t.circle(size/2)
        t.end_fill()


    t.goto(posX, posY)
    t.color(color)

    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.forward(size/2)

    t.left(90)

    t.circle(size/2, (360*percentage)/100) # r / 360 = x / 100

    t.left(90)
    t.forward(size/2)

    t.end_fill()

    if WantsBorder:
        t.color("black")
        t.setheading(90)
        t.penup()
        t.forward(size/2)
        t.pendown()
        t.left(90)
        t.circle(size/2)
    
    Write(text, posY= posY - size/1.5, posX= posX, fontSize=16)

def DrawVerticalRectGraph(percentage, width = 100, height = 400, posX = 0, posY = 0, Color = "#00ffff", WantsBorder = True, BackGroundColor = "None", BorderColor = "black", text = "", TextColor = "black", textDetach = 50):
    #go to initial position
    t.penup()
    if posX != 0 or posY != 0:
        t.goto(posX, posY)

    #start drawing the background
    if BackGroundColor != "None":
        t.color(BackGroundColor)
        t.setheading(90)
        t.pendown()
        #draw the actual rectangle
        t.begin_fill()
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.end_fill()
        t.penup()
    
    #start drawing the actual graph
    t.pendown()
    t.setheading(90)
    t.color(Color)
    t.begin_fill()
    t.forward( (percentage*height)/100 ) # height / x = 100 / percentage
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward( (percentage*height)/100 ) # height / x = 100 / percentage
    t.right(90)
    t.forward(width)
    t.end_fill()
    t.penup()

    if WantsBorder:
        t.pendown()
        t.color(BorderColor)
        t.setheading(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.penup()

    t.penup()
    t.setheading(0)
    t.forward(width / 2)

    t.setheading(-90)
    t.forward(textDetach)
    t.color(TextColor)
    t.write(arg = text, font= ("Arial", 16, "normal"), align= "Center")

    t.setheading(90)
    t.forward(textDetach)
    t.left(90)
    t.forward(width / 2)
    t.setheading(0)

def ProportionalList(ValueList, referral = 100):
    #this function returns a set of values correspondent to a referral, it's directly proportional
    #grabd 100 as referral as default
    ProportionedValues = {}

    Sum = 0    
    for n in ValueList:
        Sum += n

    for Value in ValueList:
        ProportionedValues[Value] = (Value*referral)/Sum # Value / Sum = ProportionedValues[Value] / referral
    
    return ProportionedValues

def ProportionalList100(ValueList, referralValue = "auto"):
    #this function is not so straightforward to explain, it grabs a set of values and it constructs a dictionary with the proportion of 100 to it

    if referralValue == "auto":
        referral = max(ValueList)

    else:
        referral = referralValue

    ValueWeightList = {}

    for Value in ValueList:
        ValueWeightList[Value] = (Value*100) / referral
    
    # referral / value = 100 / x

    return ValueWeightList

def PrintTotalRectGraph(GraphTitle, Values, Texts = "None", GraphOriginX = 0, GraphOriginY = 0, IndividualHeight = 500, IndividualWidth = 200, Spacing = 40, FillGraphColor = "navy", BackGroundGraphColor = "gray", WantsGraphBorder = True, GraphReferral = "auto"):
    #this function prints out a huge graph with rectangles

    GraphLength = len(Values)

    #draw the lines

    #vertical one
    t.penup()
    t.goto(GraphOriginX, GraphOriginY)
    t.color("black")
    t.pendown()
    t.setheading(90)
    t.forward(IndividualHeight + 100)

    #horizontal one
    t.penup()
    t.goto(GraphOriginX, GraphOriginY)
    t.color("black")
    t.pendown()
    t.setheading(0)
    t.forward( (IndividualWidth + Spacing)*GraphLength )

    #getting ready to print the hell out of graphs
    t.penup()
    t.goto(GraphOriginX, GraphOriginY)
    setheading(0)
    GraphIndex = 0

    #Created compared list
    Compared100Values = ProportionalList100(Values, GraphReferral)

    #Printing the hell out of graphs
    for Graph in range(0, GraphLength):
        t.forward(Spacing)
        DrawVerticalRectGraph(Compared100Values[Values[GraphIndex]], IndividualWidth, IndividualHeight, 0, 0, FillGraphColor, WantsGraphBorder, BackGroundGraphColor, "black", Texts[GraphIndex])
        setheading(0)
        t.forward(IndividualWidth)

        GraphIndex += 1

    t.pendown()
    t.color("black")
    t.forward(Spacing*2)
    t.penup()

    textPosX = GraphOriginX + Spacing
    textPosY = GraphOriginY + IndividualHeight + Spacing

    t.goto(textPosX, textPosY)
    t.write(GraphTitle, font=("Arial", 24, "normal"))

def GaussCurve(GraphTitle, Sigma, GraphOriginX = -400, GraphOriginY = -200, GraphHeight = 400, GraphWidth = 800, GraphBackgroundColor = "None", GraphColor = "#00ffff"):

    #defining other important original values:
    freq1 = [GraphWidth]
    freq2 = []
    freq3 = []

    #This variable represents the exact middle
    MedianPoint = (GraphWidth / 2) +  GraphOriginX

    t.penup()
    t.goto(GraphOriginX, GraphOriginY)

    #printing the graph's background color
    if GraphBackgroundColor != "None":
        t.color(GraphBackgroundColor)
        t.setheading(0)
        t.begin_fill()
        t.forward(GraphWidth)
        t.left(90)
        t.forward(GraphHeight)
        r.left(90)
        t.forward(GraphWidth)
        t.left(90)
        t.forward(GraphHeight)
        t.left(90)
        t.end_fill()

    #printing the graph's lines
    t.pendown()
    t.setheading(0)
    t.forward(GraphWidth)
    t.left(180)
    t.forward(GraphWidth)
    t.setheading(90)
    t.forward(GraphHeight)
    t.left(180)
    t.forward(GraphHeight)

    #start drawing the actual curve here
    t.color(GraphColor)

    #Draw the middle line, that should represent the overall mean
    t.penup()
    t.goto(MedianPoint, GraphOriginY)
    t.pendown()
    t.color("#dddddd")
    t.setheading(90)
    t.forward(GraphHeight)

    Write("Mean", MedianPoint, GraphOriginY - 30, 16)

def CalculateSigma(ValueSet):

    Sommatory = 0
    SetLength = len(ValueSet)

    #Let's focus on the Mean first
    for Value in ValueSet:
        Sommatory += Value
    
    Mean = Sommatory / SetLength

    #Let's now focus on the quatradic sum ov the values
    QuadraticSommatory = 0

    for Value in ValueSet:
        QuadraticSommatory += (Value - Mean)**2

    Sigma = math.sqrt(QuadraticSommatory / SetLength)

    return Sigma

def CalculateSigmaRanges(ValueSet, Sigma):
    #this function returns a set of values, but subdivided and categorized in classe defined by Sigma
    Corrispondencies = {}
    for n in range(-4, 4):
        Corrispondencies[n] = []

    #calculating mean (will be useful later)
    Sommatory = 0
    for Value in ValueSet:
        Sommatory += Value
    
    Mean = Sommatory / len(ValueSet)
    
    for Value in ValueSet:
        TempIndex = (Value - Mean) / Sigma
        if TempIndex < -4:
            Corrispondencies[-4].append(Value)
        elif TempIndex > +4:
            Corrispondencies[4].append(Value)
        else:
            Corrispondencies[int(TempIndex)].append(Value)

    return Corrispondencies

def NormalDistributionBlockGraph():
    #just forget it for now
    print("NormalDistributionBlockGraph not yet built!")
    
class Aereogram:

    def __init__(self, WantedName, NumValues, Colors, IndividualNames, WantedRadius, DoYouWantBorder = True, WhatBorderColor = "black", WantsToWriteStatisticalValues = False, Measure = "%", DoesHeWantOuterBorder = False):
        self.WantsOuterborder = DoesHeWantOuterBorder
        self.MeasureSymbol = Measure
        self.WantsStatisticalValuesWritten = WantsToWriteStatisticalValues
        self.BorderColor = WhatBorderColor
        self.WantsBorder = DoYouWantBorder
        self.Name = WantedName
        self.Radius = WantedRadius

        self.NumericValues = NumValues
        self.ValueColors = {}
        self.ValueName = {}

        i = 0
        for n in self.NumericValues:
            self.ValueColors[n] = Colors[i]
            i += 1

        i = 0
        for n in self.NumericValues:
            self.ValueName[n] = IndividualNames[i]
            i += 1

        self.GraphOriginX = 0
        self.GraphOriginY = 0

        #I need this variable just to calculate the Median
        TempList = self.NumericValues.copy()
        OrderedNumericList = []

        for x in range(0, len(TempList)):
            TempValue = max(TempList)
            OrderedNumericList.append(TempValue)
            TempList.remove(TempValue)

        MedianIndex = int( len(OrderedNumericList) / 2 ) + 1

        if len(OrderedNumericList) % 2 == 0:
            self.Median = (OrderedNumericList[ MedianIndex ] + OrderedNumericList[ MedianIndex - 1 ]) / 2
        else:
            self.Median = OrderedNumericList[MedianIndex]

        # This will be the sum of all values
        self.Sum = 0

        for Value in self.NumericValues:
            self.Sum += Value
        
        #This is all value's set's mean
        self.Mean = self.Sum / len(self.NumericValues)

        #Mode
        self.MostFrequentValue = mode(OrderedNumericList)

    def draw(self):
        #initial penup
        t.penup()
        t.goto(self.GraphOriginX, self.GraphOriginY)
        


        #initializing position
        t.setheading(-90)

        ProportionAngles = ProportionalList(self.NumericValues, 360)

        #Printing out the varius sectors
        for PrintingValue in self.NumericValues:
            #printing the sector
            t.left(180)
            t.pendown()
            t.begin_fill()
            t.color(self.ValueColors[PrintingValue])
            t.forward(self.Radius)
            t.left(90)
            t.circle(self.Radius, ProportionAngles[PrintingValue])
            t.left(90)
            t.forward(self.Radius)
            t.end_fill()

        #Printing Names
        t.penup()
        t.setheading(90)
        t.color("black")

        for PrintingValue in self.NumericValues:
            #going away from origin
            t.left(ProportionAngles[PrintingValue] / 2)
            t.forward(self.Radius)
            t.pendown()
            t.forward(self.Radius)

            #doing stuff away from origin (writing the name)
            t.penup()
            t.forward(20)
            t.color("black")
            if self.WantsStatisticalValuesWritten:
                t.write(str(self.ValueName[PrintingValue]) + " - " + str(PrintingValue) + self.MeasureSymbol, font=("Arial", 16, "normal"), align= "center")
            else:
                t.write(self.ValueName[PrintingValue], font=("Arial", 16, "normal"), align= "center")
            t.left(180)
            t.forward(20)

            #going back to origin
            t.forward(self.Radius*2)
            t.left(180)
            t.left(ProportionAngles[PrintingValue] / 2)
        
        #printing the border now (if the user wants to)
        if self.WantsBorder:
            t.pensize(2)
            for PrintingValue in self.NumericValues:
                t.color(self.BorderColor)
                t.pendown()
                t.forward(self.Radius)
                t.left(90)
                t.circle(self.Radius, ProportionAngles[PrintingValue])
                t.left(90)
                t.forward(self.Radius)
                t.left(180)
            t.pensize(1)

        #printing the OUTER border now (if the user wants to)
        if self.WantsOuterborder:
            t.forward(self.Radius)
            t.left(90)
            t.pendown()
            t.circle(self.Radius)
            t.penup()
            t.left(90)
            t.forward(self.Radius)
            t.left(180)
            
            
            

        t.penup()
        #resetting pensize
        t.pensize(1)

        #printing the name
        t.left(180)
        t.forward(self.Radius*1.5)
        t.write(self.Name, align="center", font=("Arial", 24, "normal"))

    def LogStatistics(self):
        #printing the header
        print(Tabbing(self.Name, 42, "_") + ".")
        print(".____________________.____________________|")
        print("|" + Tabbing("DATA NAME") + "|" + Tabbing("FREQUENCY") + "|")
        print("|____________________|____________________|")
        
        #printing the contents now
        for PrintingValue in self.NumericValues:
            print("|" + Tabbing(self.ValueName[PrintingValue]) + "|" + Tabbing(str(PrintingValue)) + "|")
        
        print("|____________________|____________________|")
        print("|Mean - - - - - - - -|" + Tabbing(self.Mean) + "|")
        print("|Median value - - - -|" + Tabbing(self.Median) + "|")
        print("|Mode - - - - - - - -|" + Tabbing(self.MostFrequentValue) + "|" + " !")
        print("|Sum- - - - - - - - -|" + Tabbing(self.Sum) + "|")
        print("|Sigma- - - - - - - -|" + Tabbing(CalculateSigma(self.NumericValues)) + "|")
        print("|____________________|____________________|")

        print("\n\n")

def DrawAerogram():
    #keep writing code here
    print("I really have no clue please forgive me")

def HistoGram(Name, Values, ValuesTexts, GraphOriginX = -400, GraphOriginY = -300, IndividualWidth = 100, IndividualHeight = 500, ColumnSpacing = 10, WantsBGBorder = False, WantsBorder = False, ColumnBackGround = "None", WantsIndexes = False, IndexColor = "#dddddd"):
    print("Maybe this can be built")

def ClearScreen():
    t.reset()
    SetTrutleSpeed(SPEED)

def FinishedPrinting():
    done()

print("Welcome to Baxter Grapher, if you encounter any issues, please take a look at the repo at my GitHub https://github.com/syumjoba")
print("Help Modules NOT yet Written")