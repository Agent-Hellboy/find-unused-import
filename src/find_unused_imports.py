import _ast
import ast
from typing import List, Any

import click

from nodes import AST_NODES, OBJECTS, get_class_str


class FollowPEP8Exception(Exception):
    """
    Raise an exception if objects are imported like `import a,b,c`
    """

    pass


def find_ast_class(body: Any, nodes: List) -> None:
    """
    Recursivly iterate over nodes and add all occurences of ast node to nodes
    """
    if "body" not in dir(body):
        nodes.append(body)
    else:
        for node in body.body:
            nodes.append(node)
            if "body" in dir(node):
                find_ast_class(node, nodes)


def iter_node(nodes: List) -> None:
    """
    Iterate over all the ast nodes present inside the file
    and process it to get the relevent info
    """
    for node in nodes:
        AST_NODES[get_class_str(node)].parse_node(node)


def get_source_ast(name: str) -> _ast.Module:
    """
    Return ast of source code
    """
    with open(name, "r") as f:
        data = f.read()
    return ast.parse(data)


def get_unused_imports(nodes: List, imported_obj: List) -> None:
    """
    Print the object if it is imported and never used inside the code
    """
    iter_node(nodes)
    unused_imports = [obj for obj in imported_obj if obj not in OBJECTS]
    print("These are the unused imports:", unused_imports)


@click.command()
@click.option("--name", help="Name of the file", required=True)
def find_unused_import(name: str) -> None:
    imported_obj = []
    nodes = []
    source_ast = get_source_ast(name)
    for node in source_ast.body:
        if type(node) == _ast.Import:
            imported_obj.append(node.names[0].name)
            if len(node.names) > 1:
                raise FollowPEP8Exception("please follow PEP 8")
        elif type(node) == _ast.ImportFrom:
            for name in node.names:
                imported_obj.append(name.name)
        else:
            find_ast_class(node, nodes)

    get_unused_imports(nodes, imported_obj)


if __name__ == "__main__":
    find_unused_import()
