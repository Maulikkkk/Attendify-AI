# 🚀 Attendify AI – Smart Attendance System

Attendify AI is an end-to-end **AI-powered attendance system** that automates classroom attendance using **Face Recognition and Voice Biometrics**.

It eliminates manual roll calls and replaces them with fast, accurate, and scalable AI-based identification.

---


## 🌐 Live Demo

👉 **Try the App (Recommended)**
https://attendifyai.streamlit.app/

👉 Landing Page (Overview)
https://attendifyai-landing-page.vercel.app/

⚡ No signup required. Try face/voice attendance instantly.


---

## 🎯 Problem

Traditional attendance systems are:

* Time-consuming (manual roll calls)
* Error-prone (proxy attendance)
* Not scalable for large classrooms

---

## 💡 Solution

Attendify AI automates attendance using:

* 📸 **Face Recognition** → mark entire class from a single image
* 🎙️ **Voice Identification** → verify students via voice biometrics
* 📱 **QR Enrollment** → instant onboarding without manual entry

---

## ✨ Key Features

* One-click attendance using class image
* Voice-based roll call verification
* Student enrollment via QR codes
* Real-time attendance tracking
* Historical data + CSV export
* Secure biometric storage

---

## 🧠 How It Works

### 1. Enrollment

* Students join via QR code or link
* Register face + voice once

### 2. Attendance Modes

* **Face Mode:** Upload class image → AI detects & matches faces
* **Voice Mode:** Students speak → embeddings matched in real-time

### 3. Data Storage

* Attendance records stored securely in database
* Accessible via dashboard

---

## 🏗️ System Architecture

```id="arch01"
Frontend (Landing Page)
        ↓
Flask Backend (Routing Layer)
        ↓
Streamlit App (Core UI + Interaction)
        ↓
ML Models
   ├── Face Recognition (dlib / face_recognition)
   └── Voice Embeddings (Resemblyzer / Librosa)
        ↓
Database (Supabase / PostgreSQL)
```

---

## 🛠️ Tech Stack

### 👨‍💻 Backend & App

* Python
* Flask
* Streamlit

### 🤖 Machine Learning

* face_recognition (dlib)
* Resemblyzer
* Librosa
* NumPy, Pandas

### 🗄️ Database

* Supabase (PostgreSQL)

### 🌐 Frontend

* HTML, CSS, JavaScript

---

## 📂 Project Structure

```
.
├── app.py                      # Main entry point (Streamlit app)
├── requirements.txt           # Dependencies
├── .gitignore
├── .python-version

├── src/
│   ├── components/            # Reusable UI components (dialogs, cards, etc.)
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── header.py
│   │   ├── footer.py
│   │   └── subject_card.py
│
│   ├── screens/               # Page-level views
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│
│   ├── pipelines/             # ML pipelines
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│
│   ├── database/              # DB config & queries
│   │   ├── db.py
│   │   └── config.py
│
│   └── ui/                    # Layout and base UI structure
│       └── base_layout.py
```


---

### 🧩 Architecture Breakdown

* **Components Layer** → reusable UI elements (dialogs, cards)
* **Screens Layer** → user-facing pages (student / teacher views)
* **Pipelines Layer** → ML logic (face + voice processing)
* **Database Layer** → data handling and persistence
* **UI Layer** → layout and styling structure

This separation ensures:

* modular code
* easier scaling
* clean ML + UI integration

---
## ⚙️ Installation

```bash id="install01"
git clone https://github.com/Maulikkkk/Attendify-AI.git
cd Attendify-AI

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash id="run01"
streamlit run app.py
```

or (if Flask entry point):

```bash id="run02"
python app.py
```

---

## 📊 Results & Performance

* ⚡ Attendance marking: ~2–5 seconds
* 🎯 Face recognition accuracy: High (depends on dataset quality)
* 🎙️ Voice matching: Real-time embedding comparison

---

## 🔐 Security Considerations

* Biometric data stored securely
* Authentication layer via backend
* No raw data exposure in frontend

---

## 🧩 Related Repository

👉 Landing Page:
https://github.com/Maulikkkk/Attendify-AI_LandingPage

---

## 🚧 Future Improvements

* Mobile app integration
* Real-time camera streaming
* Multi-classroom scaling
* Improved model accuracy with custom training
* Admin analytics dashboard

---

## 📬 Author

**Maulik Gupta**
B.Tech CSE (AI)


---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
