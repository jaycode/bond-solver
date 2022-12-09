import cv2 as cv
import numpy as np

def preprocess(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("gray", gray)
    # cv.waitKey(0)
    # cv.destroyWindow("gray")
    canny = cv.Canny(gray, 50, 150)
    rho = 1
    theta = np.pi/180
    threshold = 50
    minLinLength = 350
    maxLineGap = 6
    linesP = cv.HoughLinesP(canny, rho , theta, threshold, None, minLinLength, maxLineGap)

    def is_vertical(line):
        return line[0]==line[2]
    def is_horizontal(line):
        return line[1]==line[3]
    horizontal_lines = []
    vertical_lines = []

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if (is_vertical(l)):
                vertical_lines.append(l)

            elif (is_horizontal(l)):
                horizontal_lines.append(l)
    for i, line in enumerate(horizontal_lines):
        cv.line(cImage, (line[0], line[1]), (line[2], line[3]), (0,255,0), 3, cv.LINE_AA)

    for i, line in enumerate(vertical_lines):
        cv.line(cImage, (line[0], line[1]), (line[2], line[3]), (0,0,255), 3, cv.LINE_AA)

    cv.imshow("with_line", cImage)
    cv.waitKey(0)
    cv.destroyWindow("with_line") #close the window

if __name__ == "__main__":
    import sys
    # python test.py ../../test.jpeg
    filename = sys.argv[1]
    img = cv.imread(cv.samples.findFile(filename))
    cImage = np.copy(img) #image to draw lines

    csv_output = preprocess(img)
