#!/usr/bin/env python3

import cv2
import numpy as np
from time import time
from ultralytics import YOLO


class TrafficSignDetector:
    def __init__(self, model_path, conf_threshold=0.4):
        self.detector = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.class_names = self.detector.names
        self.colors = np.random.randint(0, 255, size=(len(self.class_names), 3), dtype=np.uint8)

        # FPS tracking
        self.fps_start_time = time()
        self.frame_count = 0
        self.fps = 0

    def run_detection(self, frame):
        results = self.detector.predict(frame, conf=self.conf_threshold)
        processed_frame = frame.copy()

        if results and len(results) > 0:
            result = results[0]
            boxes = result.boxes

            if len(boxes) > 0:
                detections = boxes.xyxy.cpu().numpy()
                confidences = boxes.conf.cpu().numpy()
                class_ids = boxes.cls.cpu().numpy().astype(int)

                for box, conf, cls_id in zip(detections, confidences, class_ids):
                    x1, y1, x2, y2 = box
                    cls_name = self.class_names[cls_id]
                    color = self.colors[cls_id].tolist()

                    # Draw bounding box and label
                    cv2.rectangle(processed_frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                    label = f"{cls_name} {conf:.2f}"
                    text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
                    cv2.rectangle(processed_frame, (int(x1), int(y1) - text_size[1] - 5),
                                  (int(x1) + text_size[0], int(y1)), color, -1)
                    cv2.putText(processed_frame, label, (int(x1), int(y1) - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Display FPS
        self.frame_count += 1
        if self.frame_count >= 10:
            fps_end_time = time()
            time_diff = fps_end_time - self.fps_start_time
            self.fps = self.frame_count / time_diff
            self.frame_count = 0
            self.fps_start_time = time()

        cv2.putText(processed_frame, f"FPS: {self.fps:.2f}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return processed_frame


def main():
    model_path = "/home/harekrishna/mohit/TSR/model 2/model/best_model.pt"# Replace with your YOLOv8 model path
    detector = TrafficSignDetector(model_path)

    # Set your stereo LEFT camera index here (e.g., 2 if using /dev/video2)
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break

        # If stereo image, split left frame (assuming side-by-side)
        frame_height, frame_width = frame.shape[:2]
        left_frame = frame[:, :frame_width // 2]

        processed_frame = detector.run_detection(left_frame)
        cv2.imshow('YOLOv8 Traffic Sign Detection', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

