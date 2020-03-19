import sys

def main(x,y):
    # Your solution riiiiight here.
    for i in range(x,y+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == "__main__":
    inputarr = sys.stdin.read()[:-1].split(' ')
    x, y = int(inputarr[0]), int(inputarr[1])
    main(x,y)