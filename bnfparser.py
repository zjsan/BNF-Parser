"""
    A Python program that can parse and validate simple arithmetic expressions adhering to the provided BNF grammar below:
    
    <expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
    <term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
    <factor> ::= <number> | "(" <expression> ")"
    <number> ::= <digit> | <digit> <number>
    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

    -This progam used the concept of recursive descent parser for the parsing of expressions


ZAINAL JUMAINE D. SANTOS
BSCS 4A

"""


class BNF:

    def __init__(self,string):
        self.string = string
        self.current_pointer = 0
        char = self.string[self.current_pointer]
       # print(char)
       # print(self.current_pointer)
      #  print(self.string)
        self.expression()


    #this function is responsible for the checking of individual characters in the provided expression
    def match(self,char):

        #if the pointer is on the end of the string the program will now stop
        if(self.current_pointer >= len(self.string)):
            return False
        
        elif(self.string[self.current_pointer] == char):
            self.current_pointer += 1
            #print(self.current_pointer)
            return True
        else:
            return False

    
    '''expression function following the given production rule:
    <expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term> '''
    def expression(self):
        if(self.term()):
            return True
        else:
            if(self.match("+")):
                if(self.term()):
                    return True
                else:
                    return False
            else:
                if(self.match("-")):
                    if(self.term()):
                        return True
                    else:
                        return False
    
    
    '''Term function following the given production rule:
    <term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>'''  
    def term(self):
        if(self.factor()):
            return True
        else:
            if(self.match("*")):
                if(self.factor()):
                    return True
                else:
                    return False
            else:
                if(self.match("/")):
                    if(self.factor()):
                        return True
                    else:
                        return False

            
    '''factor function following the given production rule:
    <factor> ::= <number> | "(" <expression> ")"
    '''       
    def factor(self):
        if(self.number()):
            return True 
        else:
            if(self.match("(")):
                if(self.expression()):
                    if(self.match(")")):
                        return True
                    else:
                        return False
                else:
                    return False 
            else:
                return False 


    '''Number function following the production rule:
    <number> ::= <digit> | <digit> <number>
    '''   

    def number(self):
        if(self.digit()):
            return True 
        else:
          if(self.digit()):
              if(self.number()):
                  return True
              else:
                  return False
          else:
              return False      
               

    
    '''digit function following the production rule:
    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9'''

    def digit(self):

        if(self.match("0")):
            return True
        elif(self.match("1")):
            return True
        elif(self.match("2")):
            return True
        elif(self.match("3")):
            return True
        elif(self.match("4")):
            return True
        elif(self.match("5")):
            return True
        elif(self.match("6")):
            return True
        elif(self.match("7")):
            return True
        elif(self.match("8")):
            return True
        elif(self.match("9")):
            return True
        else:
            return False


def main():

    exp_to_parse = str(input("Enter expression: "))
    #print(type(exp_to_parse))
    new_exp = exp_to_parse.replace(" ","")
    #print(type(new_exp))
   # print(new_exp)
    
    parsing_exp = BNF(new_exp)

    if parsing_exp.expression():
        print("Valid")
    else:
        print("Not Valid")

if __name__ == "__main__":
    main()