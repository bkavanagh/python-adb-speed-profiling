from adb.adb_commands import AdbCommands
from adb.sign_m2crypto import M2CryptoSigner
import sys
import os.path as op
import time

TESTFILE_PATH = './testfile.zip'
REMOTE_DIRECTORY = '/sdcard/'


def devices(signer=None):
    for device in AdbCommands.Devices():
        device.Open()
        if signer:
            yield AdbCommands.Connect(device, rsa_keys=[signer, ])
        else:
            yield AdbCommands.Connect(device)

def push(device, local, remote):
    print 'Pushing file to device {}'.format(device)
    return device.Push(local, remote, timeout_ms=15000)


if __name__ == '__main__':
    signer = None
    try:
        signer = M2CryptoSigner(sys.argv[1])
    except IndexError as ex:
        print 'Running without auth (pre 4.4 devices)'
    except OSError as ex:
        print 'validkey  not found in supplied path {}'.format(sys.argv[1])
        raise
    if not op.exists(TESTFILE_PATH):
        raise OSError('Please run ./testfile.py first')
    remote_path = op.join(REMOTE_DIRECTORY, op.basename(TESTFILE_PATH))
    testfile_size = op.getsize(TESTFILE_PATH)
    print 'Test file is {} bytes'.format(testfile_size)
    for device in devices(signer=signer):
        start_time = time.time()
        push(device, TESTFILE_PATH, remote_path)
        total_time = time.time() - start_time
        print 'Pushed {} bytes in {}s @ {}b/s'.format(testfile_size, total_time, testfile_size/total_time)
