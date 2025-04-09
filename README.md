# Advance Modulation Techniques GUI

This is a Python-based GUI application developed using **Tkinter**, **Matplotlib**, and **NumPy**, designed to demonstrate various **digital modulation techniques** such as:
- Amplitude Shift Keying (ASK)
- Frequency Shift Keying (FSK)
- Phase Shift Keying (PSK)

The GUI visually simulates these modulation techniques in real-time and plots the corresponding signals.

---

## 📋 Features

- Digital Signal Generation (random binary sequence)
- Carrier Signal Generation (user-defined amplitude and frequency)
- ASK, FSK, and PSK Modulation
- Interactive Matplotlib plots embedded in Tkinter
- Clear Button to reset the figure area

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (GUI)
- Matplotlib (plotting)
- NumPy (signal processing)
- SciPy (used but not fully utilized in current version)

---

## 🖼 GUI Layout

- **Main Tab**: *Advance Modulation Techniques*
  - **Left Side Panels**:
    - Digital Signal Generator
    - Carrier Signal Generator (Inputs: Amplitude, Frequency)
    - ASK, FSK, PSK Buttons
    - Clear Button
  - **Right Side Panel**:
    - 5 subplots to visualize each signal
    - Interactive Matplotlib toolbar

---

## 🚀 How to Run

1. Install the required Python libraries if not already installed:
   ```bash
   pip install matplotlib numpy scipy
   ```
2. Run the Python file:
   ```bash
   python modulation_gui.py
   ```
3. Steps to use the GUI:
  -Click Plot under Digital Signal Generator
  - Enter Amplitude and Frequency values under Carrier Generator and click Plot
  - Click respective Plot buttons for ASK, FSK, and PSK to visualize them
  - Use the Clear button to reset all plots
  
