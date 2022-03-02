from MySerial import COM

import json

if __name__ == '__main__':

    # open cyltek file
    with open('cyltek.sh', mode='r') as f:
        words = f.read()
        
    words = words.replace('\r', '')
    #print(words)

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
    com.send_data('echo "'+ words + '" > cyltek.sh\n')
    com.send_data('chmod 777 cyltek.sh\n')
    
    # com.get_data(50)
    com.close()