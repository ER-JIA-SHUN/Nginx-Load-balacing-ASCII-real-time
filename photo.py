from PIL import Image, ImageDraw, ImageFont # pillow
from colour import Color
import numpy as np
import cv2

def apixel_samplingiiart(picture, pixel_sampling, contrast,output_picture, color1='black', color2='blue', bgcolor='white'):
    # The array of apixel_samplingii symbols from white to black
    chars = np.asarray(list('           ~!@#$%^&*()-=0123456789'))
    # Load the fonts and then get the the height and width of a typical symbol 
    # You can use different fonts here
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height/letter_width
    # open the input file
    img = Image.open(picture)
    # Based on the desired output image size, calculate how many apixel_samplingii letters are needed on the width and height
    widthByLetter = round(img.size[0]*pixel_sampling*WCF)
    heightByLetter = round(img.size[1]*pixel_sampling)
    S = (widthByLetter, heightByLetter)
    # Resize the image based on the symbol width and height
    img = img.resize(S)
    # Get the RGB color values of each sampled pixel point and convert them to graycolor using the average method
    img = np.sum(np.asarray(img), axis=2)
    # Normalize the results, enhance and reduce the brightness contrast. 
    # Map graypixel_samplingale values to bins of symbols
    img -= img.min()
    img = (1.0 - img/img.max())**contrast*(chars.size-1)
    # Generate the apixel_samplingii art symbols 
    lines = ("\n".join( ("".join(r) for r in chars[img.astype(int)]) )).split("\n")
    # Create gradient color bins
    nbins = len(lines)
    colorRange = list(Color(color1).range_to(Color(color2), nbins))
    #Create an image object, set its width and height
    newImg_width= letter_width *widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    # Print symbols to image
    leftpadding=0
    y = 0
    lineIdx=0
    for line in lines:
        color = colorRange[lineIdx]
        lineIdx +=1
        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height
    # Save the image file
    newImg.save(output_picture)

def main():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    result, image = cam.read()
    # If image will detected without any error,it will show result
    if result:
        # showing result, it take frame name and image
        # output
        cv2.imshow("Camera", image)
        # saving image in local storage
        cv2.imwrite("Original.png", image)
        cv2.destroyWindow("Camera")
        picture = "Original.png"
        # pixel sampling rate in width
        # pixel_sampling: the horizontal pixel sampling rate. It should be between 0(exclusive) and 1(inclusive)
        # The larger the number, the more details in the output
        pixel_sampling = 0.1
        # contrast adjustment
        # contrast: >0. It's an image tuning factor. If contrast>1, the image will look brighter; if 0<contrast<1, the image will look darker
        contrast= 2
        apixel_samplingiiart(picture, pixel_sampling, contrast, "result_other.png","red","green")
main()