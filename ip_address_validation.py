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
    testvar = ip.split('.')
    # print (testvar[0])

    iplen = len(testvar)

    if iplen < 4 or iplen >4:
        print(ip + ' Is is not a valid IP address\n')
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


ip = ['12.233.11.2',
      'asd.adsf.sadf',
      'asdfadsfadf',
      '12232.11232.23.32231',
      '0.0.0.0',
      '255.255.255.255',
      '88.990.001123',
      'asd.adsf.sadf.sadf',
      '22a.32.32.22',
      '12.233.11.-2',
      '12.233.11..2',
      '12.233.11.',
      '12.233. 11.2']

for ipad in ip:
    valid_ip(ipad)
