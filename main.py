import psychopy
from numpy.random import random as npr
import random as rd
import psychopy.visual.backends.pygletbackend
from psychopy.hardware import crs

import pyglet
import pygame

import pygetwindow as gw

# import required module
from playsound import playsound

# for playing note.wav file


pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.mixer.init()
suono = pygame.mixer.Sound('audio1.wav')  # Crea oggetto suono con il file WAV
suono.set_volume(0.5)

# Puoi riprodurre il suono ogni volta che ne hai bisogno

import threading


def alert():
    # threading.Thread(target=playsound, args=('audio1.wav',), daemon=True).start()
    suono.play()


def draw_rg_grating(grating, red_gain=1.0, green_gain=1.0):
    # we will be changing these, so keep track of where they start
    start_phase = float(grating.phase[0])
    start_blendmode = grating.blendmode
    start_opacity = grating.opacity

    # when drawing, add to what is currently there
    grating.blendmode = "add"

    # red component

    # only affect the red channel
    pyglet.gl.glColorMask(1, 1, 1, 1)

    # use the opacity to set the gain
    grating.opacity = red_gain

    # draw *twice* to get full luminance at full opacity
    grating.draw()

    # green component

    # only affect the green channel
    pyglet.gl.glColorMask(0, 0, 0, 0)

    # set the gain of the green bars
    grating.opacity = green_gain

    # change the phase to draw in the gaps between the red bars

    # reset the drawing changes
    pyglet.gl.glColorMask(1, 1, 1, 1)
    grating.phase = start_phase
    grating.opacity = start_opacity


from numpy.random import random as npr


# def run():
#     X = 128  # width of gabor patch in pixels
#     sf = .1  # cycles per pixel
#     noiseTexture = npr([X, X]) * 2. - 1.  # a X-by-X array of random numbers in [-1,1]
#     gabor_tex = (
#                 visual.filters.makeGrating(res=X, cycles=X * sf) *
#                 visual.filters.makeMask(matrixSize=X, shape="gauss", range=[0, 1])
#         )
#
#     with psychopy.visual.Window(color="black") as win:
#
#         grating = psychopy.visual.GratingStim(
#             win=win,
#             mask="gauss",
#             sf=15.0,
#             units="height",
#             size=0.5,
#         )
#
#         # draw a red-green grating
#         grating.phase = 0
#         draw_rg_grating(
#             grating=grating,
#             red_gain=1,
#             green_gain=1,
#         )
#         win.flip()
#         psychopy.event.waitKeys()


def draw_ybrown_grating(grating, contrast=0.2):
    # we will be changing these, so keep track of where they start
    start_blendmode = grating.blendmode
    start_contrast = grating.contrast

    grating.blendmode = "avg"
    grating.contrast = contrast

    # only affect the red and green channels
    pyglet.gl.glColorMask(1, 1, 1, 1)

    grating.draw()

    # reset
    pyglet.gl.glColorMask(1, 1, 1, 1)
    grating.blendmode = start_blendmode
    grating.contrast = start_contrast

from random import randint
def main():
    veroSeDestra = True
    N=2
    from psychopy import visual
    import raccoltaDati
    import sizeinfo
    #psychopy.useVersion('2023.1.0')
    # https://discourse.psychopy.org/t/how-to-control-signal-to-noise-contrast-ratio-for-a-gabor-noise-patch/6900
    #print(crs)
    import ctypes

    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Set process DPI awareness to Per-Monitor DPI aware
    except:
        pass

    ctypes.windll.user32.SetProcessDPIAware()  # Set process DPI awareness to System DPI aware

    windowBLACK = [-1, -1, -1]
    WHITE = [1, 1, 1]
    CS = 'rgb'

    win = psychopy.visual.Window(fullscr=True, units='pix', monitor='testMonitor', blendMode='avg',
                                 color=windowBLACK, colorSpace=CS)
    win.nextEditable()
    X = int(sizeinfo.sizegabor())  # width of gabor patch in pixels
    sf = .08  # cycles per pixel
    noiseTexture = npr([X, X]) * 2. - 1.  # a X-by-X array of random numbers in [-1,1]

    gabor_tex = (
            visual.filters.makeGrating(res=X, cycles=X * sf) *
            visual.filters.makeMask(matrixSize=X, shape="gauss", range=[0, 1])
    )

    size = 520
    sf = 15  # spatial frequency in cycles per pixel
    ori = 0  # orientation in degrees
    phase = 1
    contrast = 1.0
    mean = 0.37  # mean luminance
    method = 'sin'  # sine wave grating

    # signal grating patch
    s = visual.GratingStim(
        win=win, tex=gabor_tex, mask=None,
        size=X, contrast=1.0, opacity=1.0,
        ori=ori,
        color=mean,
        phase=phase,
        colorSpace=CS,

    )

    # win = win, tex = gabor_tex, mask = None,
    #     size = X, contrast = 1.0, opacity = 1.0,

    # noise patch
    n = visual.GratingStim(
        win=win, mask='gauss',
        size=X, contrast=1.0, opacity=1.0, color=mean,
        colorSpace=CS,

    )

    from psychopy import visual, core, event
    import pyglet.gl

    import chime

    coppia = True
    sfuma = 1
    text = visual.TextStim(win=win, text='Preme un tasto per iniziare', height=30)
    text.draw()
    win.flip()

    # lettura di quanti cicli
    with open('values.txt', 'r') as f:
        lines = f.readlines()
    cicli = int(lines[1].split(':')[-1].strip())
    # lettura del dizionario
    dizionario = raccoltaDati.creazioneDizionario(N)
    t = True

    if veroSeDestra: # indovina indovinello qua ci arriva se è destra
        placeholder = sizeinfo.spawnright(N)
    else:
        placeholder = sizeinfo.spawnleft(N)
    spawnUp = placeholder[0]
    spawnDown = placeholder[1]
    while event.waitKeys():
        # while app is open
        for z in range(cicli*N*2):
            primo = 0
            for y in range(2):
                # ottieni informazioni di spawn per quanto  riguarda il lato destro







                # "quadrante, xpos, ypos", quadrante, x_pos, y_pos)
                if y == 0:
                    draw = rd.randint(0, 1)
                    primo = draw
                    spawnato = False
                    while not spawnato:  # qui viene contato sia lo spawn falso che quello vero  e non va bene
                        print("Processo di spawn z", z)
                        UpOrDown = randint(0, 1)  # 0 = up  1=down
                        posizioneQuadrante = randint(0, N - 1)
                        if UpOrDown == 0:
                            if spawnUp[posizioneQuadrante][
                                1] < cicli:  # [[corx,numero][corx,num],cory] [[0,1][50,1],36]
                                x_pos = spawnUp[posizioneQuadrante][0] - sizeinfo.getwinpixel()[0] / 2
                                y_pos = spawnUp[-1]
                                # spawnUp[posizioneQuadrante][1] = spawnUp[posizioneQuadrante][1] + 1 # questo serve per non spawnare il segnale più volte del necessario
                                print("up or down, quadrante, uscita", UpOrDown, posizioneQuadrante,
                                      spawnUp[posizioneQuadrante][1])
                                spawnato = True
                        if UpOrDown == 1:
                            if spawnDown[posizioneQuadrante][1] < cicli:
                                x_pos = spawnDown[posizioneQuadrante][0] - sizeinfo.getwinpixel()[0] / 2
                                y_pos = spawnDown[-1]
                                # spawnDown[posizioneQuadrante][1] = spawnDown[posizioneQuadrante][1] + 1 # questo serve per non spawnare il segnale più volte del necessario
                                print("up or down, quadrante, uscita", UpOrDown, posizioneQuadrante,spawnDown[posizioneQuadrante][1])
                                spawnato = True
                # Set the position of the Gabor patch to the random coordinates

                s.pos = [x_pos, y_pos]
                n.pos = [x_pos, y_pos]
                visibilita = 0
                if draw == 0:
                    alert()
                    draw += 1
                    # QUI CONTI
                    print("CONTIIIIIIIIIII")
                    if UpOrDown == 0:
                        print("UPPPPPPPPPPPP")
                        spawnUp[posizioneQuadrante][1] = spawnUp[posizioneQuadrante][1] + 1
                    else:
                        print("dooooooooooown")
                        spawnDown[posizioneQuadrante][1] = spawnDown[posizioneQuadrante][1] + 1
                    print("UPUP  quadrante, uscita",  posizioneQuadrante, spawnUp[posizioneQuadrante][1])
                    print("DOWN  quadrante, uscita",  posizioneQuadrante,spawnDown[posizioneQuadrante][1])

                else:
                    alert()
                    draw -= 1
                for o in range(10):
                    for x in range(6):
                        text = visual.TextStim(win=win, text='X', height=30, pos=[1111, 333])
                        text.draw()
                        if (x > 2):
                            visibilita = visibilita - 0.33333
                        else:
                            visibilita = visibilita + 0.33333
                        if draw == 1:



                            draw_rg_grating(
                                grating=s,
                                red_gain=visibilita,
                                green_gain=visibilita,
                            )
                            draw_rg_grating(
                                grating=n,
                                red_gain=visibilita,
                                green_gain=visibilita,
                            )
                        win.flip()
                        if draw==1:
                            #print(visibilita)
                            core.wait(0.016)
                        else:
                            core.wait(0.016)


            l = True
            event.clearEvents()
            while l:
                text = visual.TextStim(win=win,
                                       text='?',
                                       height=30,
                                       pos=[1111,333])
                text.draw()
                win.flip()
                keys = event.getKeys(['right', 'left', 'escape'])

                quadrante = sizeinfo.quadrante(UpOrDown, posizioneQuadrante, N)

                if 'right' in keys:
                    l = False
                    if (primo == 0):
                        # ("errato")
                        dizionario['Q' + str(quadrante)]["Sbagliati"] = dizionario['Q' + str(quadrante)]["Sbagliati"] + 1
                    else:
                        # ("correto")
                        dizionario['Q' + str(quadrante)]["Giusti"] = dizionario['Q' + str(quadrante)]["Giusti"] + 1

                if 'left' in keys:
                    l = False
                    if (primo == 0):
                        dizionario['Q' + str(quadrante)]["Giusti"] = dizionario['Q' + str(quadrante)]["Giusti"] + 1
                        # ("correto")
                    else:
                        # ("errato")
                        dizionario['Q' + str(quadrante)]["Sbagliati"] = dizionario['Q' + str(quadrante)]["Sbagliati"] + 1

                if 'escape' in keys:
                    l = False
                    t = False
                    try:
                        raccoltaDati.datiGabor(N, dizionario)
                    except:
                        print("")
                    win.close()
                    core.quit()

                    # print("non visto")
                # if draw:
                #     draw_rg_grating(
                #         grating=s,
                #         red_gain=1,
                #         green_gain=1,
                #     )
                #     draw_rg_grating(
                #         grating=n,
                #         red_gain=1,
                #         green_gain=1,
                #     )
                # time.sleep(1)
                # n.draw()  # draw noise in the background
                # s.draw()  # draw gabor on top of noise
                event.clearEvents('mouse')  # for pygame only
        while t:
            keys = event.getKeys(['right', 'left', 'down', 'escape'])
            text = visual.TextStim(win=win,
                                   text="La sessione è conclusa,  premere ESC per chiudere applicativo",
                                   height=30)
            text.draw()
            win.flip()
            if 'escape' in keys:
                print(dizionario)
                try:
                    raccoltaDati.datiGabor(N, dizionario)
                except:
                    print("")

                t = False
                win.close()
                core.quit()
        break


if __name__ == "__main__":
    main()

