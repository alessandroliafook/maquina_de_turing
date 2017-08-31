from machine.machine import Machine

'''
                            --- Tests for the machine ---
    The lines of the configuration file for the machine must be in the following order:
        '<current state> <current symbol> <new symbol> <direction> <new state>'
    
    Obs: The machine halts when it reaches any state starting with 'halt'.
         '*' can be used as a wildcard in <current symbol> or <current state> to match any character or state.
         '*' can be used in <new symbol> or <new state> to mean 'no change'.        
    
    
        Example:    0 0 _ r 1o
                    0 1 _ r 1i
                    ...
                    accept * : r accept2
                    accept2 * ) * halt-accept
                    ...
                        
    Write the tests for the machine here according to the following syntax:
        m = Machine()
        m.load_program(PATH...)
        m.insert_tape(TAPE STRING...)
        m.run()
                                
'''


'''
#palindrome_detector - OK
machine = Machine()
machine.load_program("./tests/palindrome_detector.in")
machine.insert_tape("1001")
machine.run()
'''

#Binary addiction - OK
machine = Machine()
machine.load_program("./tests/binary_addiction.in")
machine.insert_tape("10 10")
machine.run()


'''
#Binary Multiplication - OK
machine = Machine()
machine.load_program("./tests/binary_multiplication.in")
machine.insert_tape("100 10")
machine.run()
'''

'''
#Binary to Decimal Convertion - OK
machine = Machine()
machine.load_program("./tests/binary_to_decimal_conversion.in")
machine.insert_tape("10")
machine.run()
'''

'''
#Turing sequence machine - OK
machine = Machine()
machine.load_program("./tests/turings_sequence_machine.in")
machine.insert_tape("")
machine.run()
'''

'''
#Parentheses checker - OK
machine = Machine()
machine.load_program("./tests/parentheses_checker.in")
machine.insert_tape("12(2+(3^(4-1)))")
machine.run()
'''

'''
#Reverse Polish Boolean - OK
machine = Machine()
machine.load_program("./tests/reverse_polish_boolean.in")
machine.insert_tape("10~1&|0|")
machine.run()
'''

'''
#Primality Test - OK
machine = Machine()
machine.load_program("./tests/primality_test.in")
machine.insert_tape("11")
machine.run()
'''

'''
#4-State busy beaver  - ??
machine = Machine()
machine.load_program("./tests/4_state_busy_beaver.in")
machine.insert_tape("")
machine.run()
'''

'''
#Universal Turing Machine - OK
machine = Machine()
machine.load_program("./tests/universal_turing_machine.in")
machine.insert_tape("[ L+,0R.,1R.!1L+,1L+,0L.:,0L.,1L.:]1011")
machine.run()
'''
