from jinja2 import Template
import os, json # os for interplatform compatibility

def prep_script():

    pytemplate=open(os.path.join(".", "temp_files", "windowsettings", "windowtemplate.pytemp"))

    template=Template(pytemplate.read())

    settings = json.loads(open(os.path.join(".", "temp_files", "windowsettings", "windowsettings.json")).read())

    script=template.render(settings)

    with open(os.path.join(".", "temp_files", "windowsettings",  "window.py"), "w") as windowpy:
        windowpy.write(script)