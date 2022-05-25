import os 
tests = [
"s4.1.in",
"s4.2.in",
"s4.3.in",
"s4.4.in",
"s4.5.in",
]


for testfile in tests:
    os.system('python bloodDistribution.py {}'.format(testfile))