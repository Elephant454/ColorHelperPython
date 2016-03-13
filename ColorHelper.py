import colorsys

# main color conversion functions
def hex6ToRgbInt(color):
    return(int(color[-6:-4], 16), int(color[-4:-2], 16), int(color[-2:], 16))

def rgbFloatToHslFloat(color):
    result = colorsys.rgb_to_hls(color[0], color[1], color[2])
    return(result[0], result[2], result[1])

def hslFloatToRgbFloat(color):
    return(colorsys.hls_to_rgb(color[0], color[2], color[1]))

def rgbIntToRgbFloat(color):
    return(color[0]/256, color[1]/256, color[2]/256)

def rgbFloatToRgbInt(color):
    return(int(round(color[0]*256)), int(round(color[1]*256)), int(round(color[2]*256)))

def hslFloatToHslInt(color):
    return(int(round(color[0]*360)), int(round(color[1]*100)), int(round(color[2]*100)))

def hslIntToHslFloat(color):
    return(color[0]/256, color[1]/256, color[2]/256)

# helper color conversion methods
def hslIntComplement(color):
    return((color[0]+180)%360, color[1], color[2])
