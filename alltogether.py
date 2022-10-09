from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
import cv2
import imutils
import pandas as pd
import sys
import numpy as np

from gui2 import Ui_MainWindow

class gui(QtWidgets.QMainWindow, Ui_MainWindow):
    global frame
    global frame2
    global cap
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.chooseButton.clicked.connect(self.selectFile)
        self.playButton.clicked.connect(self.playVideo)

        self.maskButton.clicked.connect(self.playMask)
        self.trackButton.clicked.connect(self.playTracked)
        self.plotButton.clicked.connect(self.plotCoords)

        self.saveButton.clicked.connect(self.saveCoords)
        #self.progressBar()
        """
        self.radioButton.toggled.connect(self.detectBlue)
        self.radioButton_2.toggled.connect(self.detectRed)
        self.radioButton_3.toggled.connect(self.detectYellow)
        self.radioButton_4.toggled.connect(self.detectWhite)
        self.radioButton_8.toggled.connect(self.plotXF)
        self.radioButton_5.toggled.connect(self.plotYF)
        self.radioButton_6.toggled.connect(self.plotZF)
        self.radioButton_7.toggled.connect(self.plotXY)
        self.radioButton_9.toggled.connect(self.plotXYZ)
        self.radioButton_10.toggled.connect(self.csv)
        self.radioButton_11.toggled.connect(self.txt)
        """

    def selectFile(self):
        global file
        file,_ = QFileDialog.getOpenFileName(None, 'open file','',"Video Files(*.mov)")
        self.lineEdit.setText(file)
        return file

    def playVideo(self):

        cap = cv2.VideoCapture(file)

        # Read untill the video is cmpleted
        while (cap.isOpened()):
        # Capture frame by frame

            ret, frame = cap.read()
            frame = imutils.resize(frame, width=1500)
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            # Press Q on keyboard to exitq
            key = cv2.waitKey(1) & 0xFF
            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break

        cap.release()

    def playMask(self):

        if self.radioButton.isChecked():
            LowerBoundaries = (100, 110, 50)
            UpperBoundaries = (140, 255, 255)
        elif self.radioButton_2.isChecked():
            LowerBoundaries = (150, 150, 50)
            UpperBoundaries = (180, 255, 255)
        elif self.radioButton_3.isChecked():
            LowerBoundaries = (20, 100, 100)
            UpperBoundaries = (30, 255, 255)
        elif self.radioButton_4.isChecked():
            LowerBoundaries = (0, 0, 240)
            UpperBoundaries = (180, 255, 255)

        cap = cv2.VideoCapture(file)
        # Read untill the video is cmpleted
        while (cap.isOpened()):
                # Capture frame by frame

                ret, frame = cap.read()
                frame = imutils.resize(frame, width=1500)

                blurred = cv2.GaussianBlur(frame, (11, 11), 0)
                hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
                # construct a mask for the color "green", then perform
                # a series of dilations and erosions to remove any small
                # blobs left in the mask
                mask = cv2.inRange(hsv, LowerBoundaries, UpperBoundaries)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)

                # Display the resulting frame
                cv2.imshow('masked video', mask)
                # Press Q on keyboard to exitq
                key = cv2.waitKey(1) & 0xFF
                # if the 'q' key is pressed, stop the loop
                if key == ord("q"):
                    break
    
    def playTracked(self):

        if self.radioButton.isChecked():
            LowerBoundaries = (100, 110, 50)
            UpperBoundaries = (140, 255, 255)
        elif self.radioButton_2.isChecked():
            LowerBoundaries = (150, 150, 50)
            UpperBoundaries = (180, 255, 255)
        elif self.radioButton_3.isChecked():
            LowerBoundaries = (20, 100, 100)
            UpperBoundaries = (30, 255, 255)
        elif self.radioButton_4.isChecked():
            LowerBoundaries = (0, 0, 240)
            UpperBoundaries = (180, 255, 255)

        cap = cv2.VideoCapture(file)

        # Read untill the video is cmpleted
        while (cap.isOpened()):
                # Capture frame by frame
                ret, frame = cap.read()
                frame = imutils.resize(frame, width=1500)

                blurred = cv2.GaussianBlur(frame, (11, 11), 0)
                hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
                # construct a mask for the color "green", then perform
                # a series of dilations and erosions to remove any small
                # blobs left in the mask
                mask = cv2.inRange(hsv, LowerBoundaries, UpperBoundaries)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)

                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                center = None

                # loop over the contours
                for c in cnts:
                    if cv2.contourArea(c) < 500 and cv2.contourArea(c) > 100:
                        # compute the center of the contour
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                        # draw the contour and center of the shape on the image
                        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                        cv2.circle(frame, (cX, cY), 3, (255, 255, 255), -1)

                # Display the resulting frame
                cv2.imshow('masked video', frame)
                # Press Q on keyboard to exit
                key = cv2.waitKey(1) & 0xFF
                # if the 'q' key is pressed, stop the loop
                if key == ord("q"):
                    break

    def plotCoords(self):
        global AllcXProfile
        cap = cv2.VideoCapture(file)

        if self.radioButton.isChecked():
            LowerBoundaries = (100, 110, 50)
            UpperBoundaries = (140, 255, 255)
            thresh = 120
        elif self.radioButton_2.isChecked():
            LowerBoundaries = (150, 150, 50)
            UpperBoundaries = (180, 255, 255)
            thresh = 165
        elif self.radioButton_3.isChecked():
            LowerBoundaries = (20, 100, 100)
            UpperBoundaries = (30, 255, 255)
            thresh = 168
        elif self.radioButton_4.isChecked():
            LowerBoundaries = (0, 0, 240)
            UpperBoundaries = (180, 255, 255)

        global AllcX
        AllcX = []

        global AllcY
        AllcY = []

        e = 0
        XL = []
        XR = []

        YL = []
        YR = []

        AllcXProfile = []
        AllcYProfile = []

        ZL = []
        ZR = []


        while (cap.isOpened()):

                ret, frame = cap.read()
                if frame is None:
                    break

                frame = imutils.resize(frame, width=1500)
                frame2 = imutils.resize(frame, width=1500)

                y = int(self.lineEdit_5.text())
                x = int(self.lineEdit_4.text())
                h = int(self.lineEdit_3.text())
                w = int(self.lineEdit_2.text())
                frame = frame[y:y + h, x:x + w]

                y2 = int(self.lineEdit_6.text())
                x2 = int(self.lineEdit_8.text())
                h2 = int(self.lineEdit_9.text())
                w2 = int(self.lineEdit_7.text())
                ProfileView = frame2[y2:y2 + h2, x2:x2 + w2]



                blurred = cv2.GaussianBlur(frame, (11, 11), 0)
                hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
                # construct a mask for the color "green", then perform
                # a series of dilations and erosions to remove any small
                # blobs left in the mask
                mask = cv2.inRange(hsv, LowerBoundaries, UpperBoundaries)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)

                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                center = None

                # loop over the contours
                for c in cnts:
                    # compute the center of the contour
                    M = cv2.moments(c)
                    if cv2.contourArea(c) < 500 and cv2.contourArea(c) > 100:

                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                        # draw the contour and center of the shape on the image
                        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                        cv2.circle(frame, (cX, cY), 3, (255, 255, 255), -1)

                        # center = (cX, cY)
                        # print(len(cnts))
                        # If we have 2 contours in a frame that means we have detected two balls.
                        if len(cnts) == 2:
                            AllcX.append(cX)
                            AllcY.append(cY)
                        # If we detect only one contour in a frame that means we only detected one ball so then we give it conditions
                        # if we detect only one ball is the x is smaller or greater than a number we decide which ball it is. right or left one!
                        elif len(cnts) == 1:
                            if cX < thresh:
                                AllcX.append(0)
                                AllcY.append(0)

                                AllcX.append(cX)
                                AllcY.append(cY)

                            elif cX > thresh:
                                AllcX.append(cX)
                                AllcY.append(cY)

                                AllcX.append(0)
                                AllcY.append(0)


                blurredProfile = cv2.GaussianBlur(ProfileView, (11, 11), 0)
                hsvProfile = cv2.cvtColor(blurredProfile, cv2.COLOR_BGR2HSV)

                # construct a mask for the color "green", then perform
                # a series of dilations and erosions to remove any small
                # blobs left in the mask
                maskProfile = cv2.inRange(hsvProfile, LowerBoundaries, UpperBoundaries)
                maskProfile = cv2.erode(maskProfile, None, iterations=2)
                maskProfile = cv2.dilate(maskProfile, None, iterations=2)

                # find contours in the mask and initialize the current
                # (x, y) center of the ball

                cntsProfile = cv2.findContours(maskProfile.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)
                cntsProfile = imutils.grab_contours(cntsProfile)
                centerProfile = None

                # loop over the contours
                for cc in cntsProfile:
                    # compute the center of the contour
                    M2 = cv2.moments(cc)
                    if cv2.contourArea(cc) < 500:

                        cXProfile = int(M2["m10"] / M2["m00"])
                        cYProfile = int(M2["m01"] / M2["m00"])

                        # draw the contour and center of the shape on the image
                        cv2.drawContours(ProfileView, [cc], -1, (0, 0, 255), 2)
                        cv2.circle(ProfileView, (cXProfile, cYProfile), 3, (255, 255, 255), -1)

                        # center = (cX, cY)
                        # print(len(cnts))
                        # If we have 2 contours in a frame that means we have detected two balls.
                        if len(cntsProfile) == 2:
                            AllcXProfile.append(cXProfile)
                            AllcYProfile.append(cYProfile)
                        # If we detect only one contour in a frame that means we only detected one ball so then we give it conditions
                        # if we detect only one ball is the x is smaller or greater than a number we decide which ball it is. right or left one!
                        elif len(cntsProfile) == 1:
                            AllcXProfile.append(cXProfile)
                            AllcXProfile.append(0)


                # Display the resulting frame
                cv2.imshow('masked video', frame)
                # Press Q on keyboard to exit
                key = cv2.waitKey(1) & 0xFF
                # if the 'q' key is pressed, stop the loop
                if key == ord("q"):
                    break


        XL = AllcX[0::2]
        YL = AllcY[0::2]
        ZL = AllcXProfile[1::2]

        # Right Coordinates
        XR = AllcX[1::2]
        YR = AllcY[1::2]
        ZR = AllcXProfile[0::2]

        if self.radioButton_8.isChecked():
            fig = plt.figure()
            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)

            ax1.plot(XR, color='r')
            ax1.set_title("Movement Of the Right Ball")
            ax1.set_xlabel("Frames")
            ax1.set_ylabel("X Coordinates")
            ax2.plot(XL)
            ax2.set_title("Movement Of the Left Ball")
            ax2.set_xlabel("Frames")
            ax2.set_ylabel("X Coordinates")
            plt.show()

        elif self.radioButton_5.isChecked():
            fig = plt.figure()
            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)

            ax1.plot(YR, color='r')
            ax1.set_title("Movement Of the Right Ball")
            ax1.set_xlabel("Frames")
            ax1.set_ylabel("Y Coordinates")
            ax2.plot(YL)
            ax2.set_title("Movement Of the Left Ball")
            ax2.set_xlabel("Frames")
            ax2.set_ylabel("Y Coordinates")
            plt.show()

        elif self.radioButton_6.isChecked():
            fig = plt.figure()
            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)

            ax1.plot(ZR, color='r')
            ax1.set_title("Movement Of the Right Ball")
            ax1.set_xlabel("Frames")
            ax1.set_ylabel("Z Coordinates")
            ax2.plot(ZL)
            ax2.set_title("Movement Of the Left Ball")
            ax2.set_xlabel("Frames")
            ax2.set_ylabel("Z Coordinates")
            plt.show()

        elif self.radioButton_7.isChecked():
            fig = plt.figure()
            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)

            ax1.plot(XR, YR)
            ax1.set_title("Movement Of the Right Ball - 2D")
            ax1.set_xlabel("X Coordinates-Right")
            ax1.set_ylabel("Y Coordinates-Right")
            ax2.plot(XL, YL)
            ax2.set_title("Movement Of the Left Ball - 2D")
            ax2.set_xlabel("X Coordinates-Left")
            ax2.set_ylabel("Y Coordinates-Left")
            plt.show()


        elif self.radioButton_9.isChecked():
            fig = plt.figure()

            ax1 = plt.axes(projection='3d')
            xline = np.array(XR)
            yline = np.array(YR)
            zline = np.array(ZR)
            ax1.plot3D(xline[0:1000], yline[0:1000], zline[0:1000],'gray')
            ax1.set_xlabel('X Coordinates - Right')
            ax1.set_ylabel('Y Coordinates - Right')
            ax1.set_zlabel('Z Coordinates - Right')

            fig2 = plt.figure()
            ax2 = plt.axes(projection='3d')
            xlineL = np.array(XL)
            ylineL = np.array(YL)
            zlineL = np.array(ZL)
            ax2.plot3D(xlineL[0:1000], ylineL[0:1000], zlineL[0:1000], 'gray')
            ax2.set_xlabel('X Coordinates - Left')
            ax2.set_ylabel('Y Coordinates - Left')
            ax2.set_zlabel('Z Coordinates - Left')
            plt.show()

    def saveCoords(self):
        self.plotCoords()
        if self.radioButton_10.isChecked():

            df = pd.DataFrame(AllcX, columns=[" X Coordinates"])
            df.to_csv('DataX.csv', index=False)

            df = pd.DataFrame(AllcY, columns=[" Y Coordinates"])
            df.to_csv('DataY.csv', index=False)

            df = pd.DataFrame(AllcXProfile, columns=[" Z Coordinates"])
            df.to_csv('DataZ.csv', index=False)


        elif self.radioButton_11.isChecked():
            with open('DataX.txt', 'w') as f:
                for item in AllcX:
                    f.write("%s\n" % item)

            with open('DataY.txt', 'w') as f:
                for item in AllcY:
                    f.write("%s\n" % item)

            with open('DataZ.txt', 'w') as f:
                for item in AllcXProfile:
                    f.write("%s\n" % item)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = gui()
    window.setWindowTitle('Marker Detection')
    #window.setWindowIcon(QIcon('icon.png'))
    window.show()
    sys.exit(app.exec_())
