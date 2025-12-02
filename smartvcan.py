import subprocess
import re

target="scanme.nmap.org"

result=subprocess.run(
    ["nmap","-sV",target],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output=result.stdout
print ("============ RAW NMAP OUTPUT ===============")
print(output)

pattern= re.compile(r"^(\d+)/(\w+)\s+(\w+)\s+([^\s]+)",re.MULTILINE) 
matches = pattern.findall(output)

print ("\n======= Parsed Ports =========")
if not matches:
    print ("NOTHING")
else:
    for port,proto,state,service in matches:
      print (f"(port)/(proto) : (state) : (service)")

