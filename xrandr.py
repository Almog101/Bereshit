import subprocess
import math

def get_screens():
    """
    returns a list of the names of connected screens
    """
    screens = []
    output = subprocess.run(['xrandr'], capture_output=True)
    for line in output.stdout.decode().splitlines():
        if " connected" in line:
            screen_name = line.split("connected")[0][:-1]
            screens.append(screen_name)
    return screens

def change_screen_details(screen_name, brightness, gamma):
    """
    brightness - float between 0 to 1 ex. 0.5
    gamma - tuple of 3 floats between 0 to 1 ex. 1.0:1.0:1.0 
    """
    subprocess.run(['xrandr', '--output', screen_name, '--gamma',gamma, '--brightness', str(brightness)], capture_output=False)

def minimize_float(f):
    return float('%.2f' % (f))

def tuple_to_string(tup):
    return':'.join([str(f) for f in tup])

def temperature_to_rgb(temperature):
    temperature /= 100

    # ----- Red -----    
    if temperature <= 66:
        red = 255
    else:
        red = temperature - 60
        red = 329.698727446 *  math.pow(red, -0.1332047592)
        if red < 0:
            red = 0
        elif red > 255:
            red = 255

    # ----- Green -----    
    if temperature <= 66:
        green = temperature
        green = 99.4708025861 * math.log(green, math.e) - 161.1195681661
        if green < 0:
            green = 0
        elif green > 255:
            green = 255
    else:
        green = temperature - 60
        green = 288.1221695283 * math.pow(green, -0.0755148492)
        if green < 0:
            green = 0
        elif green > 255:
            green = 255
 

    # ----- Blue -----    
    if temperature >= 66:
        blue = 255
    else:
        if temperature <= 19:
            blue = 0
        else:
            blue = temperature - 10
            blue = 138.5177312231 * math.log(blue, math.e) - 305.0447927307
            if blue < 0:
                blue = 0
            elif blue > 255:
                blue = 255
    
    rgb = (red/255, green/255, blue/255)
    rgb = tuple(map(minimize_float, rgb))
    
    return rgb