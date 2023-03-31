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
        m=str(m).split(',')
        monitoruser.append(m)

    pixeluser = monitoruser[0][2].replace("width=",'')
    sizeuser= monitoruser[0][4].replace("width_mm=",'')
    print(pixeluser,sizeuser)
    valore = 2560/597*80
    print(valore)
    return valore
sizegabor()
