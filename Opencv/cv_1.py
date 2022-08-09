import cv2

img = cv2.imread(r"E:\VS Code\Python Data Science Digipodium\Opencv\girl.jpg")

if img is None:
    print("Image not found")
else:
    print("Image found")
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_BGR = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    img_yub = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    cv2.imshow('process',img)
    cv2.imshow('grey',img_grey)
    cv2.imshow('rgb',img_rgb)
    cv2.imshow('bgr',img_BGR)
    cv2.imshow('yub',img_yub)

    cv2.imwrite('grey_img.jpg',img_grey)
    cv2.imwrite('rgb_img.jpg',img_rgb)
    cv2.waitKey(0)
  
   
