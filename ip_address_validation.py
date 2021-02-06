# Test cases
# // 12.233.11.2
# // asd.adsf.sadf
# // asdfadsfadf
# // 12232.11232.23.32231
# // 0.0.0.0
# // 255.255.255.255
# // 88.990.001123

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

    dodgy_octects = []

    if iplen != 4:
        print(ip + ' Is is not a valid IP address because it does not have 4 octets \n')
        return

    for i in testvar:

        if not is_octet_Numeric(i):
            dodgy_octects.append(i)
            continue

        i = int(i)
        if not is_octect_inRange(i):
            dodgy_octects.append(i)
            continue


    if not dodgy_octects:
        print("Your input ip: '" + ip + "' is a valid ip address \n")
        return

    print("Your dodgy ip part is: " + str(dodgy_octects) )
    return

def is_octet_Numeric(octect):
        return octect.isnumeric()

def is_octect_inRange(octect):
        return octect in range(0, 256)




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
# ip = '22a.32.32.22'
# ip = 'asd.adsf.sadf.sadf'
ip = '12232.11232.23.32231'
valid_ip_approach2(ip)
# for ipad in ip:
#     valid_ip(ipad)























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
