# noinspection PyUnresolvedReferences
from machine import Machine

'''
#palindrome_detector - OK
machine = Machine()
machine.upload_states_by_archive("../tests/palindrome_detector.in")
machine.insert_tape("1001001001001001")
machine.run()
'''
'''
#Binary addiction - OK
machine = Machine()
machine.upload_states_by_archive("../tests/binary_addiction.in")
machine.insert_tape("10 10")
machine.run()
'''
'''
#Binary Multiplication - OK
machine = Machine()
machine.upload_states_by_archive("../tests/binary_multiplication.in")
machine.insert_tape("100 10")
machine.run()
'''

'''
#Binary to Decimal Convertion - OK
machine = Machine()
machine.upload_states_by_archive("../tests/binary_to_decimal_conversion.in")
machine.insert_tape("1001")
machine.run()
'''

'''
#Turing sequence machine - OK
machine = Machine()
machine.upload_states_by_archive("../tests/turings_sequence_machine.in")
machine.insert_tape("")
machine.run()
'''

'''
#Parentheses checker - OK
machine = Machine()
machine.upload_states_by_archive("../tests/parentheses_checker.in")
machine.insert_tape("12(2+(3^(4-1)))")
machine.run()
'''

'''
#Reverse Polish Boolean - OK
machine = Machine()
machine.upload_states_by_archive("../tests/reverse_polish_boolean.in")
machine.insert_tape("10~1&|0|")
machine.run()
'''

'''
#Primality Test - OK
machine = Machine()
machine.upload_states_by_archive("../tests/primality_test.in")
machine.insert_tape("101")
machine.run()
'''

'''
#4-State busy beaver  - ??
machine = Machine()
machine.upload_states_by_archive("../tests/4_state_busy_beaver.in")
machine.insert_tape("")
machine.run()
'''

'''
#Universal Turing Machine - OK
machine = Machine()
machine.upload_states_by_archive("../tests/universal_turing_machine.in")
machine.insert_tape("[ L+,0R.,1R.!1L+,1L+,0L.:,0L.,1L.:]1011")
machine.run()
'''