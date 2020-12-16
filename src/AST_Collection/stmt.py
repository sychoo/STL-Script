# stmt.py
# 2020-11-06 07:48:34
# contains core statement of the language

from sys import stdout, path
path.append("..") # Adds higher directory to python modules path.

from src.tools import String_Builder

from src.AST_Collection.core_AST import Stmt
from src.AST_Collection.val import Boolean_Val
import src.exceptions as exceptions

class Block_Stmt(Stmt):
    def __init__(self, stmt_list):
        # print(type(stmt_list))
        self.stmt_list = stmt_list
    
    def __str__(self):
        sb = String_Builder()
        sb.append("Block_Stmt: (\n")
        sb.append(str(self.stmt_list))
        sb.append(")")
        return str(sb)

    def typecheck(self, type_context):
        # TODO: differentiate the scope of the inner context and the outer context
        self.stmt_list.typecheck(type_context)

    def eval(self, eval_context):
        # TODO: differentiate the scope of the inner context and the outer context
        self.stmt_list.eval(eval_context)

class Variable_Decl_Stmt(Stmt):
    def __init__(self, decl_type, var_id_val, var_type, rhs_expr):
        self.decl_type = decl_type
        self.var_id_val = var_id_val
        self.var_type = var_type
        self.rhs_expr = rhs_expr

    def __str__(self):
        sb = String_Builder()
        sb.append("Variable_Decl_Stmt: ( ")
        sb.append(str(self.decl_type))
        sb.append(" ")
        sb.append(str(self.var_id_val))
        sb.append(": ")
        sb.append(str(self.var_type))
        sb.append(" = ")
        sb.append(str(self.rhs_expr))
        sb.append(" )")
        return str(sb)

# stmt implementation
class Val_Decl_Stmt(Variable_Decl_Stmt):
    # do not allow re-assignment for val declaration

    def typecheck(self, type_context):
        self.rhs_expr_type = self.rhs_expr.typecheck(type_context)

        # print(self.rhs_expr_type)
        # print(type(self.rhs_expr_type))

        type_context.add(self.var_id_val, self.rhs_expr_type)

        # print(type_context)
        # print("lookup: " + str(type_context.lookup(self.var_id_val)))

    def eval(self, eval_context):
        # add val_decl attribute
        self.rhs_expr = self.rhs_expr.eval(eval_context)
        eval_context.add(self.var_id_val, self.rhs_expr)



class Var_Decl_Stmt(Variable_Decl_Stmt):

    def typecheck(self, type_context):
        self.rhs_expr_type = self.rhs_expr.typecheck(type_context)
        type_context.add(self.var_id_val, self.rhs_expr_type)


    def eval(self, eval_context):
        # add var_decl attribute
        self.rhs_expr = self.rhs_expr.eval(eval_context)
        eval_context.add(self.var_id_val, self.rhs_expr)


class While_Stmt(Stmt):

    def __init__(self, condition_expr, body_block):
        self.condition_expr = condition_expr
        self.body_block = body_block

    def typecheck(self, type_context):
        self.condition_expr.typecheck(type_context)
        self.body_block.typecheck(type_context)

    def eval(self, eval_context):
        # test whether if the lhs id_expr is assignable (using the context) before the assignment
        # val cannot be reassigned
        while self.condition_expr.eval(eval_context) != Boolean_Val("false"):
            self.body_block.eval(eval_context)

    def __str__(self):
        sb = String_Builder()
        sb.append("While_Stmt: ( ")
        sb.append(str(self.condition_expr))
        sb.append(" ) { ")
        sb.append(str(self.body_block))
        sb.append(" }")

        return str(sb)

class Assign_Stmt(Stmt):

    def __init__(self, var_id_val, rhs_expr):
        self.var_id_expr = var_id_val
        self.rhs_expr = rhs_expr

    def typecheck(self, type_context):
        # bi-directional type check
        self.lhs_expr_type = type_context.lookup(self.var_id_expr)
        self.rhs_expr_type = self.rhs_expr.typecheck(type_context)

        if self.lhs_expr_type != self.rhs_expr_type:
            raise exceptions.Type_Error("Type Mismatch in Assignment Stmt: lhs type = " + str(self.lhs_expr_type) + " rhs type = " + str(self.rhs_expr_type))

        # Note that assignment statement do not return result for the typecheck
        
    def eval(self, eval_context):
        # test whether if the lhs id_expr is assignable (using the context) before the assignment
        # val cannot be reassigned

        self.rhs_expr = self.rhs_expr.eval(eval_context)
        eval_context.add(self.var_id_expr, self.rhs_expr)

    def __str__(self):
        sb = String_Builder()
        sb.append("Assign_Stmt: ( ")
        sb.append(str(self.var_id_expr))
        sb.append(" = ")
        sb.append(str(self.rhs_expr))
        sb.append(" )")

        return str(sb)


class Print_Stmt(Stmt):
    """stores either print or println expression"""

    def __init__(self, expr, token_type):
        self.expr = expr
        self.token_type = token_type

    def typecheck(self, type_context):
        # only type check when the expr is not None
        if self.expr != None:
            self.expr.typecheck(type_context)

    def eval(self, eval_context):
        # evaluate the embedded expression in the print statement (if it is not None)
        # only PRINTLN is allowed None -> to print an empty line
        if self.expr != None:
            
            self.expr = self.expr.eval(eval_context)
            # print("print type: " + str(type(self.expr)))

            if self.token_type == "PRINT":
                stdout.write(self.expr.to_str())
                stdout.flush()

            elif self.token_type == "PRINTLN":
                # print(type(self.expr))
                stdout.write(self.expr.to_str())
                stdout.write("\n")
                stdout.flush()

        else:
            if self.token_type == "PRINTLN":
                stdout.write("\n")
                stdout.flush()

    def __str__(self):
        sb = String_Builder()
        sb.append("Print_Stmt: ( ")
        sb.append(str(self.expr))
        sb.append(", ")
        sb.append(str(self.token_type))
        sb.append(" )")

        return str(sb)

# /stmt implementation