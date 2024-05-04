import sys

def count_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            byte_count = len(file.read())
            return byte_count
    except FileNotFoundError:
        print("File Not Found")
        return -1
    
if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "-c":
        print("usage: python ccwc.py -c <filename>")
    else:
        filename = sys.argv[2]
        bytecount = count_bytes(filename)
        if bytecount != -1:
            print(f"{bytecount} {filename}")


