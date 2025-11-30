import sys, subprocess, re
def main():
    pipr = subprocess.run(command, capture_output=True, text=True, stdout=subprocess.DEVNULL, check=True)
    cpmr = re.sub(r"pip\d{0:5}", "cpm", pipr)
    print(f"\n{code}\n")
