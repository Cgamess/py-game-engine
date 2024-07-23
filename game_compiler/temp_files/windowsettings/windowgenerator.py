from jinja2 import Template
import os, json # os for interplatform compatibility

pytemplate=open(os.path.join(".", "windowtemplate.pytemp"))

template=Template(pytemplate)

settings = json.loads(os.path.join(".", "windowsettings.json"))

script=template.render(settings)

with open(os.path.join(".", "window.py"), "w") as windowpy:
    windowpy.write(script)