#
#   shape class for mcUI
#
#   document for shape is docs/shape.md

class shape(shape_func):

#
#
#   Those functions are hardly under development.
#   Additionally, definition isn't definded yet.
#   Please keep it in mind
#
#

    def default_Rectangular:
       blocks = [ [10,5,10] ] # rectangular of 10x5x10  blocks

    def folder:
       blocks = [ [10,4,1],[]]


    def __init__(self,shapeName): # This method should be the last.
        shapeData = eval(shapeName)()  # eval() execute passed text as method

        if shapeData is None: # if not definded shape was called
            return None # return None to tell it failed
        elif                    # if shape was found,
            return shapeData 
