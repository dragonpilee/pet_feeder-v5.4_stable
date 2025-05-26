# Pet Feeder CAM V5.4 (Dual Mode)

![Python](https://img.shields.io/badge/Language-Python-blue)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-red)
![YOLO](https://img.shields.io/badge/Object_Detection-YOLO-yellow)
![Haar Cascade](https://img.shields.io/badge/Face_Detection-Haar_Cascade-lightgrey)
![NumPy](https://img.shields.io/badge/Math-NumPy-purple)
![Requests](https://img.shields.io/badge/HTTP-Requests-brightgreen)
![Imutils](https://img.shields.io/badge/Utils-Imutils-orange)
![ESP8266](https://img.shields.io/badge/Hardware-ESP8266-informational)
![Arduino](https://img.shields.io/badge/Controller-Arduino-00979D)

**Pet Feeder CAM V5.4** is an IoT project developed by **Alan Cyril Sunny** for remotely monitoring and feeding pets. It offers **Surveillance Mode** and **Feeder Mode**, enabling pet owners to ensure their pet’s safety and well-being even when away.

> **Developed by Alan Cyril Sunny**  
> If you find this project helpful, please consider ⭐ [starring the repository](https://github.com/dragonpilee/pet-feeder-cam)!

---

## 🔧 Features

- 🐾 **Surveillance Mode**: Real-time monitoring of pets using YOLO object detection.
- 🍖 **Feeder Mode**: Automatic feeding with face detection via Haar cascade for personalized pet interaction.
- 🔁 **Dual Mode Switching**: Toggle between modes based on your need.
- 🌐 **Web Interface**: Easy remote access and control.
- ⚙️ **Customizable Settings**: Feeding intervals, webcam refresh rates, and more.

---

## 🧰 Tech Stack

- **Python**: Backend scripting & logic
- **OpenCV**: Image processing, detection
- **YOLO**: Object detection (Surveillance)
- **Haar Cascade**: Face detection (Feeder)
- **NumPy**: Numerical operations
- **Requests**: HTTP feed access
- **Imutils**: Image resizing utilities
- **Arduino**: Hardware interfacing
- **ESP8266**: Microcontroller for connectivity

---

## ⚙️ Hardware Stack

- **ESP8266 Microcontroller**
- **Servo Motor** (for food dispensing)
- **Webcam** (live feed & detection)
- **Power Supply** (for all components)
- **Enclosure** (protective casing)

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dragonpilee/pet-feeder-cam.git
   cd pet-feeder-cam
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python pet_feeder_cam.py
   ```

---

## 🕹️ Usage

- Press `'s'` to activate Surveillance Mode
- Press `'f'` to activate Feeder Mode
- Adjust all settings from the **web interface**

---

## 👥 Contributors

- Alan Cyril Sunny  
- Litty  
- Nandhna  
- Bijili  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- OpenCV contributors
- YOLO development community
- Python, NumPy, and Requests maintainers
- Open-source hardware & software developers

---

For more information, updates, and documentation, visit the  
👉 [GitHub Repository](https://github.com/dragonpilee/pet-feeder-cam)

Feel free to fork, star ⭐, and contribute! 🐶🐱🤖
