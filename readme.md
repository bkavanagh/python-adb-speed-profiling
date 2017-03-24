python-adb speed test for python 2.7

You'll need to step back to pre 3.6 commit to run with 2.7

$ git clone https://github.com/google/python-adb.git
$ cp ./testfile.py ./python-adb/testfile.py
$ cp ./speed_test.py ./python-adb/speed_test.py
$ cd python-adb
$ git reset --hard fb09de9d920227f2b27b17086cd0b3a73ea5fb39
$ python testfile.py 1000000 # generates a 10 MB zeroed file called 'testfile.zip' in current dir
$ sudo python speed_test.py [optional path to rsa key]

or for a cProfile

$ sudo python -m cProfile -o speed_test.profile speed_test.py

You can read the profile with 

$ python -m pstats speed_test.profile


