import sys
encrypted = b'\x08\x06\x1f\x1f\x3d\x20\x17\x3b\x37\x27\x2b\x38\x3b\x20\x27\x20\x3d\x21\x20\x34\x3a\x28\x24\x23\x35\x26\x38\x21\x38\x3b\x3c\x3c\x3b\x36'

def verify(key, argv, envp):
    for i in range(len(key)):
        if encrypted[i] != ((i ^ key[i].encode('ascii')[0]) << ((i ^ 9) & 3)) | ((i ^ key[i].encode('ascii')[0]) >> (8 - ((i ^ 9) & 3))):
            return False

    return len(key) == 34


def main(argc, argv, envp):
    if argc <= 1:
        sys.stderr.write(b'I need a key!\n')
        return -1

    key = argv[1].encode('ascii')
    if verify(key, argv, envp):
        print('Correct key!')
    else:
        print('Wrong key!')

    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv, sys.environ)
