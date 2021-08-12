import cv
import numpy as np
import pyautogui

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # img = pyautogui.screenshot(region=(0, 0, 300, 400))
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv.destroyAllWindows()
out.release()