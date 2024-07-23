import os # interplatform compatibility

def reset_script():

    with open(os.path.join(".","window.py"), "w") as file:
        file.seek(0)
        file.truncate()

def reset_settings():

    with open(os.path.join(".","windowsettings.json"), "w") as file:
        file.seek(0)
        file.truncate()
        file.flush()
        file.seek(0)
        file.write(r"{}")
        file.flush()

