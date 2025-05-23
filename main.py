import cv2
import mediapipe as mp
import pyautogui
import time

cam = cv2.VideoCapture(0)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.4,model_complexity=0)
mp_drawing = mp.solutions.drawing_utils

rt = lt = dn = up = False
last_action_time = time.time()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape

    cv2.line(frame, (0, int(0.35 * height)), (width, int(0.35 * height)), (0, 0, 255), 2)
    cv2.line(frame, (0, int(0.6 * height)), (width, int(0.6 * height)), (0, 0, 255), 2)
    cv2.line(frame, (int(0.45 * width), 0), (int(0.45 * width), height), (0, 0, 255), 2)
    cv2.line(frame, (int(0.55 * width), 0), (int(0.55 * width), height), (0, 0, 255), 2)

    results = pose.process(frame)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

        center_x = (left_shoulder.x + right_shoulder.x) / 2

        current_time = time.time()
        if current_time - last_action_time > 0.5:
            if center_x < 0.45 and not lt:
                pyautogui.press("left")
                lt = True
                rt = False
                last_action_time = current_time

            elif center_x > 0.55 and not rt:
                pyautogui.press("right")
                rt = True
                lt = False
                last_action_time = current_time
            
            if left_wrist.y < 0.35:
                pyautogui.press("space")

            if 0.45 <= center_x <= 0.55:
                rt = False
                lt = False

            if left_shoulder.y > 0.6 and right_shoulder.y > 0.6 and not dn:
                pyautogui.press("down")
                dn = True
                up = False
                last_action_time = current_time

            elif left_shoulder.y < 0.35 and right_shoulder.y < 0.35 and not up:
                pyautogui.press("up")
                up = True
                dn = False
                last_action_time = current_time

            if (0.35 < left_shoulder.y < 0.6) and (0.35 < right_shoulder.y < 0.6):
                up = False
                dn = False

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Show Video", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
