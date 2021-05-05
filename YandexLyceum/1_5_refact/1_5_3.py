limit = int(input())
old_fib = 1
current_fib = 1
while old_fib <= limit:
    print(old_fib)
    new_fib = old_fib + current_fib
    old_fib = current_fib
    current_fib = new_fib