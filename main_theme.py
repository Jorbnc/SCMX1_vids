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
    img = ImageMobject(filename).scale(0.99)
    if height: 
        img.height = height
    if width:
        img.width = width
    surr = SurroundingRectangle(img, color=MBLACK, buff=0.005, corner_radius=0.04, stroke_width=0.9)
    return Group(img, surr)

def Lot(rows, cols, color=MBLACK, stroke_color=DBLUE, buff=0.1, stroke_width=2):
    unit = RoundedRectangle(corner_radius=0.1, width=1, height=1, color=color, stroke_color=stroke_color,
                           stroke_width=stroke_width, fill_opacity=1).scale(0.25)
    return VGroup(*[unit.copy() for _ in range(rows*cols)]).arrange_in_grid(rows=rows, buff=buff)

def RightArrow(mobA, mobB, dir=RIGHT*5):
    mobB.next_to(mobA, dir)
    return Arrow(mobA.get_edge_center(RIGHT),
                 mobB.get_edge_center(LEFT),
                 color=MRED, max_tip_length_to_length_ratio=0.15, stroke_width=2)

def DownArrow(mobA, mobB, dir=DOWN*5):
    mobB.next_to(mobA, dir)
    return Arrow(mobA.get_center(),
                 mobB.get_center(),
                 color=MRED, max_tip_length_to_length_ratio=0.15, stroke_width=2.25)

# ============= CUSTOM ANIMATION: TRANSFORM BY GLYPH MAP (SAW ON MANIM'S DISCORD CHANNEL)
def ir(a,b): # inclusive range, useful for TransformByGlyphMap
    return list(range(a,b+1))

class TransformByGlyphMap(AnimationGroup):
    def __init__(self, mobA, mobB, *glyph_map, replace=True, from_copy=False, show_indices=False, **kwargs):
		# replace=False does not work properly
        if from_copy:
            self.mobA = mobA.copy()
            self.replace = True
        else:
            self.mobA = mobA
            self.replace = replace
        self.mobB = mobB
        self.glyph_map = glyph_map
        self.show_indices = show_indices

        animations = []
        mentioned_from_indices = []
        mentioned_to_indices = []
        for from_indices, to_indices in self.glyph_map:
            print(from_indices, to_indices)
            if len(from_indices) == 0 and len(to_indices) == 0:
                self.show_indices = True
                continue
            elif len(to_indices) == 0:
                animations.append(FadeOut(
                    VGroup(*[self.mobA[0][i] for i in from_indices]),
                    shift = self.mobB.get_center()-self.mobA.get_center()
                ))
            elif len(from_indices) == 0:
                animations.append(FadeIn(
                    VGroup(*[self.mobB[0][j] for j in to_indices]),
                    shift = self.mobB.get_center() - self.mobA.get_center()
                ))
            else:
                animations.append(Transform(
                    VGroup(*[self.mobA[0][i].copy() if i in mentioned_from_indices else self.mobA[0][i] for i in from_indices]),
                    VGroup(*[self.mobB[0][j] for j in to_indices]),
                    replace_mobject_with_target_in_scene=self.replace
                ))
            mentioned_from_indices.extend(from_indices)
            mentioned_to_indices.extend(to_indices)

        print(mentioned_from_indices, mentioned_to_indices)
        remaining_from_indices = list(set(range(len(self.mobA[0]))) - set(mentioned_from_indices))
        remaining_from_indices.sort()
        remaining_to_indices = list(set(range(len(self.mobB[0]))) - set(mentioned_to_indices))
        remaining_to_indices.sort()
        print(remaining_from_indices, remaining_to_indices)
        if len(remaining_from_indices) == len(remaining_to_indices) and not self.show_indices:
            for from_index, to_index in zip(remaining_from_indices, remaining_to_indices):
                animations.append(Transform(
                    self.mobA[0][from_index],
                    self.mobB[0][to_index],
                    replace_mobject_with_target_in_scene=self.replace
                ))
            super().__init__(*animations, **kwargs)
        else:
            print(f"From indices: {len(remaining_from_indices)}    To indices: {len(remaining_to_indices)}")
            print("Showing indices...")
            super().__init__(
                Create(index_labels(self.mobA[0], label_height=0.15, background_stroke_width=1, background_stroke_color=RED)),
                FadeIn(self.mobB.next_to(self.mobA, DOWN), shift=DOWN),
                Create(index_labels(self.mobB[0], label_height=0.15, background_stroke_width=1, background_stroke_color=RED)),
                Wait(5),
                lag_ratio=0.5
                )
            
# ============= SKIP SOME SCENES BY USING "SUBSCENES"
class MyScene(Scene):
    def construct(self):
        members = inspect.getmembers(type(self), predicate=inspect.isfunction)
        members = [ m for m in members if m[0].startswith("subscene") ]
        members = sorted(members, key=lambda x: inspect.getsourcelines(x[1])[1])

        for name, method in members:
            skip = False
            s = inspect.signature(method)
            if 'skip' in s.parameters:
                skip = s.parameters['skip'].default
            self.next_section(name, skip_animations=skip)
            print("Skipping" if skip else "Running", name)
            method(self)
            self.wait()

# Then you inherit from MyScene and instead of writing construct() you write
# separate methods. All those which start with "subscene" will be run, in the
# order they appear in the source. Those that declare `skip=True` do not produce
# animations but are run nevertheless, because they can create objects that
# are required later. Also manim renders the last frame of the skipped ones
# to allow the animation to "continue" after in the next one
class Test(MyScene):
    def subscene1(self):
        self.c = Circle()
        self.play(Create(self.c))

    def subscene2(self, skip=True):
        self.text = Text("This is a test")
        self.text.next_to(self.c, DOWN)
        self.play(Write(self.text))

    def subscene3(self):
        self.play(self.text.animate.next_to(self.c, UP))