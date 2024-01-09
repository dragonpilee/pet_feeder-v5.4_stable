# pet_feeder-v5.4_stable
pet feeder with advaced face detection and timer

This mini project presents an Internet of Things (IoT) solution for remotely controlling a pet feeder
using an ESP8266 microcontroller. The system integrates a web interface accessible over WiFi,
allowing users to interact with the pet feeder. Key features include the ability to turn the feeder
on/off, toggle a webcam feed, and customize feeding intervals.
The ESP8266 microcontroller establishes a connection to a local WiFi network, and an embedded
web server is created using the ESP8266WebServer library. A servo motor controls the pet feeder's
mechanism, simulating the feeding action for the pet. The web interface provides a user-friendly
experience, displaying real-time information about the servo and webcam status.
Users can dynamically control the feeding process through the web interface, adjusting the feeding
frequency and enabling/disabling the webcam feed. The project aims to offer convenience for pet
owners, allowing them to monitor and feed their pets remotely.
The project also emphasizes collaboration, as indicated by the team member names in the web
interface. The system is designed to be extensible, and the code includes placeholders for additional
JavaScript logic to asynchronously communicate with the server for real-time status updates.
Overall, this IoT mini project showcases a practical application of connected devices,
demonstrating how technology can enhance the interaction between pet owners and their pets. The
web-based control interface provides an intuitive and accessible means for managing the pet
feeder's functionality.

A simple Python script using the OpenCV and requests libraries to continuously fetch an image
from a given URL and display it in a window. The script is intended for streaming images from an
IP camera, typically hosted by a mobile device.
breakdown of the code:
1. Importing Libraries:
pythonCopy code
import requests
import cv2
import numpy as np
import imutils
• requests : Used for making HTTP requests to the specified URL.
• cv2 : OpenCV library for computer vision tasks.
• numpy : NumPy library for numerical operations on arrays.
• imutils : A set of convenience functions for OpenCV, particularly for resizing
images.
2. Setting up URL:
pythonCopy code
url = "http://192.168.0.104:8080/shot.jpg"
Replace this URL with the actual URL of your IP camera. The "/shot.jpg" suffix is common
for many IP camera streams.
3. While Loop for Continuous Image Fetching:
pythonCopy code
while True:
This initiates an infinite loop that continuously fetches and displays images until the user
presses the Esc key.
4. Fetching and Decoding Image:
pythonCopy code
img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
img = cv2.imdecode(img_arr, -1)
• requests.get(url) : Fetches the image data from the specified URL.
• np.array(bytearray(img_resp.content), dtype=np.uint8) :
Converts the byte data to a NumPy array.
• cv2.imdecode(img_arr, -1) : Decodes the image using OpenCV.
5. Resizing Image:
pythonCopy code
img = imutils.resize(img, width=1000, height=1800)
Resizes the image to have a width of 1000 pixels and a height of 1800 pixels using the
imutils.resize function.
6. Displaying Image:
pythonCopy code
cv2.imshow("Pet_Feeder_CAM", img)
Displays the image in a window with the title "Pet_Feeder_CAM".
7. Exiting the Loop:
pythonCopy code
if cv2.waitKey(1) == 27:
break
The loop is terminated if the user presses the Esc key (ASCII code 27).
8. Closing OpenCV Windows:
pythonCopy code
cv2.destroyAllWindows()
Closes all OpenCV windows when the script is terminated.
In summary, this script continuously fetches images from an IP camera and displays them in a
window using OpenCV. It is a basic example and can be extended for more complex applications,
such as video streaming or computer vision tasks.

Hardware Components:
1. ESP8266 Microcontroller:
• The central processing unit that controls the entire system.
• Manages WiFi connectivity and serves as the brain for processing requests.
2. Servo Motor:
• Mechanism for controlling the pet feeder's opening and closing action.
• Attached to a designated pin on the ESP8266 for control.
3. Webcam:
• Captures live video feed for remote monitoring.
• Connected to a separate system, and its status is toggled through the ESP8266.
4. Power Supply:
• Provides the necessary power to the ESP8266, servo motor, and webcam.
Software Components:
1. Arduino Sketch:
• Written code that runs on the ESP8266.
• Manages the main logic for handling HTTP requests, servo control, feeding
intervals, and webcam toggling.
2. ESP8266WiFi Library:
• Enables the ESP8266 to connect to a local WiFi network, facilitating
communication with the web interface.
3. ESP8266WebServer Library:
• Implements the web server functionality on the ESP8266, handling incoming HTTP
requests and serving web pages.
4. Servo Library:
• Provides functions to control the servo motor, allowing the opening and closing of
the pet feeder.
5. ESP8266HTTPClient Library:
• Facilitates making HTTP requests to external systems, in this case, used for fetching
the webcam feed.
6. Web Interface (HTML, CSS, JavaScript):
•••HTML markup for creating the structure of the web pages.
CSS for styling the web pages and ensuring a user-friendly interface.
JavaScript for dynamic updates on the web interface and potentially asynchronous
communication with the server.
Block Diagram and Explanation:
1. User Interface (Web Browser):
• Users interact with the system through a web browser, accessing the web interface
hosted on the ESP8266.
2. ESP8266 Microcontroller:
• The ESP8266 runs the Arduino sketch, managing the core logic of the system.
• Handles incoming HTTP requests and controls the servo motor and webcam based
on user commands.
3. Servo Motor Control:
• The ESP8266 sends signals to the servo motor to control the pet feeder's opening
and closing actions.
• The servo motor physically manipulates the feeder mechanism.
4. Webcam Control:
• The ESP8266 toggles the webcam status based on user commands.
• If enabled, the webcam captures live video feed for remote monitoring.
5. Web Interface Generation:
• The ESP8266 generates the web interface using HTML, CSS, and JavaScript.
• The interface displays real-time information about servo and webcam status and
allows users to control the pet feeder.
6. WiFi Connectivity:
• The ESP8266 connects to a local WiFi network, enabling communication between
the microcontroller and user devices.
7. Power Supply:
•Provides the necessary power to the ESP8266, servo motor, and potentially the
webcam.
This block diagram illustrates the flow of information and control within the pet feeder system.
Users access the web interface, which communicates with the ESP8266 to control the servo, toggle
the webcam, and customize feeding intervals. The system enhances user convenience by providing
remote access and monitoring capabilities for pet owners.

