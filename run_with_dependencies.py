import subprocess
import json

# Define the 'app' variable to be used
print("Input Process ID here")
app = input("e.g. Spotify.exe, AMPLibraryAgent.exe, firefox.exe: ")

# Update the 'app' variable in the 'app.json' file
config = {"app": app}
with open("app.json", "w") as config_file:
    json.dump(config, config_file)

# Define a function to run the dependency installation script
def run_dependency_installation():
    try:
        subprocess.check_call(["python", "install_dependencies.py"])
    except subprocess.CalledProcessError as e:
        print(f"Error running dependency installation: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the dependency installation script before running main.py
run_dependency_installation()

# Now, execute main.py
subprocess.call(["python", "main.py"])
