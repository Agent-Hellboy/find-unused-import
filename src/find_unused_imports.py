import _ast
import ast  
from typing import List 

import click 

from nodes import AST_NODES, get_class_str, OBJECTS

class FollowPEP8Exception(Exception):
    pass

nodes = []
def find_ast_class(body: List) -> None: 
    for node in body.body:
        nodes.append(node)
        if 'body' in dir(node):
            find_ast_class(node)
        
def iter_node(nodes: List) -> None:
    for node in nodes:
        AST_NODES[get_class_str(node)].parse_node(node)

        
@click.command()
@click.option("--name", help="Name of the file", required=True)
def find_unused_import(name: str) -> None:
    with open(name,"r") as f:
        data = f.read()
    source_ast =ast.parse(data)
    imported_obj = []
    for node in source_ast.body:
        if type(node) == _ast.Import:
            imported_obj.append(node.names[0].name)
            if len(node.names) > 1:
                raise FollowPEP8Exception("please follow PEP 8") 

        elif type(node) == _ast.ImportFrom:
            for name in node.names:
                imported_obj.append(name.name)
        else:
            if 'body' in dir(node):
                find_ast_class(node)

    iter_node(nodes)
    unused_imports = []
    for obj in imported_obj:
        if obj in OBJECTS:
            continue
        else:
            unused_imports.append(obj)
    print("These are the unused imports:", unused_imports)

if __name__ == "__main__":
    find_unused_import()