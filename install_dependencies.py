import subprocess

def install_dependencies():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_dependencies()