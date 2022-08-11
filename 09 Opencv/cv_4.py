import cv2

# video = cv2.VideoCapture(0) # 0 is use for webcam
# video = cv2.VideoCapture(1) # 1 is use for external webcam
video = cv2.VideoCapture(r'E:\All Projects\Python Based Projects\Open CV\04 Video Capture in OpenCV\video.mp4')

while video.isOpened():
    status, img=video.read()
    if status:
        cv2.imshow('video',img)
        
        if cv2.waitKey(1) == 27:
            break
    else:
        print('Video end')
        break

video.release()
cv2.destroyAllWindows()