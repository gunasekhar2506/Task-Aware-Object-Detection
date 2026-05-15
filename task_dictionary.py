tasks= {
"step_on_something": {
    "required_affordance":
    "stable elevated support for standing and increasing reach",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "bench": 10,
        "dining table": 9,
        "chair": 8,
        # GOOD BUT CONDITIONAL
        "bed": 6,
        "couch": 5,
        # CONTEXT-DEPENDENT
        "surfboard": 4,
        "boat": 4,
        "snowboard": 3,
        "skateboard": 3,
        "suitcase": 2,
        # VERY WEAK OPTIONS
        "backpack": 1,
        "skis": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================

    "context_modifiers": {
        "beach": {
            "surfboard": 5,
            "boat": 3,
            "chair": -2,
            "dining table": -3
        },
        "living_room": {
            "chair": 3,
            "couch": 2,
            "bench": 2,
            "surfboard": -4
        },
        "garage": {
            "bench": 3,
            "chair": 1,
            "skateboard": -2
        },
        "snow": {
            "snowboard": 4,
            "skis": 2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "large_flat_surface": 3,
        "rigid_surface": 2,
        "stable_base": 3,
        "high_elevation": 2,
        "soft_surface": -3,
        "unstable_surface": -4,
        "rolling_object": -5,
        "fragile_surface": -3
    }
},
"sit_comfortably": {  
    "required_affordance":
    "comfortable stable support for seated or resting posture",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "couch": 10,
        "bed": 9,
        "chair": 8,
        # GOOD BUT LESS COMFORTABLE
        "bench": 6,
        "toilet": 4,
        # CONDITIONAL / TEMPORARY
        "car": 3,
        "bus": 3,
        "boat": 2,
        "truck": 1,
        "suitcase": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "office": {
            "chair": 5,
            "couch": -2,
            "bed": -5
        },
        "bedroom": {
            "bed": 5,
            "couch": 2,
            "chair": -1
        },
        "park": {
            "bench": 5,
            "chair": -2
        },
        "beach": {
            "boat": 2,
            "chair": -1
        },
        "public_transport": {
            "bus": 4,
            "bench": 1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "soft_surface": 4,
        "back_support": 3,
        "wide_surface": 2,
        "ergonomic_design": 3,
        "hard_surface": -2,
        "unstable_surface": -4,
        "narrow_surface": -3,
        "dirty_surface": -3,
        "socially_inappropriate": -4
    }
},
"place_flowers": {
    "required_affordance":
    "stable aesthetically suitable containment for holding flowers upright",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "vase": 10,
        "bottle": 8,
        "potted plant": 7,
        # GOOD ALTERNATIVES
        "cup": 6,
        "bowl": 4,
        # CONTEXTUAL SUPPORT SURFACES
        "dining table": 2,
        "bench": 1,
        "chair": 1,
        "sink": 1
    },


    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "dining_room": {
            "vase": 5,
            "bottle": 2,
            "cup": -2
        },
        "garden": {
            "potted plant": 4,
            "bench": 2,
            "vase": -1
        },
        "kitchen": {
            "cup": 2,
            "bottle": 2,
            "sink": 1
        },
        "event": {
            "vase": 6,
            "cup": -4,
            "bowl": -2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "tall_container": 4,
        "stable_base": 3,
        "decorative_object": 4,
        "narrow_opening": 2,
        "wide_opening": 1,
        "unstable_container": -4,
        "shallow_container": -2,
        "poor_aesthetic_match": -3,
        "socially_inappropriate": -5
    }
},
"get_potatoes_out_of_fire": { 
    "required_affordance":
    "safe retrieval and handling of hot objects from dangerous heat source",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "spoon": 10,
        "fork": 9,
        "knife": 7,
        # SUPPORT OBJECTS
        "bowl": 5,
        "cup": 4,
        # CONTEXTUAL ENVIRONMENT OBJECTS
        "oven": 3,
        "microwave": 2,
        "sink": 2,
        "refrigerator": 1,
        # VERY WEAK / IMPROVISED
        "bottle": 1,
        "book": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "kitchen": {
            "spoon": 3,
            "fork": 2,
            "bowl": 2,
            "oven": 2
        },
        "campfire": {
            "fork": 4,
            "knife": 3,
            "cup": -2
        },
        "restaurant": {
            "spoon": 4,
            "fork": 3,
            "knife": 1
        },
        "emergency": {
            "knife": 2,
            "bottle": -2,
            "book": -5
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "long_reach": 3,
        "heat_resistant": 4,
        "scooping_surface": 3,
        "piercing_capability": 2,
        "stable_grip": 2,
        "heat_conductive": -2,
        "flammable_material": -5,
        "soft_object": -4,
        "poor_grip": -3
    }
},
"water_plant": {
    "required_affordance":
    "portable controlled transfer of water to plant",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "bottle": 10,
        "cup": 8,
        "bowl": 6,
        # GOOD BUT CONDITIONAL
        "vase": 5,
        "wine glass": 4,
        # CONTEXTUAL OBJECTS
        "sink": 3,
        "potted plant": 2,
        "refrigerator": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "garden": {
            "bottle": 4,
            "bowl": 2,
            "wine glass": -3
        },
        "kitchen": {
            "cup": 3,
            "sink": 4,
            "bowl": 2
        },
        "office": {
            "cup": 4,
            "bottle": 2,
            "bowl": -2
        },
        "outdoor": {
            "bottle": 3,
            "cup": -1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "large_liquid_capacity": 3,
        "controlled_pouring": 4,
        "portable_object": 3,
        "easy_grip": 2,
        "narrow_opening": 2,
        "fragile_object": -3,
        "spill_prone_shape": -4,
        "poor_grip": -2,
        "absorbent_material": -5
    }
},
"get_lemon_out_of_tea": {
    "required_affordance":
    "precise retrieval of small object from liquid container",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "spoon": 10,
        "fork": 8,
        "knife": 6,
        # INDIRECT / SUPPORT OBJECTS
        "cup": 5,
        "bowl": 4,
        # CONTEXTUAL OBJECTS
        "wine glass": 3,
        "dining table": 1,
        "bottle": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "restaurant": {
            "spoon": 4,
            "fork": 3,
            "knife": -1
        },
        "home": {
            "knife": 2,
            "cup": 2
        },
        "event": {
            "wine glass": 3,
            "spoon": 2
        },
        "outdoor": {
            "fork": 2,
            "knife": 1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "scooping_surface": 4,
        "precision_control": 3,
        "thin_insertion_profile": 2,
        "liquid_safe_material": 2,
        "easy_grip": 2,
        "large_bulky_object": -4,
        "spill_prone_shape": -3,
        "poor_precision": -3,
        "absorbent_material": -5
    }
},
"dig_hole": {
    "required_affordance":
    "penetration and displacement of ground material",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "knife": 10,
        "spoon": 8,
        "fork": 7,
        # CONDITIONAL / IMPROVISED
        "baseball bat": 5,
        "tennis racket": 3,
        "skateboard": 3,
        "surfboard": 2,
        # CONTEXTUAL OBJECTS
        "bottle": 1,
        "boat": 1,
        "bench": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "beach": {
            "surfboard": 4,
            "bottle": 2,
            "knife": -1
        },
        "garden": {
            "spoon": 3,
            "fork": 3,
            "knife": 2
        },
        "camping": {
            "knife": 4,
            "baseball bat": 2
        },
        "snow": {
            "snowboard": 4,
            "skis": 2,
            "spoon": -1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "sharp_edge": 4,
        "rigid_structure": 3,
        "force_transfer": 3,
        "scooping_surface": 2,
        "durable_material": 2,
        "fragile_object": -5,
        "flexible_structure": -4,
        "poor_leverage": -3,
        "soft_material": -4
    }
},
"open_bottle_of_beer": {
    "required_affordance":
    "rigid leverage-based cap removal",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "knife": 10,
        "spoon": 8,
        "fork": 6,
        # CONDITIONAL / IMPROVISED
        "bottle": 5,
        "dining table": 3,
        "chair": 2,
        # CONTEXTUAL OBJECTS
        "wine glass": 1,
        "refrigerator": 1,
        "person": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "kitchen": {
            "knife": 4,
            "spoon": 3,
            "dining table": 2
        },
        "party": {
            "bottle": 4,
            "spoon": 2
        },
        "camping": {
            "knife": 5,
            "fork": 3,
            "chair": 2
        },
        "bar": {
            "knife": -2,
            "spoon": -1,
            "bottle": 1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "rigid_thin_edge": 5,
        "leverage_capability": 4,
        "durable_structure": 3,
        "easy_grip": 2,
        "compact_shape": 1,
        "soft_object": -5,
        "fragile_object": -4,
        "poor_leverage_geometry": -4,
        "flexible_structure": -3
    }
},
"open_parcel": {
    "required_affordance":
    "controlled cutting or tearing of packaging material",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "scissors": 10,
        "knife": 9,
        # CONDITIONAL / IMPROVISED
        "fork": 4,
        # CONTEXTUAL OBJECTS
        "backpack": 2,
        "suitcase": 2,
        "dining table": 1,
        "book": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "office": {
            "scissors": 5,
            "knife": -1
        },
        "kitchen": {
            "knife": 4,
            "scissors": 1
        },
        "storage_room": {
            "box": 3,
            "suitcase": 2,
            "backpack": 2
        },
        "emergency": {
            "knife": 3,
            "fork": 2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "sharp_edge": 5,
        "cutting_precision": 4,
        "stable_grip": 3,
        "controlled_force": 2,
        "compact_tool": 1,
        "blunt_object": -5,
        "fragile_object": -3,
        "poor_control": -4,
        "soft_object": -4
    }
},
"serve_wine": {
    "required_affordance":
    "socially appropriate serving and drinking of wine",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "wine glass": 10,
        "bottle": 8,
        # GOOD ALTERNATIVES
        "cup": 6,
        "bowl": 2,
        # CONTEXTUAL OBJECTS
        "dining table": 2,
        "chair": 1,
        "person": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "restaurant": {
            "wine glass": 6,
            "cup": -4,
            "bowl": -6
        },
        "home": {
            "bottle": 3,
            "cup": 1
        },
        "camping": {
            "cup": 4,
            "wine glass": -5
        },
        "party": {
            "wine glass": 3,
            "bottle": 2,
            "cup": 1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "beverage_specific_design": 5,
        "elegant_appearance": 4,
        "liquid_containment": 3,
        "easy_pouring": 2,
        "comfortable_drinking_shape": 2,
        "socially_inappropriate": -6,
        "spill_prone_shape": -3,
        "poor_drinking_ergonomics": -4,
        "fragile_object": -1
    }
},
"pour_sugar": {
    "required_affordance":
    "controlled transfer of granular material with minimal spilling",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "cup": 10,
        "spoon": 9,
        "bowl": 7,
        # GOOD ALTERNATIVES
        "bottle": 5,
        "wine glass": 3,
        # CONTEXTUAL OBJECTS
        "dining table": 1,
        "cake": 1,
        "donut": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "kitchen": {
            "spoon": 4,
            "bowl": 3,
            "cup": 2
        },
        "dining": {
            "cup": 3,
            "spoon": 3,
            "bowl": -1
        },
        "baking": {
            "bowl": 5,
            "spoon": 2
        },
        "cafe": {
            "cup": 4,
            "spoon": 4,
            "wine glass": -2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "controlled_pouring": 4,
        "precise_quantity_transfer": 4,
        "stable_grip": 3,
        "narrow_flow_control": 2,
        "easy_handling": 2,
        "spill_prone_shape": -4,
        "unstable_container": -3,
        "poor_grip": -3,
        "excessive_volume": -1
    }
},
"smear_butter": {
    "required_affordance":
    "controlled smooth spreading of soft material on surface",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "knife": 10,
        "spoon": 7,
        # CONDITIONAL / IMPROVISED
        "fork": 4,
        "bowl": 2,
        # CONTEXTUAL OBJECTS
        "cup": 1,
        "cake": 1,
        "dining table": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "breakfast": {
            "knife": 5,
            "spoon": 1
        },
        "kitchen": {
            "spoon": 3,
            "fork": 2
        },
        "baking": {
            "bowl": 4,
            "spoon": 2
        },
        "outdoor": {
            "spoon": 2,
            "fork": 1
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "flat_spreading_surface": 5,
        "smooth_edge": 4,
        "pressure_control": 3,
        "stable_grip": 2,
        "food_safe_shape": 2,
        "uneven_surface": -4,
        "poor_spreading_geometry": -5,
        "absorbent_material": -5,
        "dangerous_sharpness": -1
    }
},
"extinguish_fire": {
    "required_affordance":
    "rapid and safe suppression of fire using liquid delivery",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "fire hydrant": 10,
        "bottle": 8,
        "sink": 7,
        # GOOD ALTERNATIVES
        "bowl": 5,
        "cup": 4,
        # CONTEXTUAL OBJECTS
        "truck": 3,
        "boat": 1,
        "person": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "kitchen": {
            "sink": 5,
            "bowl": 3,
            "cup": 2
        },
        "outdoor": {
            "fire hydrant": 6,
            "bottle": 2
        },
        "urban": {
            "fire hydrant": 5,
            "truck": 3
        },
        "emergency": {
            "bottle": 3,
            "cup": 2,
            "bowl": 2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "large_liquid_capacity": 5,
        "rapid_liquid_delivery": 4,
        "safe_distance_operation": 3,
        "easy_refill": 2,
        "portable_water_source": 2,
        "flammable_material": -6,
        "fragile_object": -4,
        "tiny_capacity": -3,
        "poor_liquid_control": -3
    }
},
"pound_carpet": {
    "required_affordance":
    "generation of repeated impact force for carpet cleaning",
    # ==========================================
    # BASE TASK SCORES
    # ==========================================
    "scores": {
        # BEST OBJECTS
        "baseball bat": 10,
        "tennis racket": 8,
        # CONDITIONAL / IMPROVISED
        "book": 6,
        "bench": 4,
        "chair": 3,
        # CONTEXTUAL OBJECTS
        "bed": 1,
        "backpack": 1,
        "suitcase": 1
    },
    # ==========================================
    # CONTEXT MODIFIERS
    # ==========================================
    "context_modifiers": {
        "outdoor_cleaning": {
            "baseball bat": 5,
            "tennis racket": 4
        },
        "home": {
            "book": 3,
            "chair": 2,
            "bench": 2
        },
        "sports_area": {
            "tennis racket": 5,
            "baseball bat": 3
        },
        "quick_cleaning": {
            "book": 4,
            "chair": 2
        }
    },
    # ==========================================
    # PROPERTY MODIFIERS
    # ==========================================
    "property_modifiers": {
        "large_impact_surface": 4,
        "swingability": 4,
        "rigid_structure": 3,
        "force_transfer": 3,
        "comfortable_grip": 2,
        "fragile_object": -6,
        "tiny_contact_area": -3,
        "poor_grip": -3,
        "flexible_weak_structure": -4
    }
}
}

