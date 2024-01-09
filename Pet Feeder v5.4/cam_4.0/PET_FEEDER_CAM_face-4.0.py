import requests
import cv2
import numpy as np
import imutils

# Load YOLO
yolo_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
yolo_layer_names = yolo_net.getUnconnectedOutLayersNames()

# Load Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.0.104:8080/shot.jpg"

# List of object classes for YOLO
yolo_classes = [
    "Unknown", "dog", "cat", "bird", "rabbit", "fish", "snake", "turtle", "lion", "monkey", "human",
]

# List of objects corresponding to detected faces
feeder_objects = [
    "Human", "Dog", "Cat", "Bird", "Rabbit",
    "Fish", "Snake", "Turtle", "Hamster", "Guinea Pig",
    "Lizard", "Ferret", "Parrot", "Horse", "Pig",
    "Cow", "Sheep", "Goat", "Elephant", "Monkey"
]

# Flags for different modes
surveillance_mode = False
feeder_mode = False

# Create a window with minimize and maximize flags
cv2.namedWindow("Pet_Feeder_CAM_V4.0_Stable (Dual mode) by alan_cyril for IoT Mini Project [Team Pet Feeder]", cv2.WINDOW_NORMAL)

# While loop to continuously fetch data from the URL
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=640, height=480)

    # Press 's' key to toggle surveillance mode
    key = cv2.waitKey(1)
    if key == 27:  # Press Esc key to exit
        break
    elif key == ord('s'):  # Press 's' key to toggle surveillance mode
        surveillance_mode = not surveillance_mode
        feeder_mode = False  # Turn off feeder mode when surveillance mode is activated
        print(f"Surveillance Mode {'On' if surveillance_mode else 'Off'}")

    # Press 'f' key to toggle feeder mode
    elif key == ord('f'):
        feeder_mode = not feeder_mode
        surveillance_mode = False  # Turn off surveillance mode when feeder mode is activated
        print(f"Feeder Mode {'On' if feeder_mode else 'Off'}")

    # Process detections only if surveillance mode or feeder mode is on
    if surveillance_mode or feeder_mode:
        # Get the blob from the image
        blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)

        if surveillance_mode:
            # Set the input to the YOLO neural network for surveillance mode
            yolo_net.setInput(blob)
            yolo_detections = yolo_net.forward(yolo_layer_names)

            # Process the YOLO detections for surveillance mode
            for detection in yolo_detections:
                for obj in detection:
                    scores = obj[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    if confidence > 0.5:  # You can adjust the confidence threshold
                        # Get the coordinates of the bounding box
                        box = obj[0:4] * np.array([img.shape[1], img.shape[0], img.shape[1], img.shape[0]])
                        (x, y, w, h) = box.astype("int")

                        # Draw the bounding box and label
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Ensure that the class_id is within the range of the classes list
                        if class_id < len(yolo_classes):
                            label = f"{yolo_classes[class_id]}: {confidence:.2f}"
                        else:
                            label = f"Unknown: {confidence:.2f}"

                        cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        elif feeder_mode:
            # Convert the image to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Perform face detection for feeder mode
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces and display objects
            for i, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display object label on the face
                obj_label = feeder_objects[i] if i < len(feeder_objects) else "Unknown Object"
                cv2.putText(img, obj_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the mode status on the frame
    mode_status = "Surveillance Mode: ON" if surveillance_mode else "Feeder Mode: ON" if feeder_mode else "Both Modes: OFF"
    cv2.putText(img, mode_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Pet_Feeder_CAM_V4.0_Stable (Dual mode) by alan_cyril for IoT Mini Project [Team Pet Feeder]", img)

# Cleanup
cv2.destroyAllWindows()

