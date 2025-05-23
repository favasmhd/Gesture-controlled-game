# 🕹️ Full-Body Gesture Controlled System using MediaPipe Pose & PyAutoGUI

This project uses real-time pose detection via webcam to control keyboard actions using your body movements.

---

## 📌 Features

* Move **left/right** by shifting your shoulders
* Jump (press `space`) by **raising left wrist**
* Move **up/down** by raising or lowering both shoulders

---

## 🧠 How It Works

* **MediaPipe Pose** tracks body landmarks
* Your **shoulder and wrist positions** determine the gesture
* **PyAutoGUI** simulates key presses like `left`, `right`, `space`, `up`, and `down`

---

## 🎮 Controls

| Gesture                     | Action         |
| --------------------------- | -------------- |
| Shoulders shift left        | `Left Arrow`   |
| Shoulders shift right       | `Right Arrow`  |
| Raise left wrist above head | `Space` (jump) |
| Raise both shoulders        | `Up Arrow`     |
| Drop both shoulders         | `Down Arrow`   |

---

## 🧭 On-Screen Guide Lines

The webcam feed shows **4 red reference lines** to guide your movements:

* **Horizontal Lines**:

  * **Top line at 35% height**: Used to detect *raised* hands or shoulders.
  * **Bottom line at 60% height**: Used to detect *lowered* shoulders.

* **Vertical Lines**:

  * **Left line at 45% width** and **right line at 55% width**:

    * Define a neutral zone for shoulder alignment.
    * If your shoulders move outside this zone, it triggers `left` or `right` actions.

These lines help you understand when a gesture will be recognized.

---

## 🛠️ Requirements

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ How to Run

```bash
python3 main.py
```

Press `q` to quit the app.

---

## 📌 Notes

* Good lighting improves detection.
* Avoid cluttered backgrounds.
* You can tweak thresholds or line positions in the code if gestures feel too sensitive or unresponsive.

---
