from main_theme import *
import math

COLOR_1 = MBLACK
COLOR_2 = DBLUE
COLOR_3 = MRED
COLOR_4 = DRED
COLOR_5 = "#005a85" # Slightly darker than DARK_BLUE

Tex.set_default(font_size=30)
MathTex.set_default(font_size=35)

class eoq_02_01(MovingCameraScene): # TRC Formula
    def construct(self):

        eoq_formula_1 = MathTex(r"Q = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=COLOR_1)
        eoq_surr = SurroundingRectangle(eoq_formula_1, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.25)
        eoq_1 = VGroup(eoq_formula_1, eoq_surr)
        TRC_1 = MathTex(r"TRC(Q) = c_t\frac{D}{Q} + c_e\frac{Q}{2}")
        VGroup(eoq_1, TRC_1).arrange(RIGHT, buff=1.75)

        self.play(Write(eoq_formula_1), Create(eoq_surr), run_time=1)
        self.wait(1)
        self.play(Write(TRC_1), run_time=1)
        self.wait(1)

        eoq_formula_2 = MathTex(r"Q^{*} = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=COLOR_1)
        eoq_formula_2.move_to(eoq_formula_1.get_center())
        TRC_2 = MathTex(r"TRC(Q^{*}) = c_t\frac{D}{Q^{*}} + c_e\frac{Q^{*}}{2}")
        TRC_2.move_to(TRC_1.get_center())


        rt = 1.25
        self.play(TransformByGlyphMap(eoq_formula_1, eoq_formula_2,
                                      ([0], [0]),
                                      ([], [1]),
                                      ([*ir(2,10)], [*ir(3,11)]),
                                      ),
                                      eoq_formula_2[0][1].animate.set_color(COLOR_3),
                                      run_time=rt)
        
        self.play(TransformByGlyphMap(TRC_1, TRC_2,
                                      ([*ir(0,4)], [*ir(0,4)]),
                                      ([], [5]),
                                      ([*ir(5,11)], [*ir(6,12)]),
                                      ([], [13]),
                                      ([*ir(12,15)], [*ir(14,17)]),
                                      ([], [18]),
                                      ([16,17], [19,20]),
                                      ),
                                      TRC_2[0][5].animate.set_color(COLOR_3),
                                      TRC_2[0][13].animate.set_color(COLOR_3),
                                      TRC_2[0][18].animate.set_color(COLOR_3),
                                      run_time=rt)
        self.wait(1)

        TRC_3 = MathTex(r"TRC(Q^{*}) = c_t\frac{D}{\sqrt{\frac{2Dc_{t}}{c_{e}}}} + c_e\frac{\sqrt{\frac{2Dc_{t}}{c_{e}}}}{2}")
        TRC_3.move_to(TRC_2.get_center())
        self.play(TransformByGlyphMap(TRC_2, TRC_3,
                                      ([*ir(0,10)], [*ir(0,10)]),
                                      ([12]*4, [12,13,14,15]),
                                      ([13]*5, [16,17,18,19,20]),
                                      ([*ir(14,16)], [*ir(21,23)]),
                                      ([17]*4, [24,25,26,27]),
                                      ([18]*5, [28,29,30,31,32]),
                                      ([19,20], [33,34])
                                      ),
                                      run_time=rt)
        self.wait(1)
        self.play(FadeOut(eoq_formula_2), FadeOut(eoq_surr), TRC_3.animate.move_to(ORIGIN), run_time=1.25)
        self.wait(1)
        
        TRC_4 = MathTex(r"TRC(Q^{*}) = c_t\frac{D\sqrt{c_{e}}}{\sqrt{2Dc_{t}}} + c_e\frac{\sqrt{2Dc_{t}}}{2\sqrt{c_{e}}}")
        self.play(TransformByGlyphMap(TRC_3, TRC_4,
                                      ([*ir(0,10)], [*ir(0,10)]),
                                      ([*ir(11,17)], [*ir(15,21)]),
                                      ([12,13,19,20], [11,12,13,14]),
                                      ([18], []),
                                      ([*ir(21,29)], [*ir(22,30)]),
                                      ([30], []),
                                      ([33,34], [31,32]),
                                      ([24,25,31,32], [33,34,35,36]),
                                      ),
                                      run_time=rt)
        self.wait(1)

        TRC_5 = MathTex(r"TRC(Q^{*}) = \frac{1}{\sqrt{2}}\frac{c_t}{\sqrt{c_t}}\frac{D}{\sqrt{D}}\sqrt{c_e} + \frac{\sqrt{2}}{2}\sqrt{c_t}\sqrt{D}\frac{c_e}{\sqrt{c_e}}")
        self.play(TransformByGlyphMap(TRC_4, TRC_5,
                                      ([*ir(0,7)], [*ir(0,7)]),
                                      ([15]*3, [9,15,21]),
                                      ([], [8]),
                                      ([16,17,18], [10,11,12]),
                                      ([8,9,16,17,20,21], [13,14,16,17,18,19]),
                                      ([10, 16, 17, 19], [20, 22, 23, 24]),
                                      ([11, 12, 13, 14], [25,26,27,28]),
                                      ([22], [29]),
                                      ([31]*2, [33,44]),
                                      ([23,24,33,34,35,36], [42,43,45,46,47,48]),
                                      ([25,26,27,32], [30,31,32,34]),
                                      ([25,26,28],[39,40,41]),
                                      ([25,26,29,30], [35,36,37,38]),
                                      ),
                                      run_time=rt)
        self.wait(1)

        #property_1 = MathTex(r"\frac{a}{\sqrt{a}}", color=COLOR_3).next_to(TRC_5, UP*4)
        property_2 = MathTex(r"\frac{a}{\sqrt{a}} = \frac{a}{\sqrt{a}}", color=COLOR_3).next_to(TRC_5, UP*4)
        property_3 = MathTex(r"\frac{a}{\sqrt{a}} = \frac{a}{\sqrt{a}}\frac{\sqrt{a}}{\sqrt{a}}", color=COLOR_3).move_to(property_2.get_center())
        property_4 = MathTex(r"\frac{a}{\sqrt{a}} = \frac{a\sqrt{a}}{a}", color=COLOR_3).move_to(property_2.get_center())
        property_5 = MathTex(r"\frac{a}{\sqrt{a}} = \sqrt{a}", color=COLOR_3).move_to(property_2.get_center())
        property_surr = SurroundingRectangle(property_3, color=COLOR_3, buff=0.2, stroke_width=2, corner_radius=0.2)
        property_5_group = VGroup(property_5, property_surr)

        self.play(Write(property_2), run_time=1)
        self.wait(1)
        self.play(TransformByGlyphMap(property_2, property_3,
                                      ([*ir(0,10)], [*ir(0,10)]),
                                      ([], [*ir(11,17)]),
                                      ), run_time=rt)
        self.wait(1)
        self.play(TransformByGlyphMap(property_3, property_4,
                                      ([*ir(0,5)], [*ir(0,5)]),
                                      ([6,11,12,13], [6,7,8,9]),
                                      ([7,14], [10,10]),
                                      ([8,9,10,15,16,17], [11]*6),
                                      ), run_time=rt)
        #self.wait(1)
        self.play(Create(property_surr),
                  TransformByGlyphMap(property_4, property_5,
                                      ([*ir(0,5)],[*ir(0,5)]),
                                      ([6,10,11], []),
                                      ([7,8,9], [6,7,8]),
                                      ), run_time=1)
        self.wait(1)

        property_6 = MathTex(r"\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}", color=COLOR_3)
        property_surr_6 = property_surr.copy().move_to(property_6.get_center())
        property_6_group = VGroup(property_6, property_surr_6).move_to(property_5_group.get_center())
        implies = MathTex(r"\implies", color=COLOR_3, font_size=50).move_to(property_5_group.get_center())

        property_6_group.shift(RIGHT*2),
        self.play(property_5_group.animate.shift(LEFT*2),
                  FadeIn(implies),
                  FadeIn(property_6_group),
                  run_time=1.5)
        self.wait(1)

        TRC_6 = MathTex(r"TRC(Q^{*}) = \frac{1}{\sqrt{2}}\sqrt{c_t}\sqrt{D}\sqrt{c_e} + \frac{\sqrt{2}}{2}\sqrt{c_t}\sqrt{D}\sqrt{c_e}")
        self.play(TransformByGlyphMap(TRC_5, TRC_6,
                                      ([*ir(0,7)], [*ir(0,7)]),
                                      ([*ir(8,12)], [*ir(8,12)]),
                                      ([*ir(16,19)], [*ir(13,16)]),
                                      ([15], []),
                                      ([13,14], [15,16]),
                                      ([*ir(22,24)], [*ir(17,19)]),
                                      ([21], []),
                                      ([20], [19]),
                                      ([*ir(25,41)],  [*ir(20,36)]),
                                      ([*ir(45,48)], [*ir(37,40)]),
                                      ([44], []),
                                      ([42,43], [39,40]),
                                      ), run_time=rt)
        self.wait(1)
        TRC_7 = MathTex(r"TRC(Q^{*}) = \frac{\sqrt{2}}{2}\sqrt{c_t}\sqrt{D}\sqrt{c_e} + \frac{\sqrt{2}}{2}\sqrt{c_t}\sqrt{D}\sqrt{c_e}")
        self.play(TransformByGlyphMap(TRC_6, TRC_7,
                                      ([*ir(0,7)], [*ir(0,7)]),
                                      ([*ir(13,40)], [*ir(13,40)]),
                                      ([8], []),
                                      ([9,10,11,12], [11,8,9,10]),
                                      ([12], [12])
                                      ), run_time=rt)
        self.wait(0.75)
        self.play(FadeOut(property_5_group), FadeOut(implies), FadeOut(property_6_group), run_time=0.75)
        self.wait(0.75)
        TRC_8 = MathTex(r"TRC(Q^{*}) = \frac{\sqrt{2c_{t}Dc_{e}}}{2} + \frac{\sqrt{2c_{t}Dc_{e}}}{2}")
        self.play(TransformByGlyphMap(TRC_7, TRC_8,
                                      ([*ir(0,7)], [*ir(0,7)]),
                                      ([8,9], [8,9]),
                                      ([13,14], [8,9]),
                                      ([17,18], [8,9]),
                                      ([20,21], [8,9]),
                                      ([10,15,16,19,22,23,11,12], [10,11,12,13,14,15,16,17]),
                                      ([24], [18]),
                                      ([25,26],[19,20]),
                                      ([30,31],[19,20]),
                                      ([34,35],[19,20]),
                                      ([37,38],[19,20]),
                                      ([27,32,33,36,39,40,28,29], [21,22,23,24,25,26,27,28]),
                                      ), run_time=rt)
        self.wait(0.5)
        TRC_9 = MathTex(r"TRC(Q^{*}) = \sqrt{2c_{t}Dc_{e}}}")
        self.play(TransformByGlyphMap(TRC_8, TRC_9,
                                      ([*ir(0,15)], [*ir(0,15)]),
                                      ([16,17,18,27,28], []),
                                      ([*ir(19,26)], [*ir(8,15)])
                                      ), run_time=1)
        TRC_10 = MathTex(r"TRC(Q^{*}) = \sqrt{2Dc_{t}c_{e}}}")
        TRC_surr = SurroundingRectangle(TRC_10, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.15)
        self.play(LaggedStart(TransformByGlyphMap(TRC_9, TRC_10,
                                      ([13], [11])),
                  Create(TRC_surr),
                  lag_ratio=0.35, run_time=1.25))
        self.wait(2)

TRC_10 = MathTex(r"TRC(Q^{*}) = \sqrt{2Dc_{t}c_{e}}}")
TRC_surr = SurroundingRectangle(TRC_10, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.15)
TRC_formula = VGroup(TRC_10, TRC_surr)

property_5 = MathTex(r"\frac{a}{\sqrt{a}} = \sqrt{a}", color=COLOR_3).next_to(TRC_10, UP*5)
property_surr = SurroundingRectangle(property_5, color=COLOR_3, buff=0.2, stroke_width=2, corner_radius=0.2)
property_5_group = VGroup(property_5, property_surr)
property_6 = MathTex(r"\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}", color=COLOR_3)
property_surr_6 = property_surr.copy().move_to(property_6.get_center())
property_6_group = VGroup(property_6, property_surr_6).move_to(property_5_group.get_center())
implies = MathTex(r"\implies", color=COLOR_3, font_size=50).move_to(property_5_group.get_center())
property_5_group.shift(LEFT*2)
property_6_group.shift(RIGHT*2)
properties_group = VGroup(property_5_group, implies, property_6_group)

class eoq_02_02(MovingCameraScene): # Sensitivity[Q] derivation
    def construct(self):
        self.add(TRC_formula)
        self.wait(1)
        
        opt_txt = Tex("Minimum Cost", color=COLOR_3).shift(DOWN*0.65)
        self.play(LaggedStart(TRC_formula.animate.shift(UP*0.25), Write(opt_txt),
                              lag_ratio=0.45, run_time=1.5))
        self.wait(0.75)
        self.play(FadeOut(opt_txt), run_time=1)

        sens_1 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{\frac{c_{t}D}{Q} + \frac{c_{e}Q}{2}}{\sqrt{2Dc_{t}c_{e}}}")
        sens_1.move_to(TRC_formula.get_center())
        self.play(LaggedStart(FadeOut(TRC_formula[1]),
                  TransformByGlyphMap(TRC_10, sens_1,
                                      ([*ir(0,7)], [*ir(7,14)]),
                                      ([*ir(8,15)], [*ir(27,34)]),
                                      ([], [*ir(0,6)]),
                                      ([], [*ir(15,26)]),
                                      ), lag_ratio=0.35, run_time=1.75))
        self.wait(1)

        sens_2 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{c_{t}D}{Q\sqrt{2Dc_{t}c_{e}}} + \frac{c_{e}Q}{2\sqrt{2Dc_{t}c_{e}}}")
        sens_2.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_1, sens_2,
                                      ([*ir(0,14)], [*ir(0,14)]),
                                      ([15,16,17,19], [15,16,17,19]),
                                      ([20], [28]),
                                      ([21,22,23,25], [29,30,31,33]),
                                      ([18,24], []),
                                      ([26], [18]),
                                      ([26], [32]),
                                      ([*ir(27,34)], [*ir(20,27)]),
                                      ([*ir(27,34)], [*ir(34,41)])
                                      ), run_time=1.25)
        self.wait(1)

        sens_3 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{Q}\frac{1}{\sqrt{2}}\frac{D}{\sqrt{D}}\frac{c_t}{\sqrt{c_t}}\frac{1}{\sqrt{c_e}} + \frac{1}{2}\frac{1}{\sqrt{2}}\frac{1}{\sqrt{D}}\frac{1}{\sqrt{c_t}}\frac{c_e}{\sqrt{c_e}}Q")
        sens_3.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_2, sens_3,
                                      ([*ir(0,14)], [*ir(0,14)]),
                                      ([18], [16]),
                                      ([18], [19]),
                                      ([18], [24]),
                                      ([18], [30]),
                                      ([18], [36]),
                                      ([], [15,18,35]),
                                      ([15,16,17], [28,29,23]),
                                      ([20,21], [20,21]),
                                      ([20,21], [25,26]),
                                      ([20,21], [31,32]),
                                      ([20,21], [37,38]),
                                      ([19,22,23,24,25,26,27], [17,22,27,33,34,39,40]),
                                      ([28], [41]), # +
                                      ([32], [43]),
                                      ([32], [46]),
                                      ([32], [51]),
                                      ([32], [56]),
                                      ([32], [63]),
                                      #([32], [69]),
                                      ([], [42,45,50,55]), #
                                      ([29,30,31], [61,62,68]),
                                      ([34,35], [47,48]),
                                      ([34,35], [52,53]),
                                      ([34,35], [57,58]),
                                      ([34,35], [64,65]),
                                      ([33,36,37,38,39,40,41], [44,49,54,59,60,66,67]),
                                      ), run_time=1.25)
        self.wait(1)
        self.play(FadeIn(properties_group), run_time=1)
        self.wait(1)

        sens_4 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{Q}\frac{1}{\sqrt{2}}\sqrt{D}\sqrt{c_t}\frac{1}{\sqrt{c_e}} + \frac{1}{2}\frac{1}{\sqrt{2}}\frac{1}{\sqrt{D}}\frac{1}{\sqrt{c_t}}\sqrt{c_e}Q")
        sens_4.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_3, sens_4,
                                      ([*ir(0,22)], [*ir(0,22)]),
                                      ([23], [25]),
                                      ([24], []),
                                      ([25,26,27], [23,24,25]),
                                      ([28,29], [28,29]),
                                      ([30], []),
                                      ([31,32,33,34], [26,27,28,29]),
                                      ([41], [36]),
                                      ([*ir(42,60)], [*ir(37,55)]),
                                      ([61,62], [58,59]),
                                      ([63], []),
                                      ([64,65,66,67,68], [56,57,58,59,60]),
                                      #([68,69,70], [60,61,62]),
                                     ), run_time=1.25)
        self.wait(1)

        sens_5 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{Q}\frac{\sqrt{2}}{2}\sqrt{D}\sqrt{c_t}\frac{1}{\sqrt{c_e}} + \frac{1}{2}\frac{1}{\sqrt{2}}\frac{1}{\sqrt{D}}\frac{1}{\sqrt{c_t}}\sqrt{c_e}Q")
        sens_5.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_4, sens_5,
                                      ([18], []),
                                      ([19], [21]),
                                      ([20,21,22], [18,19,20]),
                                      ([22], [22]),
                                      ), run_time=1.25)
        self.wait(1)
        self.play(FadeOut(properties_group), run_time=1)

        sens_6 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{Q}\frac{1}{2}\sqrt{2}\sqrt{D}\sqrt{c_t}\frac{1}{\sqrt{c_e}} + \frac{1}{2}\frac{1}{\sqrt{2}}\frac{1}{\sqrt{D}}\frac{1}{\sqrt{c_t}}\sqrt{c_e}Q")
        sens_6.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_5, sens_6,
                                      ([*ir(0,17)], [*ir(0,17)]),
                                      ([], [18]),
                                      ([21,22], [19,20]),
                                      ([18,19,20], [21,22,23]),
                                      ([*ir(23,60)], [*ir(24,61)])
                                      ), run_time=1.25)
        self.wait(1)

        eoq_formula_2 = MathTex(r"Q^{*} = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=COLOR_3).next_to(sens_6, UP*3.5)
        eoq_surr = SurroundingRectangle(eoq_formula_2, color=COLOR_3, stroke_width=2, buff=0.25, corner_radius=0.25)
        eoq_group = VGroup(eoq_formula_2, eoq_surr)

        self.play(FadeIn(eoq_group), run_time=1)
        self.wait(1)
        self.play(VGroup(*[sens_6[0][i] for i in range(21,31)]).animate.set_color(COLOR_3),
                  VGroup(*[sens_6[0][i] for i in range(33,37)]).animate.set_color(COLOR_3),
                  run_time=1)
        self.wait(1)
        self.play(VGroup(*[sens_6[0][i] for i in [43,44,45,48,49,50,53,54,55,56,57,58,59,60]]).animate.set_color(COLOR_3),
                  run_time=1)
        self.wait(1)

        sens_7 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{Q}\frac{1}{2}Q^{*} + \frac{1}{2}\frac{1}{Q^{*}}Q")
        sens_7.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_6, sens_7,
                                      ([*ir(0,20)], [*ir(0,20)]),
                                      ([*ir(21,30)], [21]*10),
                                      ([33,34,35,36], [22]*4),
                                      ([31,32],[]),
                                      ([37], [23]),
                                      ([38,39,40], [24,25,26]),
                                      ([43,44,45,48,49,50,53,54,55,56], [29]*10),
                                      ([57,58,59,60], [30]*4),
                                      ([61], [31]),
                                      ([41,42,46,47,51,52], []),
                                      ([], [27,28]),
                                      ), run_time=1.25)
        self.wait(1)
        self.play(FadeOut(eoq_group), run_time=0.75)
        self.wait(1)

        sens_8 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{Q^{*}}{Q} + \frac{Q}{Q^{*}} \right)")
        sens_8.move_to(TRC_formula.get_center())
        self.play(TransformByGlyphMap(sens_7, sens_8,
                                      ([*ir(0,14)], [*ir(0,14)]),
                                      ([18,19,20], [15,16,17]),
                                      ([24,25,26], [15,16,17]),
                                      ([], [18,28]),
                                      ([15,27], []),
                                      ([21,22,16,17], [19,20,21,22]),
                                      ([23], [23]),
                                      ([31,28,29,30], [24,25,26,27])
                                      ), run_time=1.25)
        sens_surr = SurroundingRectangle(sens_8, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.25)
        self.play(Create(sens_surr), run_time=1)
        self.wait(2)

class eoq_02_03(MovingCameraScene): # Sensitivity[Q]
    def construct(self):
        sens_f = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{Q^{*}}{Q} + \frac{Q}{Q^{*}} \right)")
        sens_surr = SurroundingRectangle(sens_f, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.25)
        sens = VGroup(sens_f, sens_surr).shift(UP*0.25)
        self.add(sens)
        self.play(sens.animate.shift(UP*2))

        MathTex.set_default(font_size=30)
        table1 = MobjectTable(
            [
            [MathTex(r"Q"), MathTex(r"TRC"), MathTex(r"Q/Q^{*}"), MathTex(r"TRC/TRC^{*}", font_size=23)],
            [MathTex(r"10\small{,}000"), MathTex(r"1\small{,}250"), MathTex(r"200\%"), MathTex(r"125\%")],
            [MathTex(r"7\small{,}500"), MathTex(r"1\small{,}083"), MathTex(r"150\%"), MathTex(r"108\%")],
            [MathTex(r"5\small{,}000"), MathTex(r"1\small{,}000"), MathTex(r"100\%"), MathTex(r"100\%")],
            [MathTex(r"2\small{,}500"), MathTex(r"1\small{,}250"), MathTex(r"50\%"), MathTex(r"125\%")],
            [MathTex(r"1\small{,}000"), MathTex(r"2\small{,}600"), MathTex(r"20\%"), MathTex(r"260\%")],
            ],
            v_buff=0.25, h_buff=0.25, include_outer_lines=True,
            line_config={"color": COLOR_1, "stroke_width": 2},
            arrange_in_grid_config={"col_alignments": "rrrc"})
        [table1.add_highlighted_cell(cell, color="#e3e3e3") for cell in [(1,1),(1,2),(1,3),(1,4)]]
        
        table2 = MobjectTable(
            [
            [MathTex(r"Q"), MathTex(r"TRC"), MathTex(r"Q/Q^{*}"), MathTex(r"TRC/TRC^{*}", font_size=23)],
            [MathTex(r"2\small{,}000"), MathTex(r"11\small{,}250"), MathTex(r"200\%"), MathTex(r"125\%")],
            [MathTex(r"1\small{,}500"), MathTex(r"9\small{,}750"), MathTex(r"150\%"), MathTex(r"108\%")],
            [MathTex(r"1\small{,}000"), MathTex(r"9\small{,}000"), MathTex(r"100\%"), MathTex(r"100\%")],
            [MathTex(r"500"), MathTex(r"11\small{,}250"), MathTex(r"50\%"), MathTex(r"125\%")],
            [MathTex(r"200"), MathTex(r"23\small{,}400"), MathTex(r"20\%"), MathTex(r"260\%")],
            ],
            v_buff=0.25, h_buff=0.25, include_outer_lines=True,
            line_config={"color": COLOR_1, "stroke_width": 2},
            arrange_in_grid_config={"col_alignments": "rrrc"})
        [table2.add_highlighted_cell(cell, color="#e3e3e3") for cell in [(1,1),(1,2),(1,3),(1,4)]]
        MathTex.set_default(font_size=35)

        VGroup(table1, table2).arrange(RIGHT, buff=1.1).shift(DOWN*1.25)

        params1 = MathTex(r"D=5\small{,}000 \quad c_t = 500 \quad c_e = 0.2", font_size=32).next_to(table1, UP*0.65)
        optQ1 = MathTex(r"*", font_size=50, color=COLOR_4).next_to(table1, LEFT*0.75).shift(DOWN*0.275)
        params2 = MathTex(r"D=15\small{,}000 \quad c_t = 300 \quad c_e = 9", font_size=32).next_to(table2, UP*0.65)
        optQ2 = MathTex(r"*", font_size=50, color=COLOR_4).next_to(table2, LEFT*0.75).shift(DOWN*0.275)

        self.play(FadeIn(table1), FadeIn(table2),
                  Write(params1), Write(params2),
                  run_time=1.5)
        self.wait()

        self.play(FadeIn(optQ1), FadeIn(optQ2),
                  table1.animate.set_row_colors(COLOR_1, COLOR_1, COLOR_1, COLOR_4), # COLOR_3
                  table2.animate.set_row_colors(COLOR_1, COLOR_1, COLOR_1, COLOR_4),
                  run_time=1)
        self.wait()

        highlight1 = VGroup(*[table1.get_highlighted_cell(pos, color=COLOR_3) for pos in [(x,y) for x in range(2,7) for y in range(3,5)]])
        highlight1.set_opacity(0.5)
        highlight2 = VGroup(*[table2.get_highlighted_cell(pos, color=COLOR_3) for pos in [(x,y) for x in range(2,7) for y in range(3,5)]])
        highlight2.set_opacity(0.5)
        table1.add_to_back(highlight1)
        table2.add_to_back(highlight2)
        self.play(FadeIn(highlight1), FadeIn(highlight2), run_time=1)
        self.wait()

        self.play(*[FadeOut(x) for x in [params1, params2, optQ1, optQ2, table1, table2]], run_time=1)

        grid = Axes(x_range=[0,4.25,0.25], y_range=[0.9,2.2,0.1],
                    x_length=11.5, y_length=6,
                    axis_config={"include_numbers": True, "color": COLOR_1, "font_size": 22,
                                 "decimal_number_config": {"num_decimal_places": 2}},
                    tips=False).to_edge(DOWN).shift(UP*0.35 + RIGHT*0.65)
        x_label = grid.get_x_axis_label(MathTex(r"Q/Q^{*}").scale(0.75), edge=DOWN, direction=DOWN, buff=0.25)
        y_label = grid.get_y_axis_label(MathTex(r"\frac{TRC}{TRC^*}").scale(0.75), edge=LEFT, direction=LEFT, buff=0.2)                   
        fig = VGroup(grid, x_label, y_label)
        
        def f(x):
            return (1/2)*(x + 1/x)
        sensitivity = grid.plot(f,
                                x_range=[0.24, 4.1],
                                color=COLOR_2, use_vectorized=True, stroke_width=3.5)
        
        optimal_1 = Dot(grid.c2p(1, f(1)), radius=0.075, color=COLOR_3)
        optimal_2 = MathTex(r"TRC^{*}", color=COLOR_3, font_size=33).move_to(grid.c2p(1, 1.075))
        optimal = VGroup(optimal_1, optimal_2)

        fsize = 30
        example1_1 = MathTex(r"Q^{*} = 750", font_size=fsize)
        example1_2 = MathTex(r"\frac{500}{750} \approx 0.67 \implies 1.08", font_size=fsize)
        example1_3 = MathTex(r"\frac{1000}{750} \approx 1.33 \implies 1.04", font_size=fsize)
        dot2 = Dot(grid.c2p(0.67, f(0.67)), radius=0.075, color=COLOR_3)
        dot3 = Dot(grid.c2p(1.33, f(1.33)), radius=0.075, color=COLOR_3)
        example1 = VGroup(example1_1, example1_2, example1_3).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        example1.move_to(grid.c2p(1.25,1.45))

        fact2_1 = Line(grid.c2p(0.5, f(0.5)), grid.c2p(2, f(2)), color=COLOR_3, stroke_width=2.5)
        fact2_2 = grid.get_vertical_lines_to_graph(sensitivity, [0.5,0.5], num_lines=1, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact2_3 = grid.get_vertical_lines_to_graph(sensitivity, [2,2], num_lines=1, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact2_4 = Dot(grid.c2p(0.5, f(0.5)), radius=0.075, color=COLOR_3)
        fact2_5 = Dot(grid.c2p(2, f(2)), radius=0.075, color=COLOR_3)
        fact2_6 = MathTex(r"TRC^{*}\times 1.25 \implies +25\%", color=COLOR_3, font_size=33).move_to(grid.c2p((2+0.5)/2, 1.3))
        fact2 = VGroup(fact2_1, fact2_2, fact2_3, fact2_4, fact2_5, fact2_6)

        fact3_1 = Line(grid.c2p(1/3, f(1/3)), grid.c2p(3, f(3)), color=COLOR_3, stroke_width=2.5)
        fact3_2 = grid.get_vertical_lines_to_graph(sensitivity, [1/3,1/3], num_lines=1, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact3_3 = grid.get_vertical_lines_to_graph(sensitivity, [3,3], num_lines=1, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact3_4 = Dot(grid.c2p(1/3, f(1/3)), radius=0.075, color=COLOR_3)
        fact3_5 = Dot(grid.c2p(3, f(3)), radius=0.075, color=COLOR_3)
        fact3_6 = MathTex(r"TRC^{*}\times 1.67 \implies +67\%", color=COLOR_3, font_size=33).move_to(grid.c2p((3+1/3)/2, 1.72))
        fact3 = VGroup(fact3_1, fact3_2, fact3_3, fact3_4, fact3_5, fact3_6)

        fact4_1 = Line(grid.c2p(1/4, f(1/4)), grid.c2p(4, f(4)), color=COLOR_3, stroke_width=2.5)
        fact4_2 = grid.get_vertical_lines_to_graph(sensitivity, [1/4,1/4], num_lines=2, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact4_3 = grid.get_vertical_lines_to_graph(sensitivity, [4,4], num_lines=2, line_func=Line, color=COLOR_3, stroke_width=2.5)
        fact4_4 = Dot(grid.c2p(1/4, f(1/4)), radius=0.075, color=COLOR_3)
        fact4_5 = Dot(grid.c2p(4, f(4)), radius=0.075, color=COLOR_3)
        fact4_6 = MathTex(r"TRC^{*}\times 2.125 \implies +112.5\%", color=COLOR_3, font_size=33).move_to(grid.c2p((4+1/4)/2, 2.065))
        fact4 = VGroup(fact4_1, fact4_2, fact4_3, fact4_4, fact4_5, fact4_6)

        self.play(FadeIn(fig), run_time=1)
        self.play(Create(sensitivity), run_time=1)
        self.play(LaggedStart(GrowFromCenter(optimal_1), Write(optimal_2),
                              lag_ratio=0.4, run_time=1))
        self.wait()
        self.play(Write(example1_1), run_time=0.75)
        self.play(Write(example1_2), run_time=0.75)
        self.play(FocusOn(dot2, opacity=0.05), run_time=0.75) # FOCUS
        self.play(GrowFromCenter(dot2), run_time=0.75)
        self.play(Write(example1_3), run_time=0.75)
        self.play(FocusOn(dot3, opacity=0.05), run_time=0.75) # FOCUS
        self.play(GrowFromCenter(dot3), run_time=0.75)
        self.wait()
        self.play(FadeOut(example1), FadeOut(dot2), FadeOut(dot3), run_time=0.75)

        self.play(LaggedStart(AnimationGroup(Create(fact2_2), Create(fact2_3)),
                              AnimationGroup(GrowFromCenter(fact2_4), GrowFromCenter(fact2_5)),
                              AnimationGroup(GrowFromCenter(fact2_1)),
                              lag_ratio=0.4, run_time=1.5))
        self.play(Write(fact2_6), run_time=0.75)

        self.play(LaggedStart(AnimationGroup(Create(fact3_2), Create(fact3_3)),
                              AnimationGroup(GrowFromCenter(fact3_4), GrowFromCenter(fact3_5)),
                              AnimationGroup(GrowFromCenter(fact3_1)),
                              lag_ratio=0.4, run_time=1.5))
        self.play(Write(fact3_6), run_time=0.75)

        self.play(FadeOut(sens), run_time=0.75)
        self.play(LaggedStart(AnimationGroup(Create(fact4_2), Create(fact4_3)),
                              AnimationGroup(GrowFromCenter(fact4_4), GrowFromCenter(fact4_5)),
                              AnimationGroup(GrowFromCenter(fact4_1)),
                              lag_ratio=0.25, run_time=2))
        self.play(Write(fact4_6), run_time=0.75)

        self.wait(2)

sens = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{Q^{*}}{Q} + \frac{Q}{Q^{*}} \right)")
sens_after = sens.copy()
sens_surr = SurroundingRectangle(sens, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.25)
sens_g = VGroup(sens, sens_surr)

class eoq_02_04(MovingCameraScene): # Sensitivity[Parameters]
    def construct(self):
        sens = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{Q^{*}}{Q} + \frac{Q}{Q^{*}} \right)")
        sens_after = sens.copy()
        sens_surr = SurroundingRectangle(sens, color=COLOR_1, stroke_width=2, buff=0.25, corner_radius=0.25)
        sens_g = VGroup(sens, sens_surr)
        opt_txt = Tex(r"Different vs. Optimal $Q$", color=COLOR_3).next_to(sens, UP*1.75)
        self.play(LaggedStart(FadeIn(sens_g), Write(opt_txt),
                              lag_ratio=0.25, run_time=1.25))
        self.wait()

        sens_2 = MathTex(r"\frac{TRC(Q_{F}^{*})}{TRC(Q_{A}^{*})} = \frac{1}{2}\left( \frac{Q_{A}^{*}}{Q_{F}^{*}} + \frac{Q_{F}^{*}}{Q_{A}^{*}} \right)")
        var_txt = Tex("Forecasted $Q^{*}$ vs. Actual $Q^{*}$", color=COLOR_3).next_to(sens_2, UP*1.75)
        self.play(FadeOut(sens_surr),
                  ReplacementTransform(opt_txt, var_txt),
                  TransformByGlyphMap(sens, sens_2,
                                      ([*ir(0,4)], [*ir(0,4)]),
                                      ([], [5,6]),
                                      ([*ir(5,12)], [*ir(7,14)]),
                                      ([], [15]),
                                      ([*ir(13,20)], [*ir(16,23)]),
                                      ([], [24,27,28]),
                                      ([21,22,23,24], [25,26,29,30]),
                                      ([], [31,32,36]),
                                      ([25,26,27,28], [33,34,35,37]),
                                      ),
                  run_time=1.25)
        self.wait(2)

        q_ratio_0 = MathTex(r"\frac{Q_{A}^{*}}{Q_{F}^{*}} =")
        q_ratio_D = MathTex(r"\frac{\displaystyle \sqrt{\frac{2D_{A}c_{t}}{c_e}}}{\displaystyle \sqrt{\frac{2D_{F}c_{t}}{c_e}}}}")
        q_ratio_ct = MathTex(r"\frac{\displaystyle \sqrt{\frac{2Dc_{t_{A}}}{c_e}}}{\displaystyle \sqrt{\frac{2Dc_{t_{F}}}{c_e}}}}")
        q_ratio_ce = MathTex(r"\frac{\displaystyle \sqrt{\frac{2Dc_{t}}{c_{e_{A}}}}}{\displaystyle \sqrt{\frac{2Dc_{t}}{c_{e_{F}}}}}}")
        q_ratio_color = VGroup(q_ratio_D[0][3:5], q_ratio_D[0][14:16],
                               q_ratio_ct[0][4:7], q_ratio_ct[0][15:18],
                               q_ratio_ce[0][7:10], q_ratio_ce[0][18:]).set_color(COLOR_3)
        q_ratio_col = VGroup(q_ratio_D, q_ratio_ct, q_ratio_ce).scale(0.8).arrange(DOWN, buff=0.4)
        q_ratio_brace = BraceBetweenPoints(q_ratio_D.get_corner(UL),
                                           q_ratio_ce.get_corner(DL),
                                           color=COLOR_3)
        
        q_ratio = VGroup(q_ratio_0, q_ratio_brace, q_ratio_col).arrange(RIGHT, buff=0.25).shift(RIGHT*2.10)

        self.play(sens_2.animate.shift(LEFT*3.35),
                  var_txt.animate.shift(LEFT*3.35),
                  FadeIn(q_ratio), run_time=1.5)
        self.wait()

        q_ratio_D_2 = MathTex(r"= \sqrt{\frac{D_A}{D_F}}").next_to(q_ratio_D, RIGHT*0.6)
        q_ratio_ct_2 = MathTex(r"= \sqrt{\frac{c_{t_A}}{c_{t_F}}}").next_to(q_ratio_ct, RIGHT*0.6)
        q_ratio_ce_2 = MathTex(r"= \sqrt{\frac{c_{e_A}}{c_{e_F}}}").next_to(q_ratio_ce, RIGHT*0.6)
        q_ratio_2 = VGroup(q_ratio_D_2, q_ratio_ct_2, q_ratio_ce_2)
        self.play(FadeIn(q_ratio_2), run_time=1.25)
        self.wait()

        sens_D = MathTex(r"\frac{TRC(Q_{F}^{*})}{TRC(Q_{A}^{*})} = \frac{1}{2}\left(\sqrt{\frac{D_A}{D_F}} + \sqrt{\frac{D_F}{D_A}}\right)")
        sens_D.next_to(sens_2.get_center(), DOWN*1).align_to(sens_2, LEFT)
        self.play(VGroup(q_ratio_ct, q_ratio_ct_2, q_ratio_ce, q_ratio_ce_2).animate.fade(0.65),
                  run_time=1.25)
        self.play(sens_2.animate.shift(UP*1), var_txt.animate.shift(UP*1),
                  FadeIn(sens_D),
                  run_time=1.25)
        self.wait()


        grid = Axes(x_range=[0,4.25,0.25], y_range=[0.9,2.2,0.1],
                    x_length=11.5, y_length=6,
                    axis_config={"include_numbers": True, "color": COLOR_1, "font_size": 22,
                                 "decimal_number_config": {"num_decimal_places": 2}},
                    tips=False).to_edge(DOWN).shift(UP*0.35 + RIGHT*0.65)
        x_label = grid.get_x_axis_label(MathTex(r"Q \text{ Ratio } {\vert} \text{ Parameter Ratio}").scale(0.75), edge=DOWN, direction=DOWN, buff=0.25)
        y_label = grid.get_y_axis_label(MathTex(r"\frac{TRC}{TRC^*}").scale(0.75), edge=LEFT, direction=LEFT, buff=0.2)                   
        fig = VGroup(grid, x_label, y_label)
        
        def f(x):
            return (1/2)*(x + 1/x)
        sensitivity_1 = grid.plot(f, x_range=[0.24, 4.1],
                                  color=COLOR_1, use_vectorized=True, stroke_width=3)
        
        colD = COLOR_5
        def g(x):
            return (1/2)*(math.sqrt(x) + math.sqrt(1/x))
        g = np.vectorize(g)
        sensitivity_2 = grid.plot(g, x_range=[0.058, 4.1],
                                  color=colD, use_vectorized=True, stroke_width=3)
        
        self.play(*[FadeOut(mob) for mob in [var_txt, sens_2, q_ratio, q_ratio_2]], run_time=1)
        sens_after.scale(0.8).move_to(grid.c2p(2.25, 1.8, 0)).set_color(COLOR_1),
        self.play(FadeIn(fig),
                  FadeIn(sens_after), Create(sensitivity_1),
                  sens_D.animate.scale(0.8).move_to(grid.c2p(3.5, 1.4, 0)).set_color(colD),
                  Create(sensitivity_2),
                  run_time=1.5)
        
        q_pointers = VGroup(MathTex(r"\frac{Q_{A}^{*}}{Q_{F}^{*}}", color=colD).scale(0.7).next_to(sens_D[0][23], UP*2),
                            MathTex(r"\frac{Q_{F}^{*}}{Q_{A}^{*}}", color=colD).scale(0.7).next_to(sens_D[0][31], UP*2))
        q_pointers_arr = VGroup(Arrow(sens_D[0][23].get_center(), q_pointers[0].get_edge_center(DOWN),
                                      color=COLOR_3, buff=0.1, stroke_width=3),
                                Arrow(sens_D[0][31].get_center(), q_pointers[1].get_edge_center(DOWN),
                                      color=COLOR_3, buff=0.1, stroke_width=3),
                                      )
        self.play(FadeIn(q_pointers), GrowArrow(q_pointers_arr[0]), GrowArrow(q_pointers_arr[1]),
                  run_time=1)
        self.wait()

        example_D = MathTex(r"\frac{D_A}{D_F} = \frac{20\small{,}000}{10\small{,}000} = 2",
                          color=COLOR_5).scale(0.75).move_to(grid.c2p(0.95, 1.35, 0))
        example_then = MathTex(r"\implies \frac{Q_{A}^{*}}{Q_{F}^{*}} = \sqrt{2}", color=COLOR_5).scale(0.75)
        example_then.next_to(example_D, RIGHT*0.85)

        self.play(Write(example_D), run_time=1)
        self.wait()
        self.play(Write(example_then), run_time=1)
        self.wait()

        dot_2 = Dot(example_D[0][-1].get_center(), radius=0.065, color=COLOR_3)
        dot_sqrt = Dot(example_then[0][-1].get_center(), radius=0.065, color=COLOR_3)
        self.play(GrowFromCenter(dot_2), run_time=1)
        self.play(dot_2.animate.move_to(grid.c2p(2,g(2),0)), run_time=1)
        self.play(GrowFromCenter(dot_sqrt), run_time=1)
        self.play(dot_sqrt.animate.move_to(grid.c2p(math.sqrt(2),f(math.sqrt(2)),0)), run_time=1)
        dot_line = Line(dot_2.get_center(), dot_sqrt.get_center(), color=COLOR_3, stroke_width=2)
        self.play(GrowFromEdge(dot_line, LEFT), run_time=1)
        self.wait(2)

class eoq_02_05(MovingCameraScene): # Sensitivity[T]
    def construct(self):
        
        grid = Axes(x_range=[0,95,15], y_range=[0,110,25], 
                    x_length=7, y_length=2.7,
                    axis_config={"include_numbers": False, "tick_size": 0.05},
                    tips=False).shift(UP*1.75)
        x_values = [0,0,30,30,60,60,90]
        sawtooth = grid.plot_line_graph(
            x_values = x_values,
            y_values = [100 if i % 2 else 0 for i in range(len(x_values))],
            line_color = COLOR_1, stroke_width = 3.5, add_vertex_dots=False
            )
        brace = BraceBetweenPoints(grid.c2p(30,0,0), grid.c2p(60,0,0), buff=0.25, color=COLOR_3)
        T = MathTex(r"T^{*} = Q^{*}/D").next_to(brace, DOWN*0.5)
        T_2 = MathTex(r"T^{*} = Q^{*}/D \implies Q^* = DT^{*}").next_to(brace, DOWN*0.5)
        sens.next_to(T_2, DOWN*3.25)

        sens_replace = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{DT^{*}}{DT} + \frac{DT}{DT^{*}} \right)")
        sens_replace.move_to(sens.get_center())
        sens_replace_2 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{T^{*}}{T} + \frac{T}{T^{*}} \right)")
        sens_replace_2.move_to(sens.get_center())
        sens_T = MathTex(r"\frac{TRC(T)}{TRC(T^{*})} = \frac{1}{2}\left( \frac{T^{*}}{T} + \frac{T}{T^{*}} \right)")
        sens_T.move_to(sens.get_center())

        self.play(FadeIn(grid), FadeIn(sawtooth), run_time=1.25)
        self.play(GrowFromCenter(brace), Write(T), run_time=1)
        self.wait(0.5)
        self.play(TransformByGlyphMap(T, T_2,
                                      ([*ir(0,6)], [*ir(0,6)]),
                                      ([], [*ir(7,14)])
                                      ),
                  run_time=1.25)
        self.wait(0.5)
        self.play(FadeIn(sens), run_time=1)
        self.play(TransformByGlyphMap(sens, sens_replace,
                                      ([*ir(0,18)],[*ir(0,18)]),
                                      ([19,19,20], [19,20,21]),
                                      ([21], [22]),
                                      ([22,22], [23,24]),
                                      ([23], [25]),
                                      ([24,24], [26,27]),
                                      ([25], [28]),
                                      ([26,26,27,28], [29,30,31,32])
                                      ), run_time=1.25)
        
        self.play(TransformByGlyphMap(sens_replace, sens_replace_2,
                                      ([19,23,26,29], [])
                                      ), run_time=1.25)
        
        related = Tex(r"($T$ and $Q$ are directly related)", color=COLOR_3).scale(0.9).next_to(sens_T, DOWN*1)
        self.play(LaggedStart(TransformByGlyphMap(sens_replace_2, sens_T,
                                      ([4, 10], [4, 10])
                                      ),
                Write(related),
                lag_ratio=0.4, run_time=1.5))

        self.wait(2)

# ====================================================================================================================
class test(Scene):
    def construct(self):
        grid = Axes(x_range=[0,95,15], y_range=[0,110,25], 
                    x_length=7, y_length=2.7,
                    axis_config={"include_numbers": False, "tick_size": 0.05},
                    tips=False).shift(UP*1.75)
        x_values = [0,0,30,30,60,60,90]
        sawtooth = grid.plot_line_graph(
            x_values = x_values,
            y_values = [100 if i % 2 else 0 for i in range(len(x_values))],
            line_color = COLOR_1, stroke_width = 3.5, add_vertex_dots=False
            )
        brace = BraceBetweenPoints(grid.c2p(30,0,0), grid.c2p(60,0,0), buff=0.25, color=COLOR_3)
        T = MathTex(r"T^{*} = Q^{*}/D \implies Q^* = DT^{*}").next_to(brace, DOWN*0.5)
        sens.next_to(T, DOWN*3.25)

        sens_replace = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{DT^{*}}{DT} + \frac{DT}{DT^{*}} \right)")
        sens_replace.move_to(sens.get_center())
        sens_replace_2 = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{T^{*}}{T} + \frac{T}{T^{*}} \right)")
        sens_replace_2.move_to(sens.get_center())

        self.add(grid, sawtooth,
                 brace, T,
                 #sens,
                 #sens_replace,
                 sens_replace_2
                 )

# ====================================================================================================================
class eqtest(Scene):
    def construct(self):
        MathTex.set_default(font_size=50)
        expA = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{DT^{*}}{DT} + \frac{DT}{DT^{*}} \right)")
        expB = MathTex(r"\frac{TRC(Q)}{TRC(Q^{*})} = \frac{1}{2}\left( \frac{T^{*}}{T} + \frac{T}{T^{*}} \right)")
        self.add(expA)
        self.play(TransformByGlyphMap(expA, expB,
                                      ([19,23,26,29], [])
                                      ), run_time=2)
        self.wait(0.5)