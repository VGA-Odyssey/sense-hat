from sense_hat import SenseHat

sense = SenseHat()

# Display the letter J
letter = 65
while True:
	sense.show_letter(chr(int(letter)))
	letter += 0.25
	if letter >= 91: letter = 65
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)
	
	print("x={0}, y={1}, z={2}".format(x, y, z))

  # Update the rotation of the display depending on which way up the Sense HAT is
	if x  == -1:
	  sense.set_rotation(180-90)
	elif y == 1:
	  sense.set_rotation(90-90)
	elif y == -1:
	  sense.set_rotation(270-90)
	else:
	  sense.set_rotation(0+270)
