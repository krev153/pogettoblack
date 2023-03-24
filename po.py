from psychopy import visual, core, event
from numpy.random import random as npr
import random as rd

# https://discourse.psychopy.org/t/how-to-control-signal-to-noise-contrast-ratio-for-a-gabor-noise-patch/6900
# open window
win = visual.Window([1024, 768], units='pix', monitor='testMonitor', blendMode='avg')

X = 128  # width of gabor patch in pixels
sf = .1  # cycles per pixel
noiseTexture = npr([X, X]) * 2. - 1.  # a X-by-X array of random numbers in [-1,1]

gabor_tex = (
        visual.filters.makeGrating(res=X, cycles=X * sf) *
        visual.filters.makeMask(matrixSize=X, shape="gauss", range=[0, 1])
)

size = 256
sf = 0.01  # spatial frequency in cycles per pixel
ori = 90  # orientation in degrees
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
    phase=phase

)

# win = win, tex = gabor_tex, mask = None,
#     size = X, contrast = 1.0, opacity = 1.0,

# noise patch
n = visual.GratingStim(
    win=win, mask='gauss', tex=noiseTexture,
    size=X, contrast=1.0, opacity=1.0, color=mean

)

while not event.getKeys():
    x_pos = rd.uniform(-400, 400)
    y_pos = rd.uniform(-300, 300)

    # Set the position of the Gabor patch to the random coordinates
    s.pos = [0, 0]
    n.pos = [0, 0]

    n.draw()  # draw noise in the background
    s.draw()  # draw gabor on top of noise
    core.wait(0.01)
    win.flip()
    event.clearEvents('mouse')  # for pygame only

win.close()
core.quit()