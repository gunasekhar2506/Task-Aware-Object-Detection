from yolo_detection import detect_objects
from filtering_logic import filter_objects

import cv2


# =====================================================
# IMAGE PATH
# =====================================================

image_path = "val2017/000000007574.jpg"


# =====================================================
# USER INPUT : TASK
# =====================================================

selected_task = input(

    "Enter Task Name : "

)


# =====================================================
# RUN YOLO OBJECT DETECTION
# =====================================================

detected_objects = detect_objects(image_path)


# =====================================================
# PRINT DETECTED OBJECTS
# =====================================================

print("\nDetected Objects:\n")

for obj in detected_objects:

    print(obj)


# =====================================================
# RUN TASK-AWARE AFFORDANCE REASONING
# =====================================================

best_object = filter_objects(

    selected_task,
    detected_objects

)


# =====================================================
# LOAD IMAGE
# =====================================================

image = cv2.imread(image_path)


# =====================================================
# IF BEST OBJECT FOUND
# =====================================================

if best_object is not None:

    class_name = best_object["class"]

    confidence = best_object["confidence"]

    final_score = best_object["final_score"]

    x1, y1, x2, y2 = best_object["box"]

    # =================================================
    # DRAW BEST OBJECT BOUNDING BOX
    # =================================================

    cv2.rectangle(

        image,

        (x1, y1),

        (x2, y2),

        (0, 255, 0),

        3
    )

    # =================================================
    # LABEL
    # =================================================

    label = (

        f"{class_name} | "
        f"Score: {final_score}"

    )

    cv2.putText(

        image,

        label,

        (x1, y1 - 10),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.7,

        (0, 255, 0),

        2
    )

    # =================================================
    # PRINT FINAL RESULT
    # =================================================

    print("\nBEST OBJECT SELECTED:\n")

    print(best_object)

else:

    print("\nNo suitable object found.")


# =====================================================
# SHOW FINAL OUTPUT IMAGE
# =====================================================

cv2.imshow(

    "Task-Aware Object Selection",

    image
)

cv2.waitKey(0)

cv2.destroyAllWindows()