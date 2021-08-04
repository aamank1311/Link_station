import math


def link_station_finder():
	print("*****************************************************")
	print("*************** LINK STATION FINDER *****************")
	print("*****************************************************")
	x1 = float(input("Enter value for x coordinate for the device: "))
	print(f"x coordinate value is: {x1}")

	y1 = float(input("Enter value for y coordinate for the device: "))
	print(f"y coordinate value is: {y1}")

	r1 = 10			#reach of the 1st Link Station
	r2 = 5			#reach of the 2nd Link Station
	r3 = 12			#reach of the 3rd Link Station
	d1 = 0.0 		#distance between the 1st Link Station and the device 	
	d2 = 0.0 		#distance between the 2nd Link Station and the device 
	d3 = 0.0 		#distance between the 3rd Link Station and the device
	Power1 = 0.0 	#power of the 1st Link Station
	Power2 = 0.0 	#power of the 2nd Link Station
	Power3 = 0.0 	#power of the 3rd Link Station

	d1 = math.sqrt(((0-x1)**2)+((0-y1)**2))
	print(f"distance between the 1st Link Station and the device ({x1},{y1}) : {d1}")
	if r1>=d1:
		Power1 = (r1-d1)**2
	else:
		Power1 = 0
	print(f"power of the 1st Link Station: {Power1}")

	d2 = math.sqrt(((20-x1)**2)+((20-y1)**2))
	print(f"distance between the 2nd Link Station and the device ({x1},{y1}) : {d2}")
	if r2>=d2:
		Power2 = (r2-d2)**2
	else:
		Power2 = 0
	print(f"power of the 2nd Link Station: {Power2}")


	d3 = math.sqrt(((10-x1)**2)+((0-y1)**2))
	print(f"distance between the 2nd Link Station and the device ({x1},{y1}) : {d3}")
	if r3>=d3:
		Power3 = (r3-d3)**2
	else:
		Power3 = 0
	print(f"power of the 2nd Link Station: {Power3}")


	if (Power1>Power2) and (Power1>Power3):
		print(f"Best link station for point ({x1},{y1}) is 0,0 with power: {Power1}")
	elif (Power2>Power1) and (Power2>Power3):
		print(f"Best link station for point ({x1},{y1}) is 20,20 with power: {Power2}")
	elif (Power3>Power1) and (Power3>Power2):
		print(f"Best link station for point ({x1},{y1}) is 10,0 with power: {Power3}")
	else:
		print(f"No link station within reach for point {x1},{y1}")


link_station_finder()