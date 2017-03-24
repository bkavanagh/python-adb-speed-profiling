import sys


def generate_testfile(size=1000000):
    with open('./testfile.zip', 'wb') as f:
        f.seek(size-1)
        f.write('\0')


if __name__ == '__main__':
    try:
        generate_testfile(int(sys.argv[1]))
    except (ValueError, TypeError) as ex:
        print 'Must provide a numerical value'
    except IndexError as ex:
        generate_testfile()
