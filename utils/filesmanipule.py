def rfile(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
def wfile(filepath,newtext):
    with open(filepath, "w") as f:
        f.write(newtext)
def afile(filepath,newtext):
    with open(filepath, "a") as f:
        f.write(newtext)