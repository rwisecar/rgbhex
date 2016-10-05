# Convert RGB values into HEX values
def rgb_hex():
    invalid_msg = 'You have entered an invalid value. Please try again.'

    red = int(raw_input('Please enter a number between 0 and 255 to represent the red HEX value.'))
    green = int(raw_input('Please enter a number between 0 and 255 to represent the green HEX value.'))
    blue = int(raw_input('Please enter a number between 0 and 255 to represent the blue HEX value.'))
    if red < 0 or red > 255:
        print invalid_msg
        return
    if green < 0 or green > 255:
        print invalid_msg
        return
    if blue < 0 or blue > 255:
        print invalid_msg
        return

    val = (red << 16) + (green << 8) + blue

    print "%s" % (hex(val)[2:]).upper()

rgb_hex()

# Convert HEX values into RGV values
