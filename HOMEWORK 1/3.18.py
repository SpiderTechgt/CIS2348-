import math
color_paint = {
   'red': 35,
   'blue': 25,
   'green': 23
}

gal_of_paint = 350
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height
paint_needed = float(wall_area / gal_of_paint)

cans_amt = math.ceil(paint_needed)

print('Wall area:',wall_area,'square feet')
print('Paint needed:','{:.2f}'.format(paint_needed),'gallons')
print('Cans needed:', cans_amt,'can(s)\n')

cost_paint=0

paint_color = input('Choose a color to paint the wall:\n')
if paint_color.lower() == 'red':
    cost_paint = color_paint['red']*cans_amt
elif paint_color.lower() == 'blue':
    cost_paint = color_paint['blue']*cans_amt
else:
    cost_paint = color_paint['green']*cans_amt
print('Cost of purchasing {paint_color} paint: ${cost_paint}'.format(paint_color = paint_color, cost_paint = cost_paint))