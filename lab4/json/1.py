import json

with open('C:\\Users\\admin\\Desktop\\pp2\\lab4\\json\\data.json', 'r') as file:
    json_data = json.load(file)

print('''=======================================================================================
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------  ------''')
dn, mtu, description, speed = "", "", "", ""
for i in range(3):
    for key, value in json_data["imdata"][i]['l1PhysIf']["attributes"].items():
        if key == 'dn':
            dn = value
        if key == 'speed':
            speed = value
        if key == 'mtu':
            mtu = value
        if key == 'descr':
            description = value
    print("{0:51} {1:20} {2:8} {3:6}".format(dn,description,speed,mtu))

    