from vm.translate import comments, sentences, types
from vm.verifiquer import init, pcow
from utils import filesmanipule
from syntax.buildins import *
from syntax.classtypes import *
def translate(code):
    code = init.analize(code)
    code = pcow.analize(code)
    code = comments.all(code)
    code = sentences.rw(code)
    code = sentences.use(code)
    code = sentences.fn(code)
    code = types.all(code)

    code = "import sys\nsys.path.append('\\\\'.join(__file__.split('\\\\')[:-2]))\n" + code + "\nmain(List(sys.argv))"
    return code

def execute(file):
    code=filesmanipule.rfile(file)
    executeStr(code, file)

def executeStr(code:str, path):
    code = translate(code)
    exec(code, globals()|{"__file__":path}, locals())

def returned(file):
    code=filesmanipule.rfile(file)
    return returnedStr(code)

def returnedStr(code:str):
    code = translate(code)
    return code

