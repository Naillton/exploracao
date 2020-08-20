import time,msfrpc
client = msfrpc.Msfrpc({})
client.login("msf", "smb-version-forte")
sessao = client.call("console.create")
comando = """use auxiliary/scanner/smb/smb_version
set RHOSTS 192.168.0.2
exploit
"""
client.call("console.write", [sessao["id"], comando])
time.sleep(1)
resultado = client.call("console.read", [ sessao["id"] ])
while resultado["busy"]:
	resultado = client.call("console.read", [ sessao["id"] ])
	time.sleep(1)
print resultado["data"]
client.call("console.destroy", [sessao["id"]])
