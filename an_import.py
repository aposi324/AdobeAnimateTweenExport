#Author:        Alexander Posipanko
#Edited:        01/10/2020
#Descripton:    Script to import tween animations into GameMaker, from Adobe Animate CC2020. This is done by acting on JSON data exported
#               with Adobe Animate's "Export to Texture Atlas" feature.
#Python version 3.8

import json
import pprint
import tkinter as tk
from tkinter import filedialog
pp = pprint.PrettyPrinter(indent=1)

#Class to store each frame. An animation will be a series of frames.
class Frame:
    _x = 0
    _y = 0
    _rotation = 0
    _xScale = 1
    _yScale = 1
    _duration = 1
    string = ""

    def __init__(self,x,y,rot,xs,ys):
        self._x = x
        self._y = y
        self._rotation = rot
        self._xScale = xs
        self._yScale = ys
        self.printMe()
        self.toGML()

    def printMe(self):
        string = "X: " + str(self._x) + " Y: " + str(self._y) + " Rot: " + str(self._rotation) + " xScale: " + str(self._xScale) + " yScale: " + str(self._yScale)
        print(string)

    def toGML(self):
        string = ""
        string += "shakeX = " + str(self._x) + ";\n"
        string += "shakeY = " + str(self._y) + ";\n"
        string += "image_angle = " + str(self._rotation) + ";\n"
        string += "image_xscale = " + str(self._xScale) + ";\n"
        string += "image_yscale = " + str(self._yScale) + ";\n"
        print(string)

#Animation class will store an ordered list of all the frames. Layer support is planned in the future.
#class Animation:
#    _frames = []#
#
#    def __init__(self):
#        self._frames = []

#file = input("Enter the path to your file: ")
#print(file)
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename();

with open(file_path) as json_file:   #Open the file
    data = json.load(json_file)
    layer_data = data["ANIMATION"]["TIMELINE"]["LAYERS"]
    #pp.pprint(layer_data)
    for f in layer_data:
        asdf = f["Frames"]
        #print(asdf)
        for j in asdf:  #Level: index
            #pp.pprint(j)
            print("Frame: " + str(j["index"]))

            for n in j["elements"]:
                #frame = Frame(trans)
                trans = n["SYMBOL_Instance"]["DecomposedMatrix"]
                x = float(trans["Position"]["x"])
                y = float(trans["Position"]["y"])
                rot = float(trans["Rotation"]["z"])
                xScale = float(trans["Scaling"]["x"])
                yScale = float(trans["Scaling"]["y"])
                print(x)
                print(y)
                print(rot)
                print(xScale)
                print(yScale)
                frame = Frame(x,y,rot,xScale,yScale)
           # pp.pprint(j["elements"])
            print("=======================================================")
            

input("press enter to exit")