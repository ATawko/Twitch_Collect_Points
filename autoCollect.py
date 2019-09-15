from imagesearch import *
from ctypes import *
from PIL import Image

#Editable Variables
iteration = 0
wait_time = 60
imageNames = ["./twitch_points.png"]
imagePrecision = 0.8

while True:
    iteration += 1
    imgInfo, sizes = [], []

    print(f'Iteration: {iteration}')    

    #Find Images
    for img in imageNames:
        #Get Position
        imgPos = imagesearch(img, imagePrecision)

        #Determine Image Size
        with Image.open(img) as img:
            width, height = img.size

        #Create Object For Each Image Found
        imgInfo.append( {"pos" : imgPos, "width" : width, "height" : height} )
        

    #Click Images
    for img in imgInfo:

        if img['pos'][0] != -1:
            print("Found Image")

            print("Locking Mouse Temporarily & Clicking Icon")
            ok = windll.user32.BlockInput(True) #enable block

            #Click Icon
            userPOS = pyautogui.position()
            pyautogui.moveTo(img['pos'][0] + (width/2), img['pos'][1] + (height/2))
            pyautogui.click()
            pyautogui.moveTo(userPOS)

            #Restore Mouse Access
            ok = windll.user32.BlockInput(False) #disable block 
            print("Restored Mouse Access & Location")

        else:
            print("Image Not Found")

 
        
    
    print(f"Pausing for {wait_time} seconds.")
    print()
    time.sleep(wait_time)



