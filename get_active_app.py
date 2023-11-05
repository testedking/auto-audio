import pygetwindow as gw

def get_active_app_name():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
    except Exception as e:
        print(f"Error getting active app: {e}")
    print("No window")
    return None

# Usage
active_app = get_active_app_name()
