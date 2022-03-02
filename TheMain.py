from MySerial import COM

import json

if __name__ == '__main__':

    # open cyltek file
    with open('content.txt', mode='r') as f:
        words = f.read()
        
    words = words.replace('\r', '')
    #words = words.replace(r'"', r'\"')
    print(words)

    # open config file
    with open("config.json") as f:
        config = json.load(f)

    #print(config)

    com = COM(config["name"], config["baud"])
    # com.open()
    com.send_data('\n')
    com.send_data('\n')
    com.send_data('root\n')
    com.send_data('cd /data\n')
    com.send_data("""echo '""" + words + """' > """ + config["target"] + """\n""")
    com.send_data('chmod 777 ' + config["target"] + '\n')
    com.send_data('reboot\n')
    
    # com.get_data(50)
    com.close()