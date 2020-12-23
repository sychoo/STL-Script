# struct.py
# Tue 2020-12-01 15:36:40 EST
# contains language constructs of the language

from sys import stdout, path
# path.append("..") # Adds higher directory to python modules path.


from stl.AST_Collection.core_AST import Expr

import stl.exceptions as exceptions

class Invocation(Expr):
    """
    handles function invocation
    """
    def __init__(self, lhs_expr, func_invoked):
        self.lhs_expr = lhs_expr
        self.func_invoked = func_invoked

    def typecheck(self, type_context):
        self.lhs_expr.typecheck(type_context)

    def eval(self, eval_context):
        self.lhs_expr = self.lhs_expr.eval(eval_context)
        result = self.lhs_expr.invoke(self.func_invoked)
        return result

    def __str__(self):
        pass


class Expr_List(Expr):
    """
    not sure if it make sense to make it a subtype of Expr
    """
    def __init__(self, expr_list):
        # note that this expr_list is the raw format
        self.expr_list = expr_list

    def get_expr_list(self):
        return self.expr_list

    def typecheck(self, type_context, check_type="tuple"):
        common_type = None

        # by default, use weaker type check (for tuple)
        if check_type == "tuple":
            # when type is tuple, check all expression individually
            for expr in self.expr_list:
                expr.typecheck(type_context)

        elif check_type == "list":
            # when the type is list, make sure all expressions has homogenous types
            
            for expr in self.expr_list:
                curr_expr_type = expr.typecheck(type_context)
                if common_type == None:
                    common_type = curr_expr_type
                elif common_type != curr_expr_type:
                    raise exceptions.Type_Error("List consists of elements of different types")

        return common_type

    def eval(self, eval_context):
        self.lhs_expr = self.lhs_expr.eval(eval_context)
        result = self.lhs_expr.invoke(self.func_invoked)
        return result

    def __str__(self):
        pass

