# show_config.txt is a JUNOS conf file in set format
f=open("config.txt")
for line in f:
        if "host-name" in line:
                hostname=line.split(" ")[3].strip()
                print hostname
f.close()

