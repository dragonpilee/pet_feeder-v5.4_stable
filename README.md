**Pet Feeder CAM V4.0 (Dual Mode) by Team Pet Feeder**



### Overview
Pet Feeder CAM V4.0 is an IoT project developed by Team Pet Feeder for remotely monitoring and feeding pets. This project incorporates two modes: Surveillance Mode and Feeder Mode, providing users with versatile functionalities to ensure the well-being of their pets even when they are away.

### Features
- **Surveillance Mode**: Utilizes YOLO (You Only Look Once) object detection for real-time monitoring of pet activities.
- **Feeder Mode**: Enables automatic feeding of pets and detects faces for personalized interaction.
- **Dual Mode Operation**: Seamlessly switch between surveillance and feeder modes based on your preferences.
- **Web Interface Integration**: Control the pet feeder remotely through a user-friendly web interface.
- **Customizable**: Easily adjust feeding intervals, webcam refresh rates, and other settings to suit your pet's needs.

### Tech Stack
- **Python**: The core scripting language for the project, used for backend logic, image processing, and communication with hardware components.
- **OpenCV**: A powerful computer vision library utilized for object detection, face detection, and image manipulation.
- **YOLO (You Only Look Once)**: A state-of-the-art object detection system used in Surveillance Mode for real-time detection and tracking of objects.
- **Haar Cascade Classifier**: Employed for face detection in Feeder Mode, allowing personalized interaction with pets.
- **Requests Library**: Facilitates HTTP requests to fetch the webcam feed from the specified URL.
- **NumPy**: Utilized for numerical operations, array manipulation, and efficient data handling.
- **Imutils**: Provides convenient functions for resizing images, an essential task in image processing applications.

### Hardware Stack
- **ESP8266 Microcontroller**: Powers the pet feeder system, allowing it to connect to the Wi-Fi network and serve the web interface.
- **Servo Motor**: Controls the opening and closing of the pet feeder to dispense food to the pets.
- **Webcam**: Provides live video feed for surveillance and interaction with pets.
- **Power Supply**: Powers the ESP8266 microcontroller and servo motor to ensure continuous operation of the pet feeder system.
- **Enclosure**: Provides a housing for the hardware components, ensuring protection and stability.

### Installation
1. Clone the repository: `git clone https://github.com/team-pet-feeder/pet-feeder-cam.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python pet_feeder_cam.py`

### Usage
- Press 's' key to toggle Surveillance Mode.
- Press 'f' key to toggle Feeder Mode.
- Adjust settings in the web interface for personalized control.

### Contributors
- Alan Cyril
- Bijali Gupta
- Litty Mathew
- Nandhana Raj

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements
Special thanks to the creators of OpenCV, YOLO, and all contributors to the libraries and frameworks used in this project.

For detailed documentation and updates, visit the [project repository](https://github.com/team-pet-feeder/pet-feeder-cam). Feel free to contribute and enhance the functionality of Pet Feeder CAM V4.0! 🐾🤖
