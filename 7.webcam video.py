import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Video', frame)
    
    key = cv2.waitKey(30)
    
    if key == 27:  
        break

cap.release()
cv2.destroyAllWindows()
