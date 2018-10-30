grammar Aritmetica;

program:
    (statement)+
    ;

statement:
      expression                
    | assignStatement  
    | VARNAME                   
    | booleanExpression          
    | ifStatement
    | whileStatement
    | setNumber
    | setMathematicsManager
    ;

// Todo lo referido a conjuntos matematicos.
setMathematicsManager:
      getIntersection
    | setMerge
    | setDifference
    | setComplement
    | setBelongs
    | setSum
    | setAverage
    | setLength
    | setPrint
    ;

getIntersection:
    firstSet=VARNAME '.intersection(' secondSet=VARNAME ')';

setNumber:  
    'set['numberStart=NUMBER'..'numberEnd=NUMBER']';

setMerge:
    firstVarName=VARNAME '.merge(' secondVarName=VARNAME ')';

setDifference:
    firstVarName=VARNAME '.return_diff(' secondVarName=VARNAME ')';

setComplement:
    firstVarName=VARNAME '.complement(' secondVarName=VARNAME ')';

setBelongs:
    firstVarName=VARNAME '.includes(' element=NUMBER ')';

setSum:
    firstVarName=VARNAME '.sum()';

setAverage:
    firstVarName=VARNAME '.avg()';

setLength:
    firstVarName=VARNAME '.length()';

setPrint:
    'printf(' firstVarName=VARNAME ')';

assignStatement:
      VARNAME '=' expression
    | VARNAME '=' setMathematicsManager
    | VARNAME '=' setNumber
    ;

ifStatement:
      'if' booleanExpression 
      'then ' (statement)+ 
      ('else ' (statement)+ )?
      'fi'
    ;

whileStatement:
      'while' booleanExpression 'do'
        (statement)+
      'done'
    ;

booleanExpression:
      operand          op=COMPARATION_OPERATOR operand
    | booleanExpression op=AND_OPERATOR booleanExpression
    | booleanExpression op=OR_OPERATOR booleanExpression
    ;

operand:
      expression                 
    | VARNAME                      
    ;

expression: 
      term                      
    | expression '+' term   
    | expression '-' term   
    ;

term:   
      factor                    
    | term '*' factor       
    | term '/' factor       
    ;

factor: 
      n=NUMBER      
    | vn=VARNAME               
    | '(' expression ')'     
    ;


AND_OPERATOR : 'and';
OR_OPERATOR : 'or';
COMPARATION_OPERATOR : '=='|'<='|'>='|'<'|'>'|'!=';

VARNAME : [a-z]+;

NUMBER : DIGIT+;
DIGIT  : [0-9];
WS : [ \r\n\t] -> skip; 