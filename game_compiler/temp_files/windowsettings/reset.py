import os # interplatform compatibility

def reset_script():

    with open(os.path.join(".", "temp_files", "windowsettings", "window.py"), "w") as file:
        file.seek(0)
        file.truncate()

def reset_settings():

    with open(os.path.join(".", "temp_files", "windowsettings","windowsettings.json"), "w") as file:
        file.seek(0)
        file.truncate()
        file.flush()
        file.seek(0)
        file.write(r"{}")
        file.flush()

