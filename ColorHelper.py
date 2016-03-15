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
    return(color[0]/255, color[1]/255, color[2]/255)

def rgbFloatToRgbInt(color):
    return(int(round(color[0]*255)), int(round(color[1]*255)), int(round(color[2]*255)))

def hslFloatToHslInt(color):
    return(int(round(color[0]*359)), int(round(color[1]*99)), int(round(color[2]*99)))

def hslIntToHslFloat(color):
    return(color[0]/359, color[1]/99, color[2]/99)

# helper color conversion methods
def hslIntComplement(color):
    return((color[0]+180)%359, color[1], color[2])

def hexComplement(color):
    rgb = (int(color[-6:-4], 16)/255, int(color[-4:-2], 16)/255, int(color[-2:], 16)/255)
    hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
    hlsComplement = ((((hls[0]*359)+180)%360)/359, hls[1], hls[2])
    rgbComplement = colorsys.hls_to_rgb(hlsComplement[0], hlsComplement[1], hlsComplement[2])
    return(rgbComplement[0]*255, rgbComplement[1]*255, rgbComplement[2]*255)

