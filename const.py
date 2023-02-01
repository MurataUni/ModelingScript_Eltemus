import sys
sys.dont_write_bytecode = True

import numpy as np

class Const:
    scale = 11.
    rotate_x = -np.pi/36
    class Body:
        scale = 1.
        module_length = 2.4
        x_length = 2.
        y_length = 2.4
        body_to_chest_extension = -np.pi/32
        body_to_waist_extension = -np.pi/36
    class Chest:
        scale = 1.
        module_length = 1.5
        chest_to_neck_side_bend_right = 0.
        chest_to_neck_adduction = 0.
    class Neck:
        scale = 1.
        module_length = 1.
        x_length = 1.
        y_length = 1.5
        neck_to_head_rotation_left = 0.
        neck_to_head_side_bend_right = 0.
        neck_to_head_addction = -np.pi/32
    class Head:
        scale = 1.
    class Arm:
        z_position_chest_height_ratio = 0.65
        y_position = -0.01
        class Shoulder:
            shoulder_adapter_height = 0.8
            shoulder_adapter_width = 1.2
            shoulder_adapter_depth = 1.
            shoulder_adapter_extend = 0.4
            shoulder_height = 1.
            shoulder_width = 1.
            shoulder_depth = 1.2
        class ShoulderArmor:
            shoulder_adapter_position_ratio = 0.9
            shoulder_armor_base_x = 0.5
            shoulder_armor_base_y = 1.4
            shoulder_armor_base_length = 1.2
            shoulder_armer_panel_fore_offset = 0.4
            shoulder_armer_panel_back_offset = -0.4
            shoulder_armor_x = 4.5
            shoulder_armor_y = 0.5
            shoulder_armor_thick = 0.2
        class UpperArm:
            module_length = 1.6
            height = 1.2
            width = 1.0
        class ForeArm:
            module_length = 4.2
            height = 1.4
            width = 1.2
        class Hand:
            to_forearm_overrap = 0.3/2
            wrist_length = 0.3
            wrist_height = 0.4
            wrist_width = 0.4
            hand_length = 1.
            hand_height = 0.5
            hand_width = 1.
            glasp_position_z = wrist_length + hand_length*0.6
            glasp_position_y = -0.25
        class Finger:
            finger_1_width = 0.21
            finger_1_height = 0.18
            finger_1_length = 0.36
            finger_3_width = 0.21
            finger_3_height = 0.18
            finger_3_length = 0.18
            finger_wide_1_width = 0.4
            finger_wide_1_height = 0.18
            finger_wide_1_length = 0.36
            finger_wide_3_width = 0.4
            finger_wide_3_height = 0.18
            finger_wide_3_length = 0.18
            finger_thumb_1_width = 0.25
            finger_thumb_1_height = 0.15
            finger_thumb_1_length = 0.27
            finger_thumb_3_width = 0.25
            finger_thumb_3_height = 0.15
            finger_thumb_3_length = 0.15
        class Right:
            shoulder_flexion = -np.pi/16 
            shoulder_abduction = np.pi/2-np.pi/9
            shoulder_armer_abduction = -np.pi/2-np.pi/16.
            upper_arm_rotation_outer = 0.
            forearm_extension = -np.pi/3
            hand_rotation_outer = np.pi/2
            hand_palmar_flexion = 0.
            hand_radial_flexion = -np.pi/36
        class Left:
            shoulder_flexion = 0.
            shoulder_abduction = np.pi/2-np.pi/9
            shoulder_armer_abduction = -np.pi/2-np.pi/16.
            upper_arm_rotation_outer = 0.
            forearm_extension = -np.pi/6
            hand_rotation_outer = -np.pi/2
            hand_palmar_flexion = 0.
            hand_radial_flexion = 0.
    class Backpack:
        z_position_chest_height_ratio = 0.35
        y_position_chest_offset = -1.2
        base_x = 3.4
        base_y = 1.8
        base_thick = 1.4
        upper_panel_offset_y = 0.9
        upper_panel_x = 1.4
        upper_panel_y = 0.2
        upper_panel_length= 4.
        class SidePanel:
            position_y_offset = -0.4
            position_z_offset = 0.2
            position_x_offset_right = 1.2
            x_length = 0.8
            y_length = 0.2
            length = 4.5
        class Right:
            rotate_z = 7/18*np.pi
            rotate_y = -6/18*np.pi
        class Left:
            rotate_z = 11/18*np.pi
            rotate_y = -6/18*np.pi
    class Waist:
        class Upper:
            x_length = 2.6
            y_length = 3.
            thick = 0.5
        class Lower:
            x_length = 0.4
            y_length = 2.8
            thick = 2.
        class CoxaJoint:
            coxa_joint_z_position = 1.4
            coxa_radius = 0.4
            length = 2.4
    class Leg:
        class Thigh:
            x_length = 1.5
            y_length = 2.
            length = 4.8
            overrap = 0.5
        class Shin:
            x_length = 0.7
            y_length = 1.
            length = 5.2
        class Foot:
            x_length = 0.5
            y_length = 2.
            length = 1.5
        class Right:
            leg_extension = -np.pi/72
            leg_abduction = np.pi/2-np.pi/24
            leg_rotation_outer = np.pi/36
            shin_flexion = np.pi/36
            foot_rotation_outer = np.pi/36
            foot_palmar_flexion = -np.pi/72
            foot_radial_flexion = np.pi/24
        class Left:
            leg_extension = -np.pi/72
            leg_abduction = np.pi/2-np.pi/24
            leg_rotation_outer = np.pi/36
            shin_flexion = np.pi/36
            foot_rotation_outer = np.pi/36
            foot_palmar_flexion = -np.pi/72
            foot_radial_flexion = np.pi/24



