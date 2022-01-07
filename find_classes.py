import re 
import ast 
import inspect 
import os 
from ast import AST 
import sys 

SIP = 123

clsmembers = inspect.getmembers(ast, inspect.isclass)

def get_class_str(l):
    s = re.search(r"<(.*?)>",l)
    return s.group(1).split("'")[1]

def make_dict():
    classes = {}
    for i in clsmembers:
        classes[get_class_str(str(i[1]))] = i[0] 
    return classes

p = make_dict()
filename = "file.py"
str = ""
for i,j in p.items():
    str += f"class {j}:\n\t"
    str += "@classmethod\n\t"
    str += "def parse_node(self,obj):\n\t\tprint(obj)"
    str += "\n\n"
with open(filename,"w") as f:
    f.write(str)