import _ast
import re 

OBJECTS = []

def get_class_str(node_repr):
    node_str = type(node_repr)
    ptrn = re.search(r"<(.*?)>", str(node_str))
    return ptrn.group(1).split("'")[1]

class AST:
	@classmethod
	def parse_node(self,obj):
		pass

class Add:
	@classmethod
	def parse_node(self,obj):
		pass

class And:
	@classmethod
	def parse_node(self,obj):
		pass

class AnnAssign:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        AST_NODES[get_class_str(obj.annotation)].parse_node(obj.annotation)

class Assert:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)
        AST_NODES[get_class_str(obj.msg)].parse_node(obj.msg)

class Assign:
    @classmethod
    def parse_node(self,obj):
        for node in obj.targets:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class AsyncFor:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)

class AsyncFunctionDef:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.args)].parse_node(obj.args)
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.decorator_list:
            AST_NODES[get_class_str(node)].parse_node(node)
        OBJECTS.append(obj.name)

class AsyncWith:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.items:
            AST_NODES[get_class_str(node)].parse_node(node)

class Attribute:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        OBJECTS.append(obj.attr)


class AugAssign:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class AugLoad:
	@classmethod
	def parse_node(self,obj):
		pass 

class AugStore:
	@classmethod
	def parse_node(self,obj):
		pass 

class Await:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class BinOp:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.left)].parse_node(obj.left)
        AST_NODES[get_class_str(obj.right)].parse_node(obj.right)

class BitAnd:
	@classmethod
	def parse_node(self,obj):
		pass 

class BitOr:
	@classmethod
	def parse_node(self,obj):
		pass

class BitXor:
	@classmethod
	def parse_node(self,obj):
		pass

class BoolOp:
    @classmethod
    def parse_node(self,obj):
        for node in obj.values:
            AST_NODES[get_class_str(node)].parse_node(node)

class Break:
	@classmethod
	def parse_node(self,obj):
		pass 

class Bytes:
	@classmethod
	def parse_node(self,obj):
		pass 

class Call:
    @classmethod
    def parse_node(self,obj):
        for node in obj.args:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.keywords:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.func)].parse_node(obj.func)

class ClassDef:
    @classmethod
    def parse_node(self,obj):
        OBJECTS.append(obj.name)
        for node in obj.bases:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.keywords:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.decorator_list:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.starargs)].parse_node(obj.starargs)
        AST_NODES[get_class_str(obj.kwargs)].parse_node(obj.kwargs)

class Compare:
    @classmethod
    def parse_node(self,obj):
        for node in obj.comparators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(node)].parse_node(node)

class Constant:
	@classmethod
	def parse_node(self,obj):
		OBJECTS.append(obj.value)

class Continue:
	@classmethod
	def parse_node(self,obj):
		pass 

class Del:
	@classmethod
	def parse_node(self,obj):
		pass 

class Delete:
    @classmethod
    def parse_node(self,obj):
        for node in obj.targets:
            AST_NODES[get_class_str(node)].parse_node(node)

class Dict:
    @classmethod
    def parse_node(self,obj):
        for node in obj.keys:
            AST_NODES[get_class_str(node)].parse_node(obj.node)
        for node in obj.values:
            AST_NODES[get_class_str(node)].parse_node(obj.node)

class DictComp:
    @classmethod
    def parse_node(self,obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.key)].parse_node(obj.key)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class Div:
	@classmethod
	def parse_node(self,obj):
		pass 

class Ellipsis:
	@classmethod
	def parse_node(self,obj):
		pass 

class Eq:
	@classmethod
	def parse_node(self,obj):
		pass 

class ExceptHandler:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.type)].parse_node(obj.type)
        OBJECTS.append(obj.name)

class Expr:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class Expression:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.body)].parse_node(obj.body)

class ExtSlice:
	@classmethod
	def parse_node(self,obj):
		pass 

class FloorDiv:
	@classmethod
	def parse_node(self,obj):
		pass

class For:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)

class FormattedValue:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class FunctionDef:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.args)].parse_node(obj.args)
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.decorator_list:
            AST_NODES[get_class_str(node)].parse_node(node)
        OBJECTS.append(obj.name)

class FunctionType:
	@classmethod
	def parse_node(self,obj):
		pass

class GeneratorExp:
    @classmethod
    def parse_node(self,obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)

class Global:
    @classmethod
    def parse_node(self,obj):
        for name in obj.names:
            OBJECTS.append(name)

class Gt:
	@classmethod
	def parse_node(self,obj):
		pass 

class GtE:
	@classmethod
	def parse_node(self,obj):
		pass 

class If:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)

class IfExp:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)
        AST_NODES[get_class_str(obj.body)].parse_node(obj.body)
        AST_NODES[get_class_str(obj.orelse)].parse_node(obj.orelse)

class Import:
	@classmethod
	def parse_node(self,obj):
		pass 

class ImportFrom:
	@classmethod
	def parse_node(self,obj):
		pass 

class In:
	@classmethod
	def parse_node(self,obj):
		pass 

class Index:
	@classmethod
	def parse_node(self,obj):
		pass 

class Interactive:
	@classmethod
	def parse_node(self,obj):
		pass 

class Invert:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.operand)].parse_node(obj.operand)

class Is:
	@classmethod
	def parse_node(self,obj):
		pass

class IsNot:
	@classmethod
	def parse_node(self,obj):
		pass

class JoinedStr:
    @classmethod
    def parse_node(self,obj):
        for node in obj.values:
            AST_NODES[get_class_str(node)].parse_node(node)

class LShift:
	@classmethod
	def parse_node(self,obj):
		pass 

class Lambda:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.args)].parse_node(obj.args)      
class List:
    @classmethod
    def parse_node(self,obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)

class ListComp:
    @classmethod
    def parse_node(self,obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)

class Load:
	@classmethod
	def parse_node(self,obj):
		pass 

class Lt:
	@classmethod
	def parse_node(self,obj):
		pass

class LtE:
	@classmethod
	def parse_node(self,obj):
		pass

class MatMult:
	@classmethod
	def parse_node(self,obj):
		pass

class Mod:
	@classmethod
	def parse_node(self,obj):
		pass

class Module:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)

class Mult:
	@classmethod
	def parse_node(self,obj):
		pass

class Name:
	@classmethod
	def parse_node(self,obj):
		OBJECTS.append(obj.id)

class NameConstant:
	@classmethod
	def parse_node(self,obj):
		pass 

class NamedExpr:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)

class NodeTransformer:
	@classmethod
	def parse_node(self,obj):
		pass 

class NodeVisitor:
	@classmethod
	def parse_node(self,obj):
		pass 

class Nonlocal:
    @classmethod
    def parse_node(self,obj):
        for name in obj.names:
            OBJECTS.append(name)

class Not:
	@classmethod
	def parse_node(self,obj):
		pass 

class NotEq:
	@classmethod
	def parse_node(self,obj):
		pass 

class NotIn:
	@classmethod
	def parse_node(self,obj):
		pass 

class Num:
	@classmethod
	def parse_node(self,obj):
		pass

class Or:
	@classmethod
	def parse_node(self,obj):
		pass 

class Param:
	@classmethod
	def parse_node(self,obj):
		pass

class Pass:
	@classmethod
	def parse_node(self,obj):
		pass 

class Pow:
	@classmethod
	def parse_node(self,obj):
		pass 

class RShift:
	@classmethod
	def parse_node(self,obj):
		pass 

class Raise:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.exec)].parse_node(obj.exec)
        AST_NODES[get_class_str(obj.cause)].parse_node(obj.cause)

class Return:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class Set:
    @classmethod
    def parse_node(self,obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)

class SetComp:
    @classmethod
    def parse_node(self,obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)

class Slice:
    @classmethod
    def parse_node(self,obj):
        if obj.lower:
            AST_NODES[get_class_str(obj.lower)].parse_node(obj.lower)
        if obj.upper:
            AST_NODES[get_class_str(obj.upper)].parse_node(obj.upper)
        if obj.step:
            AST_NODES[get_class_str(obj.step)].parse_node(obj.step)

class Starred:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class Store:
	@classmethod
	def parse_node(self,obj):
		pass 

class Str:
	@classmethod
	def parse_node(self,obj):
		pass

class Sub:
	@classmethod
	def parse_node(self,obj):
		pass

class Subscript:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        AST_NODES[get_class_str(obj.slice)].parse_node(obj.slice)

class Suite:
	@classmethod
	def parse_node(self,obj):
		pass

class Try:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.handlers:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.finalbody:
            AST_NODES[get_class_str(node)].parse_node(node)        

class Tuple:
    @classmethod
    def parse_node(self,obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)

class TypeIgnore:
	@classmethod
	def parse_node(self,obj):
		pass

class UAdd:
	@classmethod
	def parse_node(self,obj):
		pass

class USub:
	@classmethod
	def parse_node(self,obj):
		pass

class UnaryOp:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.operand)].parse_node(obj.operand)

class While:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)

class With:
    @classmethod
    def parse_node(self,obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.items:
            AST_NODES[get_class_str(node)].parse_node(node)

class Yield:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class YieldFrom:
	@classmethod
	def parse_node(self,obj):
		AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class _ABC:
	@classmethod
	def parse_node(self,obj):
		pass

class alias:
    @classmethod
    def parse_node(self,obj):
        OBJECTS.append(obj.name)
        if obj.asname:
            OBJECTS.append(obj.asname)

class arg:
    @classmethod
    def parse_node(self,obj):
        OBJECTS.append(obj.arg)
        AST_NODES[get_class_str(obj.annotation)].parse_node(obj.annotation)

class arguments:
    @classmethod
    def parse_node(self,obj):
        for node in obj.posonlyargs:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.kwonlyargs:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.args:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.vararg)].parse_node(obj.vararg)
        AST_NODES[get_class_str(node.kwarg)].parse_node(node.kwarg)
        
        

class boolop:
    @classmethod
    def parse_node(self,obj):
        pass

class cmpop:
	@classmethod
	def parse_node(self,obj):
		pass

class comprehension:
    @classmethod
    def parse_node(self,obj):
        for node in obj.ifs:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)

class excepthandler:
	@classmethod
	def parse_node(self,obj):
		pass

class expr:
	@classmethod
	def parse_node(self,obj):
		pass

class expr_context:
	@classmethod
	def parse_node(self,obj):
		pass

class keyword:
    @classmethod
    def parse_node(self,obj):
        OBJECTS.append(obj.arg)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)

class mod:
	@classmethod
	def parse_node(self,obj):
		pass 

class operator:
	@classmethod
	def parse_node(self,obj):
		pass 

class slice:
	@classmethod
	def parse_node(self,obj):
		pass

class stmt:
	@classmethod
	def parse_node(self,obj):
		pass

class type_ignore:
	@classmethod
	def parse_node(self,obj):
		pass

class unaryop:
	@classmethod
	def parse_node(self,obj):
		pass 

class withitem:
    @classmethod
    def parse_node(self,obj):
        AST_NODES[get_class_str(obj.context_expr)].parse_node(obj.context_expr)
        AST_NODES[get_class_str(obj.optional_vars)].parse_node(obj.optional_vars)

AST_NODES = {
    '_ast.AST': AST, 
    '_ast.Add': Add,
    '_ast.And': And, 
    '_ast.AnnAssign': AnnAssign, 
    '_ast.Assert': Assert, 
    '_ast.Assign': Assign, 
    '_ast.AsyncFor': AsyncFor, 
    '_ast.AsyncFunctionDef': AsyncFunctionDef, 
    '_ast.AsyncWith': AsyncWith, 
    '_ast.Attribute': Attribute, 
    '_ast.AugAssign': AugAssign, 
    '_ast.AugLoad': AugLoad, 
    '_ast.AugStore': AugStore, 
    '_ast.Await': Await, 
    '_ast.BinOp': BinOp, 
    '_ast.BitAnd': BitAnd, 
    '_ast.BitOr': BitOr, 
    '_ast.BitXor': BitXor, 
    '_ast.BoolOp': BoolOp, 
    '_ast.Break': Break, 
    'ast.Bytes': Bytes, 
    '_ast.Call': Call, 
    '_ast.ClassDef': ClassDef, 
    '_ast.Compare': Compare, 
    '_ast.Constant': Constant, 
    '_ast.Continue': Continue, 
    '_ast.Del': Del, 
    '_ast.Delete': Delete, 
    '_ast.Dict': Dict, 
    '_ast.DictComp': DictComp, 
    '_ast.Div': Div, 
    'ast.Ellipsis': Ellipsis, 
    '_ast.Eq': Eq, 
    '_ast.ExceptHandler': ExceptHandler, 
    '_ast.Expr': Expr, 
    '_ast.Expression': Expression, 
    '_ast.ExtSlice': ExtSlice, 
    '_ast.FloorDiv': FloorDiv, 
    '_ast.For': For, 
    '_ast.FormattedValue': FormattedValue, 
    '_ast.FunctionDef': FunctionDef, 
    '_ast.FunctionType': FunctionType, 
    '_ast.GeneratorExp': GeneratorExp, 
    '_ast.Global': Global, 
    '_ast.Gt': Gt, 
    '_ast.GtE': GtE, 
    '_ast.If': If, 
    '_ast.IfExp': IfExp, 
    '_ast.Import': Import, 
    '_ast.ImportFrom': ImportFrom, 
    '_ast.In': In, 
    '_ast.Index': Index, 
    '_ast.Interactive': Interactive, 
    '_ast.Invert': Invert, 
    '_ast.Is': Is, 
    '_ast.IsNot': IsNot, 
    '_ast.JoinedStr': JoinedStr, 
    '_ast.LShift': LShift, 
    '_ast.Lambda': Lambda, 
    '_ast.List': List, 
    '_ast.ListComp': ListComp, 
    '_ast.Load': Load, 
    '_ast.Lt': Lt, 
    '_ast.LtE': LtE, 
    '_ast.MatMult': MatMult, 
    '_ast.Mod': Mod, 
    '_ast.Module': Module, 
    '_ast.Mult': Mult, 
    '_ast.Name': Name, 
    'ast.NameConstant': NameConstant, 
    '_ast.NamedExpr': NamedExpr, 
    'ast.NodeTransformer': NodeTransformer, 
    'ast.NodeVisitor': NodeVisitor, 
    '_ast.Nonlocal': Nonlocal, 
    '_ast.Not': Not, 
    '_ast.NotEq': NotEq, 
    '_ast.NotIn': NotIn, 
    'ast.Num': Num, 
    '_ast.Or': Or, 
    '_ast.Param': Param, 
    '_ast.Pass': Pass, 
    '_ast.Pow': Pow, 
    '_ast.RShift': RShift, 
    '_ast.Raise': Raise, 
    '_ast.Return': Return, 
    '_ast.Set': Set, 
    '_ast.SetComp': SetComp, 
    '_ast.Slice': Slice, 
    '_ast.Starred': Starred, 
    '_ast.Store': Store, 
    'ast.Str': Str, 
    '_ast.Sub': Sub, 
    '_ast.Subscript': Subscript, 
    '_ast.Suite': Suite, 
    '_ast.Try': Try, 
    '_ast.Tuple': Tuple, 
    '_ast.TypeIgnore': TypeIgnore, 
    '_ast.UAdd': UAdd, 
    '_ast.USub': USub, 
    '_ast.UnaryOp': UnaryOp, 
    '_ast.While': While, 
    '_ast.With': With, 
    '_ast.Yield': Yield, 
    '_ast.YieldFrom': YieldFrom, 
    'ast._ABC': _ABC, 
    '_ast.alias': alias, 
    '_ast.arg': arg, 
    '_ast.arguments': arguments, 
    '_ast.boolop': boolop, 
    '_ast.cmpop': cmpop, 
    '_ast.comprehension': comprehension, 
    '_ast.excepthandler': excepthandler, 
    '_ast.expr': expr, 
    '_ast.expr_context': expr_context, 
    '_ast.keyword': keyword, 
    '_ast.mod': mod, 
    '_ast.operator': operator, 
    '_ast.slice': slice, 
    '_ast.stmt': stmt, 
    '_ast.type_ignore': type_ignore, 
    '_ast.unaryop': unaryop, 
    '_ast.withitem': withitem
}