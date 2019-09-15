#from imagesearch import * 
import checkAdmin, cv2, numpy as np, time, pyautogui, ctypes
from PIL import Image

#Editable Variables
iteration = 0
wait_time = 60
imageNames = ["./images/twitch_points.png"]
imagePrecision = 0.8

userAdmin = checkAdmin.is_user_admin()

if not userAdmin:
    print('Please Run As Admin To Enable Mouse Lock on Click')
    print()

def imagesearch(image, im, precision=0.8):
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

while True:
    iteration += 1
    imgInfo, sizes = [], []
    startTime = time.time() #Iteration Start Time

    print(f'Iteration: {iteration}')
    if len(imageNames) > 1: 
        print("Images to Search: " + str(len(imageNames)))   


    #Image Search Start Time
    imageSearchStart = time.time()

    #Find Images
    screenshot = pyautogui.screenshot()
    for img in imageNames:
        #Get Position
        imgPos = imagesearch(img, screenshot, imagePrecision)

        #Determine Image Size
        with Image.open(img) as img:
            width, height = img.size

        #Create Object For Each Image Found
        imgInfo.append( {"pos" : imgPos, "width" : width, "height" : height} )

    #Image Search End time
    print()
    print("Time to Search For Image(s): " + str(round(time.time() - imageSearchStart,2)) + " Seconds")
    print()


    #Click Images
    currrentImageNumber = 1
    for img in imgInfo:

        if img['pos'][0] != -1:
            imageClickStart = time.time() #Image Click Start Time
            print("Found Image. " + str(currrentImageNumber) + "/" + str(len(imgInfo)))

            if userAdmin:
                print("Locking Mouse Temporarily & Clicking Icon")
                status = ctypes.windll.user32.BlockInput(True) #enable block

                #Click Icon
                userPOS = pyautogui.position()
                pyautogui.moveTo(img['pos'][0] + (img['width']/2), img['pos'][1] + (img['height']/2))
                pyautogui.click()
                pyautogui.moveTo(userPOS)
            
                #Restore Mouse Access
                status = ctypes.windll.user32.BlockInput(False) #disable block 
                print("Restored Mouse Access & Location")
            else:
                #Click Icon
                userPOS = pyautogui.position()
                pyautogui.moveTo(img['pos'][0] + (img['width']/2), img['pos'][1] + (img['height']/2))
                pyautogui.click()
                pyautogui.moveTo(userPOS)


            print("Time to Click: " + str(round(time.time() - imageClickStart, 2)) + " Second(s)")
            print()
            currrentImageNumber += 1 

        else:
            print("Image Not Found. " + str(currrentImageNumber) + "/" + str(len(imgInfo)))
            print()
            currrentImageNumber += 1 
    

    print("Total Iteration Time: " + str(round(time.time() - startTime, 2)))
    print(f"Pausing for {wait_time} seconds.")
    print()
    print("--------------------------------")
    print()
    time.sleep(wait_time)



