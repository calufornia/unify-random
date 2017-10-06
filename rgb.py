import requests
from PIL import Image

values = []
for i in range(5): # get 50000 random numbers; 128*128*3 = 49152
	response = requests.get('https://www.random.org/integers/?num=10000&min=0&max=255&col=1&base=10&format=plain&rnd=new').content
	random_nums = response.decode("utf-8").strip().split('\n')
	for num in random_nums:
		values.append(int(num))

pixels = []

for i in range(128 * 128):
	pixels.append((values[3*i], values[3*i+1], values[3*i+2]))

image = Image.new("RGB", (128, 128))
image.putdata(pixels)
image.show()