#!/usr/bin/python
import os, sys
import subprocess
input = sys.argv[1]
limit = int(input)
usage = []
volumes = ['vol02', 'xenbf_vol02','xenbf_vol03','iadxenbf_vol01','iadxenbf_vol02','iadxenbf_vol03','iadxenbf_vol04']
cmd = 'df -h | grep 172.25.72.31:'
server = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
output =server.communicate()
result= str(output)
s = result.split()
t = s[4::5]
count = 0
for i in t:
    usage.append(i[:-1])
loi = list(map(int,usage))
for i in loi:
        if i < limit:
                print "Status of the volume:",volumes[count],
                print "is:OK and the usage is", i
                count = count+1
 #              sys.exit(0)
        elif i == limit:
                print "Status of the volume:",volumes[count],
                print "is:WARNING and the usage is", i
                count = count+1
#             sys.exit(1)
        elif i > limit:
                print "Status of the volume:",volumes[count],
                print "is:CRITICAL and the usage is", i
                count = count+1
   #            sys.exit(2)
        else:
                print "Unknown Status" , i
