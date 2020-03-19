import sys

def main(S):
    # Your solution riiiiight here.
    c = 0
    for e in S:
        if e == '(':
            c += 1
        else:
            c -= 1
            if c < 0:
                break
    if c == 0:
        print("no")
    else:
        print("yes")

if __name__ == "__main__":
    data = sys.stdin.readlines()
    for i in data:
        main(i)