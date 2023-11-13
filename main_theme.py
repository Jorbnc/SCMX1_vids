from manim import *

# Dimensions
#config.frame_width = 60

# Colors
config.background_color = "#f9f9f9"
MBLACK = "#293241" # Blackish
DBLUE, MBLUE, LBLUE = "#003459", BLUE_D, PURE_BLUE
DRED, MRED, LRED = "#7D0000", RED_D, PURE_RED
DGREEN, MGREEN, LGREEN = "#004D00", GREEN_D, "#00F000"
HIGHLIGHT = LGREEN

Tex.set_default(color=MBLACK, #"#212427"
                #font_size=90,
                tex_template=TexFontTemplates.revx)
MathTex.set_default(color=MBLACK,
                    #font_size=90,
                    #tex_template=TexFontTemplates.biolinum
                    )

NumberLine.set_default(color=MBLACK)
DecimalNumber.set_default(color=MBLACK)

def FramedImage(filename, height=False, width=False):
    img = ImageMobject(filename)
    if height: 
        img.height = height
    if width:
        img.width = width
    surr = SurroundingRectangle(img, color=MBLACK, buff=0, corner_radius=0.02, stroke_width=1)
    return Group(img, surr)