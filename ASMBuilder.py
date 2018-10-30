import re   # Modulo para expresiones regulares

class ASMBuilder():

    def __init__(self):
        self.label_count = 0
        self.regcount = 0

    def assignment(self, name, value):
        reg1 = 'XX' + str(self.regcount)
        self.regcount += 1

        reg2 = 'XX' + str(self.regcount)
        self.regcount += 1

        return '''
            MOV  {}, '{}'
            MOV  {}, {}
            PUT  {}, {} 
        '''.format(reg1, name, reg2, value, reg1, reg2)

    def get(self, varname):
        reg1 = 'XX' + str(self.regcount)
        self.regcount += 1

        reg2 = 'XX' + str(self.regcount)
        self.regcount += 1

        return '''
            MOV {}, '{}'
            GET {}, {}
            '''.format(reg1, varname, reg1, reg2), reg2

    def add(self, value1, value2):
        reg = 'XX' + str(self.regcount)
        self.regcount += 1

        return '''
            MOV  {}, {}
            ADD  {}, {}
        '''.format(reg, value1, reg, value2), reg

    def substract(self, value1, value2):
        return '''
            MOV  AX, {}
            SUB  AX, {}
        '''.format(value1, value2)

    def multiply(self, value1, value2):
        self.label_count += 1

        return '''
                MOV EX, {}
                MOV AX, 0
            lab{}:
                ADD AX, {}

                LOOP lab{}

        '''.format(value1, self.label_count, value2, self.label_count)

    def compare(self, value1, value2):
        return '''
         MOV AX, {}
         MOV BX, {}
         CMP AX, BX
        '''.format(value1, value2)

    def conditional(self):
        pass

    def while_st(self):
        pass
        

    def correct_registers(self, program):
        regex = r"XX[0-9]+"

        reg_stack = ['AX', 'BX', 'CX', 'DX', 'EX', 'FX'][::-1]
        reg_dict = {}
        
        correct_program = []

        for index, line in enumerate(program):      # zip(L1, L2)

            print(line)
            print(reg_stack)
            print(reg_dict)
            print()


            matches = re.search(regex, line)    # Busca en la 'line' las expresiones que cumpla la expresion regular en regex
            while matches != None:
                
                reg_name = line[matches.start() : matches.end()]    # Tomo el nombre del registro ficticio
                reg = reg_dict.get(reg_name)    # Busco si ya esta en el dict
                if reg == None:
                    reg = reg_stack.pop()       # Saco el registro libre
                    reg_dict[reg_name] = reg    # Guardo en el dict el registro artificial y el real
                
                line = line[0:matches.start()] + reg + line[matches.end():]

                matches = re.search(regex, line)

                i = index + 1
                while i < len(program) and not reg_name in program[i] :   # Lo ideal seria desde donde se esta procesando hacia abajo
                    i += 1

                if i >= len(program):
                    reg_stack.append(reg_dict[reg_name])
                    reg_dict.pop(reg_name)

            correct_program.append(line)
            

        return correct_program