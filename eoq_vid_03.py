from main_theme import *
from scm_mobjects import *
import math

saw1 = Sawtooth(teeth=5)

class eoq_03_01(MovingCameraScene):
    def construct(self):
        foo = Tex(r"Po2 Example").scale(3)
        self.add(foo)

# ====================================================================================================================
class test(Scene):
    def construct(self):
        self.add()

class eqtest(Scene):
    def construct(self):
        MathTex.set_default(font_size=50)
        expA = MathTex(r"\frac{2}{3}DT_{3}T_{1} + \frac{1}{3}DT_{3}T_{1}")
        self.add(expA)
        expB = MathTex(r"\frac{\frac{2}{3}DT_{3}T_{1} + \frac{1}{3}DT_{3}T_{1}}{T_3}")
        self.play(TransformByGlyphMap(expA, expB,
                                      ([], [])
                                      ), run_time=2)
        self.wait(0.5)

