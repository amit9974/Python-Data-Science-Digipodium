import cv2

im = cv2.imread(r'E:\VS Code\Python Data Science Digipodium\Opencv\girl.jpg')

#resize img
h, w, _ = im.shape
small_img = cv2.resize(im,(w//2, h//2))


# change brightness
bright_im = cv2.add(im, 50)
dark = cv2.add(im, -50)


# stich image
stiched_img = cv2.hconcat(im,small_img)
v = cv2.vconcat(im,small_img)

# show img output
cv2.imshow('orignal', im)
cv2.imshow('small', small_img)
cv2.imshow('dark',dark)
cv2.imshow('bright', bright_im)
cv2.imshow('stiched',stiched_img)
cv2.imshow('verticle', v)


cv2.waitKey(0)