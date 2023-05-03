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

    # print(f"Monitor size: {width_mm/10:.2f} cm x {height_mm/10:.2f} cm")

    monitoruser = []
    for m in get_monitors():
        m=str(m).split(',')
        monitoruser.append(m)

    pixeluser = monitoruser[0][2].replace("width=",'')
    sizeuser= monitoruser[0][4].replace("width_mm=",'')
    valore = int(pixeluser)/int(width_mm)*80
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

def spawnright(N):  # ricordati la coordinate 0,0  è al centro dello schermo ma sul bordo sinistro,  mentre le dimensioni dello schermo  sono con la coordinata bassa sx
   ''' dimensionifinestra = getwinpixel()
    dimensioigabor = sizegabor()

    spawnorizsx = int(dimensioigabor/2)
    spawnorizdx = int(dimensionifinestra[0]/2 - sizegabor()/2)

    spawnver = int(dimensionifinestra[1]/2 - sizegabor()/2)

    spawnpoint = [spawnorizsx,spawnorizdx,spawnver] #spawn nellà metà destra a [sx,dx,ver]'''
   dimensionifinestra = getwinpixel()
   larghezza=dimensionifinestra[0]
   spawnsUp = []
   temporale = int((((larghezza*0.75)*(1/N)))) #la distanza tra  ogni   bordo e  il centro  del quadrante
   latoSX = int(0.25 * larghezza) + int(temporale/2)
   for i in range(N):
       spawnsUp.append([latoSX,0])
       latoSX = latoSX + temporale
   spawnsUp.append(int(dimensionifinestra[1]/4))
   spawnsDown = spawnsUp.copy()
   spawnsDown[-1] = -spawnsDown[-1]
   #print("Upp",spawnsUp)
   #print("down",spawnsDown)
   return spawnsUp, spawnsDown, int(0.25 * larghezza), dimensionifinestra[1], temporale
spawnright(2)

def spawnleft(N):
    dimensionifinestra = getwinpixel()
    larghezza = dimensionifinestra[0]
    spawnsUp = []
    temporale = int((((larghezza * 0.75) * (1 / N))))  # la distanza tra  ogni   bordo e  il centro  del quadrante
    latoSX = int(temporale / 2)
    for i in range(N):
        spawnsUp.append([latoSX, 0])
        latoSX = latoSX + temporale
    spawnsUp.append(int(dimensionifinestra[1] / 4))
    spawnsDown = spawnsUp.copy()
    spawnsDown[-1] = -spawnsDown[-1]
    print("Up",spawnsUp)
    print("down",spawnsDown)
    return spawnsUp, spawnsDown, int(0.75 * larghezza), dimensionifinestra[1], temporale

def DivisioneQuadrantiOriz(confine1, confine2 ,N): #date le coordinate e dati quante parti di schermo voglio nella metà verticale, restiuisce un vettore con le divisioni (Nx2 dove N = numero quadrati in orrizzontale)
    larghezza = abs(confine1-confine2)
    valorelat = int(larghezza / N)
    if confine1 <= confine2:
        min = confine1
        max =  confine2
    else:
        min = confine2
        max = confine1
    quadrantilaterali = [min]
    min = min + valorelat
    while min < max-N:
        quadrantilaterali.append(min)
        min = min + valorelat
    quadrantilaterali.append(max)

    return quadrantilaterali

def spawNumero(confine1, confine2 ,N, spawnOri, spawnVer): #confine 1, confine 2, quadranti che vuoi  in  una metà verticale, coordinata ori, coordinata verticale
    vettorediquadranti = DivisioneQuadrantiOriz(confine1, confine2 ,N)
    conta = 1
    for x in vettorediquadranti:
        if spawnOri >= x and spawnOri < vettorediquadranti[conta]:
            quadrante = conta
            break
        conta=conta+1
    if spawnVer < 0:
        quadrante = conta+N
    return quadrante

def quadrante(upordown,posizione,N):
    if upordown == 0:
        return posizione+1
    else:
        return posizione+1+N
