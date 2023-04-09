from psychopy import visual
from numpy.random import random as npr
import random as rd
import raccoltaDati
import sizeinfo

# https://discourse.psychopy.org/t/how-to-control-signal-to-noise-contrast-ratio-for-a-gabor-noise-patch/6900

import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Set process DPI awareness to Per-Monitor DPI aware
except:
    pass

ctypes.windll.user32.SetProcessDPIAware()  # Set process DPI awareness to System DPI aware

windowBLACK = [-1, -1, -1]
WHITE = [1, 1, 1]
CS = 'rgb'

win = visual.Window(fullscr=True, units='pix', monitor='testMonitor', blendMode='avg',
                    color=windowBLACK, colorSpace=CS)

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
import psychopy.visual
import psychopy.event
from psychopy import visual, core, event
import pyglet.gl


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


import chime

coppia = True
sfuma = 1
text = visual.TextStim(win=win, text='Preme un tasto per iniziare', height=30)
text.draw()
win.flip()

#lettura di quanti cicli
with open('values.txt', 'r') as f:
    lines = f.readlines()
cicli = int(lines[1].split(':')[-1].strip())
#lettura del dizionario
dizionario = raccoltaDati.creazioneDizionario(2)

while event.waitKeys():
    # while app is open
    for x in range(cicli):
        primo = 0
        for y in range(2):
            # ottieni informazioni di spawn per quanto  riguarda il lato destro
            spawns = sizeinfo.spawnright()
            x_pos = rd.uniform(spawns[0], spawns[1])
            y_pos = rd.uniform(-spawns[2], spawns[2])

            quadrante = sizeinfo.spawNumero(spawns[0], spawns[1], 2, x_pos, y_pos)
            #"quadrante, xpos, ypos", quadrante, x_pos, y_pos)
            if y == 0:
                draw = rd.randint(0, 1)
                primo = draw
            # Set the position of the Gabor patch to the random coordinates
            spawns = sizeinfo.spawnright()
            s.pos = [x_pos, y_pos]
            n.pos = [x_pos, y_pos]
            visibilita = 0
            if draw == 0:
                draw += 1
                chime.success()
            else:
                draw -= 1
                chime.info()
            for x in range(22):
                if (x > 10):
                    visibilita = visibilita - 0.1
                else:
                    visibilita = visibilita + 0.1
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
                core.wait(0.05)
        l = True
        while l:
            text = visual.TextStim(win=win,
                                   text='Premere il tasto X se ha visto lo stimolo assieme al primo segnale audio, prema invece Y '
                                        'se lo stimolo è stato visto durante il secondo segnale audio, prema invece Z se '
                                        'non ha visto nessuno stimolo', height=30)
            text.draw()
            win.flip()
            keys = event.getKeys(['right', 'left', 'down'])
            if 'right' in keys:
                l = False
                if (primo == 0):
                    #("errato")
                    dizionario['Q' + str(quadrante)]["Sbagliati"] = dizionario['Q' + str(quadrante)]["Sbagliati"]  +1
                else:
                    #("correto")
                    dizionario['Q' + str(quadrante)]["Giusti"] = dizionario['Q' + str(quadrante)]["Giusti"]  +1

            if 'left' in keys:
                l = False
                if (primo == 0):
                    dizionario['Q' + str(quadrante)]["Giusti"] = dizionario['Q'+ str(quadrante)]["Giusti"]  +1
                    #("correto")
                else:
                    #("errato")
                    dizionario['Q' + str(quadrante)]["Sbagliati"] = dizionario['Q' + str(quadrante)]["Sbagliati"]  +1


            if 'down' in keys:
                l = False
                dizionario['Q' + str(quadrante)]["Non visti"] = dizionario['Q' + str(quadrante)]["Non visti"]  +1
                #print("non visto")
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
    break
raccoltaDati.datiGabor(2,dizionario)
win.close()
core.quit()

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

# if __name__ == "__main__":
#     run()
