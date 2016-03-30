# main color conversion functions
def hexToRgb(color):
    return(int(color[-6:-4], 16), int(color[-4:-2], 16), int(color[-2:], 16))

def rgbToHex(color):
    return("#" + "{0:x}".format(color[0]) + "{0:x}".format(color[1]) + "{0:x}".format(color[2]))

def rgbToHsl(color):
    r = color[0]/255
    g = color[1]/255
    b = color[2]/255
    rgbMin = min(r, g, b)
    rgbMax = max(r, g, b)
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

        deltaR = (((rgbMax-r) / 6) + (rgbMax/2)) / deltaRgb
        deltaG = (((rgbMax-g) / 6) + (rgbMax/2)) / deltaRgb
        deltaB = (((rgbMax-b) / 6) + (rgbMax/2)) / deltaRgb

        if(r == rgbMax):
            h = deltaB - deltaG
        elif(g == rgbMax):
            h = (1/3) + deltaR - deltaB
        elif(b == rgbMax):
            h = (2/3) + deltaG - deltaR

        if(h<0):
            h += 1
        if(h>1):
            h -= 1

    return(int(round(h*360)), int(round(s*100)), int(round(l*100)))

def hslToRgb(color):
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

    h = color[0] / 360
    s = color[1] / 100
    l = color[2] / 100

    if(l==0):
        r = l*255
        g = l*255
        b = l*255
    else:
        if(l<0.5):
            v2 = l * (1+s)
        else:
            v2 = (l + s) - (s * l)

        v1 = 2 * l - v2

        r = 255 * hueToRgb(v1, v2, h + (1/3))
        g = 255 * hueToRgb(v1, v2, h)
        b = 255 * hueToRgb(v1, v2, h - (1/3))

    return(int(round(r)), int(round(g)),int(round(b)))

# helper color conversion methods
def hslComplement(color):
    return((color[0]+180)%360, color[1], color[2])
