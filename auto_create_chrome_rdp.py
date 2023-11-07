import subprocess

# app_name = "shaf-chrome-3"
APP_NAME="shaf-chrome-12"


def destroy_heroku_app(app_name):
    # Command to destroy the Heroku app
    command = ['heroku', 'apps:destroy', '--app', app_name]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"The Heroku app '{app_name}' has been successfully destroyed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while destroying the Heroku app '{app_name}': {e}")


try:
    destroy_heroku_app(APP_NAME)
except:
    pass
# Remove .git directory
subprocess.run(["rmdir", "/s", "/q", ".git"], shell=True)

# Initialize a new git repository
subprocess.run(["git", "init"], shell=True)

# Add all files to the git repository
subprocess.run(["git", "add", "."], shell=True)

# Commit the changes
subprocess.run(["git", "commit", "-m", "Initial commit"], shell=True)

# Create a Heroku app
subprocess.run(["heroku", "create", APP_NAME], shell=True)

# Set the Heroku stack to container
subprocess.run(["heroku", "stack:set", "container", '--app', APP_NAME], shell=True)

# Push the code to Heroku
subprocess.run(["git", "push", "heroku", "master"], shell=True)


# Define the command to set the environment variables
command = [
    'heroku',
    'config:set',
    'APP_NAME=' + APP_NAME,
    'VNC_TITLE=Chromium',
    'VNC_PASS=123456',
    'VNC_RESOLUTION=1280x720',
    'NO_SLEEP=1',
    '--app',
    'your-app-name'
]

# Execute the command using subprocess
subprocess.run(command, check=True)
