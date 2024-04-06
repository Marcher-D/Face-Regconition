import os
import cv2
import time

num = int(input("The number of new labels you want to add: "))
number_images = 20

for i in range(num):
    name = input("Name of the label: ")
    label = open("D:\\My python 3\\PycharmProjects\\pythonProject\\Dataset\\labels.txt", "w")
    label.write(f"{i} {name}")
    label.close()
    labelname = os.path.join("D:\\My python 3\\PycharmProjects\\pythonProject\\Dataset", name)

    cap = cv2.VideoCapture(0)
    for imgnum in range(number_images):
        print("Collecting images {}".format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(labelname, f"Num {imgnum+1} {name}.jpg")
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame", frame)
        time.sleep(0.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

