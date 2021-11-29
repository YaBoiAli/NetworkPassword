import subprocess
from time import sleep


print("Type only the network name this device has connected to before, To check Type \"display\": ")

sleep(2)


coutinue = False


def main():
    while coutinue == False:
        network = input("Enter network name: ")

        if network != 'display':

            show_profiles = subprocess.run('netsh wlan show profiles', shell=True, text = True)
            get_pass = subprocess.run(f'netsh wlan show profiles {network} key=clear')
            sleep(1)
            print(get_pass)
            cout = input("Do you wanna continue y/n? ")

            if cout == 'y':
                coutinue = False
                
            else:
                coutinue = True


        else:
            display_networks = subprocess.run('netsh wlan show profiles', shell=True, text=True)
            cout = input("Do you wanna continue y/n? ")

            if cout == 'y':
                coutinue = False
            
            else:
                coutinue = True


if __name__ == "__main__":
    main()

