import colorsys

def hex6ToRgbInt(color):
    return(int(color[-6:-4], 16), int(color[-4:-2], 16), int(color[-2:], 16))

def hex6ToRgbFloat(color):
    return(rgbIntToRgbFloat(hex6ToRgbInt(color)))

def hex6ToHslFloat(color):
    rgbFloatColor = hex6ToRgbFloat(color)
    return(colorsys.rgb_to_hls(rgbFloatColor[0], rgbFloatColor[1], rgbFloatColor[2]))

def hex6ToHslInt(color):
    hslFloatColor = hex6ToHslFloat(color)
    return(int(round(hslFloatColor[0]*360)), int(round(hslFloatColor[2]*100)), int(round(hslFloatColor[1]*100)))

def hslIntToRgbFloat(color):
    hslFloatColor = hslIntToHslFloat(color)
    return(colorsys.hls_to_rgb(hslFloatColor[0], hslFloatColor[2], hslFloatColor[1]))

#not working
def hslIntToRgbInt(color):
    hslFloatColor = hslIntToHslFloat(color)
    return(colorsys.hls_to_rgb(hslFloatColor[0], hslFloatColor[2], hslFloatColor[1]))


def hlsIntToRgbInt(color):
    return(rgbFloatToRgbInt(hslIntToRgbFloat))

def rgbIntToRgbFloat(color):
    return(color[0]/256, color[1]/256, color[2]/256)

def rgbFloatToRgbInt(color):
    return(color[0]*256, color[1]*256, color[2]*256)

def hslFloatToHslInt(color):
    return(color[0]/256, color[1]/256, color[2]/256)

def hslIntToHslFloat(color):
    return(color[0]*256, color[1]*256, color[2]*256)
