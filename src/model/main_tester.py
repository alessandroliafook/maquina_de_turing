# noinspection PyUnresolvedReferences
from machine import Machine

#palindrome_detector
machine = Machine()
machine.upload_states_by_archive("../tests/palindrome_detector.in")
machine.insert_tape("1001001001001001")
machine.run()

#Binary addiction
machine = Machine()
machine.upload_states_by_archive("../tests/binary_addiction.in")
machine.insert_tape("10 10")
machine.run()
