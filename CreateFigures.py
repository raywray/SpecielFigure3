import requests
from figure3 import figure3Data
from figure5and6 import figure5And6Data

url = "https://byu.box.com/shared/static/8z12yer0rpp3e323o502ab48s04utbfy.txt"
r = requests.get(url, allow_redirects=True)
f = open("ProbesetFiltered.txt", "w")
f.write(r.text)
f.close()
path = "ProbesetFiltered.txt"

print(path)
figure3Data(path)
figure5And6Data(path)

print("done")

