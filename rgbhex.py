# Convert RGB values into HEX values

def rgb_hex():
    invalid_msg = 'You have entered an invalid value. Please try again.'

    red = int(raw_input('Please enter a number between 0 and 255 to represent the red HEX value. '))
    green = int(raw_input('Please enter a number between 0 and 255 to represent the green HEX value. '))
    blue = int(raw_input('Please enter a number between 0 and 255 to represent the blue HEX value. '))
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

# Convert HEX values into RGV values

def hex_rgb():
    hex_val = raw_input('Please enter the six digit hexidecimal value you wish to convert to RGB. ')
    if len(hex_val) != 6:
        print('That is an invalid selection. Please try again.')
        return
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2**8

    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    red = hex_val % two_hex_digits

    print 'rgb(%s %s %s)' % (red, green, blue)

# Master Function to run program


def convert():
    while True:
        option = raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to leave the program. ')
        if option == '1':
            print('You have selected RGB to HEX.')
            rgb_hex()
        elif option == '2':
            print('You have selected HEX to RGB.')
            hex_rgb()
        elif option.upper() == 'X':
            print('You have opted to quit the program. Goodbye.')
            break
        else:
            print('That is an invalid choice.')
            break

convert()
