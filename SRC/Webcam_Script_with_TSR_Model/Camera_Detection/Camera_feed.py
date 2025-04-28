
    # model_path = "C://Z_Project//Project//yolov8n.pt"

import cv2
import numpy as np
from time import time
from ultralytics import YOLO

class TrafficSignDetector:
    def __init__(self, model_path, conf_threshold=0.25, iou_threshold=0.45):
        """
        Initialize the traffic sign detector with a YOLOv8 model
        
        Args:
            model_path (str): Path to the .pt YOLO model file
            conf_threshold (float): Confidence threshold for detections
            iou_threshold (float): IOU threshold for NMS
        """
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        
        # Load YOLO model
        self.model = self.load_model(model_path)
        
        # Get class names from the model
        self.class_names = self.model.names
        
        # Define colors for visualization
        np.random.seed(42)  # For reproducible colors
        self.colors = np.random.randint(0, 255, size=(len(self.class_names), 3), dtype=np.uint8)
    
    def load_model(self, model_path):
        """
        Load the YOLOv8 model from the specified path
        
        Args:
            model_path (str): Path to the .pt model file
            
        Returns:
            The loaded model
        """
        # Load the model using YOLO class from ultralytics
        model = YOLO(model_path)
        
        return model
    
    def detect(self, frame):
        """
        Perform detection on a frame
        
        Args:
            frame (numpy.ndarray): Input frame
            
        Returns:
            processed_frame (numpy.ndarray): Frame with detections drawn
            detections (list): List of detection results
        """
        # Create a copy of the frame for drawing
        processed_frame = frame.copy()
        
        # Perform inference with confidence threshold
        results = self.model.predict(frame, conf=self.conf_threshold, iou=self.iou_threshold)
        
        # Process results (YOLOv8 format)
        if results and len(results) > 0:
            # Get the first result (for single image)
            result = results[0]
            
            # Get boxes, confidence scores, and class IDs
            boxes = result.boxes
            
            # If boxes exist
            if len(boxes) > 0:
                # Convert to numpy for easier processing
                if hasattr(boxes, 'xyxy'):
                    detections = boxes.xyxy.cpu().numpy()  # [x1, y1, x2, y2]
                    confidences = boxes.conf.cpu().numpy()  # confidence scores
                    class_ids = boxes.cls.cpu().numpy().astype(int)  # class ids
                    
                    # Draw detections
                    for i, (box, conf, cls_id) in enumerate(zip(detections, confidences, class_ids)):
                        x1, y1, x2, y2 = box
                        
                        # Get class name and color
                        cls_name = self.class_names[cls_id]
                        color = self.colors[cls_id].tolist()
                        
                        # Draw bounding box
                        cv2.rectangle(processed_frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                        
                        # Draw label
                        label = f"{cls_name} {conf:.2f}"
                        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
                        cv2.rectangle(processed_frame, 
                                    (int(x1), int(y1) - text_size[1] - 5), 
                                    (int(x1) + text_size[0], int(y1)), 
                                    color, 
                                    -1)
                        cv2.putText(processed_frame, 
                                label, 
                                (int(x1), int(y1) - 5), 
                                cv2.FONT_HERSHEY_SIMPLEX, 
                                0.5, 
                                (255, 255, 255), 
                                2)
                
                return processed_frame, boxes
        
        # Return the original frame if no detections
        return processed_frame, []

def main():
    # Path to your YOLO model
    model_path = "/home/harekrishna/Documents/Camera_Detection/best_model.pt" # Update this to your actual model path
    
    # Initialize detector
    detector = TrafficSignDetector(model_path, conf_threshold=0.4)
    
    # Open webcam
    cap = cv2.VideoCapture(0)  # Use 0 for default camera
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Set camera resolution (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Variables for FPS calculation
    fps_start_time = time()
    frame_count = 0
    fps = 0
    
    print("Press 'q' to quit")
    
    while True:
        # Read frame from camera
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image")
            break
        
        # Calculate FPS
        frame_count += 1
        if frame_count >= 10:  # Update FPS every 10 frames
            fps_end_time = time()
            time_diff = fps_end_time - fps_start_time
            fps = frame_count / time_diff
            frame_count = 0
            fps_start_time = time()
        
        # Run detection
        processed_frame, detections = detector.detect(frame)
        
        # Display FPS
        cv2.putText(processed_frame, f"FPS: {fps:.2f}", (20, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display the frame
        cv2.imshow('Traffic Sign Detection', processed_frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
 
