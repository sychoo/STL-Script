
# 2020-11-06 08:00:03

from sys import stdout, path
# path.append("..") # Adds higher directory to python modules path.

from stl.tools import String_Builder, Tools
from stl.AST_Collection.core_AST import Val
from stl.val_types import List_Type

# val implementation

class Primitive_Val(Val):
    """super class for values, store primitive value types"""
    
    def __eq__(self, rhs):
        # this check is necessary because the program seems to pass None sometimes for rhs
        if rhs != None:

            # greater or equal to
            result = None

            if self.value == rhs.value:
                result = Boolean_Val("true")
            else:
                result = Boolean_Val("false")

        else:
            result = Boolean_Val("false")
            
        return result 
    
    def __ne__(self, rhs):
        # debug
        # this check is necessary because the program seems to pass None sometimes for rhs
        # print(str(rhs) + str(type(rhs)))
        if rhs != None:

            # greater or equal to
            result = None

            if self.value != rhs.value:
                result = Boolean_Val("true")
            else:
                result = Boolean_Val("false")

        else:
            # if rhs is None, return true since they are not equal
            result = Boolean_Val("true")
        
        return result
    
    def to_py_obj(self):
        # convert to python object
        return self.value
# /top-level classes


class Int_Val(Primitive_Val):
    # python operator overload
    # https://www.geeksforgeeks.org/operator-overloading-in-python/
    def __init__(self, value, value_type="INT"):
        # cast to Python integer type
        self.value = int(value)
        self.value_type = value_type

    def __neg__(self):
        # unary minus for Int_Val
        result = Int_Val(-self.value)
        return result 

    def __add__(self, rhs):
        """return Int_Val class type. Type signature not hardcoded for future modification"""
        # assume rhs is also a Int_Val type
        result = Int_Val(self.value + rhs.value,  self.value_type)
        return result

    def __sub__(self, rhs):
        result = Int_Val(self.value - rhs.value,  self.value_type)
        return result

    def __mul__(self, rhs):
        result = Int_Val(self.value * rhs.value,  self.value_type)
        return result

    def __truediv__(self, rhs):
        # note that integer division will return integer
        result = Int_Val(self.value // rhs.value,  self.value_type)
        return result

    def __ge__(self, rhs):
        # greater or equal to
        result = None

        if self.value >= rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")


        return result

    def __gt__(self, rhs):
        # greater or equal to
        result = None

        if self.value > rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result  

    def __le__(self, rhs):
        # greater or equal to
        result = None

        if self.value <= rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result 
    
    def __lt__(self, rhs):
        # greater or equal to
        result = None

        if self.value < rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result 
    



    # def typecheck(self, type_context):
        # pass

    # def eval(self, eval_context):
    #     pass

class Float_Val(Primitive_Val):
    def __init__(self, value, value_type="FLOAT"):
        # cast to Python float type
        self.value = float(value)
        self.value_type = value_type

    def __neg__(self):
        # unary minus for Float_Val
        result = Float_Val(-self.value)
        return result 

    def __add__(self, rhs):
        """return Float_Val class type. Type signature not hardcoded for future modification"""
        # assume rhs is also a Float_Val type
        result = Float_Val(self.value + rhs.value,  self.value_type)
        return result

    def __sub__(self, rhs):
        result = Float_Val(self.value - rhs.value,  self.value_type)
        return result

    def __mul__(self, rhs):
        result = Float_Val(self.value * rhs.value,  self.value_type)
        return result

    def __truediv__(self, rhs):
        # note that integer division will return integer
        result = Float_Val(self.value / rhs.value,  self.value_type)
        return result

    def __ge__(self, rhs):
        # greater or equal to
        result = None

        if self.value >= rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result

    def __gt__(self, rhs):
        # greater or equal to
        result = None

        if self.value > rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result  

    def __le__(self, rhs):
        # greater or equal to
        result = None

        if self.value <= rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result 
    
    def __lt__(self, rhs):
        # greater or equal to
        result = None

        if self.value < rhs.value:
            result = Boolean_Val("true")
        else:
            result = Boolean_Val("false")

        return result 
    
    # def typecheck(self, type_context):
    #     pass

    # def eval(self, eval_context):
    #     pass


class String_Val(Primitive_Val):
    """note that string has already been converted to internal Python type"""

    def to_str(self):
        """override to_str method in Val class
        get rid of the double quotes for the string
        """
        return self.value[1:-1]
    # def typecheck(self, type_context):
    #     pass

    # def eval(self, eval_context):
    #     pass


class Boolean_Val(Primitive_Val):
    def __init__(self, value, value_type="BOOLEAN"):
        # convert boolean value to internal type
        self.value = Tools.str_to_bool(value)
        self.value_type = value_type

    def to_str(self):
        return Tools.bool_to_str(self.value)

    def logical_and(self, rhs):
        # short-circuit evaluation
        return Boolean_Val(Tools.bool_to_str(self.value and rhs.value))

    def logical_or(self, rhs):
        return Boolean_Val(Tools.bool_to_str(self.value or rhs.value))
    
    def logical_implies(self, rhs):
        return Boolean_Val(Tools.bool_to_str((not self.value) or rhs.value))

    def logical_not(self):
        return Boolean_Val(Tools.bool_to_str(not self.value))

    @staticmethod
    def logical_and_list(boolean_val_list):
        # set the result to true by default
        result = Boolean_Val("true")

        # loop through the boolean value list and calculate the logical and value
        for boolean_val in boolean_val_list:
            result = boolean_val.logical_and(result)

            # short circuit for the multiple logical and connectives
            if result == Boolean_Val("false"):
                return result

        return result

    # def typecheck(self, type_context):
    #     pass

    # def eval(self, eval_context):
    #     pass

    # def __str__(self):
        # """override parent class Val's method due to discrepancy"""

class Id_Val(Val):
    """stores identifier of the variable, variable expression
    stores 
            type signature
            variable identifier signature
            and STL formula operator
    """

    def __init__(self, var_id):
        """take the identifier name of the variable"""
        self.var_id = var_id

    def __str__(self):
        sb = String_Builder()
        sb.append("Id_Val: ( ")
        sb.append(self.var_id)
        sb.append(" )")

        return str(sb)

    def get_id(self):
        return self.var_id

    def eval(self, eval_context):
        return eval_context.lookup(self)

    
    def typecheck(self, type_context):
        result = type_context.lookup(self)
        # print(result)
        # print(type(result))
        return result


class Meta_Id_Val(Val):
    """stores identifier of the variable, variable expression
    stores 
            type signature
            variable identifier signature
            and STL formula operator
    """

    def __init__(self, var_id):
        """take the identifier name of the variable"""
        self.var_id = var_id

    def __str__(self):
        sb = String_Builder()
        sb.append("Meta_Id_Val: ( ")
        sb.append(self.var_id)
        sb.append(" )")

        return str(sb)

    def get_id(self):
        return self.var_id

    def eval(self, eval_context):
        """eval function for Meta_Identifier will generate a list of evaluations for further comparisons for relational operators"""
        #debugger

        # next step:
        # for each binary/unary comparison, logic, arithmetic operations, 
        # add comparison of [] list, which will check whether all list of values satisfies the condition
        # evalute a meta identifier
        # $1.content -> {"param" : param}
        # return a list of values?


        # self.var_id : meta variable's name, i.e. $param
        # lookup_value_list = list()

        # context_var_ids = eval_context.get_current_conext_var_id()

        # loop through all the variable ids
        # for var_id in context_var_ids:
        
        # list for accumulating the overall value
        value_list = list()

        # look for the valid signal dictionary in the evaluation context
        # this will look something like {"1": {"content": {}}, "2": {"content": {}}, ... }
        valid_signal_dict = eval_context.lookup(Meta_Id_Val("$this")).get_signal_dict()

        
        # get rid of the "$" - dollar sign at the beginning
        self.var_id = self.var_id[1:]

        # parse the self.var_id - the variable name for the current meta variable
        splited_var_id_list = self.var_id.split(".")

        # look up the concrete variable in the signal dictionary
        for time_index in valid_signal_dict.keys():
            valid_signal_dict_content = valid_signal_dict[time_index]["content"]
            
            # recursively look up the splited var id until reaching the right level
            for splited_var_id in splited_var_id_list:
                valid_signal_dict_content = valid_signal_dict_content[splited_var_id]

            # only allow int -> Int_Val at current stage
            # TODO: array -> Array_Val
            if isinstance(valid_signal_dict_content, int):
                # append the obtained value to the value_list
                value_list.append(Int_Val(valid_signal_dict_content))         

        # signal_content_dict = eval_context.lookup(Meta_Id_Val(var_id))
        # get rid of the $ sign when looking it up in the signal dictionary
        # lookup_value_list.append(signal_content_dict[self.var_id[1:]])
        # return eval_context.lookup(self)
        # print(value_list)

        return value_list

    
    def typecheck(self, type_context):
        # do not require type check, simply pass
        pass


class List_Val(Primitive_Val):

    def __init__(self, expr_list, value_type="LIST"):
        """take the identifier name of the variable"""
        self.expr_list = expr_list
        self.value_type = value_type

    def __str__(self):
        sb = String_Builder()
        sb.append("List_Val: ( ")
        sb.append(str(self.expr_list))
        sb.append(" )")

        return str(sb)

    def eval(self, eval_context):
        return self
    
    def typecheck(self, type_context):
        # type check happens in expr list to ensure homogeneous types
        common_type = self.expr_list.typecheck(type_context, "list")
        return List_Type(common_type)

class Tuple_Val(Primitive_Val):

    def __init__(self, expr_list, value_type="TUPLE"):
        """take the identifier name of the variable"""
        self.expr_list = expr_list
        self.value_type = value_type

    def __str__(self):
        sb = String_Builder()
        sb.append("Tuple_Val: ( ")
        sb.append(str(self.expr_list))
        sb.append(" )")

        return str(sb)

    def eval(self, eval_context):
        return self
    
    def typecheck(self, type_context):
        # type check happens in expr list to ensure type correctness in tuple
        self.expr_list.typecheck(type_context, "tuple")
