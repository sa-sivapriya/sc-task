import requests

entry = {
        "name": [
            "BaksoCrypt"
        ],
        "extensions": ".adr",
        "extensionPattern": "",
        "ransomNoteFilenames": "",
        "comment": "Based on my-Little-Ransomware",
        "encryptionAlgorithm": "",
        "decryptor": "",
        "resources": [
            "https://twitter.com/JakubKroustek/status/760482299007922176"
        ],
        "screenshots": "https://0xc1r3ng.wordpress.com/2016/06/24/bakso-crypt-simple-ransomware/"
    }
put_entry = {
    "decryptor": "Test"
}
print("Initialization .....")
resp = requests.post("http://127.0.0.1:8000/login")
print(resp.json()['msg'])

print("Test get all entries")
resp = requests.get("http://127.0.0.1:8000/ransoms")
print(resp.json()['data'])

print("Test get one entry")
resp = requests.get("http://127.0.0.1:8000/ransom/?name=7ev3n&name=7ev3n-HONE$T")
print(resp.json()['data'])

print("Test add entry")
resp = requests.post("http://127.0.0.1:8000/ransom",json=entry)
print(resp.json()['msg'])

print("Test get created entry")
resp = requests.get("http://127.0.0.1:8000/ransom/?name=BaksoCrypt")
print(resp.json()['data'])

print("Test Update created entry")
resp = requests.put("http://127.0.0.1:8000/ransom/?name=BaksoCrypt",json=put_entry)
print(resp.json()['msg'])

print("Test get updated entry")
resp = requests.get("http://127.0.0.1:8000/ransom/?name=BaksoCrypt")
print(resp.json()['data'])

print("Test Delete created entry")
resp = requests.delete("http://127.0.0.1:8000/ransom/?name=BaksoCrypt")
print(resp.json()['msg'])

print("Test get Deleted entry")
resp = requests.get("http://127.0.0.1:8000/ransom/?name=BaksoCrypt")
print(resp.json()['data'])