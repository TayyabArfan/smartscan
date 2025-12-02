import sys
import subprocess
import re

if len(sys.argv)!=2:
   print("usage:python3 smartscan.py <target>")
   sys.exit(1)

target=sys.argv[1]

result=subprocess.run(
    ["nmap","-sV","-T4",target],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

print ("=============== Raw NMAP Output ================")
print (result.stdout)

matches=[]

port_regex=re.compile(r"(\d+)/(tcp|udp)\s+(open|closed|filtered|unfiltered)\s+(.+)")

for line in result.stdout.splitlines():
  m = port_regex.search(line)
  if m:
     port,proto,state,service=m.groups()
     matches.append((port,proto,state,service))

print ("===== Parsed Ports ======")
open_ports = [m for m in matches if m[2] == "open"]
if not open_ports:
   print ("no open ports found")
else:
     for port,proto,state,service in matches:
            print (f"{port}/{proto:<3} open {service}")

