from syntax.classtypes import List, Bool, Enum, String, Tuple, Dict, Number, CNum, regex, Lambda
__all__ = (
funcType := (lambda x:x).__class__,
LambdaType := Lambda,
regexType := regex,
regexcompileType := regexType.regexCompile(r"\d").__class__,
regexcompiletoType := regexType["",""].__class__,
dictType := Dict,
listType := List,
tupleType := Tuple,
strType := String,
NumberType := Number,
ComplexNumberType := CNum,
boolType := Bool,
enumType := Enum,
)
if __name__ == "__main__":
    for i in __all__:print(i)