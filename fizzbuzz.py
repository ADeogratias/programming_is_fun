# programming is fun :)

# We are going to try and code the famous fizzbuzz game. An easy coding interview question that was often used by companies to see if a programmer they want to hire really knows how to code.

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

# fizzbuzz_naive_approach2()

# the naive approach is fixed and it is working, but it is very uggly.
# such codes are difficult to read and maintain.


# We are going to try and improve the codes implemented above

def fizzbuzz_approach3():

    for i in range(1, 101):
        # check if both fizz and buzz
        if i%3 == 0 and i%5 == 0:
            print('fizzbuzz')

        # otherwise is it just a multiple of 3
        elif i%3 == 0:
            print('fizz')

        # or just a multiple of 5
        elif i%5 == 0:
            print('buzz')

        # Then just outupt the number
        else:
            print(i)

    return 0

# fizzbuzz_approach3()
# The implementation above is working, but still has more room for improvement

# Lets still improve the above implementation

# wondering why improve this if it is working?

# Well, lets supposed we want to change and work with multiples of 7 and 9
# then you would have to change everywhere in the codes where there is 3 and 5

def fizzbuzz_approach4():

    for i in range(1 ,101):
        output = ""
        if i%3==0: output += "fizz"
        if i%5==0: output += "buzz"

        if output == "": output = i

        print(output)

    return 0

# fizzbuzz_approach4()

# The above implementation is slightly improved but we can still do better.

# We created a dictionary to help us loop through any multiple we might be interested
# it, and the good thing about this implementation is that you do not have to change any
# code in case you add more multiples to the game. You just have to add the dictionary and you are done with any additional multiple.

def fizzbuzz_approach5():
    multiples_dict = {3:"fizz", 5:"buzz", 7:"bazz"}

    for i in range(1 ,101):
        output = ""
        for j in multiples_dict:
            if i%j==0: output += multiples_dict[j]

        if output == "": output = i

        print(output)

    return 0

fizzbuzz_approach5()

# We are now satisfied with the the current approach
# Thank you for walking through the different fizzbuzz approaches