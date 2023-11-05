from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_application_volume(app_name, volume):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_control = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == app_name:
            volume_control.SetMasterVolume(volume, None)

# Example usage of set_application_volume function
# set_application_volume("firefox.exe", 0.5)  # Set Firefox volume to 50%

# You can add this function to your volume_control.py
