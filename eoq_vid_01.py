from main_theme import *
import random
from itertools import *

COLOR_1 = MBLACK
COLOR_2 = DBLUE
COLOR_3 = MRED
COLOR_4 = DRED

# EOQ Formula
formula = MathTex(r"Q^{*} = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=COLOR_1).move_to([0, 0, 0])
formula_surr = SurroundingRectangle(formula, color=COLOR_1, buff=0.4, corner_radius=0.25)
formula_and_surr = VGroup(formula, formula_surr)

#First Axis
grid = Axes(x_range=[0, 365, 30], y_range=[0, 500, 100], x_length=11, y_length=3.5,
            axis_config={"color": COLOR_1, "font_size": 24}, tips=False)

# Labels for the x-axis and y-axis.
y_label = grid.get_y_axis_label(Tex("Inventory").scale(0.65).rotate(90 * DEGREES),
                                edge=LEFT, direction=LEFT, buff=0.3)
x_label = grid.get_x_axis_label(Tex("Time").scale(0.65),edge=DOWN, direction=DOWN, buff=0.3)

# EOQ: D = 2400, ct=100, ce=3 => Q = 400
replenishments = 6 #2400/400
replenishment_period = (400/2400)*365
x_values = [i * replenishment_period for n in range(replenishments) for i in (n, n)] + [365]
sawtooth = grid.plot_line_graph(
    x_values = x_values,
    y_values = [400 if i % 2 else 0 for i in range(len(x_values))],
    line_color = COLOR_2, stroke_width = 3, add_vertex_dots=False,
)

class eoq_01_01(MovingCameraScene):

    def construct(self):

        # EOQ: INTRODUCTION + FORMULA
        eoq_text = Tex(r"Economic Order Quantity").scale(1.5)
        eoq_math = MathTex(r"EOQ")
        self.play(Write(eoq_text), run_time=1)
        self.play(ReplacementTransform(eoq_text, eoq_math), run_time=1)
        self.wait(1)

        op_scm_text = Tex(r"Operations Management\\Supply Chain Management").scale(1.5)
        self.play(eoq_math.animate.move_to([0,1.5,0]), run_time=0.5, rate_func=smooth)
        self.wait(1)
        self.play(Write(op_scm_text), run_time=1.5)
        self.play(FadeOut(op_scm_text), run_time=0.7)
        self.play(ReplacementTransform(eoq_math, formula), run_time=1)
        self.play(Create(formula_surr), run_time=1)
        self.wait(1)

        # FIRST AXIS AND SAWTOOTH: CREATE
        q_dot = Dot(point=grid.c2p(0, 400, 0), radius=0.05, color=COLOR_3)
        self.play(FadeIn(grid), FadeIn(x_label), FadeIn(y_label),
                  ReplacementTransform(formula_and_surr, q_dot),
                  run_time=2, rate_func=smooth)
        self.play(Create(sawtooth, run_time=1.75, rate_func=linear))

        # SECOND AXIS: DEFINE + CREATE
        grid_2= Axes(x_range=[0, 1600, 200], y_range=[0, 3000, 500],
                     x_length=11, y_length=3.5,
                     axis_config={"color": COLOR_1,"font_size": 24}, tips=False)
        y_label_2 = grid.get_y_axis_label(Tex("Cost").scale(1.1).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label_2 = grid.get_x_axis_label(Tex("Order Quantity").scale(1.1),
                                        edge=DOWN, direction=DOWN, buff=0.3)
        q_dot_2 = Dot(point=grid_2.c2p(400, 0, 0), radius=0.05, color=COLOR_3)
        self.play(ReplacementTransform(grid, grid_2),
                  ReplacementTransform(x_label, x_label_2), ReplacementTransform(y_label, y_label_2),
                  FadeOut(sawtooth),
                  ReplacementTransform(q_dot, q_dot_2),
                  run_time=1, rate_func=smooth)

        # INVENTORY COST FUNCTIONS: DEFINITION
        x_values_2 = np.arange(1, 1600, 20)
        holding_cost = grid_2.plot_line_graph(
            x_values = x_values_2,
            y_values = [3*x/2 for x in x_values_2],
            line_color = COLOR_2, stroke_width = 2, add_vertex_dots=False)
        setup_cost = grid_2.plot_line_graph(
            x_values = np.arange(80, 1600, 20),
            y_values = [100*2400/x for x in np.arange(80, 1600, 20)],
            line_color = COLOR_2, stroke_width = 2, add_vertex_dots=False)
        total_cost = grid_2.plot_line_graph(
            x_values = np.arange(80, 1600, 20),
            y_values = [3*x/2 + 100*2400/x for x in np.arange(80, 1600, 20)],
            line_color = COLOR_2, stroke_width = 4, add_vertex_dots=False)

        # OPTIMAL POINTS: SHOW
        opt_point = Dot(point=grid_2.c2p(400, 1200, 0), radius=0.05, color=COLOR_3)
        min_text = Tex("Minimum Total Cost", font_size=20, color=COLOR_3).move_to(grid_2.c2p(500, 1500, 0))
        line_1 = Line(start=q_dot_2.get_center(), end=grid_2.c2p(400, 1200, 0), stroke_width=1, color=COLOR_3)

        # SHOW HOLDING AND SETUP COSTS
        self.play(Create(holding_cost), Create(setup_cost),run_time=1, rate_func=linear)
        self.play(Create(total_cost), Create(line_1),run_time=0.75, rate_func=smooth)
        self.play(Create(opt_point), Write(min_text),run_time=0.50, rate_func=smooth)
        self.wait(0.75)

        holding_text = Tex(r"Holding cost", font_size=20, color=COLOR_3).move_to(grid_2.c2p(1000, 1200, 0))
        setup_text = Tex(r"Ordering cost", font_size=20, color=COLOR_3).move_to(grid_2.c2p(800, 500, 0))
        self.play(holding_cost.animate.set_color(COLOR_3), Write(holding_text), run_time=0.5)
        self.play(holding_cost.animate.set_color(COLOR_2), holding_text.animate.set_color(COLOR_2), run_time=0.5)
        self.play(setup_cost.animate.set_color(COLOR_3), Write(setup_text), run_time=0.5)
        self.play(setup_cost.animate.set_color(COLOR_2), setup_text.animate.set_color(COLOR_2), run_time=0.5)
        self.wait(1)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=1) # FadeOut all mobjects in this scene
        self.wait(1)

class eoq_01_02(MovingCameraScene):

    def construct(self):
        txt_scale = 1.5
        formula_and_surr.move_to([0, 2.25, 0])
        eoq_model = VGroup(grid, sawtooth, x_label, y_label).move_to([0, -0.75, 0])
        self.play(FadeIn(formula_and_surr), FadeIn(eoq_model), run_time=1.5)
        self.wait(3) # 12
        
        x_axis_lenght = 17
        y_axis_length = 5

        # ============= EPQ
        ax1 = Axes(x_range=[0, 365, 73], y_range=[0, 400, 100],
                   x_length=x_axis_lenght, y_length=3,
                   axis_config={"color":COLOR_1},tips=False)
        p = 25
        epq_values = [0, 0+p, 73, 73+p, 146, 146+p, 219, 219+p, 292, 292+p, 365]
        epq = ax1.plot_line_graph(x_values=epq_values,
                                  y_values=[350 if i % 2 else 0 for i in range(len(epq_values))],
                                  line_color=COLOR_2, stroke_width=3, add_vertex_dots=False)
        epq_vlines = VGroup()
        for x in epq_values[1::2]: # Starting at index 1, every 2 indices
            epq_vlines += ax1.get_vertical_line(ax1.c2p(x, 350),
                                                line_config={"dashed_ratio": 0.8}, color=COLOR_2)
        epq_text = Tex(r"Finite Replenishment").scale(1.8).next_to(ax1.c2p(5, 420), RIGHT)
        epq_model = VGroup(ax1, epq, epq_vlines, epq_text)

        # ============= CONTINUOUS REVIEW
        ax2 = Axes(x_range=[0, 365, 73], y_range=[0, 600, 100],
                   x_length=x_axis_lenght, y_length=y_axis_length,
                   axis_config={"color": COLOR_1,"font_size": 24}, tips=False)
        
        def get_continuous_data(I_0, s, Q):
            x_onhand, x_ip, time = [0], [0], 0
            y_onhand, y_ip, level = [I_0], [I_0], I_0
            for _ in range(96):
                time += 2.34
                level -= random.randint(1,25)
                if level > s:
                    x_onhand.append(time), y_onhand.append(level)
                    x_ip.append(time), y_ip.append(level)
                else:
                    x_ip.extend([time, time]), y_ip.extend([level, level + Q])
                    x_onhand.append(time), y_onhand.append(level)
                    for _ in range(8):
                        time += 2.34
                        level -= random.randint(1,25)
                        x_onhand.append(time), y_onhand.append(level)
                        x_ip.append(time), y_ip.append(level + Q)
                    level += Q  
                    x_onhand.append(time), y_onhand.append(level)
            return x_onhand, y_onhand, x_ip, y_ip, s
        continuous_x_onhand, continuous_y_onhand, continuous_x_ip, continuous_y_ip, s = get_continuous_data(I_0=375, s=230, Q=265)

        continuous_onhand = ax2.plot_line_graph(x_values = continuous_x_onhand,
                                                y_values = continuous_y_onhand,
                                                line_color = COLOR_2, stroke_width=3, add_vertex_dots=False)
        continuous_ip = ax2.plot_line_graph(x_values = continuous_x_ip,
                                            y_values = continuous_y_ip,
                                            line_color = COLOR_2, stroke_width=2, add_vertex_dots=False)
        continuous_ip = DashedVMobject(continuous_ip["line_graph"], num_dashes=250)
        s_limit = ax2.get_horizontal_line(ax2.c2p(365, s), line_config={"dashed_ratio": 0.9}, stroke_width=3, color=COLOR_4)
        continuous_text = Tex(r"Continuous Review").scale(1.8).next_to(ax2.c2p(5, 600), RIGHT)
        continuous_model = VGroup(ax2, continuous_onhand, s_limit, continuous_ip, continuous_text)
        
        # ============= PERIODIC REVIEW
        ax3 = Axes(x_range=[0, 365, 73], y_range=[0, 600, 100],
                   x_length=x_axis_lenght, y_length=y_axis_length,
                   axis_config={"color":COLOR_1,"font_size": 24}, tips=False)
        
        def get_periodic_data(I_0, S):
            x_onhand, x_ip, time = [0], [0], 0
            y_onhand, y_ip, level = [I_0], [I_0], I_0
            for _ in range(5):
                for _ in range(20):
                    level -= random.randint(1,22)
                    time += 2.44
                    x_onhand.append(time), y_onhand.append(level)
                    x_ip.append(time), y_ip.append(level)
                x_ip.append(time), y_ip.append(S)
                diff = S - y_onhand[-1]
                for _ in range(10):
                    level -= random.randint(1,22)
                    time += 2.34
                    x_onhand.append(time), y_onhand.append(level)
                    x_ip.append(time), y_ip.append(level + diff)
                level += diff
                x_onhand.append(time), y_onhand.append(level)

            return x_onhand, y_onhand, x_ip, y_ip, S
            
        periodic_x_onhand, periodic_y_onhand, periodic_x_ip, periodic_y_ip, S = get_periodic_data(I_0=400, S=550)

        periodic_plot = ax3.plot_line_graph(x_values = periodic_x_onhand,
                                            y_values = periodic_y_onhand,
                                            line_color = COLOR_2, stroke_width = 3, add_vertex_dots=False)
        periodic_ip = ax2.plot_line_graph(x_values = periodic_x_ip,
                                            y_values = periodic_y_ip,
                                            line_color = COLOR_2, stroke_width=2, add_vertex_dots=False)
        periodic_ip = DashedVMobject(periodic_ip["line_graph"], num_dashes=250)
        S_limit = ax3.get_horizontal_line(ax3.c2p(365, S), line_config={"dashed_ratio": 0.9}, stroke_width=3, color=COLOR_4)
        periodic_text = Tex(r"Periodic Review").scale(1.8).next_to(ax3.c2p(5, 620), RIGHT)
        
        periodic_model = VGroup(ax3, periodic_plot, S_limit, periodic_ip, periodic_text)

        # ============= ADD AXIS LABELS TO ALL MODELS (VGROUPS)
        for ax, model in [(ax1, epq_model), (ax2, continuous_model), (ax3, periodic_model)]:
            model += ax.get_x_axis_label(Tex("Time").scale(0.65), edge=DOWN, direction=DOWN, buff=0.1)

        # All models and zoom out
        VGroup(epq_model, continuous_model, periodic_model).arrange(DOWN, buff=0.75, center=False, aligned_edge=LEFT).move_to([15.75, 0, 0])
        
        final_arrow = Arrow(start=LEFT, end=RIGHT, color=COLOR_3, stroke_width=4.5,
                            max_tip_length_to_length_ratio=0.15,).next_to(formula_and_surr, RIGHT*2)
        core_concept_text = Tex(r"Core Concept").scale(txt_scale).next_to(final_arrow, RIGHT*2)
        next_text = Tex(r"Fundamental\\Strategy") # Tex(r"Fundamental\\Strategy", tex_environment="flushleft") # to align left
        next_text.scale(txt_scale).next_to(final_arrow, RIGHT*2)

        self.play(self.camera.frame.animate.scale(1.15).move_to([1.25, 0, 0]),
                  GrowArrow(final_arrow), Write(core_concept_text), run_time=1)
        self.wait(6.25)
        self.play(ReplacementTransform(core_concept_text, next_text), run_time=1)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(2).move_to([9.5, 0, 0]), 
                  FadeOut(next_text), FadeOut(final_arrow),
                  FadeIn(ax1), FadeIn(epq_model[-1]),
                  FadeIn(ax2), FadeIn(continuous_model[-1]),
                  FadeIn(ax3), FadeIn(periodic_model[-1]),
                  run_time=1.25)
        self.play(Create(epq), Create(epq_vlines), Write(epq_text),
                  Create(continuous_ip), Create(continuous_onhand), Create(s_limit), Write(continuous_text),
                  Create(periodic_ip), Create(periodic_plot), Create(S_limit), Write(periodic_text),
                  run_time=2)
        self.wait(1.25)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=1) # FadeOut all mobjects in this scene
        self.wait(1)

class eoq_01_03(MovingCameraScene):

    def construct(self):

        timeline = NumberLine(x_range=[1900, 2030, 10],  length=12,
                              numbers_to_include=[1900, 1913, 1950, 2000, 2020],
                              tick_size=0.075, font_size=25,
                              decimal_number_config={"group_with_commas": False,
                                                     "num_decimal_places": 0}).move_to([0,-3,0])
        
        text_1913 = MathTex(r"1913", color=COLOR_3)
        dot_1913 = Dot(timeline.n2p(1913), 0.05, color=COLOR_3)
        self.play(GrowFromEdge(timeline, LEFT), run_time=1)
        self.play(Write(text_1913), run_time=0.75)
        self.play(ReplacementTransform(text_1913, dot_1913), run_time=0.75)
        
        harris_pic = FramedImage("img/0_harris.jpg", height=4.5)
        harris_name = Tex("Ford Whitman Harris", font_size=25).next_to(harris_pic, UP)
        harris = Group(harris_pic, harris_name)
        self.play(FadeIn(harris_pic), Write(harris_name), run_time=1)
        self.wait(4.75)

        paper1 = FramedImage("img/0_paper1.png", height=4.5).move_to([2.005,0,0])
        source = Tex(r"Images: www.academia.edu", font_size=17).to_edge(DOWN + RIGHT).shift(UP)
        self.play(harris.animate.shift(LEFT*2), FadeIn(paper1), Write(source), run_time=1)
        factory = Tex(r"\textit{Factory,\\The Magazine of Management}", font_size=20).next_to(paper1, UP)
        self.wait(2)
        self.play(Write(factory), run_time=1)
        self.wait(1)

        self.play(FadeOut(harris), FadeOut(paper1), FadeOut(factory), FadeOut(source), run_time=0.75)
        self.wait(1)

        paper2 = FramedImage("img/0_paper2.png", height=4.5)
        self.play(FadeIn(paper2), Write(source), run_time=1)
        self.wait(3.5)

        less_visible = Tex(r"\textbf{Less visible:}\\Capital Interest\\Depreciation",
                           tex_environment="flushleft", font_size=22)
        vs = Tex(r"vs.", font_size=22)
        more_apparent = Tex(r"\textbf{More apparent:}\\Ordering or Setup Costs",
                            tex_environment="flushleft", font_size=22)
        text_row = VGroup(less_visible, vs, more_apparent).arrange(RIGHT, buff=1)#.next_to(paper2, UP)
        balance = Tex(r"Balance", font_size=22).next_to(vs, UP)
        
        self.play(paper2.animate.fade(0.95), Write(balance), run_time=0.5)
        self.wait(2.5)
        self.play(Write(less_visible), run_time=1)
        self.wait(1)
        self.play(Write(vs), run_time=0.25)
        self.wait(1)
        self.play(Write(more_apparent), run_time=1)
        self.wait(1.25)

        self.play(FadeOut(text_row), FadeOut(balance), FadeOut(source), FadeOut(paper2), run_time=1)
        self.wait(1)

        timeline_dot = VGroup(timeline, dot_1913)
        self.play(timeline_dot.animate.move_to([0,0,0]), run_time=2, rate_func=smooth)
        self.wait(5.25)
        eoq_arrow = Arrow(timeline.n2p(1913), timeline.n2p(1970), color=COLOR_3,
                          max_tip_length_to_length_ratio=0.035, stroke_width=3).shift(LEFT*0.25 + UP*0.5)
        self.play(GrowArrow(eoq_arrow), run_time=3.75, rate_func=linear)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.75)

        self.wait(1.5)

vspace = 2
stroke_width = 2
Tex.set_default(font_size=25)

class eoq_01_04(MovingCameraScene):

    def construct(self):
        self.wait(2)

        raw = ImageMobject("sku/materials_steel_03.png")
        comp = Group(ImageMobject("sku/parts_metal_03.png"),
                     ImageMobject("sku/tech_circuit_02.png")).arrange(DOWN, buff=1)
        final = Group(ImageMobject("sku/tech_smartphone_02.png"),
                      ImageMobject("sku/vehicle_motorcycle_02.png")).arrange(DOWN, buff=1)
        for img in [comp, final]:
            img.width = 2
        raw.width = 3
        inv_img = Group(raw, comp, final).arrange(RIGHT, buff=1).shift(DOWN*0.25)

        raw_txt = Tex("Raw Materials")
        comp_txt = Tex("Components")
        final_txt = Tex("Final Products")
        inv_all = Group(raw_txt, comp_txt, final_txt,
                        raw, comp, final).arrange_in_grid(rows=2,
                                                          buff=0.75,
                                                          col_alignments="ccc",
                                                          row_alignments="cc",
                                                          col_widths=[3,3,3],
                                                          row_heights=[2,2]).shift(LEFT*0.25)
        self.play(FadeIn(inv_img))
        self.wait(4)

        for x in [raw_txt, comp_txt, final_txt]:
            self.play(Write(x), run_time=0.5)
            self.wait(0.5)

        sku = RoundedRectangle(corner_radius=0.1, width=0.75, height=0.75,
                               color=COLOR_1, stroke_color=COLOR_2,
                               stroke_width=2, fill_opacity=1)

        unit_txt = Tex("Unit of inventory").next_to(sku, UP*0.5)
        self.play(LaggedStart(FadeOut(inv_all),
                              GrowFromCenter(sku),
                              Write(unit_txt)
                              ), lag_ratio=0.45, run_time=1.75)
        self.wait(1.75)

        sku_2 = RoundedRectangle(corner_radius=0.1,
                                 width=1, height=1,
                                 color=COLOR_1, stroke_color=COLOR_2,
                                 stroke_width=2, fill_opacity=1).scale(0.25)
        sku_matrix = VGroup(*[sku_2.copy() for _ in range(200)]).arrange_in_grid(rows=8, buff=0.1)
        surr_sku = SurroundingRectangle(sku_matrix, color=COLOR_2,
                                        buff=0.1, corner_radius=0.1, stroke_width=2)
        sku_txt = Tex("One year of demand").next_to(surr_sku, UP*0.5)
        self.play(ReplacementTransform(sku, sku_matrix),
                  ReplacementTransform(unit_txt, sku_txt),
                  Create(surr_sku), run_time=0.80)
        self.wait(2)

        timeline = NumberLine(x_range=[0,12,1], length=10,
                              numbers_with_elongated_ticks=[6], longer_tick_multiple=2).shift(DOWN*1.25)
        unit_time_txt = Tex("Unit Time").next_to(timeline, DOWN)
        self.play(ReplacementTransform(sku_txt, unit_time_txt), GrowFromCenter(timeline),
                  FadeOut(sku_matrix), FadeOut(surr_sku))
        self.wait(3.2)

        sku_2.scale(0.75)
        sku_batch = VGroup(*[sku_2.copy() for _ in range(35)]).arrange_in_grid(rows=7, buff=0.1)
        sku_batch.next_to(timeline, UP*0.5).align_to(timeline, LEFT)
        
        brace_txt = Tex(r"Acquiring and Maintaining Inventory").next_to(timeline, UP*9.25)
        self.play(GrowFromCenter(sku_batch), Write(brace_txt), run_time=0.5)
        for x in range(len(sku_batch)):
            self.play(FadeOut(sku_batch[0]), sku_batch.animate.shift(RIGHT * 0.1),
                      run_time=0.06, rate_func=smooth)
            sku_batch.remove(sku_batch[0])

        
        sku_batch = VGroup(*[sku_2.copy() for _ in range(35)]).arrange_in_grid(rows=7, buff=0.1)
        sku_batch.next_to(timeline, UP*0.5).align_to(timeline, LEFT).shift(RIGHT*5)
        self.play(GrowFromCenter(sku_batch), run_time=0.5)
        for x in range(len(sku_batch)):
            self.play(FadeOut(sku_batch[0]), sku_batch.animate.shift(RIGHT * 0.1),
                      run_time=0.06, rate_func=smooth)
            sku_batch.remove(sku_batch[0])

        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(1)

total_cost_txt = Tex(r"Total Inventory Cost")
total_cost_txt.shift(UP*3 + LEFT*4)
total_cost_math = MathTex(r"= cD + c_t\frac{D}{Q} + c_e\frac{Q}{2}",
                          font_size=30).next_to(total_cost_txt, RIGHT*0.25)
tcgroup1 = VGroup(total_cost_txt, total_cost_math)
equals = total_cost_math[0][0]
material_math = total_cost_math[0][1:3]
plus1 = total_cost_math[0][3]
setup_math = total_cost_math[0][4:9]
plus2 = total_cost_math[0][9]
holding_math = total_cost_math[0][10:]

class eoq_01_05(MovingCameraScene):

    def construct(self):
        material_eq = MathTex(r"cD").shift(UP*1.5)
        material_txt = Tex("Material Cost").shift(UP*2.5)
        self.play(Write(total_cost_txt), run_time=0.75)
        self.wait(2.25)
        self.play(Write(material_txt), run_time=0.75)
        self.wait(5)

        procurement_text = Tex(r"Procurement")
        production_text = Tex(r"Production")
        proc_or_prod = VGroup(procurement_text, production_text).arrange(RIGHT, buff=1).shift(UP*2)
        self.play(Write(procurement_text), run_time=0.75)
        self.play(Write(production_text), run_time=0.75)
        self.play(FadeOut(proc_or_prod), run_time=0.75)
        self.play(Write(material_eq), run_time=0.75)

        c_arrow = Arrow(material_eq.get_edge_center(LEFT) - [1.25,0,0],
                        material_eq.get_edge_center(LEFT),
                        max_tip_length_to_length_ratio=0.075,
                        color=COLOR_3,
                        stroke_width=stroke_width)
        c_text = Tex(r"Unit Cost").next_to(c_arrow, LEFT)
        self.play(Write(c_text), GrowArrow(c_arrow), run_time=0.75)
        self.wait(1)
        D_arrow = Arrow(material_eq.get_edge_center(RIGHT) + [1.25,0,0],
                        material_eq.get_edge_center(RIGHT),
                        max_tip_length_to_length_ratio=0.075,
                        color=COLOR_3,
                        stroke_width=stroke_width)
        D_text = Tex(r"Total Demand").next_to(D_arrow, RIGHT)
        self.play(Write(D_text), GrowArrow(D_arrow), run_time=0.75)
        self.wait(2)

        # FOR MERCHANTS 
        merchants_img = FramedImage("img/1_retail.png", width=4)
        purchase_prep_text = Tex(r"Purchase price + Sale preparation costs")
        pack_n_label_arrow = Arrow(purchase_prep_text.get_edge_center(RIGHT),
                                   purchase_prep_text.get_edge_center(RIGHT) + [1.25,0,0],
                                   max_tip_length_to_length_ratio=0.075,
                                   color=COLOR_3,
                                   stroke_width=stroke_width)
        pack_n_label_text = Tex(r"Packaging \&\\Labeling", tex_environment="flushleft")
        Group(merchants_img,
              purchase_prep_text,
              pack_n_label_arrow,
              pack_n_label_text).arrange(RIGHT, buff=0.35).next_to(material_eq, DOWN*1.75)
        merchants_text = Tex(r"\textbf{Unit Cost for Merchants:}")
        VGroup(purchase_prep_text,
               merchants_text).arrange(UP, buff=0.35, center=False, aligned_edge=LEFT)
        self.play(FadeOut(c_arrow), FadeOut(c_text), FadeOut(D_arrow), FadeOut(D_text),
                  FadeIn(merchants_img), Write(merchants_text), 
                  material_eq[0][0].animate.set_color(COLOR_3), run_time=0.75)
        self.wait(1)
        self.play(Write(purchase_prep_text[0][0:13]), run_time=0.75)
        self.wait(1.25)
        self.play(Write(purchase_prep_text[0][13:]), run_time=0.75)
        self.wait(3.25)
        self.play(GrowArrow(pack_n_label_arrow), Write(pack_n_label_text), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(pack_n_label_arrow), FadeOut(pack_n_label_text), run_time=0.75)
        self.wait(0.25)
        freight_mhandling_text = Tex("(Per-unit) Freight Transportation \& Material Handling")
        VGroup(purchase_prep_text,
               freight_mhandling_text).arrange(DOWN, buff=0.35, center=False, aligned_edge=LEFT)
        self.play(Write(freight_mhandling_text), run_time=1.25)
        self.wait(3.25)
        load_unload = Tex(r"Loading \& Unloading").next_to(
            freight_mhandling_text.get_edge_center(RIGHT) - [1,0.25,0],
            DOWN*1.5)
        load_arrow = Arrow(load_unload.get_center() +  [0,0.8,0],
                           load_unload.get_center(),
                           max_tip_length_to_length_ratio=0.25,
                           color=COLOR_3, stroke_width=stroke_width)
        self.play(GrowArrow(load_arrow), Write(load_unload), run_time=0.75)
        self.wait(0.5)
        self.play(FadeOut(merchants_img),
                  FadeOut(merchants_text),
                  FadeOut(purchase_prep_text),
                  FadeOut(freight_mhandling_text),
                  FadeOut(load_unload),
                  FadeOut(load_arrow),
                  )

        # FOR PRODUCERS
        manufacturing_img = FramedImage("img/1_manuf2.png", width=4).move_to(merchants_img.get_center())
        producers_text = Tex(r"\textbf{Unit Cost for Producers:}")
        pos = merchants_text.get_edge_center(LEFT)
        producers_text.move_to(pos).align_to(pos, LEFT)
        total_unit_prodcost = Tex(r"Total Unitary Production Cost:")
        prod_related = Tex("Raw Materials $+$ Direct Labor $+$ Overhead")
        prod_totalunit = VGroup(producers_text,
                                total_unit_prodcost,
                                prod_related).arrange(DOWN,
                                                      buff=0.35,
                                                      center=False,
                                                      aligned_edge=LEFT)
        # Group(manufacturing_img,
        #       prod_totalunit).arrange(RIGHT, buff=0.35,).next_to(material_eq, DOWN*1.5)
        self.play(FadeIn(manufacturing_img), Write(producers_text), run_time=0.75)
        self.wait(2.5)
        self.play(Write(prod_related[0][0:12]), run_time=0.75)
        self.wait(1.75)
        self.play(Write(total_unit_prodcost), run_time=0.75)
        self.wait(2.25)
        self.play(Write(prod_related[0][12:]), run_time=0.75)
        self.wait(1.25)
        self.play(FadeOut(manufacturing_img), FadeOut(prod_totalunit),
                  material_eq[0][0].animate.set_color(COLOR_1),
                  run_time=1)
        self.wait(2.85)
        
        D_surr = SurroundingRectangle(material_eq[0][1],
                                      color=COLOR_3, buff=0.05, stroke_width=stroke_width)
        self.play(Create(D_surr), run_time=1)
        self.wait(2.5)
        known = Tex("Known and Constant", color=COLOR_3).next_to(D_surr.get_center(), DOWN*3.25)
        self.play(Write(known), run_time=1.25)
        self.wait(2)
        self.play(FadeOut(D_surr), FadeOut(known), run_time=1)
        self.wait(1.75)
        self.play(FadeOut(material_txt), FadeIn(equals), ReplacementTransform(material_eq, material_math))
        self.wait(1.5)

class eoq_01_06(MovingCameraScene):

    def construct(self):
        setup_eq = MathTex(r"c_t\frac{D}{Q}")
        
        self.add(total_cost_txt, equals, material_math)
        self.play(FadeIn(plus1), run_time=.5)
        self.wait(0.5)

        # Lots
        sku = RoundedRectangle(corner_radius=0.1, width=1, height=1, color=COLOR_1, stroke_color=COLOR_2,
                               stroke_width=2, fill_opacity=1).scale(0.25)
        lot1 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        lot2 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        lot3 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        VGroup(lot1, lot2, lot3).arrange(RIGHT, buff=2).shift(DOWN*0.65)
        
        setup_txt = Tex("Setup Cost").next_to(lot2, UP*5)
        self.play(Write(setup_txt), run_time=0.75)
        self.wait(1)

        ordering_txt = Tex("Ordering Cost").next_to(setup_txt, DOWN*3)
        ordering_arrow = Arrow(setup_txt.get_center(),
                               ordering_txt.get_center(),
                               max_tip_length_to_length_ratio=0.15,
                               color=COLOR_3,
                               stroke_width=stroke_width)
        self.play(GrowArrow(ordering_arrow), Write(ordering_txt), run_time=0.75)
        self.wait(0.75)
        self.play(FadeOut(ordering_arrow), FadeOut(ordering_txt), run_time=0.75)
        self.wait(0.25)

        fixed_txt_1 = Tex("Fixed Cost").next_to(lot1, UP*0.75)
        fixed_txt_2 = Tex("Fixed Cost").next_to(lot2, UP*0.75)
        fixed_txt_3 = Tex("Fixed Cost").next_to(lot3, UP*0.75)

        arr1 = Arrow(setup_txt.get_corner(DL), fixed_txt_1.get_corner(UR),
                     max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=stroke_width)
        arr2 = Arrow(setup_txt.get_edge_center(DOWN), fixed_txt_2.get_edge_center(UP),
                     max_tip_length_to_length_ratio=0.3, color=COLOR_3, stroke_width=stroke_width)
        arr3 = Arrow(setup_txt.get_corner(DR), fixed_txt_3.get_corner(UL),
                     max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=stroke_width)
        
        self.play(GrowFromCenter(lot1), GrowFromCenter(lot2), GrowFromCenter(lot3),
                  GrowFromPoint(fixed_txt_1, lot1.get_center()),
                  GrowFromPoint(fixed_txt_2, lot2.get_center()),
                  GrowFromPoint(fixed_txt_3, lot3.get_center()),
                  GrowArrow(arr1), GrowArrow(arr2), GrowArrow(arr3), run_time=1)
        self.wait(4.5)
        self.play(*[FadeOut(mob) for mob in [lot2,
                                             fixed_txt_1, fixed_txt_2, fixed_txt_3,
                                             arr1, arr2, arr3]], run_time=1)
        self.wait(1)

        lot_big = VGroup(*[sku.copy() for _ in range(81)]).arrange_in_grid(rows=9, buff=0.1)
        lot_big.move_to(lot1.get_center())

        same_txt = Tex(r"Same fixed cost").move_to(midpoint(lot_big.get_edge_center(RIGHT),
                                                            lot3.get_edge_center(LEFT)
                                                            ))
        
        arrL = Arrow(same_txt.get_edge_center(LEFT), lot_big.get_edge_center(RIGHT),
                     max_tip_length_to_length_ratio=0.075, color=COLOR_3, stroke_width=stroke_width)
        arrR = Arrow(same_txt.get_edge_center(RIGHT), lot3.get_edge_center(LEFT),
                     max_tip_length_to_length_ratio=0.075, color=COLOR_3, stroke_width=stroke_width)

        self.play(FadeIn(lot_big), Write(same_txt),
                  GrowArrow(arrL), GrowArrow(arrR), run_time=1)

        self.wait(2.5)
        self.play(*[FadeOut(mob) for mob in [lot_big, lot1, lot3, arrL, arrR, same_txt]], run_time=1)

        total_setup_txt = Tex("Total Setup Cost").next_to(lot2, UP*5)
        self.play(ReplacementTransform(setup_txt, total_setup_txt), run_time=1)

        self.wait(3)

        year_sku = VGroup(*[sku.copy() for _ in range(225)]).arrange_in_grid(rows=9, buff=0.150)
        year_sku.next_to(total_setup_txt, DOWN*2)
        self.play(GrowFromCenter(year_sku), run_time=1)
        self.wait(0.5)

        year_surr = SurroundingRectangle(year_sku, color=COLOR_3, buff=0.15, corner_radius=0.1, stroke_width=3)
        year_txt = Tex("$D$ units", color=COLOR_3).next_to(year_surr, DOWN*0.5)
        self.play(Create(year_surr), Write(year_txt), rate_func=linear, run_time=1.5)
        
        self.wait(1)
        self.play(FadeOut(year_surr), FadeOut(year_txt), run_time=0.5)

        lot_sku = VGroup(*[sku.copy() for _ in range(45)]).arrange_in_grid(rows=9, buff=0.150)
        pos = year_sku.get_edge_center(LEFT)
        lot_sku.next_to(pos, RIGHT*0, buff=0).align_to(pos, LEFT)
        lot_surr = SurroundingRectangle(lot_sku, color=COLOR_3, buff=0.075, corner_radius=0.1, stroke_width=2.5)
        other_surr = VGroup(*[lot_surr.copy() for _ in range(4)]).arrange(RIGHT, buff=0)
        other_surr.next_to(lot_surr, RIGHT, buff=0)

        lot_txt = Tex("$Q$ units", color=COLOR_3).next_to(lot_surr, LEFT*0.5)
        self.play(Create(lot_surr), Write(lot_txt), run_time=1, rate_func=linear)

        self.wait(1.5)
        self.play(FadeOut(lot_txt), Create(other_surr), run_time=2)

        self.wait(2)

        equals_ = MathTex(r"=").next_to(total_setup_txt, RIGHT*0.5).scale(0.5)
        setup_eq.next_to(equals_, RIGHT*0.15).scale(0.5)
        self.play(Write(setup_eq[0][2:]), run_time=0.75)
        self.wait(3)
        self.play(Write(setup_eq[0][0:2]), run_time=0.75)
        self.wait(1)
        self.play(Write(equals_), run_time=0.75)
        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in [lot_surr, other_surr, year_sku, total_setup_txt, equals_]],
                  setup_eq.animate.move_to(total_setup_txt.get_center() + [0,0.5,0])
                  )
        self.play(setup_eq[0][0:2].animate.set_color(COLOR_3))
        self.wait(4)

        img_office = FramedImage("img/2_office.png", width=4)#.to_edge(DOWN + LEFT).shift(UP*0.5 + RIGHT)
        img_routes = FramedImage("img/2_routes.png", width=4)#.to_edge(DOWN + LEFT).shift(UP*0.5 + RIGHT)
        img_unload = FramedImage("img/2_unloading.png", width=4)#.to_edge(DOWN + LEFT).shift(UP*0.5 + RIGHT)

        g_fixed = Group(img_office, img_routes, img_unload).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.5)

        self.play(FadeIn(img_office), run_time=1.25)
        self.wait(8.75)
        self.play(FadeIn(img_routes), run_time=1.25)
        self.wait(5.75)
        self.play(FadeIn(img_unload), run_time=1.25)
        self.wait(11)
        self.play(FadeOut(g_fixed), run_time=1)

        self.wait(2)
        img_few  = FramedImage("img/3_fewitems.png", width=4)
        img_many  = FramedImage("img/3_manyitems.png", width=4)
        Group(img_many, img_few).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.5)
        self.play(FadeIn(img_many), FadeIn(img_few), run_time=1)
        self.wait(9)
        self.play(FadeOut(img_many), FadeOut(img_few), run_time=1)
        self.wait(1.5)

        fixvar_setup_eq = MathTex(r"(c_{t_f} + c_{t_v}Q)\frac{D}{Q}", font_size=30)
        fixvar_arr = Arrow(setup_eq[0][0].get_center(),
                           (setup_eq[0][0].get_x(), fixvar_setup_eq.get_y() + 0.25, 0),
                           max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=stroke_width)
        fixvar_setup_eq[0][0:10].set_color(COLOR_3)
        #self.play(GrowArrow(fixvar_arr), run_time=1)
        #self.play(Write(fixvar_setup_eq), FadeOut(fixvar_arr), run_time=1)
        self.play(TransformByGlyphMap(setup_eq, fixvar_setup_eq,
                                      ([0,1], [0,1,2,3,4]),
                                      ([0,1], [5,6,7,8,9]),
                                      ([2,3,4], [10,11,12]), from_copy=True,
                                      ), run_time=2)
        self.wait(3.5)

        fixvar_setup_eq_2 = MathTex(r"c_{t_f}\frac{D}{Q} + c_{t_v}Q\frac{D}{Q}", font_size=30)
        fixvar_setup_eq_3 = MathTex(r"c_{t_f}\frac{D}{Q} + c_{t_v}D", font_size=30)

        self.play(TransformByGlyphMap(fixvar_setup_eq, fixvar_setup_eq_2,
                                      ([1,2,3], [0,1,2]),
                                      ([10,11,12], [3,4,5]),
                                      ([10,11,12], [11,12,13]),
                                      ([4], [6]),
                                      ([5,6,7], [7,8,9]),
                                      ([8], [10]),
                                      ([0,9], [])
                                      ), run_time=2)
        
        Q_cancel_1 = Line(fixvar_setup_eq_2[0][10].get_corner(UR), fixvar_setup_eq_2[0][10].get_corner(DL),
                          color=COLOR_3, stroke_width=stroke_width)
        Q_cancel_2 = Line(fixvar_setup_eq_2[0][13].get_corner(UR), fixvar_setup_eq_2[0][13].get_corner(DL),
                          color=COLOR_3, stroke_width=stroke_width)
        self.play(Create(Q_cancel_1), Create(Q_cancel_2), run_time=0.75)
        self.play(FadeOut(Q_cancel_1), FadeOut(Q_cancel_2),
                  TransformByGlyphMap(fixvar_setup_eq_2, fixvar_setup_eq_3,
                                      ([11], [10]),
                                      ([10,12,13], [])
                                      ), run_time=2)
        self.wait(3.5)
        arr_fixvar = Arrow(fixvar_setup_eq_3[0][7:].get_edge_center(UP),
                           material_math.get_corner(DR),
                           max_tip_length_to_length_ratio=0.025, color=COLOR_3, stroke_width=stroke_width)
        
        self.play(GrowArrow(arr_fixvar), run_time=1)

        self.wait(6)

        no_escale = Tex(r"Assumes no economies of scale", tex_environment="flushleft", color=COLOR_3)
        no_escale.next_to(fixvar_setup_eq_3, DOWN*2)
        self.play(Write(no_escale), run_time=0.75)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [fixvar_setup_eq_3, arr_fixvar, no_escale]])
        self.wait(6)

        img_machine = FramedImage("img/4_machine_setup.png", width=4)
        img_learning = FramedImage("img/4_learning.png", width=4)
        img_opportunity = FramedImage("img/4_opportunity.png", width=4)
        g_fixed = Group(img_machine, img_learning, img_opportunity).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.5)

        self.play(FadeIn(img_machine), run_time=1)
        self.wait(6)
        self.play(FadeIn(img_learning), run_time=1)
        self.wait(10)
        self.play(FadeIn(img_opportunity), run_time=1)
        self.wait(8)

        self.play(FadeOut(g_fixed), run_time=1)
        self.play(ReplacementTransform(setup_eq, setup_math), run_time=1.25)
        self.wait(1)     

class eoq_01_07(Scene): # Holding Cost
    def construct(self):
        self.add(total_cost_txt, equals, material_math, plus1, setup_math)
        self.play(FadeIn(plus2), run_time=.5)
        self.wait(0.5)

        holding_txt = Tex("Holding Cost").shift(UP*2)
        self.play(Write(holding_txt), run_time=1)
        self.wait(1)

        carrying_txt = Tex("Carrying Cost").next_to(holding_txt, DOWN*5)
        arrow1 = Arrow(holding_txt.get_center(), carrying_txt.get_center(),
                       color=COLOR_3,
                       max_tip_length_to_length_ratio=0.15,
                       stroke_width=2)
        self.play(LaggedStart(GrowArrow(arrow1), Write(carrying_txt), run_time=1.25, lag_ratio=0.75))
        self.wait(1)

        self.play(FadeOut(arrow1), FadeOut(carrying_txt), run_time=0.75)
        self.wait(3)

        lot1 = Lot(4,4)
        lot2 = Lot(7,7)
        different_txt = Tex(r"Different\\Holding Costs")
        VGroup(lot1, different_txt, lot2).arrange(RIGHT, buff=1.5)
        arrowL = Arrow(different_txt.get_edge_center(LEFT), lot1.get_edge_center(RIGHT),
                       color=COLOR_3, max_tip_length_to_length_ratio=0.15,
                       stroke_width=2)
        arrowR = Arrow(different_txt.get_edge_center(RIGHT), lot2.get_edge_center(LEFT),
                       color=COLOR_3, max_tip_length_to_length_ratio=0.15,
                       stroke_width=2)
        self.play(FadeIn(lot1), run_time=1)
        self.wait(1)
        self.play(FadeIn(lot2), run_time=1)
        self.wait(1)
        self.play(GrowArrow(arrowL), GrowArrow(arrowR), Write(different_txt), run_time=1.25)
        self.wait(4.5)
        self.play(*[FadeOut(mob) for mob in [lot1, arrowL, different_txt, arrowR, lot2]], run_time=1)
        self.wait(3)

        capital_txt = Tex(r"\textbf{Cost of Capital}").shift(UP*0.75)
        self.play(Write(capital_txt), run_time=1)
        self.wait(1)
        capital_img = FramedImage("img/5_money.png", width=4).next_to(capital_txt, LEFT, buff=0.5).align_to(capital_txt, UP)
        self.play(FadeIn(capital_img), run_time=1)
        self.wait(5.5)
        alternative = Tex("Alternative investments").next_to(capital_img, RIGHT*8)
        self.play(Write(alternative), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(alternative), run_time=1)
        self.wait(1)

        equity = Tex("Equity")
        equity_surr = SurroundingRectangle(equity,
                                           color=COLOR_1, buff=0.08, corner_radius=0.025, stroke_width=1.5)
        equity = VGroup(equity,
                        equity_surr)
        debt = Tex("Debt")
        debt = VGroup(debt,
                      equity_surr.copy().move_to(debt.get_center()))
        equity_debt = VGroup(equity, debt).arrange(RIGHT, buff=2).next_to(capital_img, RIGHT*8)
        equity_debt.shift(UP*0.5)
        wacc = Tex(r"WACC").next_to(equity_debt, DOWN*2.5)
        wacc = VGroup(wacc,
                      equity_surr.copy().move_to(wacc.get_center()))
        wacc_txt = Tex(r"Weighted Average Cost of Capital").next_to(wacc, DOWN)

        self.play(FadeIn(equity_debt), run_time=1.25)
        self.wait(2)
        self.play(FadeIn(wacc), Write(wacc_txt), run_time=1)
        self.wait(2.5)
        self.play(ReplacementTransform(equity_debt, wacc), run_time=1)
        self.wait(1.75)
        self.play(*[FadeOut(mob) for mob in [capital_img, capital_txt, wacc, wacc_txt]], run_time=1)

        self.wait(1)
        storage_txt = Tex(r"\textbf{Cost of Storage}").next_to(capital_txt.get_left(), buff=0).shift(UP*0.5)
        self.play(Write(storage_txt), run_time=1)
        self.wait(1.25)

        prime_img = FramedImage("img/5_prime2.png", width=4)
        storage_img = FramedImage("img/5_storage.png", width=4)
        refrige_img = FramedImage("img/5_refrigeration.png", width=4)
        storage_group = Group(prime_img, storage_img, refrige_img).arrange(RIGHT, buff=0.5)
        storage_group.next_to(storage_txt, DOWN*0.5)
        self.play(FadeIn(prime_img), run_time=1)
        self.wait(4.5)
        self.play(FadeIn(storage_img), run_time=1)
        self.wait(4)
        self.play(FadeIn(refrige_img), run_time=1)
        self.wait(7)
        self.play(*[FadeOut(mob) for mob in [storage_txt, prime_img, storage_img, refrige_img]], run_time=1)

        self.wait(1)
        foo_img = FramedImage("img/5_other.png", width=7)
        other_holding = VGroup(Tex("Perishability"),
                               Tex("Shrinkage"),
                               Tex("Insurance"),
                               Tex("Taxation")).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        Group(foo_img, other_holding).arrange(RIGHT, buff=1).next_to(holding_txt, DOWN*2)

        self.play(FadeIn(foo_img), run_time=1)
        self.wait(0.5)
        for mob in other_holding:
            self.play(Write(mob), run_time=0.75)
            self.wait(0.25)


        self.wait(3)
        self.play(FadeOut(foo_img), FadeOut(other_holding), run_time=1)

        self.wait(2)
        all_hold = Tex(r"Capital Cost {\quad\quad\quad\quad} Storage Cost {\quad\quad\quad\quad} Perishability, etc.")
        self.play(FadeIn(all_hold), run_time=1)
        self.wait(3)
        c_e = MathTex(r"c_e")
        self.play(ReplacementTransform(all_hold, c_e), run_time=1)
        self.wait(3)
        c_e_foo = MathTex(r"\% \text{ of } c =", font_size=45).next_to(c_e, LEFT, buff=0.1).shift(UP*0.085)
        self.play(Write(c_e_foo), run_time=1)
        self.wait(2.75)
        holding_rate_txt = Tex("Holding rate")
        rate_arr = DownArrow(c_e_foo[0][0], holding_rate_txt)
        self.play(LaggedStart(GrowArrow(rate_arr), Write(holding_rate_txt), run_time=1.5, lag_ratio=0.5))
        self.wait(2)

        totalhold_txt = Tex("Total Holding Cost $=$").move_to(midpoint(holding_txt.get_center(),
                                                                       c_e.get_center()))
        totalhold_txt.shift([-2, 0.75, 0])
        
        self.play(FadeOut(c_e_foo), FadeOut(rate_arr), FadeOut(holding_rate_txt),
                  ReplacementTransform(holding_txt, totalhold_txt), run_time=1)
        self.wait(1)
        self.play(c_e.animate.move_to(totalhold_txt.get_right() + [0.3,0,0]), run_time=1)
        inventory_held_txt = Tex(r"$\times$ Inventory held during the year").next_to(c_e.get_right(), buff=0).shift([0.1,0,0])
        self.play(Write(inventory_held_txt), run_time=1)
        
        self.wait(3)
        howmuch = Tex("How much inventory is held?")
        self.play(Write(howmuch), run_time=1)
        self.wait(3)
        self.play(FadeOut(howmuch), run_time=0.5)
        self.wait(0.5)
        
        demand_txt = Tex("Demand")
        constant_txt = Tex(r"Constant throughout the year")
        arrow2 = RightArrow(demand_txt, constant_txt)
        VGroup(demand_txt, constant_txt, arrow2).move_to(ORIGIN)
        self.play(Write(demand_txt), run_time=1)
        self.wait(1)
        self.play(LaggedStart(GrowArrow(arrow2), Write(constant_txt), lag_ratio=0.5, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(constant_txt), run_time=0.75)
        self.wait(0.5)

        steady_txt = Tex(r"Steady rate of consumption").next_to(constant_txt.get_left(), buff=0)
        self.play(Write(steady_txt), run_time=2)
        self.wait(2)
        self.play(FadeOut(arrow2), FadeOut(steady_txt), FadeOut(demand_txt), run_time=0.75)

        self.wait(1)
        yshift = -0.75
        self.play(*[FadeIn(mob) for mob in [grid.shift([0, yshift, 0]),
                                            x_label.shift([0, yshift, 0]),
                                            y_label.shift([0, yshift, 0])]], run_time=1)
        self.wait(1.25)
        size_Q = MathTex(r"Q\;\text{units}", font_size=25, color=COLOR_1).next_to(grid.c2p(0,400), LEFT*1)
        self.play(Write(size_Q), run_time=0.75)
        self.wait(0.5)
        sawtooth.shift([0, yshift, 0])
        self.play(Create(sawtooth), run_time=6, rate_func=linear)
        self.wait(4)

        avg = grid.get_horizontal_line(grid.c2p(365, 200), line_config={"dashed_ratio": 1}, stroke_width=3, color=COLOR_4)
        self.play(Create(avg), run_time=1.5)
        self.wait(2)

        q_2 = MathTex(r"\frac{Q}{2}").scale(0.7).next_to(avg, RIGHT*0.5)
        self.play(Write(q_2), run_time=1)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in [totalhold_txt,
                                             inventory_held_txt, size_Q, avg,
                                            # grid, 
                                            # x_label, y_label,
                                            # sawtooth,
                                             ]],
                                             ReplacementTransform(VGroup(c_e, q_2), holding_math),
                                             run_time=1.5)
        
        self.wait(3)
        
class eoq_01_08(Scene): # Holding Cost
    def construct(self):

        yshift = -0.75

        eoq_model = VGroup(grid.shift([0, yshift, 0]),
                           x_label.shift([0, yshift, 0]),
                           y_label.shift([0, yshift, 0]),
                           sawtooth.shift([0, yshift, 0]))
        
        self.add(total_cost_txt, equals, material_math, plus1, setup_math, plus2, holding_math,
                 eoq_model)
        self.wait(2)

        self.play(eoq_model.animate.scale(0.65).shift(LEFT*2.25 + UP*0.5))
        assumptions = VGroup(Tex(r"\textbf{EOQ Assumptions:}"),
                        Tex(r"$\bullet$ Known and constant demand"),
                        Tex(r"$\bullet$ Continuous demand"),
                        Tex(r"$\bullet$ Instantaneous replenishment"),
                        Tex(r"$\bullet$ No quantity discounts"),
                        Tex(r"$\bullet$ No specific perishability"),
                        Tex(r"$\bullet$ Infinite planning horizon"),
                        Tex(r"$\bullet$ Continuous review of inventory"),
                        Tex(r"$\bullet$ No order size or capacity restrictions"),
                        Tex(r"$\bullet$ No planned backorders"),
                        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(eoq_model, RIGHT*2.5)
        self.wait(1.25)
        self.play(Write(assumptions[0]), run_time=1) # Title
        self.wait(3.25)
        self.play(Write(assumptions[1]), run_time=1) # Known and constant
        self.wait(2.75)

        # Continuous
        lines = VGroup(*[Line(grid.c2p(i*replenishment_period, 400, 0),
                              grid.c2p((i+1)*replenishment_period, 0, 0),
                              stroke_width=3, color=COLOR_2) for i in range(6)])
        self.play(LaggedStart(Write(assumptions[2]),
                              sawtooth.animate.set_color(BLUE_A),
                              *[Create(line) for line in lines], run_time=2, rate_func=linear, lag_ratio=0.7))
        self.play(FadeOut(lines), sawtooth.animate.set_color(COLOR_2), run_time=0.5)
        self.wait(1.25)

        # Insta replenishment
        self.play(Write(assumptions[3]), run_time=1) 
        self.wait(0.5)
        lines = VGroup(*[Line(grid.c2p(i*replenishment_period, 0, 0),
                              grid.c2p(i*replenishment_period, 400, 0),
                              stroke_width=3, color=COLOR_2) for i in range(6)])
        self.play(LaggedStart(
            sawtooth.animate.set_color(BLUE_A),
            *[Create(line) for line in lines], run_time=1.75, rate_func=linear, lag_ratio=0.6))
        self.play(FadeOut(lines), sawtooth.animate.set_color(COLOR_2), run_time=0.5)
        self.wait(3.75)

        self.play(Write(assumptions[4]), run_time=1) # No discounts
        self.wait(2.5)
        self.play(Write(assumptions[5]), run_time=1) # No item perish
        self.wait(2.75)
        self.play(Write(assumptions[6]), run_time=1) # Infinite horizon
        self.wait(11.25)
        self.play(Write(assumptions[7]), run_time=1) # Cont review
        self.wait(11)
        self.play(Write(assumptions[8]), run_time=1) # No size or capacity restrictions
        self.wait(3.5)
        self.play(Write(assumptions[9]), run_time=1) # No planned backorders
        self.wait(5)

        stockout_cost = Tex(r"$+$ Cost of Stockouts?", color=COLOR_3).scale(1.2).next_to(holding_math, RIGHT*0.5)
        self.play(Write(stockout_cost), run_time=1)
        self.wait(14)
        self.play(FadeOut(stockout_cost))
        self.wait(20.25)
        self.play(FadeOut(eoq_model), FadeOut(assumptions), tcgroup1.animate.move_to(ORIGIN), run_time=1.5)
        self.wait(0.25)

class eoq_01_09(MovingCameraScene):  # Total Cost Expression
    def construct(self):
        tcgroup1.move_to(ORIGIN)
        self.add(tcgroup1)
        self.wait(1.5)

        TC_1 = MathTex(r"TC=cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}", font_size=30)
        self.play(ReplacementTransform(total_cost_txt, TC_1[0][0:2]),
                  TransformByGlyphMap(total_cost_math, TC_1,
                                      (list(range(15)), list(range(2, 17))),
                                      ([], [0,1])
                                      ), run_time=1.5)
        self.wait(7.5)
        TC_2 = MathTex(r"TC(Q) = cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}", font_size=30)
        self.play(TransformByGlyphMap(TC_1, TC_2,
                                      ([0,1], [0,1]),
                                      ([], [2,3,4]),
                                      (list(range(2, len(TC_1[0]))), list(range(5, len(TC_2[0])))), 
                                      ), run_time=1.5)
        self.wait(19.5)
        TRC_1 = MathTex(r"TRC(Q) = c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}", font_size=30)
        self.play(TransformByGlyphMap(TC_2, TRC_1,
                                      ([0], [0]),
                                      ([], [1]),
                                      (list(range(1,6)), list(range(2,7))),
                                      ([6,7,8], []),
                                      (list(range(9,len(TC_2[0]))), list(range(7, len(TRC_1[0])))),
                                      ), run_time=1.5)
        self.wait(2)

        # AXIS: DEFINE + CREATE
        grid= Axes(x_range=[0, 1600, 200], y_range=[0, 3000, 500],
                     x_length=11, y_length=3.5,
                     axis_config={"color": COLOR_1,"font_size": 24}, tips=False)
        y_label = grid.get_y_axis_label(Tex("Cost").scale(1.1).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label = grid.get_x_axis_label(Tex("Order Quantity").scale(1.1),
                                        edge=DOWN, direction=DOWN, buff=0.3)
        coord_system = VGroup(grid, y_label, x_label).shift(DOWN*0.5 + RIGHT*0.25)
        
        self.play(FadeIn(coord_system), TRC_1.animate.shift(UP*2.5), run_time=1.5)
        q_dot_2 = Dot(point=grid.c2p(400, 0, 0), radius=0.05, color=COLOR_3)

        # INVENTORY COST FUNCTIONS: DEFINITION
        x_values_2 = np.arange(1, 1600, 20)
        holding_cost = grid.plot_line_graph(x_values = x_values_2, y_values = [3*x/2 for x in x_values_2],
                                            line_color = COLOR_2, stroke_width = 2, add_vertex_dots=False)
        setup_cost = grid.plot_line_graph(x_values = np.arange(80, 1600, 20),
                                          y_values = [100*2400/x for x in np.arange(80, 1600, 20)],
                                          line_color = COLOR_2, stroke_width = 2, add_vertex_dots=False)
        total_cost = grid.plot_line_graph(x_values = np.arange(80, 1600, 20),
                                          y_values = [3*x/2 + 100*2400/x for x in np.arange(80, 1600, 20)],
                                          line_color = COLOR_2, stroke_width = 4, add_vertex_dots=False)

        # OPTIMAL POINTS: SHOW
        opt_point = Dot(point=grid.c2p(400, 1200, 0), radius=0.05, color=COLOR_3)
        min_text = Tex("Minimum Total Cost", font_size=20, color=COLOR_3).move_to(grid.c2p(500, 1500, 0))
        line_1 = Line(start=q_dot_2.get_center(), end=grid.c2p(400, 1200, 0), stroke_width=1, color=COLOR_3)

        # SHOW HOLDING AND SETUP COSTS
        self.wait(2)
        self.play(Create(setup_cost), run_time=3, rate_func=smooth)
        self.wait(6)
        self.play(Create(holding_cost), run_time=3, rate_func=linear)
        self.wait(8)
        self.play(Create(total_cost), run_time=2)
        self.wait(1.5)
        self.play(Create(line_1), run_time=1)
        self.play(Create(opt_point), Write(min_text),run_time=0.50, rate_func=smooth)
        self.wait(0.75)

        TRC_2 = MathTex(r"TRC'(Q) = \frac{d}{dQ}\left(c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}\right)", font_size=30)
        TRC_2.shift(UP*2.5)
        self.play(TransformByGlyphMap(TRC_1, TRC_2,
                                      ([0,1,2], [0,1,2]),
                                      ([], [3]),
                                      ([3,4,5,6], [4,5,6,7]),
                                      ([], [8,9,10,11,12]),
                                      ([*ir(7,17)], [*ir(13,23)]),
                                      ([], [24])
                                      ), run_time=1)
        self.wait(8)

class test(Scene):
    def construct(self):
        expA = MathTex(r"=cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}", font_size=80)
        expB = MathTex(r"TC=cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}", font_size=80)
        self.add(expA)
        self.play(TransformByGlyphMap(expA, expB,
                                      ([], [])
                                      ), run_time=1)