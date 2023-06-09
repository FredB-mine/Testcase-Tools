# encoding: utf-8

# version 2 Config Template
from cyaron import *         # cyaron
from libs.glib import ToolSet   # ToolSet

# Constant Definitions
version = '2.0.0'
std_name = 'std.cpp'
data_set = 10

# Experimental Function
no_gen = False
genOut = False  # Generate Output in Gen.generator


# Gen class
class Gen:
    class static:
        pass

    class functions:
        pass

    # gen.generator:
    #  param: data_group -> which data is being generated
    #  directly write input data to io
    #  See https://github.com/luogu-dev/cyaron/wiki/输入输出-IO
    @staticmethod
    def generator(data_group: int, io: IO) -> None:
        # A+B problem, generate two integers in range of int
        a = randint(ToolSet.INT_MIN, ToolSet.INT_MAX)
        b = randint(ToolSet.INT_MIN, ToolSet.INT_MAX)
        io.input_writeln(a, b)
