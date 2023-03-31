def sizegabor():
    import ctypes
    from screeninfo import get_monitors

    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    width_px = user32.GetSystemMetrics(0)
    height_px = user32.GetSystemMetrics(1)
    hdc = gdi32.CreateDCW("DISPLAY", None, None, None)
    width_mm = gdi32.GetDeviceCaps(hdc, 4)  # HORZSIZE
    height_mm = gdi32.GetDeviceCaps(hdc, 6)  # VERTSIZE
    gdi32.DeleteDC(hdc)

    #print(f"Monitor size: {width_mm/10:.2f} cm x {height_mm/10:.2f} cm")

    monitoruser = []
    for m in get_monitors():
        print(str(m))
        m=str(m).split(',')
        monitoruser.append(m)

    pixeluser = monitoruser[0][2].replace("width=",'')
    sizeuser= monitoruser[0][4].replace("width_mm=",'')
    print(pixeluser,sizeuser)
    valore = int(pixeluser)/int(width_mm)*80
    print(valore)
    return valore



def getwinpixel():
    import ctypes
    from screeninfo import get_monitors

    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    width_px = user32.GetSystemMetrics(0)
    height_px = user32.GetSystemMetrics(1)
    winsize = [width_px, height_px] #larghezza altezza

    return winsize

def spawnright():
    dimensionifinestra = getwinpixel()
    dimensioigabor = sizegabor()

    spawnorizsx = int(dimensioigabor/2)
    spawnorizdx = int(dimensionifinestra[0]/2 - sizegabor()/2)

    spawnver = int(dimensionifinestra[1]/2 - sizegabor()/2)

    spawnpoint = [spawnorizsx,spawnorizdx,spawnver]
    return spawnpoint