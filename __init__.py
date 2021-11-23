import os

def get_working_dir() -> str:
    for f in os.listdir("./"):
        if os.path.isdir(os.path.join("./", f)) and f != "build":
            return f
    else:
        raise ValueError("Not found the working directory")

WORK_DIR = get_working_dir()
