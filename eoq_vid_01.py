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
        eoq_text = Tex(r"Economic Order Quantity")
        eoq_math = MathTex(r"EOQ")
        self.play(Write(eoq_text), run_time=1)
        self.play(ReplacementTransform(eoq_text, eoq_math), run_time=1)
        self.wait(1)

        op_scm_text = Tex(r"Operations Management\\Supply Chain Management")
        self.play(eoq_math.animate.move_to([0,1.5,0]), run_time=0.5, rate_func=smooth)
        self.wait(1)
        self.play(Write(op_scm_text), run_time=1.5)
        self.play(FadeOut(op_scm_text), run_time=0.5)
        self.play(ReplacementTransform(eoq_math, formula), run_time=1)
        self.play(Create(formula_surr), run_time=1)
        self.wait(1)

        # FIRST AXIS AND SAWTOOTH: CREATE
        self.play(Create(grid), Write(x_label), Write(y_label), run_time=1.75)
        q_dot = Dot(point=grid.c2p(0, 400, 0), radius=0.05, color=COLOR_3)
        self.play(ReplacementTransform(formula_and_surr, q_dot), run_time=1, rate_func=smooth)
        self.play(Create(sawtooth, run_time=1.25, rate_func=linear))

        # SECOND AXIS: DEFINE + CREATE
        grid_2= Axes(x_range=[0, 1600, 200], y_range=[0, 3000, 500],
                     x_length=11, y_length=3.5,
                     axis_config={"color": COLOR_1,"font_size": 24}, tips=False)
        y_label_2 = grid.get_y_axis_label(Tex("Cost").scale(0.65).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label_2 = grid.get_x_axis_label(Tex("Order Quantity").scale(0.65),
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
        epq_text = Tex(r"Economic Production Quantity").scale(0.95).next_to(ax1.c2p(5, 420), RIGHT)
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
        continuous_text = Tex(r"Continuous Review").scale(0.95).next_to(ax2.c2p(5, 600), RIGHT)
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
        periodic_text = Tex(r"Periodic Review").scale(0.95).next_to(ax3.c2p(5, 620), RIGHT)
        
        periodic_model = VGroup(ax3, periodic_plot, S_limit, periodic_ip, periodic_text)

        # ============= ADD AXIS LABELS TO ALL MODELS (VGROUPS)
        for ax, model in [(ax1, epq_model), (ax2, continuous_model), (ax3, periodic_model)]:
            model += ax.get_x_axis_label(Tex("Time").scale(0.65), edge=DOWN, direction=DOWN, buff=0.1)

        # All models and zoom out
        VGroup(epq_model, continuous_model, periodic_model).arrange(DOWN, buff=0.75, center=False, aligned_edge=LEFT).move_to([15.75, 0, 0])
        
        final_arrow = Arrow(start=LEFT, end=RIGHT, color=COLOR_3).next_to(formula_and_surr, RIGHT*2)
        core_concept_text = Tex(r"Core Concept").next_to(final_arrow, RIGHT*2)
        next_text = Tex(r"Fundamental\\Strategy") # Tex(r"Fundamental\\Strategy", tex_environment="flushleft") # to align left
        next_text.next_to(final_arrow, RIGHT*2)

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
        self.play(Write(text_1913), run_time=0.5)
        self.play(ReplacementTransform(text_1913, dot_1913), run_time=0.75)
        
        harris_pic = FramedImage("img/harris2.jpg", height=4.5)
        harris_name = Tex("Ford Whitman Harris", font_size=25).next_to(harris_pic, UP)
        harris = Group(harris_pic, harris_name)
        self.play(FadeIn(harris_pic), Write(harris_name), run_time=1)
        self.wait(5)

        paper1 = FramedImage("img/paper1.png", height=4.5).move_to([2,0,0])
        source = Tex(r"Images: www.academia.edu", font_size=17).to_edge(DOWN + RIGHT).shift(UP)
        self.play(harris.animate.shift(LEFT*2), FadeIn(paper1), Write(source), run_time=1)
        factory = Tex(r"\textit{Factory,\\The Magazine of Management}", font_size=15).next_to(paper1, UP)
        self.wait(2)
        self.play(Write(factory), run_time=1)
        self.wait(1)

        self.play(FadeOut(harris), FadeOut(paper1), FadeOut(factory), FadeOut(source), run_time=0.75)
        self.wait(1)

        paper2 = FramedImage("img/paper2.png", height=4.5)
        self.play(FadeIn(paper2), Write(source), run_time=1)
        self.wait(3.5)

        less_visible = Tex(r"\textbf{Less visible:}\\Capital Interest\\Depreciation",
                           tex_environment="flushleft", font_size=22)
        vs = Tex(r"vs.", font_size=22)
        more_apparent = Tex(r"\textbf{More apparent:}\\Ordering or Setup Costs",
                            tex_environment="flushleft", font_size=22)
        text_row = VGroup(less_visible, vs, more_apparent).arrange(RIGHT, buff=1).next_to(paper2, UP)
        balance = Tex(r"Balance", font_size=22).next_to(vs, UP)
        
        self.play(Write(balance), run_time=0.5)
        self.wait(2.5)
        self.play(Write(less_visible), run_time=1)
        self.wait(1)
        self.play(Write(vs), run_time=0.25)
        self.wait(1)
        self.play(Write(more_apparent), run_time=1)
        self.wait(1)

        self.play(FadeOut(text_row), FadeOut(balance), FadeOut(source), FadeOut(paper2), run_time=1)
        self.wait(0.25)

        timeline_dot = VGroup(timeline, dot_1913)
        self.play(timeline_dot.animate.move_to([0,0,0]), run_time=0.75, rate_func=smooth)
        self.wait(2)
        
        here_text = Tex(r"You're\\around here", font_size=25, color=COLOR_3).next_to(timeline.n2p(2025), UP*1)
        self.play(Write(here_text), run_time=1)
        self.wait(3.5)
        eoq_arrow = Arrow(timeline.n2p(1913), timeline.n2p(1970), color=COLOR_3).shift(LEFT*0.25 + UP*0.5)
        self.play(GrowArrow(eoq_arrow), run_time=4, rate_func=linear)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

        self.wait(2)

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

total_cost_txt = Tex(r"Total Cost $=$ Material Cost $+$ Setup Cost $+$ Holding Cost $+$ Shortage Cost",
                     font_size=30)
total_cost_txt.shift(UP*3)
total_txt = total_cost_txt[0][0:10]
material_txt = total_cost_txt[0][10:22]
setup_txt = total_cost_txt[0][22:32]
holding_txt = total_cost_txt[0][32:44]
shortage_txt = total_cost_txt[0][44:]

material_math = MathTex(r"cD").shift(UP*2)
setup_math = MathTex(r"cD").shift(UP*2)
holding_math = MathTex(r"cD").shift(UP*2)
shortage_math = MathTex(r"cD").shift(UP*2)

class eoq_01_05(MovingCameraScene):

    def construct(self):
        
        self.play(Write(total_txt), run_time=0.75)
        self.wait(2.25)
        self.play(Write(material_txt), run_time=0.75)
        self.wait(5)

        procurement_text = Tex(r"Procurement")
        production_text = Tex(r"Production")
        proc_or_prod = VGroup(procurement_text, production_text).arrange(RIGHT, buff=1).shift(UP*2)
        self.play(Write(procurement_text), run_time=0.75)
        self.play(Write(production_text), run_time=0.75)
        self.play(FadeOut(proc_or_prod), run_time=0.75)
        self.play(Write(material_math), run_time=0.75)

        c_arrow = Arrow(material_math.get_edge_center(LEFT) - [1.25,0,0],
                        material_math.get_edge_center(LEFT),
                        max_tip_length_to_length_ratio=0.075,
                        color=COLOR_3,
                        stroke_width=stroke_width)
        c_text = Tex(r"Unit Cost").next_to(c_arrow, LEFT)
        self.play(Write(c_text), GrowArrow(c_arrow), run_time=0.75)
        self.wait(1)
        D_arrow = Arrow(material_math.get_edge_center(RIGHT) + [1.25,0,0],
                        material_math.get_edge_center(RIGHT),
                        max_tip_length_to_length_ratio=0.075,
                        color=COLOR_3,
                        stroke_width=stroke_width)
        D_text = Tex(r"Total Demand").next_to(D_arrow, RIGHT)
        self.play(Write(D_text), GrowArrow(D_arrow), run_time=0.75)
        self.wait(2)

        # FOR MERCHANTS 
        merchants_img = FramedImage("img/purchases.png", width=4)[0]
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
              pack_n_label_text).arrange(RIGHT, buff=0.35).next_to(material_math, DOWN*3)
        merchants_text = Tex(r"\textbf{Unit Cost for Merchants:}")
        VGroup(purchase_prep_text,
               merchants_text).arrange(UP, buff=0.35, center=False, aligned_edge=LEFT)
        self.play(FadeOut(c_arrow), FadeOut(c_text), FadeOut(D_arrow), FadeOut(D_text),
                  FadeIn(merchants_img), Write(merchants_text), 
                  material_math[0][0].animate.set_color(COLOR_3), run_time=0.75)
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
        manufacturing_img = FramedImage("img/manufacturing.png", width=4.3)[0]
        producers_text = Tex(r"\textbf{Unit Cost for Producers:}")
        total_unit_prodcost = Tex(r"Total Unitary Production Cost:")
        prod_related = Tex("Raw Materials $+$ Direct Labor $+$ Overhead")
        prod_totalunit = VGroup(producers_text,
                                total_unit_prodcost,
                                prod_related).arrange(DOWN,
                                                      buff=0.35,
                                                      center=False,
                                                      aligned_edge=LEFT)
        Group(manufacturing_img,
              prod_totalunit).arrange(RIGHT, buff=0.35,).next_to(material_math, DOWN*2)
        self.play(FadeIn(manufacturing_img), Write(producers_text), run_time=0.75)
        self.wait(2.5)
        self.play(Write(prod_related[0][0:12]), run_time=0.75)
        self.wait(1.75)
        self.play(Write(total_unit_prodcost), run_time=0.75)
        self.wait(2.25)
        self.play(Write(prod_related[0][12:]), run_time=0.75)
        self.wait(1.25)
        self.play(FadeOut(manufacturing_img), FadeOut(prod_totalunit),
                  material_math[0][0].animate.set_color(COLOR_1),
                  run_time=1)
        self.wait(2.85)
        
        D_surr = SurroundingRectangle(material_math[0][1],
                                      color=COLOR_3, buff=0.05, stroke_width=stroke_width)
        self.play(Create(D_surr), run_time=1)
        self.wait(2.5)
        known = Tex("Known and Constant", color=COLOR_3).next_to(D_surr.get_center(), DOWN*3.25)
        self.play(Write(known), run_time=1.25)
        self.wait(2)
        self.play(FadeOut(D_surr), FadeOut(known), run_time=1)
        self.wait(1.75)
        self.play(FadeOut(material_txt), material_math.animate.move_to(material_txt.get_center()))
        self.wait(1.5)

        self.play(Write(setup_txt))

material_math.move_to(material_txt.get_center())

class eoq_01_06(MovingCameraScene):

    def construct(self):
        
        self.add(total_txt, material_math, setup_txt)
        self.wait(2)