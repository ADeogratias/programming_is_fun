# programming is fun :)

# We are going to try and code the famous fizzbuzz game. An easy coding interview question

# It is very famous and we felt like we should consider
# working on it and trying different approaches to it

# Fizz buzz is a group word game for children to teach them about division.[1] Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz".

# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...

# the game details can be found here: https://en.wikipedia.org/wiki/Fizz_buzz

# We are going to play the game to a 100

# Lets first try and naive_approach

def fizzbuzz_naive_approach():

    # we do a range that goes to 101
    # because the range function is last
    # number exclusive and first number inclusive
    for i in range(1, 101):
        # if i is a multiple of 3, print fizz
        if i%3 == 0:
            print('fizz')

        # if i is a multiple of 5, print buzz
        if i%5 == 0:
            print('buzz')

        if i%3 and i%5 != 0:
            print(i)

    return 0

# fizzbuzz_naive_approach()
# the problem with this approach is that for muliples
# of both 3 and 5 it prints fizz on one row and buzz on the row below.

# Let's fix that
def fizzbuzz_naive_approach2():

    for i in range(1, 101):
        if i%3 == 0 and i%5 != 0:
            print('fizz')

        if i%5 == 0 and i%3 != 0:
            print('buzz')

        if i%3 == 0 and i%5 == 0:
            print('fizzbuzz')

        if i%3 != 0 and i%5 != 0:
            print(i)

    return 0

fizzbuzz_naive_approach2()
