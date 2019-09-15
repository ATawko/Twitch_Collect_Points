from imagesearch import *

iteration = 0
wait_time = 60

while True:
    iteration += 1
    print(f'Iteration: {iteration}')

    time1 = time.process_time()
    
    for i in range(10):
        pos = imagesearch("./twitch_points.png", 0.8)
        #imagesearcharea("./panda.png", 0, 0, 800, 600, 0.8, im)
    
    if pos[0] != -1:
        print("Found Image in: " + str(round(time.process_time() - time1,2)) + " seconds")
        currentPOS = pyautogui.position()
        print('Current Mouse Location: ' + str(currentPOS) + ", Image Location: " + str(pos))

        pyautogui.moveTo(pos[0] + 15, pos[1] + 15)
        pyautogui.click()
        pyautogui.moveTo(currentPOS)

    else:
        print("Image Not Found")
        
    
    print(f"Pausing for {wait_time} seconds.")
    print()
    time.sleep(wait_time)



