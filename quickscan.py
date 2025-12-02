{"id":"98152","variant":"standard","title":"imp roved quickscan.py"}
import sys
import os
if    len(sys.argv)!= 2:
    print ("Usage:python3 quickscan.py<target>")
    sys.exit(1)
target=sys.argv[1]

print (f"[+] starting quick scan on {target}...")
os.system(f"nmap -sV -T4 -O {target}")
print ("[+] scan finished.")

