import pygame, json, os # im using os.path.join for inter platform conpatibility

flags=[
    pygame.FULLSCREEN,    # create a fullscreen display
    pygame.DOUBLEBUF,     # only applicable with OpenGL
    pygame.HWSURFACE,     # (obsolete in pygame 2) hardware accelerated, only in FULLSCREEN
    pygame.OPENGL,        # create an OpenGL-renderable display
    pygame.RESIZABLE,     # display window should be sizeable
    pygame.NOFRAME,       # display window will have no border or controls
    pygame.SCALED,        # resolution depends on desktop size and scale graphics
    pygame.SHOWN,         # window is opened in visible mode (default)
    pygame.HIDDEN         # window is opened in hidden mode
]
with open(os.path.join(".", "settings.json"), 'r') as data:
    settings:dict = json.loads(data.read())
    settings["flags"] = list(settings["flags"])

checkflags = settings["flags"]

enabled=0
for index, value in enumerate(checkflags):
    # print(index, flags[index])
    enabled |= flags[index] * value



path = os.path.join("..", "temp_files", "settings", "windowsettings.json")

with open(path, "r+") as output:

    temp_json=json.loads(output.read())

    temp_json["flags"] = enabled.to_bytes((enabled.bit_length() + 7) // 8, 'little').hex()

    print(temp_json)

    output.seek(0)

    output.truncate()

    output.seek(0)

    output.write(json.dumps(temp_json))