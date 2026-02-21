import cv2
import os
import datetime
from detector import detect
from config import SAVE_IMAGES, VIDEO_SOURCE

os.makedirs("captures", exist_ok=True)
os.makedirs("logs", exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)

vehicle_count = 0

print("AI Traffic Monitoring System Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)

    for label, conf, x1, y1, x2, y2 in detections:
        vehicle_count += 1

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        if SAVE_IMAGES:
            filename = f"captures/{label}_{vehicle_count}.jpg"
            cv2.imwrite(filename, frame)

        with open("logs/traffic_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {label}\n")

    cv2.putText(frame, f"Vehicle Count: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.imshow("AI Traffic Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
