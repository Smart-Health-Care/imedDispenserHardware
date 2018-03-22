from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
#@shar
def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):
    # # Loop over all decoded objects
    # for decodedObject in decodedObjects:
    #     points = decodedObject.location
    #
    #     # If the points do not form a quad, find convex hull
    #     if len(points) > 4:
    #         hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
    #         hull = list(map(tuple, np.squeeze(hull)))
    #     else:
    #         hull = points;
    #
    #     # Number of points in the convex hull
    #     n = len(hull)
    #
    #     # Draw the convext hull
    #     for j in range(0, n):
    #         cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)
    cv2.waitKey(1)


# Main
if __name__ == '__main__':
    # Read image
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        decodedObjects = decode(img)
        if decodedObjects:
            break
        display(img, decodedObjects)
