# Task-Aware Object Detection System

This project performs:

- YOLO object detection
- Global context inference
- Task-aware affordance reasoning
- Property-based object scoring
- Context-aware object selection

---

# Features

- Automatic context detection
- Affordance reasoning
- Symbolic task-object scoring
- Bounding-box visualization
- COCO-compatible reasoning pipeline

---

# Project Structure

```text
HA/
│
├── main_pipeline.py
├── filtering_logic.py
├── yolo_detection.py
├── task_dictionary.py
├── context_rules.py
├── object_properties.py
├── requirements.txt
└── README.md
```

---

# Installation

Install required packages:

```bash
pip install -r requirements.txt
```

---

# Run

```bash
python main_pipeline.py
```

---

# Example Tasks

- step_on_something
- sit_comfortably
- place_flowers
- get_potatoes_out_of_fire
- water_plant
- get_lemon_out_of_tea
- dig_hole
- open_bottle_of_beer
- open_parcel
- serve_wine
- pour_sugar
- smear_butter
- extinguish_fire
- pound_carpet

---

# Pipeline

YOLO Detection
↓
Global Context Inference
↓
Task-Aware Affordance Reasoning
↓
Best Object Selection

---

# Dataset

COCO val2017 dataset used for testing.

---

# Model

YOLOv8n from Ultralytics.
