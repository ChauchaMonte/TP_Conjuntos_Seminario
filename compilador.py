from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from AritmeticaLexer import AritmeticaLexer
from AritmeticaParser import AritmeticaParser
from AritmeticaListener import AritmeticaListener
import antlr4
from ASMBuilder import ASMBuilder

class RealListener(AritmeticaListener):
    
    def __init__(self):
        self.step = 0
        self.variables = {}

        self.builder = ASMBuilder()
        self.asm_program = []

        self.stack = []
        


    def enterProgram(self, ctx:AritmeticaParser.ProgramContext):
        for node in ctx.children:
            self.visitStatement(node)


    def exitProgram(self, ctx:AritmeticaParser.ProgramContext):
        program = []
        for instruction in self.asm_program:
            for line in instruction.split('\n'):
                if line.strip() != '':
                    program.append(line)

        correct_program = self.builder.correct_registers(program)

        for line in correct_program:
            print('-'  + line)
        


    def visitStatement(self, ctx:AritmeticaParser.StatementContext):
        print(str(self.step) + "visitStatement")
        self.step += 1

        for node in ctx.children:
            if type(node) == AritmeticaParser.ExpressionContext:
                result = self.visitExpression(node)
                print(result)
            
            elif type(node) == AritmeticaParser.AssignStatementContext:
                self.visitAssignStatement(node)

            elif type(node) == antlr4.tree.Tree.TerminalNodeImpl:   # VARNAME
                result = self.variables[node.symbol.text]
                print(node.symbol.text + ' = ' + str(result))

            elif type(node) == AritmeticaParser.BooleanExpressionContext:
                result = self.visitBooleanExpresion(node)
                print(result)

            elif type(node) == AritmeticaParser.IfStatementContext:
                condition = self.visitBooleanExpresion(node.children[1])
                if condition:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        self.visitStatement(node.children[i])
                        i += 1
                else:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        i += 1
                        # sale del while cuando encuentra el ELSE
                    
                    i += 1      # Para saltear el ELSE
                    while i < len(node.children) - 1:
                        self.visitStatement(node.children[i])
                        i += 1

            elif type(node) == AritmeticaParser.SetNumberContext:
                self.visitSetNumber(node)

            elif type(node) == AritmeticaParser.WhileStatementContext:
                self.visitWhileStatement(node)
            
            # Hay una solicitud del tipo conjuntos matematicos.
            elif type(node) == AritmeticaParser.SetMathematicsManagerContext:
                # La envio al metodo correspondiente.
                self.setVisitSetMathematicsManager(node)

    # Destinado a gestionar todo lo referido a los conjuntos matematicos.
    def setVisitSetMathematicsManager(self,ctx:AritmeticaParser.SetMathematicsManagerContext):
        # Interseccion.
        if type(ctx.children[0]) == AritmeticaParser.GetIntersectionContext:
            return self.setVisitGetIntersection(ctx.children[0])

        # Union.
        elif type(ctx.children[0]) == AritmeticaParser.SetMergeContext:
            return self.setVisitMerge(ctx.children[0])

        # Diferencia.
        elif type(ctx.children[0]) == AritmeticaParser.SetDifferenceContext:
            return self.setVisitDifference(ctx.children[0])

        # Complemento.
        elif type(ctx.children[0]) == AritmeticaParser.SetComplementContext:
            return self.setVisitComplement(ctx.children[0])
        
        # Pertenece.
        elif type(ctx.children[0]) == AritmeticaParser.SetBelongsContext:
            return self.setVisitBelongs(ctx.children[0])
        
        # Suma.
        elif type(ctx.children[0]) == AritmeticaParser.SetSumContext:
            return self.setVisitSum(ctx.children[0])
        
        # Promedio.
        elif type(ctx.children[0]) == AritmeticaParser.SetAverageContext:
            return self.setVisitAverage(ctx.children[0])
        
        # Longitud.
        elif type(ctx.children[0]) == AritmeticaParser.SetLengthContext:
            return self.setVisitLength(ctx.children[0])
        
        # Realizo el Print.
        elif type(ctx.children[0]) == AritmeticaParser.SetPrintContext:
            # La envio al metodo correspondiente.
            return self.setVisitPrintContext(ctx.children[0])

    
    # Retorna una lista con los elementos que pertenecen a ambos conjuntos.
    def setVisitGetIntersection(self,ctx:AritmeticaParser.GetIntersectionContext):
        # Muestro los elementos de cada conjunto.
        print("Elementos de cada conjunto")
        print(str(set(self.variables[ctx.firstSet.text]))+"  "+str(set(self.variables[ctx.secondSet.text])) )

        # Muestro los elementos que coinciden de los conjuntos.
        print("Resuelve la interseccion")
        print(str(list(set(self.variables[ctx.firstSet.text]) & set(self.variables[ctx.secondSet.text]))))
        
        # Retorno directamente los elementos que coinciden.
        return list(set(self.variables[ctx.firstSet.text]) & set(self.variables[ctx.secondSet.text]))
    
    # Retorna una lista de elementos de ambos conjunto.
    def setVisitMerge(self,ctx:AritmeticaParser.SetMergeContext):
        # Muestro los elementos de cada conjunto.
        print("Elementos de cada conjunto")
        print(str(set(self.variables[ctx.firstVarName.text]))+"  "+str(set(self.variables[ctx.secondVarName.text])) )
        
        # Muestro los elementos unidos.
        print("Resuelve la union")
        print(str(list(set(self.variables[ctx.firstVarName.text]).union(self.variables[ctx.secondVarName.text]))))

        # Retorno directamente la lista con todos los elementos.
        return list(set(self.variables[ctx.firstVarName.text]).union(self.variables[ctx.secondVarName.text]))

    # Metodo que retorna la lista de elementos diferentes.
    def setVisitDifference(self,ctx:AritmeticaParser.SetDifferenceContext):
        # Muestro los elementos de cada conjunto.
        print("Elementos de cada conjunto")
        print(str(set(self.variables[ctx.firstVarName.text]))+"  "+str(set(self.variables[ctx.secondVarName.text])) )
        
        # Muestro los elemento que quedan pos diferencia.
        print("Resuelvo la diferencia")
        print(str(list(set(self.variables[ctx.firstVarName.text]).symmetric_difference(set(self.variables[ctx.secondVarName.text])))))

        # Retorno directamente la lista con los elementos diferentes.
        return list(set(self.variables[ctx.firstVarName.text]).symmetric_difference(set(self.variables[ctx.secondVarName.text])))

    # Metodo que retorna la lista de elementos del complemento.
    def setVisitComplement(self,ctx:AritmeticaParser.SetComplementContext):
        # Muestro los elementos de cada conjunto.
        print("Elementos de cada conjunto")
        print(str(set(self.variables[ctx.firstVarName.text]))+"  "+str(set(self.variables[ctx.secondVarName.text])) )
        
        # Muestro los elemento que quedan pos complemento.
        print("Resuelve el complemento")
        print(str(list(set(self.variables[ctx.firstVarName.text]) - set(self.variables[ctx.secondVarName.text]))))

        # Retorno los elementos resultantes del complemento
        return list(set(self.variables[ctx.firstVarName.text]) - set(self.variables[ctx.secondVarName.text]))
   
    # Metodo que retorna si pertenece el elemento a un conjunto.
    def setVisitBelongs(self,ctx:AritmeticaParser.SetBelongsContext):
        # Muestro los elementos del conjunto mas el elemento buscado.
        print("Elementos del conjunto")
        print(str(set(self.variables[ctx.firstVarName.text]))+" Elemento buscado: "+ctx.element.text)

        # Muestro si existe el elemento en el conjunto.
        print("Muestro si existe el elemento en el conjunto")
        if (int(ctx.element.text) in (self.variables[ctx.firstVarName.text])):
            print("Existe")
        else:
            print("No existe")

        # Realizo la busqueda del elemento.
        print("Resuelvo la busqueda del elemento")
        if (int(ctx.element.text) in (self.variables[ctx.firstVarName.text])):
            return True
        return False
    
    # Metodo que retorna la suma completa de los elementos de un conjunto.
    def setVisitSum(self,ctx:AritmeticaParser.SetSumContext):
        # Muestro los elementos del conjunto.
        print("Elementos del conjunto")
        print(str(set(self.variables[ctx.firstVarName.text])))

        # Muestro el resultado de la suma.
        print("Resultado de la suma")
        print(sum(set(self.variables[ctx.firstVarName.text])))        
        
        # Resuelvo la suma.
        print("Resuelvo la suma")
        return (sum(set(self.variables[ctx.firstVarName.text])))

    # Metodo que retorna el promedio de los elementos del conjunto.
    def setVisitAverage(self,ctx:AritmeticaParser.SetAverageContext):
        # Muestro los elementos del conjunto.
        print("Elementos del conjunto")
        print(str(set(self.variables[ctx.firstVarName.text])))

        # Muestro la cantidad de elementos del conjunto, la suma de sus elementos y el promedio.
        print("Cantidad de elementos: "+ str(len((self.variables[ctx.firstVarName.text]))))
        print("Suma de los elementos: "+ str(sum((self.variables[ctx.firstVarName.text]))))
        print("Promedio: "+str(sum(set(self.variables[ctx.firstVarName.text]))/len(set(self.variables[ctx.firstVarName.text]))))
        
        # Resuelvo el promedio.
        print("Resuelvo el promedio")
        return (sum(set(self.variables[ctx.firstVarName.text]))/len(set(self.variables[ctx.firstVarName.text])))

    # Metodo que retorna la longitud del conjunto.
    def setVisitLength(self,ctx:AritmeticaParser.SetLengthContext):
        # Muestro los elementos del conjunto.
        print("Elementos del conjunto")
        print(str(set(self.variables[ctx.firstVarName.text])))
        
        # Muestro la cantidad de elementos del conjunto.
        print("Cantidad de elementos: "+ str(len((self.variables[ctx.firstVarName.text]))))
        
        # Resuelvo la longitud del conjunto.
        print("Resuelvo longitud")
        return (len(set(self.variables[ctx.firstVarName.text])))
        
    # Metodo que retorna un Print del conjunto.
    def setVisitPrintContext(self,ctx:AritmeticaParser.SetPrintContext):
        # Muestro los elementos del conjunto.
        print("Elementos del conjunto")
        print(str(set(self.variables[ctx.firstVarName.text])))

        # Resuelvo Print.
        print("Resuelvo Print")
        return(print(str(set(self.variables[ctx.firstVarName.text]))))
        
    def visitWhileStatement(self, ctx:AritmeticaParser.WhileStatementContext):
        print(str(self.step) + "visitWhileStatement")
        self.step += 1

        while self.visitBooleanExpresion(ctx.children[1]):
            print('en el while!!!')
            i = 3
            while i < len(ctx.children) - 1 and type(ctx.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                self.visitStatement(ctx.children[i])
                i += 1

    def visitIfStatement(self, ctx:AritmeticaParser.IfStatementContext):
        print(str(self.step) + "visitIfStatement")
        self.step += 1
        pass

    # Ok
    def visitBooleanExpresion(self, ctx:AritmeticaParser.BooleanExpressionContext):
        print(str(self.step) + "visitBooleanExpression")
        self.step += 1

        if ctx.op.text == 'and':
            be_left = self.visitBooleanExpresion(ctx.children[0])
            be_right = self.visitBooleanExpresion(ctx.children[2])
            return be_left and be_right

        if ctx.op.text == 'or':
            be_left = self.visitBooleanExpresion(ctx.children[0])
            be_right = self.visitBooleanExpresion(ctx.children[2])
            return be_left or be_right

        left =  self.visitOperand(ctx.children[0])
        right = self.visitOperand(ctx.children[2])
        op = ctx.children[1].symbol.text


        self.asm_program.append(self.builder.compare(left, right))


        return eval(str(left) + op + str(right))

    # Ok
    def visitOperand(self, ctx:AritmeticaParser.OperandContext):
        print(str(self.step) + "visitOperand")
        self.step += 1

        node = ctx.children[0]
        if type(node) == AritmeticaParser.ExpressionContext:
            return self.visitExpression(node)

        if type(node) == antlr4.tree.Tree.TerminalNodeImpl:
            return self.variables[node.symbol.text]
        
        return ''   # No deberia pasar

    # 
    def visitAssignStatement(self, ctx:AritmeticaParser.AssignStatementContext):
        print(str(self.step) + "visitAssignStatement")
        self.step += 1

        name = ctx.children[0].symbol.text

        #self.asm_program.append(self.builder.assignment(name, value))

        if type(ctx.children[2]) == AritmeticaParser.SetMathematicsManagerContext:
            value = self.setVisitSetMathematicsManager(ctx.children[2])
            print("SetMathematicsManagerContext")

        elif type(ctx.children[2]) == AritmeticaParser.SetNumberContext:
            value = self.visitSetNumber(ctx.children[2])
            print("SetNumberContext")

        elif type(ctx.children[2]) == AritmeticaParser.ExpressionContext:
            value = self.visitExpression(ctx.children[2])
            print("ExpressionContext")
            
        self.variables[name] = value


    # Ok
    def visitExpression(self, ctx:AritmeticaParser.ExpressionContext):
        print(str(self.step) + "visitExpression")
        self.step += 1

        if type(ctx.children[0]) == AritmeticaParser.TermContext:
            # Es un Term
            return self.visitTerm(ctx.children[0])
        
        # Es una Expression + - Term
        value1 = self.visitExpression(ctx.children[0])
        value2 = self.visitTerm(ctx.children[2])

        # Construir ASM suma
        if ctx.children[1].symbol.text == '-':
            asm, reg = self.builder.substract(value1, value2)
            self.asm_program.append(asm)
        else:
            asm, reg = self.builder.add(value1, value2)
            self.asm_program.append(asm)

        return reg

    # Ok
    def visitTerm(self, ctx:AritmeticaParser.TermContext):
        print(str(self.step) + "visitTerm")
        self.step += 1

        if type(ctx.children[0]) == AritmeticaParser.FactorContext:
            # Es un factor
            return self.visitFactor(ctx.children[0])

        # Es un term * / factor
        value1 = self.visitTerm(ctx.children[0])
        value2 = self.visitFactor(ctx.children[2])

        if ctx.children[1].symbol.text == '*':
            self.asm_program.append(self.builder.multiply(value1, value2))
            
            return value1 * value2

        return value1 / value2

    def visitSetNumber(self, ctx:AritmeticaParser.SetNumberContext):
        
        # Variable que guarda el conjunto de numeros.
        elements = []

        # Agrego al arreglo de elementos los valores que se encuentran entre los rangos indicados de start y end.
        for i in range(int(ctx.numberStart.text), int(ctx.numberEnd.text) + 1):
            elements.append(i)
        
        # Muestro el conjunto que almacene.
        for i,val in enumerate(elements):
            print("[{}] = {}".format(i,val))
        
        return elements


    # Ok
    def visitFactor(self, ctx:AritmeticaParser.FactorContext):
        print(str(self.step) + "visitFactor")
        self.step += 1

        if ctx.n != None:
            return int(ctx.n.text)          # Es un numero, esta bien

        if ctx.vn != None:

            asm, reg = self.builder.get(ctx.vn.text)           # GET XX1, XX2
            self.asm_program.append(asm)

            return reg
            
        if ctx.children[0].symbol.text != '(':
            nodo = ctx.children[0]
            return int(nodo.symbol.text)

        return self.visitExpression(ctx.children[1])
        

def program1():
    '''
    MOV  AX, 'a'
    MOV  BX, 46
    PUT  AX, BX 
    '''
    return "a = 46\n"


def program2():
    '''
    MOV  AX, 46
    ADD  AX, 2
    '''
    return "46 + 2\n"


def program3():
    '''
    MOV  AX, 46
    ADD  AX, 2
    '''
    return "46 + 2 * 4\n"


def program4():
    '''
    MOV AX, 34
    MOV BX, 12
    CMP AX, BX
    '''
    return "34 == 12"

def program5():
    return "a = 3 + 1"

def program6():
    return "a = 3 + 1 \n b = 45 + 8"


def program7():
    return '''a = 3 + 1 \n 
              b = 45 + a  '''

# Metodo que muestra el funcionamiento de una interseccion.
def program8():
    return '''
            a=set[1..6] \n
            b=set[5..10] \n
            b.intersection(a)
            '''
# Metodo que muestra el funcionamiento de la union.
def program9():
    return '''
            a=set[1..6] \n
            b=set[5..10] \n
            a.merge(b)
            '''

# Metodo que muestra el funcionamiento del complemento.
def program10():
    return '''
            a=set[1..6] \n
            b=set[5..10] \n
            b.complement(a)
            '''

# Metodo que muestra el funcionamiento de la diferencia.
def program11():
    return '''
            a=set[1..6] \n
            b=set[5..10] \n
            a.return_diff(b)
            '''

# Metodo que muestra el funcionamiento si pertenece o no un elemento a un conjunto.
def program12():
    return '''
            a=set[1..6] \n
            a.includes(5)
            '''

# Metodo que muestra el funcionamiento de la suma.
def program13():
    return '''
            a=set[1..10] \n
            a.sum()
            '''

# Metodo que muestra el funcionamiento del promedio.
def program14():
    return '''
            a=set[1..10] \n
            a.avg()
            '''

# Metodo que muestra el funcionamiento de la longitud del conjunto.
def program15():
    return '''
            a=set[1..10] \n
            a.length()
            '''

# Metodo que muestra el funcionamiento del print.
def program16():
    return '''
            a=set[1..10] \n
            printf(a)
            '''

def main():
    # Llamar el metodo que corresponda.
    program = program16()

    input = InputStream(program)
    lexer = AritmeticaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AritmeticaParser(stream)

    tree = parser.program()
    
    listener = RealListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 

if __name__ == '__main__':
    main()