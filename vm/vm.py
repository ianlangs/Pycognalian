from vm.translate import comments, sentences, types
from vm.verifiquer import init, pcow
from utils import filesmanipule
from syntax.buildins import *
from syntax.classtypes import *
import utils

def translate(code):
    try:
        code = init.analize(code, init.pinit)
        code = pcow.analize(code, pcow.pcow)
    except SyntaxError as s:
        print(s.msg)
        pass
    code = comments.all(code)
    code = sentences.rw(code)
    code = sentences.use(code)
    code = sentences.fn(code)
    code = types.all(code)

    code = "import sys, os\nsys.path.append(os.path.dirname(__file__))\n" + code + "\nmain(List(sys.argv))"
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

