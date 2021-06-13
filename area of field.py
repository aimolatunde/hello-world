# conversion unit from square metre to acre is
sqm_per_acre = 4046.86
# accepting input of width and length in metres of the land (or field)
width = float(input("enter the width of your field in meters"))
length = float(input("enter the length of your field in meters"))
area_in_sqm = width*length
# converting the result to acres
area_in_acre = area_in_sqm/sqm_per_acre
print("your field is", area_in_acre, "acres")
