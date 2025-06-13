import os
import shutil
import subprocess

def detect_dep():
    temp_dir = "temp_pipreqs_dir"
    os.makedirs(temp_dir, exist_ok=True)
    shutil.move("LLM_solution.py", os.path.join(temp_dir, "LLM_solution.py"))
    subprocess.run(["pipreqs", "--force", temp_dir], check=True)
    with open(os.path.join(temp_dir, "requirements.txt"), "r") as f:
        requirements = f.read()
    shutil.rmtree(temp_dir)
    return requirements