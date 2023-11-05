import time
from ocr import capture_screen_and_ocr
from volume_control import set_application_volume
from get_active_app import get_active_app_name
import pyautogui
import json
import os


target_fps = 1  # Desired frame rate

# Load app_settings from the JSON file
with open("app_settings.json", "r") as file:
    app_settings = json.load(file)

game = str()
executable_name = str()
gameState = str()
CurrentVolume = str("louder")
app = "AMPLibraryAgent.exe"

# Load the game names, executable names, and screenshot regions from the app_region_presets.json file
with open("app_region_presets.json", "r") as file:
    app_region_presets = json.load(file)

# Initialize a flag to control program execution
active_app_flag = False

# Initialize a timestamp to track the last time the app was checked
last_check_time = 0

os.system("cls")
print("Starting ")
while True:
    start_time = time.time()

    current_time = time.time()

    # Check for the active app less often when it doesn't match the game executable title
    if (current_time - last_check_time) >= 0:  # Check every # seconds
        active_app = get_active_app_name()
        last_check_time = current_time  # Update the last check time

        if active_app:
            active_exe_name = active_app.lower().replace(" ", "")
            # print("Active App:", active_exe_name)

            if active_exe_name in app_region_presets["games"]:
                game = active_exe_name
                for state, state_info in app_region_presets["games"][game]["states"].items():
                    if state != gameState:
                        # print(state)
                        gameState = state
                        regions = state_info["region"]  # Define regions here
                        if regions:
                            # print(regions)
                            ocr_text = capture_screen_and_ocr(regions[0], regions[1], regions[2], regions[3])

                        if state_info["expected_string"].lower() in ocr_text.lower():
                            # If the lowercase "expected_string" is found in the lowercase ocr_text, print the message
                            # print("expected_string_found")
                            #print(state)
                            #print(ocr_text)
                            # Use the volume control function from volume_control.py
                            if state_info["ModifyVolume"] == "louder":
                                #print("Volume: Louder")
                                CurrentVolume = "louder"
                                set_application_volume(app, app_settings["games"][game][app]["louder"])
                            elif state_info["ModifyVolume"] == "quieter":
                                #print("Volume: Quieter")
                                CurrentVolume = "quieter"
                                set_application_volume(app, app_settings["games"][game][app]["quieter"])
                            elif state_info["ModifyVolume"] == "invalid":
                                #print("Volume: Invalid")   
                                #print("Using Previous: " + CurrentVolume)
                                if CurrentVolume == "louder":
                                    #CurrentVolume = "louder"
                                    # Set to Louder volume
                                    set_application_volume(app, app_settings["games"][game][app]["louder"])
                                else:
                                    #CurrentVolume = "quieter"
                                    # Set to Quieter volume
                                    set_application_volume(app, app_settings["games"][game][app]["quieter"])
                                # Handle "invalid" state here
                                

                            if ocr_text != state_info["expected_string"]:
                                # The text in this region doesn't match the expected_string
                                # Capture and process regions for other states
                                for other_state, other_state_info in app_region_presets.get(game, {}).items():
                                    if other_state != state:
                                        other_regions = other_state_info["region"]
                                        if other_regions:
                                            for other_region in other_regions:
                                                screenshot = pyautogui.screenshot(region=other_region)
                                                screenshot = screenshot.convert('RGB')
                                                screenshot = screenshot.resize((other_region[2], other_region[3]))
                                                screenshot, ocr_text = capture_screen_and_ocr(screenshot)
                                                # Your OCR-based actions here

                active_app_flag = True  # Set the flag to True for the active app

        if executable_name in app_settings and executable_name in app_settings.get(game, {}):
            # Use the volume control function from volume_control.py
            print("control volume here:")
            # control_volume(executable_name, app_settings[game][executable_name])

    # Calculate the time taken for the operation
    time_taken = time.time() - start_time

    # Calculate the delay needed to achieve the target frame rate
    delay = 1 / target_fps - time_taken

    # Check if we need to introduce a delay
    if delay > 0:
        time.sleep(delay)
    #print("active_app_flag:" + str(active_app_flag))
    #print("active_app:" + str(active_app.lower()))
    #if active_app_flag:
    #    print(ocr_text)
