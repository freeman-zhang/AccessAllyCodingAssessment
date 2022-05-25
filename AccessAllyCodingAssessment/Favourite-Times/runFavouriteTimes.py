import os 
tests = [
"j4_sample.01.in",
"j4_sample.02.in",
"j4.01.in",
"j4.02.in",
"j4.03.in",
"j4.04.in",
"j4.05.in",
"j4.06.in",
"j4.07.in",
"j4.08.in",
"j4.09.in",
"j4.10.in",
"j4.11.in",
"j4.12.in",
"j4.13.in",
"j4.14.in",
"j4.15.in"
]


for testfile in tests:
    os.system('python favouriteTimes.py {}'.format(testfile))