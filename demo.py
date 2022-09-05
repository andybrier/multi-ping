#!/usr/bin/env python

"""
Copyright 2017 Pani Networks Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

# A small demo, which demonstrates how to use MultiPing


from multiping import MultiPing
from multiping import multi_ping
import datetime
import time
import subprocess


if __name__ == "__main__":
  # A list of addresses and names, which should be pinged.
    addrs = [ "114.114.114.114", "127.0.0.1"]
    fileName='/tmp/logs.txt'
    cmd1 = ['tcpdump', '-i', 'eth0', '-s', '0', '-w', '/tmp/tair.pcap', '-W', '256', '-C', '1', 'dst', 'port', '9736']
    proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    with open(fileName,'w')as file:
            file.write('-------')

            for i in range(100000):
                mp = MultiPing(addrs)
                mp.send()
                responses, no_response = mp.receive(0.02)

                current_time = datetime.datetime.now()


                if not no_response:
                    file.write("%s all done, received responses from everyone \n" %current_time)
                else:
                    file.write(" %s   %d. retry, resending to: %s \n" % (current_time, i + 1, no_response))
                    proc.kill()
                time.sleep(1)
                
            file("done, exit")
