import os

def main():
    statinfo = os.stat('0x5800e3d6dc0f')
    print(statinfo.st_size)

if __name__ == "__main__":
    main()
