from identifier import identify_mime

fps = [
'/home/robert/Pictures/IMG_20190618_134010.jpg',
'/home/robert/Pictures/Reimagining Talent Management for Business 4.0_200318.pdf',
'/home/robert/Pictures/Screenshot_20190717_093122.png'
]

for x in fps:
	n = identify_mime(x)
	print(n)