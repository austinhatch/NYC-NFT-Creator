from copy import copy
from fileinput import filename
import image as image
import random
from ByteComponent import ByteComponent
from PaletteGenerator import PaletteGenerator
from imgToSvg import imgToSvg
import os

def bytesToSvg(bytes, palette):
    print(len(palette))
    print(len(bytes))
    rects = []
    for byte in bytes:
        rects.append(byte.toSVG(palette))
    return rects

class NFTSeeder:

    backgroundColors= []
    headPalettes = []
    skinPalettes = []
    jacketPalettes = []
    heads = []
    skins = []
    jackets = []

    def addHead(self,byteComponents):
        self.heads.append(byteComponents.copy())

    def addJacket(self,byteComponents):
        self.jackets.append(byteComponents.copy())
    
    def addSkin(self,byteComponents):
        self.skins.append(byteComponents.copy())
    
    def addHeadPalette(self,colors):
        self.headPalettes.append(colors.copy())
    
    def addJacketPalette(self,colors):
        self.jacketPalettes.append(colors.copy())
    
    def addSkinPalette(self,colors):
        self.skinPalettes.append(colors.copy())

    def addBackgroundColor(self,color):
        self.backgroundColors.append(color)
    
    
    def generateNFTImages(self,count):
        for i in range (0, count):
            head = random.choice(self.heads)
            headPalette = random.choice(self.headPalettes)

            jacket = random.choice(self.jackets)
            jacketPalette = random.choice(self.jacketPalettes)

            skin = random.choice(self.skins)
            skinPalette = random.choice(self.skinPalettes)

            background = random.choice(self.backgroundColors)

            filename = "NYC"+ str(i) + ".svg"
            dirname = os.path.dirname(__file__)
            svgFile = open(dirname+ "/GeneratedNFTs/"+filename, "w")

            header = '<svg width="780" height="1000" viewbox ="0,0,780,1000" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges"  style ="background: black">'
            svgFile.write(header)
            headRects = bytesToSvg(head, headPalette)
            skinRects = bytesToSvg(skin, skinPalette)
            jacketRects = bytesToSvg(jacket, jacketPalette)
            for rect in skinRects:
                svgFile.write(rect)
            for rect in jacketRects:
                svgFile.write(rect)
            for rect in headRects:
                svgFile.write(rect)
            svgFile.write('</svg>')

            headFile = "head"+ str(i) + ".svg"
            dirname = os.path.dirname(__file__)
            svgFile = open(dirname+ "/Components/"+headFile, "w")
            header = '<svg width="780" height="1000" viewbox ="0,0,780,1000" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">'
            svgFile.write(header)
            for rect in headRects:
                 svgFile.write(rect)
            svgFile.write('</svg>')

            bodyFile = "body" + str(i) + ".svg"
            dirname = os.path.dirname(__file__)
            svgFile = open(dirname+ "/Components/"+bodyFile, "w")
            header = '<svg width="780" height="1000" viewbox ="0,0,780,1000" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges"  style ="background: black">'
            svgFile.write(header)
            for rect in skinRects:
                    svgFile.write(rect)
            for rect in jacketRects:
                svgFile.write(rect)
            svgFile.write('</svg>')

            bodyFile = "skin" + str(i) + ".svg"
            dirname = os.path.dirname(__file__)
            svgFile = open(dirname+ "/Components/"+bodyFile, "w")
            header = '<svg width="780" height="1000" viewbox ="0,0,780,1000" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">'
            svgFile.write(header)
            for rect in skinRects:
                    svgFile.write(rect)
            svgFile.write('</svg>')








