def area_of_circle(r):

	"""computes and returns the area of circle """

	return 3.142 * r ** 2



radius = float(input("Enter radius of circle: "))
area = area_of_circle(radius)
print(f"Area of circle with radius {radius} is {area:.4f}")

help(area_of_circle)