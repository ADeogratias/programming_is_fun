# We are going to work on the ip address validation algorithm

def valid_ip(ip):
    # testvar = ip.replace(" ","")
    testvar = ip.split('.')
    # print(testvar)
    # print (testvar[2])
    #
    iplen = len(testvar)

    if iplen < 4 or iplen >4:
        print(ip + ' Is is not a valid IP address because it does not have 4 octets \n')
        return

    for i in testvar:

        if i.isnumeric() == False:
            print(ip + ' Is not a valid IP address \n')
            return
        i = int(i)
        if ( i < 0 or i > 255):
            print( ip + ' Is not a valid IP address \n')
            return


    print("Your input ip: '" + ip + "' is a valid ip address \n")
    return

def valid_ip_approach2(ip):
    testvar = ip.split('.')
    iplen = len(testvar)

    error_octect = []

    if iplen != 4:
        print(ip + ' Is is not a valid IP address because it does not have 4 octets \n')
        return

    for i in testvar:

        if not i.isnumeric():
            error_octect.append(i)
            continue

        i = int(i)
        if not i in range(0, 256):
            error_octect.append(i)
            continue


    if not error_octect:
        print("Your input ip: '" + ip + "' is a valid ip address \n")
        return

    print("Your error ip part is: " + str(error_octect))
    return



# using the try and catch to make things shorter


def valid_ip_approach3(ip):
    testvar = ip.split('.')
    iplen = len(testvar)

    error_octect = []

    if iplen != 4:
        print(ip + ' Is is not a valid IP address because it does not have 4 octets \n')
        return

    for i in testvar:

        try:
            i = int(i)
            if not i in range(0, 256):
                error_octect.append(i)
                continue

        except ValueError:
            error_octect.append(i)
            continue

    if not error_octect:
        print("Your input ip: '" + ip + "' is a valid ip address \n")
        return

    print("Your error ip part is: " + str(error_octect))
    return

# driver code

# ip = ['12.233.11.2',
#       'asd.adsf.sadf',
#       'asdfadsfadf',
#       '12232.11232.23.32231',
#       '0.0.0.0',
#       '255.255.255.255',
#       '88.990.001123',
#       'asd.adsf.sadf.sadf',
#       '22a.32.32.22',
#       '12.233.11.-2',
#       '12.233.11..2',
#       '12.233.11.',
#       '12.233. 11.2']
# ip = '#sgd.32.32.22'
# ip = '22a.32.32.22'
# ip = 'asd.adsf.sadf.sadf'
# ip = '12232.11232.23.32231'
# ip = '....'
valid_ip_approach3(ip)
# for ipad in ip:
#     valid_ip(ipad)




# using a built in function
# def fun(variable):
#     if (variable.isnumeric() == True):
#         number = int(variable)
#         if (number < 0 or number > 255):
#             return number
#     else:
#         return variable
#
#
# # sequence
# sequence = ['asdf', '2324532', '22', '12']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print(list(filtered))
