
from PIL import Image
from helper import *
from time import sleep
import cv2
from numpy import ndarray

import os ,argparse,json

Gmap = json.load(open("map.json"))


def main(src, color):
    if src[-4:] in [".jpg", ".png", "jpeg"]:
        printImage(src, color)
    elif src[-4:] in [".mp4", ".avi", ".mkv"]:
        pass
    else:
        print("Unsupported file type")
        return
    
    # get video file framerate
    framerate = min(cv2.VideoCapture(src).get(cv2.CAP_PROP_FPS), 7)

    # get video frame by frame and pass it to the printImage function
    cap = cv2.VideoCapture(src)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        printImage(frame, color)
        sleep(1/framerate)
    
    

def printImage(src,color):
    txtimag = []
    
    if type(src) == str:
        img = Image.open(src)
    elif type(src) == ndarray:
        img = Image.fromarray(src)
    


    cW,cH=getTerminalSize()
    # print(f"terminal width: {cW} terminal height: {cH}")
    # print(f"image width: {img.width} image height: {img.height}")

    r = cW/img.width
    real_width = int(cW * 1)
    real_height = int(img.height * r* 0.38)

    img = img.resize((real_width,real_height ))

    # print(f"new image width: {img.width} new image height: {img.height}")
    

    
    # convert the image to grayscale with the given number of colors
    img = img.convert("L")
    img = img.quantize(colors=color,method=Image.Quantize.MAXCOVERAGE)
    img = img.convert("L")

    


    # multiply the pixel values by 255 to get the full range of grayscale values
    img = img.point(lambda p: p * 0.2745)

    # print(f"image width: {img.width} image height: {img.height}")



    # loop through the image and get the pixel values
    for i in range(img.height):
        for j in range(img.width):
            txtimag.append(Gmap[str(img.getpixel((j, i)))])
        txtimag.append("\n")
    
    # print the image pixel values to the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("".join(txtimag))

 

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert an image to a text file with pixel values")

    parser.add_argument("src", help="The source image file Example: path/to/image.jpg", type=ValidateFile)
    
    parser.add_argument("-c", "--color", help="The number of colors to use in the image. Default is 45. Example: 20", type=colorType, default=45)


    args = parser.parse_args()


    main(args.src, int(args.color))







