from yolo_detection import detect_objects
from filtering_logic import filter_objects, infer_context

import cv2

# USER INPUT : IMAGE PATH

image_path = input(

    "Enter Image Path : "

)

# USER INPUT : TASK

selected_task = input(

    "Enter Task : "

)

# RUN YOLO OBJECT DETECTION

detected_objects = detect_objects(

    image_path
)

# PRINT DETECTED OBJECTS

print("\nDetected Objects:\n")

for obj in detected_objects:

    print(obj)

# GLOBAL CONTEXT INFERENCE

inferred_context = infer_context(

    detected_objects
)

print(

    "\nInferred Context : ",
    inferred_context
)

# TASK-AWARE FILTERING

best_object = filter_objects(

    selected_task,
    detected_objects
)

# LOAD IMAGE

image = cv2.imread(image_path)

# IF OBJECT FOUND

if best_object is not None:

    x1, y1, x2, y2 = best_object["box"]

    # DRAW BOUNDING BOX
    
    cv2.rectangle(

        image,

        (x1, y1),

        (x2, y2),

        (0, 255, 0),

        3
    )

    print("\nBest Object Found\n")

    print(best_object)

else:

    print(

        "\nNo suitable object found for this task."
    )

# SHOW OUTPUT IMAGE

cv2.imshow(

    "Task-Aware Object Detection",

    image
)

cv2.waitKey(0)

cv2.destroyAllWindows()
