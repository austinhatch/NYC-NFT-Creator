from copy import copy
from fileinput import filename

from numpy import append
import image as image
import random
from ByteComponent import ByteComponent
from PaletteGenerator import PaletteGenerator
from NFTSeeder import NFTSeeder
from imgToSvg import imgToSvg




def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for HW 04. The images
    are then displayed.
    """
    numNFTs = input("Number of NFTs to Generate: ")
    num = int(numNFTs)

    seeder = NFTSeeder()

    imgToSVG = imgToSvg("head")

    imgToSVG.convertImageToSVG("head.png")
    head1 = imgToSVG.byteComponents
    # print(imgToSVG.bounds)
    # strRLE = imgToSVG.toRLE()
    # strRLE = "0" +  "120" + "614" + "818" + "139" + strRLE
    # intRLE = strRLE.encode('utf-8')
    # print(intRLE.hex())
    headColors = imgToSVG.colors
    seeder.addHead(head1)
    # seeder.addHeadPalette(headColors)
    paletteGenerator = PaletteGenerator(head1)
    paletteGenerator.parsePalette()
    # newPalettes = [["#ff1dce","#ff6fff", "#8b008b"]]
    # newPalettes = [["#E6067B"], ["#008000"], ["#FFD700"]]
    # newPalettes = [["#EE7600","#FF0000"]]
    newPalettes = [["#4B0082"]]
    # newPalettes = [["#FB6F90","#fdc7d4"]]
    # newPalettes = [["#F6B45E"]]
    # newPalettes = [["#50C878"]]


    for palette in newPalettes:
        paletteGenerator.decodeGradient(headColors, len(palette))
        genPalette = paletteGenerator.generateNewPalette(palette)
        seeder.addHeadPalette(genPalette)

    imgToSVG = imgToSvg("skin")
    
    imgToSVG.convertImageToSVG("skin.png")
    skin1 = imgToSVG.byteComponents
    print("skin:"+str(len(skin1)))
    skinColors = imgToSVG.colors
    seeder.addSkin(skin1)
    print(str(len(seeder.skins)))
    seeder.addSkinPalette(skinColors)
    paletteGenerator = PaletteGenerator(skin1)
    paletteGenerator.parsePalette()
    # newPalettes = [["#9b7653"], ["#704214"]]
    # newPalettes = [["#916643"]]
    newPalettes =[]
    for palette in newPalettes:
        paletteGenerator.decodeGradient(skinColors, len(palette))
        genPalette = paletteGenerator.generateNewPalette(palette)
        seeder.addSkinPalette(genPalette)

    imgToSVG = imgToSvg("body")
    imgToSVG.convertImageToSVG("jacket.png")
    jacket1 = imgToSVG.byteComponents
    jacketColors = imgToSVG.colors
    seeder.addJacket(jacket1)
    # seeder.addJacketPalette(jacketColors)
    paletteGenerator = PaletteGenerator(jacket1)
    paletteGenerator.parsePalette()
    # newPalettes = (["#880808"], ["#a9a9a9"], ["#FBCEB1"],["#00FF00"])
    # newPalettes = [["#432616"]]
    # newPalettes = [["#ff4f00","#ff7518"]]
    newPalettes=[["#36454F"]]
    for palette in newPalettes:
        paletteGenerator.decodeGradient(jacketColors, len(palette))
        genPalette = paletteGenerator.generateNewPalette(palette)
        seeder.addJacketPalette(genPalette)


    seeder.addBackgroundColor("#ffcccb")
    seeder.addBackgroundColor("#ADD8E6")
    seeder.generateNFTImages(num)




if __name__ == "__main__":
    main()
