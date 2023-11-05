import subprocess

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
