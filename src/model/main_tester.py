
from machine import Machine

#palindrome_detector
machine = Machine()
machine.upload_states_by_archive("../tests/palindrome_detector.in")
machine.insert_tape("101")
machine.run()
