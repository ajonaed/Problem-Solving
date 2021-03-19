# def inception(counter):
#     if counter > 3:
#         return counter
#     else:
#         # inception(counter+1) # Return None, as First Call of the function doesn't have anything.
#         return inception(counter+1) + 1  # we need to return the value of last function's return value
holder = [1]

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
def factorialNonRecursive(n):
    answer = 1
    for i in range(n,0,-1):
        answer *= i
    return answer
def febonacciNonrecursive(n):
    a, b = 0,1
    for i in range(0,n):
        a, b = b , a+b
    return a

def febonacci(n):
    if n <= 1:
        return n
    else:
        return febonacci(n-1) + febonacci(n-2)

def main():
    # print(inception(0))
    # print('Recursively: ',factorial(5))
    # print('Non-recursively: ',factorialNonRecursive(5))
    print(febonacciNonrecursive(7))
    print(febonacci(7))


if __name__ == '__main__':
    main()
