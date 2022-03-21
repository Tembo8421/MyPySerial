from MySerial import COM

import os
import json
import time

from argparse import ArgumentParser

def go_for_start(com):
    com.send_data('\n')
    com.send_data('root\n')
    #com.send_data('killall python3\n')
    com.send_data('echo 0 > /proc/mtprintk\n')
    com.send_data('cd /data\n')
    com.log.info('go_for_start() done !')

def show_ip(com):
    com.send_data("""ip -o addr show | awk '/inet/ {print $2, $3, $4}'\n""")
    com.log.info('show_ip() done !')

def send_file(com, source, target):
    words = ""
    try:
        with open(source, mode='r') as f:
            words = f.read()
    except:
      raise

    words = words.replace('\r', '')

    com.send_data("""echo '""" + words + """' > """ + target + """\n""")
    com.send_data('chmod 777 ' + target + '\n')
    com.log.info('send_file() done !')

def start_wifi(com):
    com.send_data('killall wpa_supplicant\n')
    time.sleep(1)
    com.send_data('wpa_supplicant -Dnl80211 -iwlan0 -c/data/wifi/wpa_supplicant.conf &\n')
    time.sleep(1)
    com.send_data('dhcpc.script start wlan0\n')
    com.log.info('start_wifi() done !')

def send_cmd(com, cmdline):
    com.send_data(cmdline + '\n')
    com.log.info('send_cmd() done !')

if __name__ == '__main__':

# open config file
    with open("config.json") as f:
        config = json.load(f)
    #print(config)

# parse args
    parser = ArgumentParser(prog="CYL-Serial",
                            description="CYL-Serial Com for Thermal",
                            epilog="enjoy !!!")
                            
    parser.add_argument("-n", help="com name", dest="com_name", default=config["name"])
    parser.add_argument("-b", help="baud rate", dest="com_baud", default=config["baud"])
    parser.add_argument("-i", help="show ip", dest="com_ip", action="store_true")
    parser.add_argument("-m", help="send msg", dest="com_msg", default='')

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", help="send file", dest="com_file", nargs=2)
    group.add_argument("-F", help="send file by default path in config.json", dest="com_df", action="store_true")

    args = parser.parse_args()

# open com
    com = COM(args.com_name, args.com_baud)
    # com.open()
    go_for_start(com)

    try:
        if (args.com_df):
            send_file(com, config["source"], config["target"])
        elif (args.com_file):
            send_file(com, args.com_file[0], args.com_file[1])
        else:
            pass
    except:
        print("Error: The source file does not appear to exist.")
        com.close()
        raise

    if (args.com_ip):
        show_ip(com)

    if (args.com_msg):
        send_cmd(com, args.com_msg)
        
    time.sleep(5)
    com.close()

    os.system('pause')
