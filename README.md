# 🚗 Hill Climb Racing Hand Gesture Control

# Introduction
Welcome to the Hill Climb Racing Hand Gesture Control project! This project allows you to play the classic game Hill Climb Racing using only hand gestures, utilizing advanced computer vision techniques. By detecting hand movements and gestures through a webcam, the program translates these gestures into game controls, offering an immersive gaming experience without the need for traditional input devices.

# Features
Gesture Control: Use hand gestures to play Hill Climb Racing.

🖐️ Open Hand (Five Fingers): Accelerate the vehicle.
✊ Closed Fist (Zero Fingers): Reverse the vehicle.
Real-Time Processing: The application processes video input in real-time for a smooth and responsive gaming experience.

Interactive Interface: Displays the number of detected fingers on the screen for better understanding and interaction.

# Technologies Used
**Python:** The core programming language for this project.
**OpenCV:** For capturing and processing video input from the webcam.
**CvZone HandTrackingModule:** To detect hand movements and gestures accurately.
**PyAutoGUI:** To simulate keyboard inputs based on detected gestures.
**NumPy:** For numerical operations and handling image data efficiently.


# Installation
# Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6 or higher
Pip (Python package manager)


#Installation Steps
# 1. Clone the repository:

git clone https://github.com/yourusername/hill-climb-racing-gesture-control.git
cd hill-climb-racing-gesture-control

# 2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
.\venv\Scripts\activate

# 3. Install the required packages:
pip install -r requirements.txt

# 4. Launch the application:
python hill_climb_racing.py


# Usage

# 1. Start the game:

Open **Hill Climb Racing** on your device.
Position your left hand within the camera's field of view.

# 2. Control the game using gestures:

Five Fingers (Open Hand): Accelerate the car.
Zero Fingers (Closed Fist): Move the car in reverse.

# 3. Exit the application:

Press the **'q'** key to exit the program at any time.

# Contributing
Contributions are welcome! If you'd like to improve this project, feel free to submit a pull request or open an issue.
