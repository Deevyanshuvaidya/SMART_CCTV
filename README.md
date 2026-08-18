# 🎥 SMART_CCTV

> **An intelligent computer-vision-based CCTV surveillance system with real-time face recognition, visitor tracking, entry/exit monitoring, and automated attendance-style logging.**

**SMART_CCTV** is a desktop-based intelligent surveillance application developed using **Python, OpenCV, Tkinter, Haar Cascade Classifiers, and LBPH Face Recognition**.

The system transforms a conventional webcam/CCTV camera into a smarter monitoring solution capable of detecting and recognizing registered individuals, identifying unknown faces, tracking visitor movement, recording entry and exit events, and maintaining visitor information in local files.

The project was also deployed and tested in a **college hostel environment**, where it was used as a practical smart-surveillance solution.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Project Objectives](#-project-objectives)
* [Key Features](#-key-features)
* [How the System Works](#-how-the-system-works)
* [Technology Stack](#-technology-stack)
* [Computer Vision Techniques](#-computer-vision-techniques)
* [System Architecture](#-system-architecture)
* [Application Modules](#-application-modules)
* [Project Structure](#-project-structure)
* [Face Registration](#-face-registration)
* [Face Training](#-face-training)
* [Face Recognition](#-face-recognition)
* [Unknown Face Detection](#-unknown-face-detection)
* [Visitor In/Out Detection](#-visitor-inout-detection)
* [Data Storage](#-data-storage)
* [GUI](#-graphical-user-interface)
* [Installation](#-installation)
* [Requirements](#-requirements)
* [Running the Application](#-running-the-application)
* [Using the System](#-using-the-system)
* [Complete Workflow](#-complete-workflow)
* [Example Use Case](#-example-use-case)
* [Project Deployment](#-project-deployment)
* [Advantages](#-advantages)
* [Limitations](#-limitations)
* [Future Improvements](#-future-improvements)
* [Privacy and Security](#-privacy-and-security)
* [Contributing](#-contributing)
* [Author](#-author)
* [Demo](#-demo)
* [License](#-license)

---

# 🔎 Overview

Traditional CCTV systems primarily record video footage that must later be reviewed manually.

**SMART_CCTV** adds an intelligent computer-vision layer to the surveillance process.

Instead of simply recording camera footage, the application can:

* Capture faces from a camera.
* Create a face dataset for registered users.
* Train a face-recognition model.
* Recognize registered individuals in real time.
* Identify unknown individuals.
* Save images of unknown faces.
* Detect movement through camera-frame differences.
* Determine whether a visitor is entering or leaving.
* Record visitor events with date and time.
* Store visitor records in an Excel workbook.
* Provide a graphical interface for operating the system.

The main application is implemented as a Tkinter desktop GUI that provides access to recording, visitor records, identification, and in/out monitoring functionality.

---

# 🎯 Problem Statement

Conventional CCTV systems generally depend on continuous human monitoring or manual review of recorded footage.

This creates several problems:

* Security personnel need to monitor cameras continuously.
* Identifying a particular person from recorded footage is time-consuming.
* Visitor movement may not be logged automatically.
* Unknown individuals may go unnoticed.
* Entry and exit information may need to be maintained manually.
* Large amounts of CCTV footage are difficult to analyze manually.

The goal of SMART_CCTV is to automate several of these activities using **computer vision and face recognition**.

---

# 🚀 Project Objectives

The primary objectives of this project are:

1. Build an intelligent CCTV monitoring application.
2. Detect faces from a live camera feed.
3. Register known individuals using face samples.
4. Train a face-recognition model.
5. Recognize registered individuals automatically.
6. Detect unknown individuals.
7. Save unknown-face images for later inspection.
8. Detect visitor movement.
9. Determine entry and exit direction.
10. Maintain visitor records with timestamps.
11. Provide an easy-to-use desktop GUI.
12. Demonstrate a practical real-world smart-surveillance system.

---

# ✨ Key Features

## 👤 Face Registration

The system allows a new person to be registered by providing:

* A numeric ID
* A name
* Camera-based face samples

The registration process captures multiple images of the person's face and stores them in the training-image directory.

The implemented registration process captures up to approximately 60 face samples for a registered person.

---

## 🧠 Face Training

After collecting face samples, the system trains an **LBPH Face Recognizer** using OpenCV.

The trained model is saved as:

```text
TrainingImageLabel/Trainer.yml
```

This trained model is later loaded during real-time recognition.

---

## 🎥 Real-Time Face Recognition

The application accesses the camera using OpenCV and processes the video stream frame by frame.

For each detected face, the system:

1. Detects the face.
2. Extracts the face region.
3. Passes it to the trained LBPH recognizer.
4. Predicts the user's ID.
5. Matches the ID with the stored user information.
6. Displays the person's identity on the video feed.

The recognition implementation reads the trained `Trainer.yml` model and uses the `Bookface.csv` file to map recognized IDs to names.

---

# 🚨 Unknown Face Detection

If the recognition confidence does not meet the configured threshold, the system treats the face as:

```text
Unknown
```

Unknown faces can be saved automatically to:

```text
ImagesUnknown/
```

This provides a useful mechanism for reviewing individuals who are not registered in the system.

---

# 🚪 Visitor In/Out Detection

One of the key features of SMART_CCTV is movement-based visitor tracking.

The system uses consecutive camera frames and calculates their difference:

```text
Frame 1
   ↓
Frame 2
   ↓
Absolute Difference
   ↓
Blur
   ↓
Grayscale
   ↓
Threshold
   ↓
Contour Detection
   ↓
Movement Detection
```

The implementation uses OpenCV functions such as:

* `VideoCapture`
* `absdiff`
* `blur`
* `cvtColor`
* `threshold`
* `findContours`
* `boundingRect`

to identify movement in the camera view.

The detected movement position is then used to determine whether the person has moved into or out of the monitored area.

---

# 📊 Visitor Logging

When an entry or exit event is detected, the application records:

* Event type
* Date
* Time

Example:

```text
Visitors | Date       | Time
--------------------------------
In       | 18-08-2026 | 10:30:15
Out      | 18-08-2026 | 12:45:21
```

The current implementation stores these records in:

```text
Book1.xlsx
```

using the `openpyxl` library.

---

# 🛠️ Technology Stack

| Technology         | Purpose                                 |
| ------------------ | --------------------------------------- |
| **Python**         | Core programming language               |
| **OpenCV**         | Computer vision and camera processing   |
| **Tkinter**        | Desktop graphical user interface        |
| **Pillow (PIL)**   | Image processing and GUI image handling |
| **NumPy**          | Numerical and image-data processing     |
| **Pandas**         | Reading and processing tabular data     |
| **OpenPyXL**       | Excel file creation and visitor logging |
| **CSV**            | User ID/name storage                    |
| **Haar Cascade**   | Face detection                          |
| **LBPH**           | Face recognition                        |
| **XML Classifier** | Haar Cascade face-detection model       |
| **YAML Model**     | Trained LBPH model storage              |

The repository contains Python modules using Tkinter, OpenCV, Pillow, NumPy, Pandas, CSV, datetime, and OpenPyXL, along with Haar Cascade XML files and a trained/model-related file.

---

# 👁️ Computer Vision Techniques

SMART_CCTV combines multiple computer-vision techniques.

## 1. Haar Cascade Face Detection

The project uses:

```text
haarcascade_frontalface_default.xml
```

to detect faces from camera frames.

The Haar Cascade classifier detects potential face regions before the recognition stage.

---

## 2. LBPH Face Recognition

The system uses OpenCV's:

```python
cv2.face.LBPHFaceRecognizer_create()
```

LBPH stands for:

> **Local Binary Patterns Histograms**

The algorithm is trained using the collected face samples and generates a model that can later be used to recognize registered users.

---

## 3. Motion Detection

Visitor movement is detected using frame differencing.

Conceptually:

```text
Current Frame - Previous Frame
            ↓
       Motion Areas
            ↓
       Contour Detection
            ↓
      Movement Position
            ↓
       In / Out Event
```

The project compares consecutive webcam frames and analyzes the resulting contours to determine movement direction.

---

# 🏗️ System Architecture

The overall system can be represented as:

```text
                         ┌─────────────────────┐
                         │   Camera / Webcam   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   OpenCV Capture    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌──────────────────┐             ┌──────────────────┐
          │  Face Detection  │             │  Motion Detection│
          │  Haar Cascade    │             │ Frame Difference │
          └────────┬─────────┘             └────────┬─────────┘
                   │                                │
                   ▼                                ▼
          ┌──────────────────┐             ┌──────────────────┐
          │ Face Recognition │             │  In / Out Logic  │
          │      LBPH        │             └────────┬─────────┘
          └────────┬─────────┘                      │
                   │                                │
          ┌────────┴─────────┐                      ▼
          │                  │              ┌──────────────────┐
          ▼                  ▼              │ Visitor Records │
      Known User          Unknown           │    Book1.xlsx   │
          │                  │              └──────────────────┘
          │                  │
          ▼                  ▼
    Display Name       Save Unknown
                        Face Image
```

---

# 🧩 Application Modules

The project is divided into several Python modules.

## `main.py`

The main application entry point.

It creates the primary Tkinter interface titled:

```text
Smart CCTV Camera
```

The GUI provides buttons for:

* Record
* Visitors
* Identification
* In/Out
* Exit

The buttons call functionality from other modules.

---

## `FinalFinalTestface.py`

This is one of the main face-recognition modules.

It contains functionality for:

* Face sample collection
* Face dataset creation
* Model training
* Face recognition
* Unknown-face handling
* Tkinter interface for face-recognition operations

The module uses OpenCV's Haar Cascade and LBPH recognizer.

---

## `finaltestface.py`

This file is another face-processing module used by the application.

It provides supporting functionality for the face-recognition workflow and is imported by other parts of the project.

---

## `identify.py`

This module provides identification-related functionality used by the main GUI.

It is connected to the **Identification** button in `main.py`.

---

## `in_out.py`

This module handles visitor movement detection.

It:

1. Opens the webcam.
2. Captures frames.
3. Compares consecutive frames.
4. Detects motion.
5. Determines movement direction.
6. Saves an image of the event.
7. Records the event in Excel.

---

## `record.py`

This module is responsible for camera recording functionality and is connected to the **Record** option in the main GUI.

---

## `login.py`

This module contains login-related functionality and forms part of the application's supporting GUI functionality.

---

# 📁 Project Structure

The repository currently contains the following major files and directories:

```text
SMART_CCTV/
│
├── TrainingImageLabel/
│
├── icons/
│
├── TrainingImage/
│
├── Book1.xlsx
├── Bookface.csv
│
├── Confirmfacedetecter.py
├── Creating database testface.py
├── FinalFinalTestface.py
├── Testface.py
├── finaltestface.py
├── identify.py
├── in_out.py
├── login.py
├── main.py
├── openFile.py
├── record.py
├── test.py
├── test2.py
├── test3.py
│
├── haarcascade_eye.xml
├── haarcascade_frontalface_default.xml
│
├── keras_model.h5
├── labels.txt
│
└── README.md
```

> **Note:** Some files in the repository represent development/testing iterations of the computer-vision implementation. The primary user-facing application is launched through `main.py`.

---

# 👤 Face Registration

Before the system can recognize a person, that person needs to be registered.

The registration workflow is:

```text
Enter ID
   ↓
Enter Name
   ↓
Open Camera
   ↓
Detect Face
   ↓
Capture Face Samples
   ↓
Save Images
   ↓
Store ID + Name
```

The application stores face information in the training-image directory and records the ID/name mapping in:

```text
Bookface.csv
```

The face-registration implementation validates that the ID is numeric and the name is alphabetical before capturing samples.

---

# 🧠 Face Training

Once sufficient face samples have been collected, the system trains the recognition model.

The training process:

```text
Training Images
      ↓
Load Images
      ↓
Convert to Grayscale
      ↓
Extract IDs
      ↓
LBPH Face Recognizer
      ↓
Train Model
      ↓
Trainer.yml
```

The model is saved as:

```text
TrainingImageLabel/Trainer.yml
```

and can subsequently be loaded for recognition.

---

# 🔍 Face Recognition

During recognition, the system continuously reads camera frames.

For every frame:

```text
Camera Frame
     ↓
Face Detection
     ↓
Face Region
     ↓
LBPH Prediction
     ↓
ID + Confidence
     ↓
Bookface.csv
     ↓
Person Name
```

The recognition code loads the trained model and the CSV database containing IDs and names.

---

# 🚨 Unknown Person Workflow

When the recognition confidence is outside the configured recognition range, the system labels the person:

```text
Unknown
```

Unknown face images can then be saved for review.

```text
Unknown Face
      ↓
ImagesUnknown/
      ↓
Security Review
```

This provides an additional security layer for individuals who have not been registered in the system.

---

# 🚪 In/Out Detection Workflow

The visitor-monitoring module works independently from standard face recognition.

The process is:

```text
Camera
  ↓
Capture Frame 1
  ↓
Capture Frame 2
  ↓
Compare Frames
  ↓
Detect Difference
  ↓
Find Contours
  ↓
Calculate Bounding Box
  ↓
Determine Movement Direction
  ↓
IN / OUT
  ↓
Save Image
  ↓
Record Date + Time
```

The implementation uses camera-frame differences and contour coordinates to infer movement direction.

---

# 📊 Data Storage

The current project uses lightweight local storage rather than a centralized database.

## `Bookface.csv`

Stores registered face information.

Example:

```csv
Id,Name
1,John
2,Alice
3,David
```

The face-recognition system reads this file to associate recognized IDs with names.

---

## `Book1.xlsx`

Stores visitor movement information.

Example:

```text
Visitors | Date       | Time
--------------------------------
In       | 18-08-2026 | 09:10:25
Out      | 18-08-2026 | 11:45:32
```

The `in_out.py` module creates and updates this workbook using OpenPyXL.

---

## Face Dataset

Captured face samples are stored locally and used for training.

```text
TrainingImage/
```

Each registered user can have multiple captured face samples.

---

## Trained Model

The trained LBPH model is stored as:

```text
TrainingImageLabel/Trainer.yml
```

---

## Unknown Faces

Unknown detected faces can be stored under:

```text
ImagesUnknown/
```

---

# 🖥️ Graphical User Interface

The main application uses **Tkinter**.

The primary interface is titled:

```text
Smart CCTV Camera
```

and provides functionality including:

```text
┌─────────────────────────────────────┐
│         Smart CCTV Camera           │
│                                     │
│       [ Camera / Security ]         │
│                                     │
│   [ Record ]     [ Visitors ]       │
│                                     │
│          [ Identification ]         │
│                                     │
│            [ In / Out ]             │
│                                     │
│              [ Exit ]               │
└─────────────────────────────────────┘
```

The actual application creates dedicated buttons for recording, visitors, identification, and In/Out functionality.

---

# ⚙️ Requirements

Before installing the project, make sure your system has:

* Python 3.x
* Webcam / USB camera
* Windows/Linux/macOS-compatible Python environment
* pip
* Git

For the face-recognition functionality, the OpenCV installation must include the `cv2.face` module required by the LBPH recognizer.

---

# 📦 Python Dependencies

The project uses libraries including:

```text
opencv-python / OpenCV
Pillow
NumPy
Pandas
OpenPyXL
Tkinter
```

Depending on your Python/OpenCV environment, additional OpenCV-contrib functionality may be required for:

```python
cv2.face.LBPHFaceRecognizer_create()
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Deevyanshuvaidya/SMART_CCTV.git
```

---

## 2. Navigate to the Project

```bash
cd SMART_CCTV
```

---

## 3. Create a Virtual Environment

Recommended:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

Install the required Python packages:

```bash
pip install opencv-contrib-python pillow numpy pandas openpyxl
```

If you already have OpenCV installed, make sure the version you use provides:

```python
cv2.face
```

---

# ▶️ Running the Application

Start the main application:

```bash
python main.py
```

The Tkinter Smart CCTV interface should open.

The main GUI initializes the application window and connects the available operations to their respective Python modules.

---

# 🧪 Using the System

## Step 1 — Start the Application

Run:

```bash
python main.py
```

---

## Step 2 — Register a Person

Use the face-registration functionality.

Provide:

```text
ID
Name
```

The camera will capture multiple face samples.

---

## Step 3 — Train the Model

Run the training operation after collecting face samples.

The system creates:

```text
Trainer.yml
```

---

## Step 4 — Start Identification

Use the:

```text
Identification
```

option.

The camera will detect faces and attempt to identify registered individuals.

---

## Step 5 — Monitor Unknown Individuals

If an individual cannot be identified, the system displays:

```text
Unknown
```

and can save the detected face image.

---

## Step 6 — Monitor Visitor Movement

Use:

```text
In / Out
```

to start movement detection.

The system detects movement through camera-frame differences and records the resulting event.

---

## Step 7 — View Visitor Records

The:

```text
Visitors
```

option provides access to the stored visitor information.

---

# 🔄 Complete System Workflow

The complete workflow can be summarized as:

```text
                 SMART CCTV
                     │
                     ▼
              Camera / Webcam
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Face Recognition       Motion Detection
          │                     │
          ▼                     ▼
   Haar Face Detection     Frame Difference
          │                     │
          ▼                     ▼
      LBPH Model          Movement Analysis
          │                     │
     ┌────┴────┐          ┌─────┴─────┐
     │         │          │           │
     ▼         ▼          ▼           ▼
   Known     Unknown      IN          OUT
     │         │          │           │
     ▼         ▼          └─────┬─────┘
   Display   Save Image         │
   Identity                    ▼
                         Excel Record
```

---

# 🏫 Project Deployment

SMART_CCTV was not developed only as a theoretical prototype.

The project was **worked on and deployed in a college hostel environment**, where it was demonstrated as a practical smart-surveillance application. The original repository README also links to a LinkedIn post documenting the deployment/demo.

### Deployment concept

```text
College Hostel
      │
      ▼
 CCTV / Camera
      │
      ▼
 SMART_CCTV
      │
 ┌────┼───────────┐
 ▼    ▼           ▼
Face  Motion    Visitor
ID    Detection  Logs
 │      │          │
 ▼      ▼          ▼
Known  In/Out    Excel
/Unknown
```

---

# 💡 Practical Use Cases

The system can be adapted for environments such as:

### 🏫 Educational Institutions

* College hostels
* Laboratories
* Computer labs
* Restricted areas

### 🏢 Offices

* Employee identification
* Restricted-area monitoring
* Visitor tracking

### 🏠 Residential Buildings

* Entrance monitoring
* Visitor logging
* Unknown-person detection

### 🏭 Industrial Environments

* Restricted-area monitoring
* Employee access monitoring
* Security surveillance

### 🏨 Hostels

* Entry/exit monitoring
* Visitor management
* Security assistance

---

# ✅ Advantages

## Automation

Reduces the need for completely manual CCTV monitoring.

## Real-Time Processing

Face detection and recognition operate directly on camera frames.

## Face-Based Identification

Registered individuals can be identified automatically.

## Unknown Person Detection

Unknown faces can be recorded for later inspection.

## Visitor Tracking

Movement-based entry and exit events can be recorded automatically.

## Local Storage

The current system can operate using local files without requiring a remote server or cloud service.

## Desktop Application

Tkinter provides a simple graphical interface for interacting with the system.

---

# ⚠️ Limitations

The current version is a practical prototype and has several limitations.

## 1. Local Camera Dependency

The current implementation primarily accesses the local camera through:

```python
cv2.VideoCapture(0)
```

so it is designed around a directly accessible camera.

---

## 2. Local File Storage

Data is stored using:

```text
CSV
Excel
Local Images
YAML Model
```

rather than a centralized production database.

---

## 3. LBPH Recognition

LBPH is lightweight and useful for local applications, but modern deep-learning face-recognition systems can provide stronger robustness under challenging conditions.

---

## 4. Lighting Conditions

Face recognition performance may be affected by:

* Poor lighting
* Strong backlighting
* Significant facial angles
* Occlusion
* Camera quality

---

## 5. Dataset Quality

Recognition quality depends heavily on the quality and diversity of the training images.

---

## 6. Single-Camera Architecture

The current implementation is primarily designed around a local camera rather than a distributed multi-camera surveillance network.

---

# 🔮 Future Improvements

SMART_CCTV can be significantly expanded into a production-grade surveillance platform.

## 🤖 Advanced AI

Replace or complement LBPH with modern deep-learning models such as:

* FaceNet
* ArcFace
* DeepFace
* InsightFace
* YOLO-based detection pipelines

---

## 📹 Multiple CCTV Cameras

Add support for:

```text
Camera 1
Camera 2
Camera 3
Camera 4
...
```

using RTSP/IP camera streams.

---

## 🌐 Web Dashboard

Build a web dashboard using:

```text
React / Next.js
+
Node.js / Python Backend
+
Database
```

to monitor cameras remotely.

---

## 🗄️ Database Integration

Replace CSV/Excel storage with:

```text
PostgreSQL
MySQL
MongoDB
SQLite
```

for more reliable data management.

---

## 🔔 Real-Time Alerts

Add notifications through:

* Email
* SMS
* Telegram
* WhatsApp
* Mobile push notifications

for important security events.

---

## 🚨 Intelligent Event Detection

The system could detect:

* Unauthorized access
* Loitering
* Intrusion
* Crowd formation
* Violence
* Fire/smoke
* Abandoned objects
* Restricted-area entry

---

## ☁️ Cloud Integration

A future version could synchronize:

```text
Cameras
   ↓
AI Processing
   ↓
Cloud Server
   ↓
Database
   ↓
Web Dashboard
   ↓
Mobile Application
```

---

## 📱 Mobile Application

A mobile application could allow security personnel to:

* View live cameras
* Receive alerts
* Review unknown faces
* Check visitor logs
* Search historical events

---

# 🔐 Privacy and Security

Face recognition involves sensitive biometric information.

A production deployment should therefore implement appropriate privacy and security controls.

Recommended improvements include:

* Encrypt stored biometric data.
* Restrict access to face datasets.
* Use authenticated users for administrative functions.
* Avoid storing unnecessary biometric information.
* Define data-retention policies.
* Secure CCTV camera access.
* Protect stored visitor records.
* Log administrative actions.
* Follow applicable privacy and data-protection requirements.

This repository is primarily a technical project/demo and should not be treated as a production-ready biometric-security platform without additional security, privacy, testing, and compliance work.

---

# 🧪 Testing Recommendations

For a production-quality version, the following tests should be added.

### Face Detection

Test:

* Single face
* Multiple faces
* Different lighting
* Different distances
* Partial occlusion

### Face Recognition

Test:

* Registered person
* Unknown person
* Multiple registered people
* Similar-looking people
* Different camera angles

### Motion Detection

Test:

* Person entering
* Person leaving
* Multiple movements
* Camera noise
* Lighting changes

### Data Storage

Test:

* CSV creation
* Excel logging
* Duplicate users
* Invalid user data
* Missing files

---

# 📈 Performance Considerations

The current system processes camera frames locally, which makes it suitable for smaller deployments and prototype environments.

Performance can be improved by:

* Reducing camera resolution.
* Processing every second/third frame.
* Optimizing face-detection parameters.
* Using GPU acceleration.
* Moving AI inference to a dedicated service.
* Using optimized deep-learning models.
* Separating camera capture from AI inference.

---

# 🧱 Recommended Production Architecture

A more scalable future architecture could look like:

```text
                    CCTV Cameras
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Camera 1    Camera 2    Camera 3
             │           │           │
             └───────────┼───────────┘
                         ▼
                  Video Processing
                         │
                         ▼
                  AI / CV Engine
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
         Face Match   Motion     Events
              │       Detection      │
              └──────────┼──────────┘
                         ▼
                     Backend API
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Database     Alerts     Storage
             │
             ▼
       Web/Mobile Dashboard
```

This would allow SMART_CCTV to evolve from a local desktop application into a distributed intelligent surveillance platform.

---

# 📚 What This Project Demonstrates

This project demonstrates practical experience with:

```text
Python Development
        │
        ├── OpenCV
        ├── Computer Vision
        ├── Face Detection
        ├── Face Recognition
        ├── Motion Detection
        ├── Image Processing
        │
        ├── Tkinter GUI
        ├── CSV Data Handling
        ├── Excel Automation
        ├── Machine Learning Model Usage
        └── Real-Time Camera Processing
```

It also demonstrates how multiple independent technologies can be integrated into one practical application.

---

# 🏆 Project Highlights

### Intelligent Surveillance

Transforms a traditional camera into a computer-vision-assisted monitoring system.

### Face Recognition

Uses Haar Cascade detection with LBPH recognition.

### Visitor Monitoring

Tracks movement and records entry/exit events.

### Unknown Detection

Captures unknown faces for further inspection.

### Data Logging

Maintains visitor information using CSV and Excel files.

### Desktop GUI

Provides an accessible Tkinter-based user interface.

### Real-World Deployment

The system was demonstrated in a college-hostel environment rather than remaining only as a theoretical project.

---

# 🎥 Demo & Real-World Deployment

## 🏫 Successfully Deployed in Our College Hostel

SMART_CCTV was successfully **deployed and tested in our college hostel environment** during our college period.

The system was not limited to a development or demonstration setup — it was **actually installed and used for real-time hostel surveillance**, where it performed reliably during our deployment period.

The system was used for:

* 🎥 Real-time CCTV monitoring
* 👤 Face detection and identification
* 🚨 Unknown-person detection
* 🚪 Visitor In/Out monitoring
* 📊 Automated visitor record management
* 🖼️ Capturing relevant visitor/unknown-person images

The deployment gave us practical experience in taking a computer-vision project from development to a **real-world working environment**.

> **Deployment Status:** ✅ Successfully deployed and working successfully during our college hostel deployment period.

---

## 🎬 Project Demo

The project was also demonstrated through a LinkedIn post showcasing the SMART_CCTV system and its real-world implementation.

**Demo & Deployment:**
[View SMART_CCTV Demo on LinkedIn](https://www.linkedin.com/posts/deevanshu-vaidya-598320253_smarttechnology-realtimedata-automation-ugcPost-7100302609978200064-ROHF/?utm_source=chatgpt.com)

---

## 🌟 Real-World Impact

Deploying SMART_CCTV in our college hostel helped us validate the system beyond a local development environment.

The project demonstrated how computer vision, face recognition, and automated visitor tracking can be combined to create a practical security-monitoring solution.

This real-world deployment also helped us understand challenges associated with:

* Camera positioning
* Real-time video processing
* Face-recognition accuracy
* Lighting conditions
* Visitor movement detection
* Continuous application operation
* Local data management

The experience provided valuable practical exposure to **deploying and maintaining a computer-vision-based application in an actual environment**.


---

# 🤝 Contributing

Contributions and improvements are welcome.

## 1. Fork the Repository

```bash
git clone https://github.com/Deevyanshuvaidya/SMART_CCTV.git
```

## 2. Create a Feature Branch

```bash
git checkout -b feature/new-feature
```

## 3. Make Your Changes

Implement your improvement and test it locally.

## 4. Commit

```bash
git add .
git commit -m "Add new feature"
```

## 5. Push

```bash
git push origin feature/new-feature
```

## 6. Create a Pull Request

Explain:

* What you changed
* Why you changed it
* How you tested it

---

# 👨‍💻 Author

## Deevyanshu Vaidya

GitHub:

https://github.com/Deevyanshuvaidya

Project:

https://github.com/Deevyanshuvaidya/SMART_CCTV

---

# ⭐ Project Summary

**SMART_CCTV** is a Python-based intelligent surveillance system that combines computer vision, face recognition, motion detection, and local data logging to provide a smarter alternative to conventional CCTV monitoring.

### Core Technologies

```text
Python
OpenCV
Tkinter
Pillow
NumPy
Pandas
OpenPyXL
Haar Cascade
LBPH Face Recognition
CSV
Excel
```

### Core Features

```text
✓ Face Registration
✓ Face Dataset Creation
✓ Face Training
✓ Real-Time Face Recognition
✓ Unknown Face Detection
✓ Motion Detection
✓ Visitor In/Out Detection
✓ Visitor Logging
✓ Image Capture
✓ Desktop GUI
✓ Local Data Storage
✓ Practical Hostel Deployment
```

The project demonstrates how **computer vision and automation can be combined with a conventional CCTV camera to create an intelligent, practical, and extensible surveillance system.**

---

# 📄 License

⚖️ Copyright & Usage

© 2026 Deevyanshu Vaidya. All Rights Reserved.

This project and its source code are provided for educational, demonstration, and portfolio purposes.

The source code, documentation, design, and original implementation are the intellectual property of the author unless otherwise stated.

Unauthorized:

Copying or reproducing the source code
Redistributing the project or substantial portions of it
Publishing modified or unmodified versions as your own work
Using the project commercially without permission
Removing or modifying copyright and attribution notices

may result in copyright or other intellectual-property issues where applicable.

If you wish to reuse, redistribute, modify, or use substantial portions of this project for another purpose, please contact the author and obtain appropriate permission first.

Third-Party Components

This project may use third-party libraries, frameworks, datasets, models, icons, images, or other components that are subject to their respective licenses and copyrights.

Users are responsible for complying with the applicable licenses and terms of those third-party components
