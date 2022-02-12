print("강한친구 대한육군")
print("강한친구 대한육군")

print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|\"^\"`    |')
print('||_/=\\\\__|')

numbers = input()
lst = numbers.split(" ")
print(int(lst[0])*int(lst[1]))

if __name__ == "__main__":
    numbers = input()
    lst = numbers.split(" ")
    a = int(lst[0])
    b = int(lst[1])
    # plus
    print(a+b)
    # minus
    print(a-b)
    # product
    print(a*b)
    # if latter number is not zero
    if b != 0:
        # integer division
        print(a//b)
        # remainder
        print(a%b)
    