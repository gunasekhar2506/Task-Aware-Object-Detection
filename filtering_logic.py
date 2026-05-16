from task_dictionary import tasks
from object_properties import object_properties
from context_rules import context_rules


# GLOBAL CONTEXT INFERENCE


def infer_context(detected_objects):

    # EXTRACT DETECTED CLASS NAMES
   

    detected_classes = [

        obj["class"]

        for obj in detected_objects
    ]

    # =================================================
    # STORE CONTEXT SCORES
    # =================================================

    context_scores = {}

    # =================================================
    # CHECK EACH CONTEXT
    # =================================================

    for context_name, context_data in context_rules.items():

        score = 0

        strong_matches = 0

        medium_matches = 0

        # =============================================
        # STRONG EVIDENCE
        # =============================================

        strong_objects = context_data["strong"]

        for item in strong_objects:

            if item in detected_classes:

                strong_matches += 1

                score += 5

        # =============================================
        # MEDIUM EVIDENCE
        # =============================================

        medium_objects = context_data["medium"]

        for item in medium_objects:

            if item in detected_classes:

                medium_matches += 1

                score += 1

        # =============================================
        # CONTEXT VALIDATION
        # =============================================

        # weak-only contexts are unreliable

        if strong_matches == 0 and medium_matches < 2:

            score = 0

        # =============================================
        # BONUS FOR MULTIPLE STRONG OBJECTS
        # =============================================

        if strong_matches >= 2:

            score += 3

        # =============================================
        # SAVE SCORE
        # =============================================

        context_scores[context_name] = score

    # =================================================
    # NO CONTEXTS
    # =================================================

    if len(context_scores) == 0:

        return None

    # =================================================
    # BEST CONTEXT
    # =================================================

    best_context = max(

        context_scores,

        key=context_scores.get
    )

    best_score = context_scores[best_context]

    # =================================================
    # UNKNOWN CONTEXT HANDLING
    # =================================================

    if best_score < 5:

        return None

    return best_context


# =====================================================
# MAIN FILTERING FUNCTION
# =====================================================

def filter_objects(

    selected_task,
    detected_objects

):

    # =================================================
    # LOAD TASK DATA
    # =================================================

    task_data = tasks[selected_task]

    base_scores = task_data["scores"]

    context_modifiers = task_data["context_modifiers"]

    property_modifiers = task_data["property_modifiers"]

    # =================================================
    # AUTOMATIC CONTEXT INFERENCE
    # =================================================

    selected_context = infer_context(

        detected_objects
    )

    print(

        "\nInferred Context : ",
        selected_context
    )

    # =================================================
    # STORE FINAL OBJECTS
    # =================================================

    final_objects = []

    # =================================================
    # PROCESS EACH DETECTED OBJECT
    # =================================================

    for obj in detected_objects:

        class_name = obj["class"]

        # =============================================
        # IGNORE IRRELEVANT OBJECTS
        # =============================================

        if class_name not in base_scores:

            continue

        # =============================================
        # START WITH BASE SCORE
        # =============================================

        final_score = base_scores[class_name]

        # =============================================
        # APPLY CONTEXT MODIFIERS
        # =============================================

        if selected_context is not None:

            if selected_context in context_modifiers:

                context_data = context_modifiers[selected_context]

                if class_name in context_data:

                    final_score += context_data[class_name]

        # =============================================
        # APPLY PROPERTY MODIFIERS
        # =============================================

        if class_name in object_properties:

            properties = object_properties[class_name]

            for prop in properties:

                if prop in property_modifiers:

                    final_score += property_modifiers[prop]

        # =============================================
        # CONFIDENCE BONUS
        # =============================================

        confidence_bonus = obj["confidence"] * 2

        final_score += confidence_bonus

        # =============================================
        # SAVE FINAL SCORE
        # =============================================

        obj["final_score"] = round(

            final_score,
            2
        )

        # =============================================
        # SAVE OBJECT
        # =============================================

        final_objects.append(obj)

    # =================================================
    # NO OBJECTS
    # =================================================

    if len(final_objects) == 0:

        return None

    # =================================================
    # SORT OBJECTS
    # =================================================

    final_objects.sort(

        key=lambda x: x["final_score"],

        reverse=True
    )

    # =================================================
    # PRINT SCORES
    # =================================================

    print("\nObject Scores:\n")

    for item in final_objects:

        print(

            item["class"],
            " ---> ",
            item["final_score"]
        )

    # =================================================
    # RETURN BEST OBJECT
    # =================================================

    return final_objects[0]
