import cv2
import numpy as np
import os
import PIL
import time
import requests
import tensorflow as tf
import keras
import subprocess
# import screee
import multiprocessing
# from mss import mss
import pickle

labels = ["with_mask", "without_mask"]

url = "http://hjk:005@192.168.43.1:8080/shot.jpg"  # replace it with 0 to use system default camera

# path to your model
os.chdir("convv")
model = keras.models.load_model("model.h5")

# path to haar cascade
os.chdir("/home/hemanth/PycharmProjects/face_mask_social_tele/dataa")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

"""
def hjk():
    print("hii")
    #os.system('captureimagecam.py')
"""


def main():
    # time.sleep(5)
    #import PIL.ImageGrab
    #im = PIL.ImageGrab.grab()
    #im.save('/home/hemanth/PycharmProjects/face_mask_social_tele/eporting_image/epotingimage.jpg')
    # im.show()
    # time.sleep(5)
    import pyautogui

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screenshot1.png')
    files = {
        'photo': open('screenshot1.png', 'rb')}

    resp = requests.post('https://api.telegram.org/bot1661354902:AAF45IAEwKkmiyeyLv6dWxoQbjSWZb7DN-4/sendPhoto?chat_id'
                         '=-1001422894866&caption=Peoples violating covid protocol by not wearing face mask',
                         files=files)

    # change with your chat id and bot token

    print(resp.status_code)


while True:

    cap = cv2.VideoCapture(url)

    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        toTest = gray[y:y + h, x:x + w]
        toTest = cv2.resize(toTest, (100, 100))
        # cv2.imshow("test2", toTest) #shows the cropped image which is sent to cnn (optional)
        toTest = toTest.reshape(1, 100, 100, 1)

        prediction = model.predict(toTest, verbose=0)

        if np.argmax(prediction) == 0:
            cv2.rectangle(img, (x, y), (x + w, y + h), (48, 216, 48), 2)
            cv2.putText(img, "Mask", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (48, 216, 48), 2)
            cv2.putText(img, str(round(prediction[0][0] * 100, 2)) + "%", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (48, 216, 48), 2)
        elif np.argmax(prediction) == 1:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "No mask", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.putText(img, str(round(prediction[0][1] * 100, 2)) + "%", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 0, 255), 2)
        h = (np.argmax(prediction))
        # time.sleep(5)
        # print(h)
        if h == 1:

            if __name__ == '__main__':
                main()
            # subprocess.run("python screee.py")
            # p1 = multiprocessing.Process(name='p1', target=dhjk)
            # p1.start()
            # os.system('screee.py')
            print("nomask")
            # time.sleep(3)

        # print(tf.gather(labels, np.argmax(prediction)))
    #cv2.namedWindow('FACE MASK AUTOMATION', cv2.WINDOW_FREERATIO)
    #cv2.setWindowProperty('FACE MASK AUTOMATION ', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    hjk2 = cv2.resize(img, (1600, 840))
    cv2.imshow("FACE MASK AUTOMATION", hjk2)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
