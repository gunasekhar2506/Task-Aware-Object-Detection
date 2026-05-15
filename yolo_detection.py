from ultralytics import YOLO
# LOAD MODEL
model = YOLO("yolov8n.pt")
def detect_objects(
    image_path,
    confidence_threshold=0.4
):
    results = model(image_path)
    detections = []
    names = results[0].names
    # EXTRACT ALL INFO
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        class_name = names[cls_id]
        confidence = float(box.conf[0])
        # IGNORE LOW CONFIDENCE DETECTIONS
        if confidence < confidence_threshold:
            continue
        # BOUNDING BOX COORDINATES
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        detections.append({
            "class": class_name,
            "confidence": confidence,
            "box": [
                int(x1),
                int(y1),
                int(x2),
                int(y2)
            ]
        })
    return detections