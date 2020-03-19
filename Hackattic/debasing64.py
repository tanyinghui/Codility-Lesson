import base64
import sys

def main(A):
    # Your solution riiiiight here.
    result = []
    for e in A:
        result += [str(base64.b64decode(e))[2:-1]]
    return result

if __name__ == "__main__":
    data = sys.stdin.readlines()
    output = main(data)
    for e in output:
        print(e)