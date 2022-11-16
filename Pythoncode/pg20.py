import os, ipaddress

os.system('cls') #os.system will clear the consoele at the start of the exexcution
while True:

    ip = input('Enter Ip Address:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-' *50)
        print('IP is not valid')
    finally:
        if ip == 'q':
           print('Script finished')
           break

