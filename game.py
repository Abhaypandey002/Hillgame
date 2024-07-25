# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import pyautogui

# detector = HandDetector(detectionCon=0.5, maxHands=2)
# cap = cv2.VideoCapture(1)
# cap.set(3, 600)
# cap.set(4, 400)

# while True:
#     success, img = cap.read()
#     img = cv2.flip(img, 1)
#     hand, img = detector.findHands(img)
#     if hand and hand[0]["type"] == ["Left"]:
#         fingers = detector.fingersUp(hand[0])
#         totalFingers = fingers.count(1)
#         cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
#         if totalFingers == 5:
#             pyautogui.keyDown("right")
#             pyautogui.keyUp("left")
#         if totalFingers == 0:
#             pyautogui.keyDown("left")
#             pyautogui.keyUp("right")


#     cv2.imshow('Camera Feed', img)
#     cv2.waitKey(1)



import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

# Initialize the hand detector
detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(1)  # Default camera
cap.set(3, 600)  # Set width
cap.set(4, 400)  # Set height

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        continue
        
    img = cv2.flip(img, 1)  # Flip image for a mirror effect
    hand, img = detector.findHands(img)  # Detect hands
    
    if hand and hand[0]["type"] == "Left":  # Correct hand type check
        fingers = detector.fingersUp(hand[0])  # Count fingers
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
        # Right key press
        if totalFingers == 5:
            if not pyautogui.keyDown('right'):
                pyautogui.keyDown("right")
                pyautogui.keyUp("left")
            time.sleep(0.1)
        
        # Left key press
        elif totalFingers == 0:
            if not pyautogui.keyDown('left'):
                pyautogui.keyDown("left")
                pyautogui.keyUp("right")
            time.sleep(0.1)

    cv2.imshow('Camera Feed', img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
