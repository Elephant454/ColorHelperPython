import colorsys

# main color conversion functions
def hex6ToRgbInt(color):
    return(int(color[-6:-4], 16), int(color[-4:-2], 16), int(color[-2:], 16))

#def rgbFloatToHslFloat(color):
#    result = colorsys.rgb_to_hls(color[0], color[1], color[2])
#    return(result[0], result[2], result[1])

#def hslFloatToRgbFloat(color):
#    return(colorsys.hls_to_rgb(color[0], color[2], color[1]))

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

def rgbFloatToHslFloat(color):
    rgbMin = min(color[0], color[1], color[2])
    rgbMax = max(color[0], color[1], color[2])
    deltaRgb = rgbMax - rgbMin

    l = (rgbMin+rgbMax) / 2
    if(deltaRgb == 0):
        h = 0
        s = 0
    else:
        if(l<0.5):
            s = deltaRgb / (rgbMax+rgbMin)
        else:
            s = deltaRgb / (2 - rgbMax - rgbMin)

        deltaR = (((rgbMax-color[0]) / 6) + (rgbMax/2)) / deltaRgb
        deltaG = (((rgbMax-color[1]) / 6) + (rgbMax/2)) / deltaRgb
        deltaB = (((rgbMax-color[2]) / 6) + (rgbMax/2)) / deltaRgb

        if(color[0] == rgbMax):
            h = deltaB - deltaG
        elif(color[1] == rgbMax):
            h = (1/3) + deltaR - deltaB
        elif(color[2] == rgbMax):
            h = (2/3) + deltaG - deltaR

        if(h<0):
            h += 1
        if(h>1):
            h -= 1

    return(h, s, l)

def hslFloatToRgbFloat(color):
    def hueToRgb(v1, v2, vH):
        if(vH < 0):
            vH += 1
        if(vH > 1):
            vH -= 1
        if((6*vH) < 1):
            return (v1 + (v2-v1) * 6 * vH)
        if((2*vH) < 1):
            return(v2)
        if((3*vH) < 2):
            return(v1 + (v2-v1) * ((2/3) - vH) * 6)
        return(v1)

    if(color[1]==0):
        r = color[2]*255
        g = color[2]*255
        b = color[2]*255
    else:
        if(color[2]<0.5):
            v2 = color[2] * (1+color[1])
        else:
            v2 = (color[2] + color[1]) - (color[1] * color[2])

        v1 = 2 * color[2] - v2

        r = 255 * hueToRgb(v1, v2, color[0] + (1/3))
        g = 255 * hueToRgb(v1, v2, color[0])
        b = 255 * hueToRgb(v1, v2, color[0] - (1/3))

    return(r, g, b)
