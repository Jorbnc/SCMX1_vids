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
        source = Tex(r"Images: www.academia.edu")
        self.play(harris.animate.shift(LEFT*2), FadeIn(paper1), run_time=1)
        
        self.wait(7)