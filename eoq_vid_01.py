from main_theme import *
import random
from itertools import *

COLOR_1 = MBLACK
COLOR_2 = DBLUE
COLOR_3 = MRED
COLOR_4 = DRED
COLOR_5 = "#005a85" # Slightly darker than DARK_BLUE

Tex.set_default(font_size=30)
MathTex.set_default(font_size=35)

# EOQ Formula
formula = MathTex(r"Q = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=COLOR_1).scale(1.1).move_to([0, 0, 0])
formula_surr = SurroundingRectangle(formula, color=COLOR_1, buff=0.2, corner_radius=0.15, stroke_width=2.5)
formula_and_surr = VGroup(formula, formula_surr)

#First Axis
grid = Axes(x_range=[0, 365, 30], y_range=[0, 500, 100], x_length=11, y_length=3.5,
            axis_config={"color": COLOR_1, "font_size": 24}, tips=False)

# Labels for the x-axis and y-axis.
y_label = grid.get_y_axis_label(Tex("Inventory").scale(1).rotate(90 * DEGREES),
                                edge=LEFT, direction=LEFT, buff=0.3)
x_label = grid.get_x_axis_label(Tex("Time").scale(1),edge=DOWN, direction=DOWN, buff=0.3)

# EOQ: D = 2400, ct=100, ce=3 => Q = 400 
replenishments = 6 #2400/400
replenishment_period = (400/2400)*365
x_values = [i * replenishment_period for n in range(replenishments) for i in (n, n)] + [365]
sawtooth = grid.plot_line_graph(
    x_values = x_values,
    y_values = [400 if i % 2 else 0 for i in range(len(x_values))],
    line_color = COLOR_2, stroke_width = 3.5, add_vertex_dots=False,
)

class eoq_01_logo(Scene):
    def construct(self):
        logo = ImageMobject("img/logo.png")
        logo.width = 4.85
        convexed_txt = Tex(r"\textbf{Convexed}", font_size=50)
        convexed_group = Group(logo, convexed_txt).arrange(DOWN, buff=0.35)
        self.play(FadeIn(convexed_group), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(convexed_group), run_time=1)
        self.wait(0.5)

class eoq_01_intro(MovingCameraScene):
    def construct(self):
        self.wait(1.5)

        lot_25 = Lot(rows=5, cols=5, buff=0.125).scale(1.2)
        lot_600 = VGroup(*[lot_25.copy() for _ in range(24)]).arrange_in_grid(rows=4, buff=0.125)
        surrounding = SurroundingRectangle(lot_600, color=COLOR_1, buff=0.15, corner_radius=0.15,
                                           stroke_width=2)
        
        lot_all = VGroup(lot_600, surrounding).scale(0.5)
        demand_txt = Tex(r"How much we will sell this year").next_to(lot_all, UP*0.75)
        gadget = ImageMobject(r"sku\tech_gadget_01.png").scale(0.4).next_to(lot_600[0][0], LEFT*4)
        line = Line(gadget.get_edge_center(RIGHT), lot_600[0][0].get_center(), 
                    color=COLOR_3, stroke_width=1.9)
        self.play(GrowFromCenter(lot_600), Create(surrounding), run_time=1)
        self.wait(0.5)
        self.play(Write(demand_txt), run_time=0.75)
        self.play(FadeIn(gadget), GrowFromEdge(line, RIGHT), run_time=0.75)
        self.wait(1.5)

        # ========== Orders
        k = 0.30
        self.play(FadeOut(surrounding), FadeOut(gadget), FadeOut(line),
                  lot_600[0].animate.shift(LEFT*k), lot_600[1].animate.shift(LEFT*k),
                  lot_600[2].animate.shift(DOWN*0), lot_600[3].animate.shift(DOWN*0),
                  lot_600[4].animate.shift(RIGHT*k), lot_600[5].animate.shift(RIGHT*k),
                  lot_600[6].animate.shift(LEFT*k + DOWN*k), lot_600[7].animate.shift(LEFT*k + DOWN*k),
                  lot_600[8].animate.shift(DOWN*k), lot_600[9].animate.shift(DOWN*k),
                  lot_600[10].animate.shift(RIGHT*k + DOWN*k), lot_600[11].animate.shift(RIGHT*k + DOWN*k),
                  lot_600[12].animate.shift(LEFT*k + DOWN*k*2), lot_600[13].animate.shift(LEFT*k + DOWN*k*2),
                  lot_600[14].animate.shift(DOWN*k*2), lot_600[15].animate.shift(DOWN*k*2),
                  lot_600[16].animate.shift(RIGHT*k + DOWN*k*2), lot_600[17].animate.shift(RIGHT*k + DOWN*k*2),
                  lot_600[18].animate.shift(LEFT*k + DOWN*k*3), lot_600[19].animate.shift(LEFT*k + DOWN*k*3),
                  lot_600[20].animate.shift(DOWN*k*3), lot_600[21].animate.shift(DOWN*k*3),
                  lot_600[22].animate.shift(RIGHT*k + DOWN*k*3), lot_600[23].animate.shift(RIGHT*k + DOWN*k*3),
                  run_time=1)
        surr_month = [SurroundingRectangle(VGroup(lot_600[i], lot_600[i+1]),
                                           color=COLOR_2,
                                           stroke_width=2.25,
                                           buff=0.065, corner_radius=0.065) for i in range(0,24,2)]
        self.play(*[Create(surr) for surr in surr_month], run_time=0.75)
        self.wait(1)

        self.play(LaggedStart(
                  AnimationGroup(*[FadeOut(surr) for surr in surr_month]),
                  AnimationGroup(
                  lot_600[0].animate.shift(LEFT*k*1.5), lot_600[1].animate.shift(LEFT*k*0.5),
                  lot_600[2].animate.shift(LEFT*k*0.5), lot_600[3].animate.shift(RIGHT*k*0.5),
                  lot_600[4].animate.shift(RIGHT*k*0.5), lot_600[5].animate.shift(RIGHT*k*1.5),
                  lot_600[6].animate.shift(LEFT*k*1.5), lot_600[7].animate.shift(LEFT*k*0.5),
                  lot_600[8].animate.shift(LEFT*k*0.5), lot_600[9].animate.shift(RIGHT*k*0.5),
                  lot_600[10].animate.shift(RIGHT*k*0.5), lot_600[11].animate.shift(RIGHT*k*1.5),
                  lot_600[12].animate.shift(LEFT*k*1.5), lot_600[13].animate.shift(LEFT*k*0.5),
                  lot_600[14].animate.shift(LEFT*k*0.5), lot_600[15].animate.shift(RIGHT*k*0.5),
                  lot_600[16].animate.shift(RIGHT*k*0.5), lot_600[17].animate.shift(RIGHT*k*1.5),
                  lot_600[18].animate.shift(LEFT*k*1.5), lot_600[19].animate.shift(LEFT*k*0.5),
                  lot_600[20].animate.shift(LEFT*k*0.5), lot_600[21].animate.shift(RIGHT*k*0.5),
                  lot_600[22].animate.shift(RIGHT*k*0.5), lot_600[23].animate.shift(RIGHT*k*1.5)),
                  lag_ratio=0.35,
                  run_time=1))
        surr_twice = [SurroundingRectangle(VGroup(lot_600[i]),
                                           color=COLOR_2,
                                           stroke_width=2.25,
                                           buff=0.065, corner_radius=0.065) for i in range(0,24)]
        self.play(*[Create(surr) for surr in surr_twice], run_time=0.75)
        self.wait(.85)

        costs = Tex("What about the costs?", font_size=50)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.7)
        self.play(Write(costs), run_time=0.75)
        self.wait(0.75)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.7)
        self.wait(0.5)

class eoq_01_01(MovingCameraScene):

    def construct(self):

        # EOQ: INTRODUCTION + FORMULA
        eoq_text = Tex(r"Economic Order Quantity", font_size=50)
        eoq_math = MathTex(r"EOQ", font_size=55)
        self.play(Write(eoq_text), run_time=1)
        self.play(ReplacementTransform(eoq_text, eoq_math), run_time=1)
        self.wait(1)

        op_scm_text = Tex(r"Operations Management\\Supply Chain Management", font_size=50)
        self.play(eoq_math.animate.move_to([0,1.25,0]), run_time=0.5, rate_func=smooth)
        self.wait(1)
        self.play(Write(op_scm_text), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(op_scm_text), run_time=0.7)
        self.play(ReplacementTransform(eoq_math, formula),
                  Create(formula_surr), run_time=1.5)
        self.wait(1)

        # FIRST AXIS AND SAWTOOTH: CREATE
        q_dot = Dot(point=grid.c2p(0, 400, 0), radius=0.075, color=COLOR_3)
        self.play(FadeIn(grid), FadeIn(x_label), FadeIn(y_label),
                  ReplacementTransform(formula_and_surr, q_dot),
                  run_time=1.85, rate_func=smooth)
        self.play(Create(sawtooth, run_time=1.9, rate_func=linear))

        # SECOND AXIS: DEFINE + CREATE
        grid_2= Axes(x_range=[0, 1600, 200], y_range=[0, 3000, 500],
                     x_length=11, y_length=3.5,
                     axis_config={"color": COLOR_1,"font_size": 24}, tips=False)
        y_label_2 = grid.get_y_axis_label(Tex("Cost").scale(1).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label_2 = grid.get_x_axis_label(Tex("Order Quantity").scale(1),
                                        edge=DOWN, direction=DOWN, buff=0.3)
        q_dot_2 = Dot(point=grid_2.c2p(400, 0, 0), radius=0.075, color=COLOR_3)
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
        opt_point = Dot(point=grid_2.c2p(400, 1200, 0), radius=0.075, color=COLOR_3)
        min_text = Tex(r"Minimum\\Total Cost", color=COLOR_3).move_to(grid_2.c2p(400, 1700, 0))
        line_1 = Line(start=q_dot_2.get_center(), end=grid_2.c2p(400, 1200, 0), stroke_width=1.9, color=COLOR_3)

        # SHOW HOLDING AND SETUP COSTS
        self.play(Create(holding_cost), Create(setup_cost),run_time=1, rate_func=linear)
        self.play(Create(total_cost), Create(line_1),run_time=0.75, rate_func=smooth)
        self.play(Create(opt_point), Write(min_text),run_time=0.50, rate_func=smooth)
        self.wait(0.75)

        holding_text = Tex(r"Holding cost", color=COLOR_3).move_to(grid_2.c2p(1000, 1100, 0))
        setup_text = Tex(r"Ordering cost", color=COLOR_3).move_to(grid_2.c2p(800, 550, 0))
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
                                  line_color=COLOR_2, stroke_width=4, add_vertex_dots=False)
        epq_vlines = VGroup()
        for x in epq_values[1::2]: # Starting at index 1, every 2 indices
            epq_vlines += ax1.get_vertical_line(ax1.c2p(x, 350),
                                                line_config={"dashed_ratio": 0.75}, color=COLOR_2,
                                                stroke_width=3)
        epq_text = Tex(r"Finite Replenishment").scale(2).next_to(ax1.c2p(5, 420), RIGHT)
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
                                                line_color = COLOR_2, stroke_width=4, add_vertex_dots=False)
        continuous_ip = ax2.plot_line_graph(x_values = continuous_x_ip,
                                            y_values = continuous_y_ip,
                                            line_color = COLOR_2, stroke_width=3, add_vertex_dots=False)
        continuous_ip = DashedVMobject(continuous_ip["line_graph"], num_dashes=250)
        s_limit = ax2.get_horizontal_line(ax2.c2p(365, s), line_config={"dashed_ratio": 0.9}, stroke_width=4, color=COLOR_4)
        continuous_text = Tex(r"Continuous Review").scale(2).next_to(ax2.c2p(5, 600), RIGHT)
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
                                            line_color = COLOR_2, stroke_width = 4, add_vertex_dots=False)
        periodic_ip = ax2.plot_line_graph(x_values = periodic_x_ip,
                                            y_values = periodic_y_ip,
                                            line_color = COLOR_2, stroke_width=3, add_vertex_dots=False)
        periodic_ip = DashedVMobject(periodic_ip["line_graph"], num_dashes=250)
        S_limit = ax3.get_horizontal_line(ax3.c2p(365, S), line_config={"dashed_ratio": 0.9}, stroke_width=3, color=COLOR_4)
        periodic_text = Tex(r"Periodic Review").scale(2).next_to(ax3.c2p(5, 620), RIGHT)
        
        periodic_model = VGroup(ax3, periodic_plot, S_limit, periodic_ip, periodic_text)

        # ============= ADD AXIS LABELS TO ALL MODELS (VGROUP)
        # for ax, model in [(ax1, epq_model), (ax2, continuous_model), (ax3, periodic_model)]:
        #     model += ax.get_x_axis_label(Tex("Time").scale(0.65), edge=DOWN, direction=DOWN, buff=0.1)

        # All models and zoom out
        VGroup(epq_model, continuous_model, periodic_model).arrange(DOWN, buff=1, center=False, aligned_edge=LEFT).move_to([15.75, 0, 0])
        
        final_arrow = Arrow(start=LEFT, end=RIGHT, color=COLOR_3, stroke_width=4,
                            max_tip_length_to_length_ratio=0.125,).next_to(formula_and_surr, RIGHT*2)
        core_concept_text = Tex(r"Core Concept", color=COLOR_3).scale(1.25).next_to(final_arrow, RIGHT*2)
        next_text = Tex(r"Fundamental\\Strategy", color=COLOR_3).scale(1.25).next_to(final_arrow, RIGHT*2)

        self.play(self.camera.frame.animate.scale(1.05).move_to([0.65, 0, 0]),
                  GrowArrow(final_arrow), Write(core_concept_text), run_time=1)
        self.wait(6.25)
        self.play(ReplacementTransform(core_concept_text, next_text), run_time=1)
        self.wait(2)

        self.play(self.camera.frame.animate.scale(2.2).move_to([9.5, 0, 0]), 
                  FadeOut(next_text), FadeOut(final_arrow),
                  FadeIn(ax1), FadeIn(epq_model[-1]),
                  FadeIn(ax2), FadeIn(continuous_model[-1]),
                  FadeIn(ax3), FadeIn(periodic_model[-1]),
                  run_time=1.25)
        self.play(Create(epq), Create(epq_vlines), #Write(epq_text),
                  Create(continuous_ip), Create(continuous_onhand), Create(s_limit), #Write(continuous_text),
                  Create(periodic_ip), Create(periodic_plot), Create(S_limit), #Write(periodic_text),
                  run_time=2.25, rate_func=linear)
        self.wait(1.15)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=1) # FadeOut all mobjects in this scene
        self.wait(0.85)

class eoq_01_03(MovingCameraScene): # Origins

    def construct(self):

        timeline = NumberLine(x_range=[1900, 2030, 10],  length=12,
                              numbers_to_include=[1900, 1913, 1950, 2000, 2020],
                              tick_size=0.075, font_size=28,
                              decimal_number_config={"group_with_commas": False,
                                                     "num_decimal_places": 0}).shift(DOWN*2.5)
        
        text_1913 = MathTex(r"1913", color=COLOR_3, font_size=50)
        dot_1913 = Dot(timeline.n2p(1913), 0.075, color=COLOR_3)
        self.play(GrowFromEdge(timeline, LEFT), run_time=1)
        self.play(Write(text_1913), run_time=0.75)
        self.play(ReplacementTransform(text_1913, dot_1913), run_time=0.75)
        
        harris_pic = FramedImage("img/0_harris.jpg", height=4.5).shift(UP*0.25)
        harris_name = Tex("Ford Whitman Harris", font_size=30).next_to(harris_pic, UP)
        harris = Group(harris_pic, harris_name)
        self.play(FadeIn(harris_pic), Write(harris_name), run_time=1)
        self.wait(4.75)

        paper1 = FramedImage("img/0_paper1.png", height=4.5).move_to([2.005,0.25,0])
        source = Tex(r"Images: www.academia.edu", font_size=17).to_edge(DOWN + RIGHT).shift(UP*1.25 + LEFT*0.15)
        self.play(harris.animate.shift(LEFT*2), FadeIn(paper1), Write(source), run_time=1)
        factory = Tex(r"\textit{Factory,\\The Magazine of Management}", font_size=24).next_to(paper1, UP)
        self.wait(2)
        self.play(Write(factory), run_time=1)
        self.wait(1)

        self.play(FadeOut(harris), FadeOut(paper1), FadeOut(factory), FadeOut(source), run_time=0.75)
        self.wait(1)

        paper2 = FramedImage("img/0_paper2.png", height=4.5).shift(UP*0.25)
        self.play(FadeIn(paper2), Write(source), run_time=1)
        self.wait(3.5)

        lot = Lot(rows=5, cols=5, buff=0.085)
        surr_i = SurroundingRectangle(lot, color=COLOR_1, buff=0.085, stroke_width=2.5, corner_radius=0.085)
        node_i = VGroup(lot, surr_i).scale(1.25)
        node_j = surr_i.copy()
        VGroup(node_i, node_j).arrange(RIGHT, buff=3).shift(UP)
        supplier_txt = Tex(r"Supplier", font_size=26).next_to(node_i, DOWN*0.75)

        arrLR = Arrow(node_i.get_edge_center(RIGHT), node_j.get_edge_center(LEFT), 
                      color=COLOR_1, stroke_width=3, max_tip_length_to_length_ratio=0.048,
                      buff=0.1).shift(DOWN*0.5)
        arrRL = Arrow(node_j.get_edge_center(LEFT), node_i.get_edge_center(RIGHT),
                      color=COLOR_1, stroke_width=3, max_tip_length_to_length_ratio=0.048,
                      buff=0.1).shift(UP*0.5)

        more_apparent = Tex(r"More Apparent\\Ordering Costs",
                            tex_environment="flushleft", font_size=26, color=COLOR_3).next_to(arrRL, UP*2)
        more_subtle = Tex(r"More Subtle\\Holding Costs\\(capital interest, depreciation)",
                            tex_environment="flushleft", font_size=26, color=COLOR_3).next_to(node_j, DOWN*1.5)
        more_apparent[0][12:].set_color(COLOR_1)
        more_subtle[0][10:].set_color(COLOR_1)

        self.play(paper2.animate.fade(0.96),
                  Create(surr_i), GrowFromCenter(lot),
                  Create(node_j),
                  Write(supplier_txt), run_time=1)
        self.wait(0.75)
        self.play(GrowArrow(arrRL), Write(more_apparent), run_time=1.25)
        self.wait(0.25)
        self.play(lot.animate.move_to(node_j.get_center()), GrowArrow(arrLR), run_time=1.25)
        self.wait(1.5)
        self.play(Write(more_subtle), run_time=1)
        self.wait(2)
        for i in range(3):
            self.play(lot[i].animate.fade(1), run_time=1.35)
        self.play(*[FadeOut(x) for x in [node_i, node_j, supplier_txt,
                                         more_apparent, more_subtle,
                                         arrLR, arrRL,
                                         paper2, source]],
                  run_time=1)
        self.wait(1)

        # =============================================================================================

        timeline_dot = VGroup(timeline, dot_1913)
        self.play(timeline_dot.animate.move_to([0,0,0]), run_time=1.5, rate_func=smooth)

        fsize = 0.70
        offset = 1
        fpaper1 = FramedImage(r"img\0_fakepaper1.png", width=fsize).move_to(timeline.n2p(1920)).shift(UP*offset)
        fpaper2 = FramedImage(r"img\0_fakepaper2.png", width=fsize).move_to(timeline.n2p(1930)).shift(DOWN*1.25)
        fpaper3 = FramedImage(r"img\0_fakepaper4.png", width=fsize).move_to(timeline.n2p(1940)).shift(UP*offset)
        fpaper4 = FramedImage(r"img\0_fakepaper4.png", width=fsize).move_to(timeline.n2p(1950)).shift(DOWN*1.25)
        self.play(LaggedStart(FadeIn(fpaper1), FadeIn(fpaper2), FadeIn(fpaper3), FadeIn(fpaper4),
                              lag_ratio=0.5, run_time=3))
        self.wait(0.5)
        self.play(*[FadeOut(f) for f in [fpaper1, fpaper2, fpaper3, fpaper4]], run_time=1)
        self.wait(0.25)
        eoq_arrow = Arrow(timeline.n2p(1913), timeline.n2p(1970), color=COLOR_3,
                          max_tip_length_to_length_ratio=0.035, stroke_width=3).shift(LEFT*0.25 + UP*0.5)
        self.play(GrowArrow(eoq_arrow), run_time=3.75, rate_func=linear)

        self.wait(0.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.75)

        self.wait(1.5)

vspace = 2
stroke_width = 2

class eoq_01_04(MovingCameraScene):

    def construct(self):
        self.wait(1.5)

        raw = ImageMobject("sku/materials_steel_01.png")
        comp = Group(ImageMobject("sku/parts_metal_03.png"),
                     ImageMobject("sku/tech_circuit_02.png")).arrange(DOWN, buff=1)
        final = Group(ImageMobject("sku/tech_smartphone_02.png"),
                      ImageMobject("sku/vehicle_motorcycle_02.png")).arrange(DOWN, buff=1)
        for img in [comp, final]:
            img.width = 2
        raw.width = 4.25
        inv_img = Group(raw, comp, final).arrange(RIGHT, buff=0.8).shift(DOWN*0.25)

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
        self.wait(4.5)

        for x in [raw_txt, comp_txt, final_txt]:
            self.play(Write(x), run_time=0.5)
            self.wait(0.5)

        sku = RoundedRectangle(corner_radius=0.1, width=0.75, height=0.75,
                               color=COLOR_1, stroke_color=COLOR_2,
                               stroke_width=2, fill_opacity=1)

        unit_txt = Tex("Unit of inventory", color=COLOR_2).next_to(sku, UP*0.5)
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
        surr_sku = SurroundingRectangle(sku_matrix, color=COLOR_1,
                                        buff=0.1, corner_radius=0.1, stroke_width=2.5)
        sku_txt = Tex("One year of demand", color=COLOR_2).next_to(surr_sku, UP*0.5)
        self.play(ReplacementTransform(sku, sku_matrix),
                  ReplacementTransform(unit_txt, sku_txt),
                  Create(surr_sku), run_time=0.80)
        self.wait(2)

        timeline = NumberLine(x_range=[0,12,1], length=10, tick_size=0.05).shift(DOWN*1.5).scale(1.1)
        unit_time_txt = Tex("Unit Time").next_to(timeline, DOWN)
        self.play(ReplacementTransform(sku_txt, unit_time_txt), GrowFromCenter(timeline),
                  FadeOut(sku_matrix), FadeOut(surr_sku))
        self.wait(2.5)

        sku_2.scale(0.75)
        sku_batch = VGroup(*[sku_2.copy() for _ in range(35)]).arrange_in_grid(rows=7, buff=0.1).scale(1.25)
        sku_batch.next_to(timeline, UP*0.75).align_to(timeline, LEFT)
        
        brace_txt = Tex(r"Acquiring and Holding Inventory", color=COLOR_3).next_to(timeline, UP*11.5)
        self.play(GrowFromCenter(sku_batch), Write(brace_txt), run_time=0.5)
        for x in range(len(sku_batch)):
            self.play(FadeOut(sku_batch[0]), sku_batch.animate.shift(RIGHT * 0.105),
                      run_time=0.06, rate_func=smooth)
            sku_batch.remove(sku_batch[0])

        self.wait(0.3)
        sku_batch = VGroup(*[sku_2.copy() for _ in range(35)]).arrange_in_grid(rows=7, buff=0.1).scale(1.25)
        sku_batch.next_to(timeline, UP*0.75).align_to(timeline, LEFT).shift(RIGHT*5.5)
        self.play(GrowFromCenter(sku_batch), run_time=0.5)
        for x in range(len(sku_batch)):
            self.play(FadeOut(sku_batch[0]), sku_batch.animate.shift(RIGHT * 0.105),
                      run_time=0.06, rate_func=smooth)
            sku_batch.remove(sku_batch[0])

        self.wait(1.4)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(1)

total_cost_txt = Tex(r"\textbf{Total Inventory Cost}", font_size=30)
total_cost_txt.to_corner(UL).shift(DOWN*0.35 + RIGHT*0.25)
total_cost_math = MathTex(r"= cD + c_t\frac{D}{Q} + c_e\frac{Q}{2}",
                          font_size=35).next_to(total_cost_txt, RIGHT*0.35)
tcgroup1 = VGroup(total_cost_txt, total_cost_math)
tcgroup1_surr = SurroundingRectangle(tcgroup1, color=COLOR_1, stroke_width=2, buff=0.15, corner_radius=0.075)

equals = total_cost_math[0][0]
material_math = total_cost_math[0][1:3]
plus1 = total_cost_math[0][3]
setup_math = total_cost_math[0][4:9]
plus2 = total_cost_math[0][9]
holding_math = total_cost_math[0][10:]

class eoq_01_05(MovingCameraScene): # Material Cost

    def construct(self):
        material_eq = MathTex(r"cD").scale(1.2).shift(UP*1.65)
        material_txt = Tex(r"\textbf{Material Cost}").shift(UP*2.5)
        self.play(Write(total_cost_txt), run_time=0.75)
        self.wait(2.25)
        self.play(Write(material_txt), run_time=0.75)
        self.wait(1.5)

        lot_600 = Lot(rows=20, cols=30, buff=0.125).scale(1.08)
        surrounding = SurroundingRectangle(lot_600, color=COLOR_1, buff=0.16, corner_radius=0.16,
                                           stroke_width=2.5)
        
        procurement_text = Tex(r"Procurement", color=COLOR_2)
        production_text = Tex(r"Production", color=COLOR_2)
        proc_or_prod = VGroup(procurement_text, production_text).arrange(RIGHT, buff=1.25).shift(UP*1.65)

        material_lot = VGroup(lot_600, surrounding).scale(0.5).next_to(proc_or_prod, DOWN*2.2)
        
        self.play(GrowFromCenter(lot_600), Create(surrounding), run_time=1.25)
        self.wait(2)
        self.play(Write(procurement_text), run_time=0.75)
        self.play(Write(production_text), run_time=0.75)
        self.wait(0.25)
        self.play(FadeOut(proc_or_prod), run_time=0.75)
        self.play(Write(material_eq), run_time=0.75)

        c_arrow = Arrow(material_eq.get_edge_center(LEFT) - [1.25,0,0],
                        material_eq.get_edge_center(LEFT),
                        max_tip_length_to_length_ratio=0.1,
                        color=COLOR_3,
                        stroke_width=2.25)
        c_text = Tex(r"Unit Cost", color=COLOR_2).next_to(c_arrow, LEFT)
        self.play(Write(c_text), GrowArrow(c_arrow), run_time=0.75)
        self.wait(1)
        D_arrow = Arrow(material_eq.get_edge_center(RIGHT) + [1.25,0,0],
                        material_eq.get_edge_center(RIGHT),
                        max_tip_length_to_length_ratio=0.1,
                        color=COLOR_3,
                        stroke_width=2.25)
        D_text = Tex(r"Total Demand", color=COLOR_2).next_to(D_arrow, RIGHT)
        lot_arrow = Arrow(D_text.get_center() + [0, 0.05, 0],
                          D_text.get_center() - [0, 0.85, 0],
                          max_tip_length_to_length_ratio=0.2,
                          color=COLOR_3,
                          stroke_width=2.5)
        self.play(LaggedStart(AnimationGroup(Write(D_text), GrowArrow(D_arrow)),
                              GrowArrow(lot_arrow),
                              lag_ratio=0.40, run_time=1.25))
        self.wait(1.5)

        # FOR MERCHANTS 
        merchants_img = FramedImage("img/1_retail.png", width=4)
        purchase_prep_text = Tex(r"Purchase price + Sale preparation costs")
        pack_n_label_arrow = Arrow(purchase_prep_text.get_edge_center(RIGHT),
                                   purchase_prep_text.get_edge_center(RIGHT) + [1.25,0,0],
                                   max_tip_length_to_length_ratio=0.15,
                                   color=COLOR_3,
                                   stroke_width=2.5)
        pack_n_label_text = Tex(r"Packaging \&\\Labeling", tex_environment="flushleft", color=COLOR_2)
        Group(merchants_img,
              purchase_prep_text,
              pack_n_label_arrow,
              pack_n_label_text).arrange(RIGHT, buff=0.25).to_edge(DOWN).shift(UP*0.15) # <--------------
        VGroup(purchase_prep_text, pack_n_label_arrow, pack_n_label_text).shift(UP*0.25)
        merchants_text = Tex(r"\textbf{Unit Cost for Merchants}", color=COLOR_5)
        VGroup(purchase_prep_text,
               merchants_text).arrange(UP, buff=0.35, center=False, aligned_edge=LEFT)
        
        self.play(FadeOut(material_lot), FadeOut(lot_arrow),
                  FadeOut(c_arrow), FadeOut(c_text), FadeOut(D_arrow), FadeOut(D_text),
                  FadeIn(merchants_img), Write(merchants_text), 
                  material_eq[0][0].animate.set_color(COLOR_5), run_time=0.75)
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
        load_unload = Tex(r"Loading \& Unloading", color=COLOR_2).next_to(
            freight_mhandling_text.get_edge_center(RIGHT) - [1,0.25,0],
            DOWN*2)
        load_arrow = Arrow(load_unload.get_center() +  [0,0.9,0],
                           load_unload.get_center(),
                           max_tip_length_to_length_ratio=0.2,
                           color=COLOR_3, stroke_width=2.5)
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
        producers_text = Tex(r"\textbf{Unit Cost for Producers}", color=COLOR_5)
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
                                      color=COLOR_3, buff=0.05, corner_radius=0.015,
                                      stroke_width=stroke_width)
        self.play(Create(D_surr), run_time=1)
        self.wait(2.5)
        known = Tex("Known and Constant", color=COLOR_3).next_to(D_surr.get_center(), DOWN*3.25)
        self.play(Write(known), run_time=1.25)
        self.wait(2)
        self.play(FadeOut(D_surr), FadeOut(known), run_time=1)
        self.wait(1.75)
        self.play(FadeOut(material_txt), FadeIn(equals), ReplacementTransform(material_eq, material_math),
                  Create(tcgroup1_surr))
        self.wait(1.5)

class eoq_01_06(MovingCameraScene): # Setup Cost

    def construct(self):
        setup_eq = MathTex(r"c_t\frac{D}{Q}")
        
        self.add(total_cost_txt, equals, material_math, tcgroup1_surr)
        self.play(FadeIn(plus1), run_time=.5)
        self.wait(0.25)

        # Lots
        sku = RoundedRectangle(corner_radius=0.1, width=1, height=1, color=COLOR_1, stroke_color=COLOR_2,
                               stroke_width=2, fill_opacity=1).scale(0.25)
        lot1 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        lot2 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        lot3 = VGroup(*[sku.copy() for _ in range(25)]).arrange_in_grid(rows=5, buff=0.1)
        VGroup(lot1, lot2, lot3).arrange(RIGHT, buff=2).shift(DOWN*0.75)
        
        setup_txt = Tex(r"\textbf{Ordering Cost}").shift(UP*1.75)
        self.play(Write(setup_txt), run_time=0.75)
        self.wait(1.25)

        ordering_txt = Tex(r"\textbf{Setup Cost}").next_to(setup_txt, DOWN*3.25)
        manufc_txt = Tex(r"(Manufacturing)", font_size=28).next_to(ordering_txt, RIGHT*0.5)
        ordering_arrow = Arrow(setup_txt.get_center(),
                               ordering_txt.get_center(),
                               max_tip_length_to_length_ratio=0.15,
                               color=COLOR_3,
                               stroke_width=2.25)
        self.play(LaggedStart(AnimationGroup(GrowArrow(ordering_arrow), Write(ordering_txt)),
                              Write(manufc_txt),
                              lag_ratio=0.35, run_time=1))
        self.wait(0.5)
        self.play(FadeOut(ordering_arrow), FadeOut(ordering_txt), FadeOut(manufc_txt), run_time=0.75)
        self.wait(0.25)

        fixed_txt_1 = Tex("Fixed Cost", color=COLOR_3).next_to(lot1, UP*0.75)
        fixed_txt_2 = Tex("Fixed Cost", color=COLOR_3).next_to(lot2, UP*0.75)
        fixed_txt_3 = Tex("Fixed Cost", color=COLOR_3).next_to(lot3, UP*0.75)

        arr1 = Arrow(setup_txt.get_corner(DL), fixed_txt_1.get_corner(UR),
                     max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=2.25)
        arr2 = Arrow(setup_txt.get_edge_center(DOWN) + [0, 0.12, 0],
                     fixed_txt_2.get_edge_center(UP) - [0, 0.12, 0],
                     max_tip_length_to_length_ratio=0.125, color=COLOR_3, stroke_width=2.25)
        arr3 = Arrow(setup_txt.get_corner(DR), fixed_txt_3.get_corner(UL),
                     max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=2.25)
        
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

        same_txt = Tex(r"Same fixed cost", color=COLOR_3)
        same_txt.move_to(midpoint(lot_big.get_edge_center(RIGHT),
                                  lot3.get_edge_center(LEFT)))
        arrL = Arrow(same_txt.get_edge_center(LEFT), lot_big.get_edge_center(RIGHT),
                     max_tip_length_to_length_ratio=0.125, color=COLOR_3, stroke_width=2.5)
        arrR = Arrow(same_txt.get_edge_center(RIGHT), lot3.get_edge_center(LEFT),
                     max_tip_length_to_length_ratio=0.125, color=COLOR_3, stroke_width=2.5)

        self.play(FadeIn(lot_big), Write(same_txt),
                  GrowArrow(arrL), GrowArrow(arrR), run_time=1)

        self.wait(2.5)
        self.play(*[FadeOut(mob) for mob in [lot_big, lot1, lot3, arrL, arrR, same_txt]], run_time=1)

        total_setup_txt = Tex(r"\textbf{Total Ordering Cost}").move_to(setup_txt.get_center())
        self.play(ReplacementTransform(setup_txt, total_setup_txt), run_time=1)

        self.wait(3)

        year_sku = VGroup(*[sku.copy() for _ in range(225)]).arrange_in_grid(rows=9, buff=0.150)
        year_sku.next_to(total_setup_txt, DOWN*2.5)
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
        lot_surr = SurroundingRectangle(lot_sku, color=COLOR_3, buff=0.075, corner_radius=0.1, stroke_width=2.6)
        other_surr = VGroup(*[lot_surr.copy() for _ in range(4)]).arrange(RIGHT, buff=0)
        other_surr.next_to(lot_surr, RIGHT, buff=0)

        lot_txt = Tex("$Q$ units", color=COLOR_3).next_to(lot_surr, LEFT*0.5)
        self.play(Create(lot_surr), Write(lot_txt), run_time=1, rate_func=linear)

        self.wait(1.5)
        self.play(FadeOut(lot_txt), Create(other_surr), run_time=2)

        self.wait(2)

        equals_ = MathTex(r"=").next_to(total_setup_txt, RIGHT*0.55)
        setup_eq.next_to(equals_, RIGHT*0.55)
        self.play(Write(setup_eq[0][2:]), run_time=0.75)
        self.wait(3)
        self.play(Write(setup_eq[0][0:2]), run_time=0.75)
        self.wait(1)
        self.play(Write(equals_), run_time=0.75)
        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in [lot_surr, other_surr, year_sku, total_setup_txt, equals_]],
                  setup_eq.animate.move_to(total_setup_txt.get_center() - [0,0.25,0])
                  )
        
        img_office = FramedImage("img/2_office.png", width=4)
        img_routes = FramedImage("img/2_routes.png", width=4)
        img_unload = FramedImage("img/2_unloading.png", width=4)
        g_fixed = Group(img_office, img_routes, img_unload).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.15)

        o_txt = Tex(r"\textbf{Costs of Ordering Inventory}", color=COLOR_5)
        o_txt.next_to(img_office, UP*1.15).align_to(img_office, LEFT)
        self.play(setup_eq[0][0:2].animate.set_color(COLOR_3))
        self.wait(4)
        self.play(Write(o_txt), FadeIn(img_office), run_time=1.25)
        self.wait(8.75)
        self.play(FadeIn(img_routes), run_time=1.25)
        self.wait(5.75)
        self.play(FadeIn(img_unload), run_time=1.25)
        self.wait(11)
        self.play(FadeOut(g_fixed), run_time=1)

        self.wait(2)
        img_few  = FramedImage("img/3_fewitems.png", width=4)
        img_many  = FramedImage("img/3_manyitems.png", width=4)
        Group(img_many, img_few).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.15)
        self.play(FadeIn(img_many), FadeIn(img_few), run_time=1)
        self.wait(9)
        self.play(FadeOut(img_many), FadeOut(img_few), FadeOut(o_txt), run_time=1)
        self.wait(1.5)

        fixvar_setup_eq = MathTex(r"(c_{t_f} + c_{t_v}Q)\frac{D}{Q}").shift(DOWN*0.25)
        fixvar_arr = Arrow(setup_eq[0][0].get_center(),
                           (setup_eq[0][0].get_x(), fixvar_setup_eq.get_y() + 0.25, 0),
                           max_tip_length_to_length_ratio=0.05, color=COLOR_3, stroke_width=stroke_width)
        fixvar_setup_eq[0][0:10].set_color(COLOR_3)

        self.play(TransformByGlyphMap(setup_eq, fixvar_setup_eq,
                                      ([0,1], [0,1,2,3,4]),
                                      ([0,1], [5,6,7,8,9]),
                                      ([2,3,4], [10,11,12]), from_copy=True,
                                      ), run_time=2)
        self.wait(3.5)

        fixvar_setup_eq_2 = MathTex(r"c_{t_f}\frac{D}{Q} + c_{t_v}Q\frac{D}{Q}").shift(DOWN*0.25)
        fixvar_setup_eq_3 = MathTex(r"c_{t_f}\frac{D}{Q} + c_{t_v}D").shift(DOWN*0.25)

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
                           material_math.get_edge_center(DOWN),
                           max_tip_length_to_length_ratio=0.0265, color=COLOR_3, stroke_width=2.25)
        
        self.play(GrowArrow(arr_fixvar), run_time=1)

        self.wait(6)

        no_escale = Tex(r"Assumes no economies of scale", tex_environment="flushleft", color=COLOR_3)
        no_escale.next_to(fixvar_setup_eq_3, DOWN*2)
        self.play(Write(no_escale), run_time=0.75)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [fixvar_setup_eq_3, arr_fixvar, no_escale]])

        img_machine = FramedImage("img/4_machine_setup.png", width=4)
        img_learning = FramedImage("img/4_learning2.png", width=4)
        img_opportunity = FramedImage("img/4_opportunity.png", width=4)
        g_fixed = Group(img_machine, img_learning, img_opportunity).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(UP*0.15)

        s_txt = Tex(r"\textbf{Setup Costs in Manufacturing}", color=COLOR_5)
        s_txt.next_to(img_machine, UP*1.15).align_to(img_machine, LEFT)

        self.wait(6)

        self.play(Write(s_txt), FadeIn(img_machine), run_time=1)
        self.wait(6)
        self.play(FadeIn(img_learning), run_time=1)
        self.wait(10)
        self.play(FadeIn(img_opportunity), run_time=1)
        self.wait(8)

        self.play(FadeOut(g_fixed), FadeOut(s_txt), run_time=1)
        self.play(ReplacementTransform(setup_eq, setup_math), run_time=1.25)
        self.wait(1)     

class eoq_01_07(Scene): # Holding Cost
    def construct(self):
        self.add(total_cost_txt, equals, material_math, plus1, setup_math, tcgroup1_surr)
        self.play(FadeIn(plus2), run_time=.5)
        self.wait(0.5)

        holding_txt = Tex(r"\textbf{Holding Cost}").shift(UP*1.75)
        self.play(Write(holding_txt), run_time=1)
        self.wait(1)

        carrying_txt = Tex(r"\textbf{Carrying Cost}").next_to(holding_txt, DOWN*3.25)
        arrow1 = Arrow(holding_txt.get_center(), carrying_txt.get_center(),
                       color=COLOR_3,
                       max_tip_length_to_length_ratio=0.15,
                       stroke_width=2.25)
        self.play(LaggedStart(GrowArrow(arrow1), Write(carrying_txt), run_time=1.25, lag_ratio=0.75))
        self.wait(1)

        self.play(FadeOut(arrow1), FadeOut(carrying_txt), run_time=0.75)
        self.wait(3)

        lot1 = Lot(4,4) 
        lot2 = Lot(7,7)
        different_txt = Tex(r"Different\\Holding Costs", color=COLOR_3)
        VGroup(lot1, different_txt, lot2).arrange(RIGHT, buff=1.5).shift(DOWN*0.5)
        arrowL = Arrow(different_txt.get_edge_center(LEFT), lot1.get_edge_center(RIGHT),
                       color=COLOR_3, max_tip_length_to_length_ratio=0.125,
                       stroke_width=2.25)
        arrowR = Arrow(different_txt.get_edge_center(RIGHT), lot2.get_edge_center(LEFT),
                       color=COLOR_3, max_tip_length_to_length_ratio=0.125,
                       stroke_width=2.25)
        self.play(GrowFromCenter(lot1), run_time=1)
        self.wait(1)
        self.play(GrowFromCenter(lot2), run_time=1)
        self.wait(1)
        self.play(GrowArrow(arrowL), GrowArrow(arrowR), Write(different_txt), run_time=1.25)
        self.wait(4.5)
        self.play(*[FadeOut(mob) for mob in [lot1, arrowL, different_txt, arrowR, lot2]], run_time=1)
        self.wait(3)

        capital_img = FramedImage("img/5_money2.png", width=4).to_edge(DOWN).shift(UP*0.15 + LEFT*4)
        capital_txt = Tex(r"\textbf{Cost of Capital}", color=COLOR_5).next_to(capital_img, UP*0.75)
        self.play(Write(capital_txt), run_time=1)
        self.wait(1)
        
        self.play(FadeIn(capital_img), run_time=1)
        self.wait(5.5)
        alternative = Tex("Alternative investments").next_to(capital_img, RIGHT*8)
        self.play(Write(alternative), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(alternative), run_time=1)
        self.wait(1)

        equity = Tex("Equity")
        equity_surr = SurroundingRectangle(equity, color=COLOR_1, buff=0.1,
                                           corner_radius=0.025, stroke_width=2.25,
                                           fill_color=DBLUE, fill_opacity=0.1)
        equity = VGroup(equity,
                        equity_surr)
        debt = Tex("Debt")
        debt = VGroup(debt,
                      equity_surr.copy().move_to(debt.get_center()))
        equity_debt = VGroup(equity, debt).arrange(RIGHT, buff=2).next_to(capital_img, RIGHT*8).shift(UP*0.5)
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

        prime_img = FramedImage("img/5_prime2.png", width=4)
        storage_img = FramedImage("img/5_storage.png", width=4)
        refrige_img = FramedImage("img/5_refrigeration_2.png", width=4)
        storage_group = Group(prime_img, storage_img, refrige_img).arrange(RIGHT, buff=0.5)
        storage_group.to_edge(DOWN).shift(UP*0.15)

        storage_txt = Tex(r"\textbf{Cost of Storage}", color=COLOR_5).next_to(storage_img,UP*0.75)
        self.play(Write(storage_txt), run_time=1)
        self.wait(1.25)
        self.play(FadeIn(prime_img), run_time=1)
        self.wait(4.5)
        self.play(FadeIn(storage_img), run_time=1)
        self.wait(4)
        self.play(FadeIn(refrige_img), run_time=1)
        self.wait(7)
        self.play(*[FadeOut(mob) for mob in [storage_txt, prime_img, storage_img, refrige_img]], run_time=1)

        self.wait(1)
        foo_img = FramedImage("img/5_other.png", width=7)
        other_holding = VGroup(Tex(r"Perishability"),
                               Tex(r"Shrinkage"),
                               Tex(r"Insurance"),
                               Tex(r"Taxation")).set_color(COLOR_5).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        Group(foo_img, other_holding).arrange(RIGHT, buff=1).to_edge(DOWN).shift(UP*0.15)

        self.play(FadeIn(foo_img), run_time=1)
        self.wait(0.5)
        for mob in other_holding:
            self.play(Write(mob), run_time=0.75)
            self.wait(0.25)


        self.wait(3)
        self.play(FadeOut(foo_img), FadeOut(other_holding), run_time=1)

        self.wait(2)
        all_hold = Tex(r"\textbf{Capital Cost {\quad\quad\quad\quad} Storage Cost {\quad\quad\quad\quad} Perishability, etc.}", color=COLOR_5)
        self.play(FadeIn(all_hold), run_time=1)
        self.wait(3)
        c_e = MathTex(r"c_e", font_size=40)
        self.play(ReplacementTransform(all_hold, c_e), run_time=1)
        self.wait(3)
        c_e_foo = MathTex(r"\% \text{ of } c =", font_size=40).next_to(c_e, LEFT, buff=0.1).shift(UP*0.085)
        self.play(Write(c_e_foo), run_time=1)
        self.wait(2.75)
        holding_rate_txt = Tex("Holding rate", color=COLOR_2)
        rate_arr = DownArrow(c_e_foo[0][0], holding_rate_txt)
        self.play(LaggedStart(GrowArrow(rate_arr), Write(holding_rate_txt), run_time=1.5, lag_ratio=0.5))
        self.wait(2)

        totalhold_txt = Tex(r"\textbf{Total Holding Cost} $=$").move_to(midpoint(holding_txt.get_center(),
                                                                       c_e.get_center()))
        totalhold_txt.shift([-2, 0.75, 0])
        
        self.play(FadeOut(c_e_foo), FadeOut(rate_arr), FadeOut(holding_rate_txt),
                  ReplacementTransform(holding_txt, totalhold_txt), run_time=1)
        self.wait(1)
        self.play(c_e.animate.move_to(totalhold_txt.get_right() + [0.3,0,0]), run_time=1)
        inventory_held_txt = Tex(r"$\times$ Inventory held during the year").next_to(c_e.get_right(), buff=0).shift([0.1,0,0])
        self.play(Write(inventory_held_txt), run_time=1)
        
        self.wait(3)
        howmuch = Tex("How much inventory is held?", color=COLOR_3)
        self.play(Write(howmuch), run_time=1)
        self.wait(3)
        self.play(FadeOut(howmuch), run_time=0.5)
        self.wait(0.5)
        
        demand_txt = Tex("Demand", color=COLOR_2)
        constant_txt = Tex(r"Constant throughout the year", color=COLOR_3)
        arrow2 = RightArrow(demand_txt, constant_txt)
        VGroup(demand_txt, constant_txt, arrow2).move_to(ORIGIN)
        self.play(Write(demand_txt), run_time=1)
        self.wait(1)
        self.play(LaggedStart(GrowArrow(arrow2), Write(constant_txt), lag_ratio=0.5, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(constant_txt), run_time=0.75)
        self.wait(0.35)

        steady_txt = Tex(r"Steady rate of consumption", color=COLOR_3).next_to(constant_txt.get_left(), buff=0)
        self.play(Write(steady_txt), run_time=1)
        self.wait(3.15)
        self.play(FadeOut(arrow2), FadeOut(steady_txt), FadeOut(demand_txt), run_time=0.75)

        self.wait(1)
        yshift = DOWN*0.85 + RIGHT*0.35
        self.play(*[FadeIn(mob) for mob in [grid.shift(yshift),
                                            x_label.shift(yshift),
                                            y_label.shift(yshift)]], run_time=1)
        self.wait(1.25)
        size_Q = MathTex(r"Q\;\text{units}", font_size=28, color=COLOR_3).next_to(grid.c2p(0,400), LEFT*1)
        self.play(Write(size_Q), run_time=0.75)
        self.wait(0.5)
        sawtooth.shift(yshift)
        self.play(Create(sawtooth), run_time=6, rate_func=linear)
        self.wait(4.5)

        # Continuous Demand
        cont_txt = Tex("Continuous Demand", font_size=28, color=COLOR_3).move_to(grid.c2p(180, 470))
        self.play(Write(cont_txt), run_time=1)
        lines = VGroup(*[Line(grid.c2p(i*replenishment_period, 400, 0),
                              grid.c2p((i+1)*replenishment_period, 0, 0),
                              stroke_width=3, color=COLOR_2) for i in range(6)])
        self.play(LaggedStart(sawtooth.animate.set_color(BLUE_A),
                              *[Create(line) for line in lines], run_time=2.5, rate_func=linear, lag_ratio=0.7))
        self.play(FadeOut(lines), FadeOut(cont_txt), sawtooth.animate.set_color(COLOR_2), run_time=0.5)
        self.wait(3.5)

        avg = grid.get_horizontal_line(grid.c2p(365, 200), line_config={"dashed_ratio": 1}, stroke_width=3, color=COLOR_4)
        self.play(Create(avg), run_time=1.5)
        self.wait(2)

        q_2 = MathTex(r"\frac{Q}{2}", font_size=28).next_to(avg, RIGHT*0.5)
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
        
class eoq_01_08(Scene): # Assumptions
    def construct(self):

        yshift = DOWN*0.85 + RIGHT*0.35

        eoq_model = VGroup(grid.shift(yshift),
                           x_label.shift(yshift),
                           y_label.shift(yshift),
                           sawtooth.shift(yshift))
        
        self.add(total_cost_txt, equals, material_math, plus1, setup_math, plus2, holding_math,
                 eoq_model, tcgroup1_surr)
        self.wait(2)

        self.play(eoq_model.animate.scale(0.60).shift(LEFT*(2.75 + 0.25) + UP*0.6))
        assumptions = VGroup(Tex(r"\textbf{EOQ Assumptions:}"),
                        Tex(r"$\bullet$ Known and constant demand"),
                        Tex(r"$\bullet$ Continuous demand"),
                        Tex(r"$\bullet$ Instantaneous replenishment"),
                        Tex(r"$\bullet$ No quantity discounts"),
                        Tex(r"$\bullet$ No perishability constraints"),
                        Tex(r"$\bullet$ Infinite planning horizon"),
                        Tex(r"$\bullet$ Continuous review of inventory"),
                        Tex(r"$\bullet$ No order size or capacity restrictions"),
                        Tex(r"$\bullet$ No backorders"),
                        Tex(r"$\bullet$ Constant cost parameters"),
                        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(eoq_model, RIGHT*2.5)
        assumptions.scale(0.95)
        self.wait(1.25)
        self.play(Write(assumptions[0]), run_time=1) # Title
        self.wait(3.25)
        self.play(Write(assumptions[1]), run_time=1) # Known and constant
        self.wait(2.75)

        # Continuous
        lines = VGroup(*[Line(grid.c2p(i*replenishment_period, 400, 0),
                              grid.c2p((i+1)*replenishment_period, 0, 0),
                              stroke_width=3, color=COLOR_2) for i in range(6)])
        self.play(Write(assumptions[2]), run_time=1)
        self.wait(1)    
        self.play(LaggedStart(sawtooth.animate.set_color(BLUE_A),
                              *[Create(line) for line in lines],
                              run_time=2, rate_func=linear, lag_ratio=0.5))
        self.play(FadeOut(lines), sawtooth.animate.set_color(COLOR_2), run_time=0.75)
        self.wait(2)

        # Insta replenishment
        self.play(Write(assumptions[3]), run_time=1) 
        self.wait(3)
        lines = VGroup(*[Line(grid.c2p(i*replenishment_period, 0, 0),
                              grid.c2p(i*replenishment_period, 400, 0),
                              stroke_width=3, color=COLOR_2) for i in range(6)])
        self.play(LaggedStart(sawtooth.animate.set_color(BLUE_A),
                              *[Create(line) for line in lines], 
                              run_time=1.75, rate_func=linear, lag_ratio=0.5))
        self.play(FadeOut(lines), sawtooth.animate.set_color(COLOR_2), run_time=0.5)
        self.wait(1.25)

        self.play(Write(assumptions[4]), run_time=1) # No discounts
        self.wait(2.5)
        self.play(Write(assumptions[5]), run_time=1) # No item perish
        self.wait(5.25)
        self.play(Write(assumptions[6]), run_time=1) # Infinite horizon
        self.wait(4)
        perp_arrow = Arrow([-2.45,0,0], [+1.2,0,0],
                           color=COLOR_3, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.045).shift(DOWN*1.75 + LEFT*0.25)
        perp_txt = Tex("Perpetual", color=COLOR_3).scale(0.95).next_to(perp_arrow, DOWN*0.35)
        self.play(LaggedStart(GrowArrow(perp_arrow), Write(perp_txt), run_time=1.5, lag_ratio=0.5))
        self.wait(2.5)
        self.play(FadeOut(perp_arrow), FadeOut(perp_txt), run_time=1)
        self.wait(1.25)
        self.play(Write(assumptions[7]), run_time=1) # Cont review
        self.wait(2.5)
        check_inv = Circle(radius=0.25, stroke_width=2,
                           color=COLOR_3, fill_opacity=0.3).move_to(grid.c2p(4*replenishment_period, 400, 0))
        self.play(GrowFromCenter(check_inv), run_time=1)
        self.play(check_inv.animate.move_to(grid.c2p(5*replenishment_period, 0, 0)),
                  run_time=3, rate_func=linear)
        self.play(FadeOut(check_inv), run_time=1)
        self.wait(10)

        self.play(Write(assumptions[8]), run_time=1) # No size or capacity restrictions
        self.wait(3.5)
        self.play(Write(assumptions[9]), run_time=1) # No planned backorders

        self.wait(4.5)

        arr_costs = VGroup()
        for i in [1, 4, 10]:
            arr = Arrow(total_cost_math[0][i].get_center(),
                        total_cost_math[0][i].get_center() + DOWN*1.5,
                        color=COLOR_3, stroke_width=2.25, max_tip_length_to_length_ratio=0.125)
            arr_costs.add(arr)
        costs_constant = Tex("Constant over time", color=COLOR_3).next_to(arr_costs, DOWN*0.5)

        self.play(LaggedStart(GrowArrow(arr_costs[0]),
                              GrowArrow(arr_costs[1]),
                              GrowArrow(arr_costs[2]),
                              lag_ratio=0.6, run_time=2))
        self.wait(0.70)
        self.play(Write(costs_constant), run_time=0.80)
        self.wait(1.5)
        self.play(FadeOut(arr_costs), FadeOut(costs_constant), Write(assumptions[10]), run_time=1)
        self.wait(3.5)

        stockout_cost = Tex(r"$+$ Cost of Stockouts?", color=COLOR_3).scale(1.15).next_to(holding_math, RIGHT*1)
        self.play(Write(stockout_cost), run_time=1)
        self.wait(14)
        self.play(FadeOut(stockout_cost))
        self.wait(21.5)
        self.play(FadeOut(eoq_model), FadeOut(assumptions),
                  tcgroup1.animate.move_to(ORIGIN),
                  tcgroup1_surr.animate.move_to(ORIGIN), run_time=1.5)
        self.wait(0.25)

class eoq_01_09(MovingCameraScene):  # Total Cost Expression
    def construct(self):
        tcgroup1.move_to(ORIGIN)
        tcgroup1_surr.move_to(ORIGIN)
        self.add(tcgroup1, tcgroup1_surr)
        self.wait(1.5)

        TC_1 = MathTex(r"TC=cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}")
        self.play(FadeOut(tcgroup1_surr),
                  ReplacementTransform(total_cost_txt, TC_1[0][0:2]),
                  TransformByGlyphMap(total_cost_math, TC_1,
                                      (list(range(15)), list(range(2, 17))),
                                      ([], [0,1])
                                      ), run_time=1.5)
        self.wait(1)
        self.play(*[TC_1[0][i].animate.set_color(COLOR_3) for i in [3, 6, 7, 12, 13]], run_time=0.75)
        self.play(*[TC_1[0][i].animate.set_color(COLOR_3) for i in [4, 8]], run_time=0.75)
        self.wait(5)
        TC_2 = MathTex(r"TC(Q) = cD + c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}")
        self.play(TransformByGlyphMap(TC_1, TC_2,
                                      ([0,1], [0,1]),
                                      ([], [2,3,4]),
                                      (list(range(2, len(TC_1[0]))), list(range(5, len(TC_2[0])))), 
                                      ), run_time=1.5)
        self.wait(2)
        arr_unaff = Arrow(TC_2[0][6:8].get_center(), TC_2[0][6:8].get_center() + [0,1.5,0],
                          color=MRED, max_tip_length_to_length_ratio=0.125, stroke_width=2.25)
        unaff_txt = Tex("Remains unaffected by changes in $Q$", color=COLOR_3).next_to(arr_unaff, UP*0.5)
        self.play(LaggedStart(GrowArrow(arr_unaff), Write(unaff_txt), lag_ratio=0.5, run_time=1.5))
        self.wait(4)
        self.play(FadeOut(arr_unaff), FadeOut(unaff_txt), run_time=1)
        self.wait(5)
        focus = SurroundingRectangle(TC_2[0][9:], stroke_width=2, corner_radius=0.1, color=COLOR_3)
        self.play(Create(focus), run_time=1.25)
        self.wait(2)
        self.play(FadeOut(focus), run_time=0.75)
        self.wait(1)
        TRC_1 = MathTex(r"TRC(Q) = c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}")
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
        y_label = grid.get_y_axis_label(Tex("Cost", font_size=27).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label = grid.get_x_axis_label(Tex("Order Quantity: $Q$", font_size=27),
                                        edge=DOWN, direction=DOWN, buff=0.3)
        coord_system = VGroup(grid, y_label, x_label).shift(DOWN*0.5 + RIGHT*0.25)
        pos = UP*2
        self.play(FadeIn(coord_system), TRC_1.animate.shift(pos), run_time=1.5)
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
        opt_point = Dot(point=grid.c2p(400, 1200, 0), radius=0.075, color=COLOR_3)
        min_text = Tex("Minimum TRC", font_size=30, color=COLOR_3).next_to(opt_point, UP*0.65)
        line_1 = Line(start=q_dot_2.get_center(), end=grid.c2p(400, 1200, 0), stroke_width=2, color=COLOR_3)

        # SHOW HOLDING AND SETUP COSTS
        setup_text = Tex(r"Ordering cost", font_size=28, color=COLOR_2).move_to(grid.c2p(800, 500, 0))
        holding_text = Tex(r"Holding cost", font_size=28, color=COLOR_2).move_to(grid.c2p(1000, 1115, 0))
        TRC_text = MathTex(r"TRC(Q)", font_size=32, color=COLOR_2).move_to(grid.c2p(225, 2350, 0))
        self.wait(2)
        setup_arrow = Arrow(TRC_1[0][7:12].get_edge_center(DOWN),
                              TRC_1[0][7:12].get_edge_center(DOWN) - [0,3.25,0],
                              color=MRED, max_tip_length_to_length_ratio=0.05, stroke_width=2.25)
        self.play(LaggedStart(Create(setup_cost), Write(setup_text), GrowArrow(setup_arrow),
                              lag_ratio=0.8, run_time=3, rate_func=smooth))
        self.play(FadeOut(setup_arrow), run_time=1)
        self.wait(5)


        holding_arrow = Arrow(TRC_1[0][13:].get_edge_center(DOWN),
                              TRC_1[0][13:].get_edge_center(DOWN) - [0,2.35,0],
                              color=MRED, max_tip_length_to_length_ratio=0.05, stroke_width=2)
        self.play(LaggedStart(Create(holding_cost), Write(holding_text), GrowArrow(holding_arrow),
                              lag_ratio=0.45, run_time=2.5, rate_func=linear))
        self.play(FadeOut(holding_arrow), run_time=1)
        self.wait(7.5)
        self.play(LaggedStart(Write(TRC_text), Create(total_cost),
                              lag_ratio=0.25, run_time=2))
        self.wait(1.5)
        self.play(Create(line_1), run_time=1)
        self.play(Create(opt_point), Write(min_text), run_time=0.50, rate_func=smooth)
        self.wait(18)

        foo = Rectangle(width=20, height=20, fill_color=COLOR_1, fill_opacity=0.75)
        calc_3b1b_a = FramedImage("img/6_3b1b_main.png")
        calc_3b1b_b = FramedImage("img/6_3b1b_calculus.png", width=12)
        self.play(LaggedStart(FadeIn(foo), FadeIn(calc_3b1b_a), lag_ratio=0.25, run_time=1))
        self.wait(1.5)
        self.play(FadeOut(calc_3b1b_a), FadeIn(calc_3b1b_b), run_time=1)
        self.wait(3)
        self.play(FadeOut(calc_3b1b_b), FadeOut(foo), run_time=1)
        self.wait(1)

        
        foo = grid.plot(lambda x: 3*x/2 + 100*2400/x, x_range=[80, 400, 20], use_vectorized=True) # Helper func
        alpha = ValueTracker(0.2)
        tangent = always_redraw(lambda : TangentLine(foo,
                                                     alpha=alpha.get_value(),
                                                     color=COLOR_4, stroke_width=2,
                                                     length=6))
        
        camera_1 = self.camera.frame.save_state()
        self.play(GrowFromCenter(tangent),
                  *[FadeOut(mob) for mob in [holding_cost, holding_text, setup_cost, setup_text,
                                             line_1, opt_point, min_text]],
                  run_time=1.5)
        self.play(alpha.animate.set_value(0.6), run_time=5, rate_func=rate_functions.smooth)
        self.wait(2.5)
        self.play(self.camera.frame.animate.scale(0.75).move_to(opt_point.get_center()),
                  alpha.animate.set_value(1), run_time=2)
        self.wait(0.25)
        slope_txt = Tex("slope $= 0$", font_size=28, color=COLOR_4).move_to(grid.c2p(200, 1000, 0))
        self.play(Write(slope_txt), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(opt_point), FadeIn(min_text), run_time=1)
        self.wait(1)
        self.play(Restore(camera_1), FadeOut(tangent), FadeOut(slope_txt), run_time=1.25)
        self.wait(5)

        TRC_2 = MathTex(r"TRC'(Q) = \frac{d}{dQ}\left(c_{t}\frac{D}{Q} + c_{e}\frac{Q}{2}\right)")
        TRC_2.shift(pos)
        self.play(TransformByGlyphMap(TRC_1, TRC_2,
                                      ([0,1,2], [0,1,2]),
                                      ([], [3]),
                                      ([3,4,5,6], [4,5,6,7]),
                                      ([], [8,9,10,11,12]),
                                      ([*ir(7,17)], [*ir(13,23)]),
                                      ([], [24])
                                      ), run_time=1)
        
        optimal_0 = MathTex(r"0 = -c_{t}\frac{D}{Q^2} + \frac{c_{e}}{2}").shift(pos)
        self.wait(3)
        self.play(TransformByGlyphMap(TRC_2, optimal_0,
                                      ([*ir(0,6)], [0]*7),
                                      ([7], [1]),
                                      ([*ir(8,12)], []),
                                      ([], [2]),
                                      ([*ir(13,17)], [*ir(3,7)]),
                                      ([], [8]),
                                      ([18], [9]),
                                      ([24], []),
                                      ([21], []),
                                      ([19,20,22,23], [10,11,12,13]),
                                      ), run_time=1.75)
        self.wait(6)
        optimal_2 = MathTex(r"c_{t}\frac{D}{Q^2} = \frac{c_{e}}{2}").shift(pos)
        self.play(TransformByGlyphMap(optimal_0, optimal_2,
                                      ([0,2,9], []),
                                      ([*ir(3,8)], [*ir(0,5)]),
                                      ([*ir(10,13)], [*ir(7,10)])
                                      ), run_time=1.75)
        optimal_3 = MathTex(r"c_{t}\frac{D}{Q} = c_{e}\frac{Q}{2}").shift(pos)
        self.wait(1.75)
        self.play(TransformByGlyphMap(optimal_2, optimal_3,
                                      ([0,1,2,3,4], [0,1,2,3,4]),
                                      ([5], []),
                                      ([4], [8]),
                                      ([6,7,8], [5,6,7]),
                                      ([9,10], [9,10])
                                      ), run_time=1.75)
        self.wait(0.5)
        arr_equal = Arrow(optimal_3.get_center() - [0,0.25,0], opt_point.get_center() - [0.05,0.75,0],
                          color=COLOR_3, max_tip_length_to_length_ratio=0.035, stroke_width=2)
        self.play(GrowArrow(arr_equal), FadeIn(setup_cost), FadeIn(holding_cost), run_time=1)
        self.wait(2)
        self.play(FadeOut(arr_equal), run_time=0.75)
        self.wait(0.75)
        optimal_4 = MathTex(r"\frac{2c_{t}D}{c_{e}} = Q^2").shift(pos)
        self.play(TransformByGlyphMap(optimal_3, optimal_4,
                                      ([10,0,1,2,3,6,7,5], [0,1,2,3,4,5,6,7]),
                                      ([4], [8]),
                                      ([8], [8]),
                                      ([9], []),
                                      ([], [9]),
                                      ), run_time=1.5)
        self.wait(1)
        sqrt_formula = MathTex(r"Q = \sqrt{\frac{2c_{t}D}{c_{e}}}").shift(pos)
        self.play(TransformByGlyphMap(optimal_4, sqrt_formula,
                                      ([8,7,9], [0,1,2]),
                                      ([9], [3]),
                                      ([*ir(0,6)], [*ir(4,10)]),
                                      ), run_time=1.5)
        surr_form = SurroundingRectangle(sqrt_formula, color=COLOR_1, buff=0.275, corner_radius=0.175, stroke_width=2.25)
        self.play(Create(surr_form), run_time=1)
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in [grid, x_label, y_label, setup_cost, holding_cost, total_cost,
                                             TRC_text, opt_point, min_text]], run_time=1)
        self.wait(2)

class eoq_01_10(MovingCameraScene):  # EOQ Example
    def construct(self):
        pos = UP*2
        eoq_formula = MathTex(r"Q = \sqrt{\frac{2c_{t}D}{c_{e}}}").shift(pos)
        surr_form = SurroundingRectangle(eoq_formula, color=COLOR_1, buff=0.275, corner_radius=0.175, stroke_width=2.25)
        eoq_exp = VGroup(eoq_formula, surr_form)
        self.add(eoq_formula, surr_form)
        
        qpro10 = FramedImage("img/7_qpro10_x.png", width=3.75).to_corner(DL).shift(UP*0.25 + RIGHT*0.5)
        qpro10_txt = Tex(r"\textit{Q-Pro 10}", font_size=30, color=COLOR_5).next_to(qpro10, UP*0.65)
        self.play(eoq_exp.animate.next_to(qpro10_txt, UP*3).align_to(qpro10, LEFT),
                  FadeIn(qpro10), Write(qpro10_txt),
                  run_time=1)
        self.wait(7)
        qpro_demand = Tex("$D = 10\small{,}000$ units/year")
        qpro_ct = Tex(r"$c_t = \$ 950/$order")
        qpro_ce = Tex(r"$c_e = 20\%$ of $\$ 125$")
        qpro_data = VGroup(qpro_demand, qpro_ct, qpro_ce).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(qpro10, RIGHT*1.5)
        qpro_data.set_color(COLOR_2)
        self.play(Write(qpro_demand), run_time=1)
        self.wait(7)
        self.play(Write(qpro_ct), run_time=1)
        self.wait(8.25)
        self.play(Write(qpro_ce), run_time=1)
        self.wait(5.5)
        qpro_EOQ_1 = MathTex(r"Q = \sqrt{\frac{2(950)(10\small{,}000)}{0.20(125)}}")
        qpro_EOQ_2 = MathTex(r"Q \approx 872")
        qpro_EOQ = VGroup(qpro_EOQ_1, qpro_EOQ_2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        qpro_EOQ.next_to(qpro_data, RIGHT*4).align_to(qpro_data, DOWN).set_color(COLOR_2)
        
        self.play(Write(qpro_EOQ_1), run_time=1.5)
        self.wait(2)
        self.play(Write(qpro_EOQ_2), run_time=1)
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in [qpro10, qpro10_txt, qpro_data, qpro_EOQ]], run_time=1)
        self.wait(1)
        #
        grid = Axes(x_range=[0, 365, 30], y_range=[0, 1000, 200], x_length=11, y_length=2,
                    axis_config={"color": COLOR_1, "font_size": 25},
                    x_axis_config={"include_numbers": True, "tick_size": 0.075, "buff": 0.1},
                    y_axis_config={"include_ticks": False}, tips=False).shift(DOWN*0.35)

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label(Tex("Inventory").scale(0.85).rotate(90*DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.25)
        x_label = grid.get_x_axis_label(Tex("Days").scale(0.85),edge=DOWN, direction=DOWN, buff=0.20)

        # EOQ
        replenishments = 12
        replenishment_period = (872/10_000)*365
        x_values = [i*replenishment_period for n in range(replenishments) for i in (n, n)]
        x_values.append(x_values[-1]+replenishment_period)
        sawtooth = grid.plot_line_graph(
            x_values = x_values,
            y_values = [872 if i % 2 else 0 for i in range(len(x_values))],
            line_color=COLOR_2, stroke_width=2.25, add_vertex_dots=False,
        )
        
        brace_N = BraceBetweenPoints(grid.c2p(365, 1000), grid.c2p(0, 1000), buff=0.2, color=COLOR_3, stroke_width=0)
        qpro_N = MathTex(r"\frac{D}{Q} = \frac{10\small{,}000}{872} \approx 11.5 \text{ orders}",
                         font_size=30, color=COLOR_2).next_to(brace_N, UP*0.5)
        
        brace_T = BraceBetweenPoints(grid.c2p(31, 0), grid.c2p(65, 0), buff=0.55, color=COLOR_3, stroke_width=0)
        qpro_T = MathTex(r"10\small{,}000T = 872", font_size=30, color=COLOR_2).next_to(brace_T, DOWN*0.65)
        
        qpro_Q = MathTex(r"Q = 872", font_size=27, color=COLOR_2).next_to(grid.c2p(0, 872), RIGHT*0.5 + UP*0.65)

        self.play(*[FadeIn(mob) for mob in [grid, x_label, y_label, sawtooth, qpro_Q]],
                  Write(qpro_N), GrowFromCenter(brace_N), run_time=1.5)
        self.wait(1.75)
        self.play(LaggedStart(FocusOn(qpro_T), Write(qpro_T),
                              lag_ratio=0.5, run_time=1.75))

        qpro_T_2 = MathTex(r"T = \frac{872}{10\small{,}000}", font_size=30, color=COLOR_2).next_to(brace_T, DOWN*0.65)
        qpro_T_3 = MathTex(r"T = 0.0872 \;\;\text{years}", font_size=30, color=COLOR_2).next_to(brace_T, DOWN*0.65)
        qpro_T_4 = MathTex(r"T \approx 32 \;\;\text{days}", font_size=30, color=COLOR_2).next_to(brace_T, DOWN*0.65)

        self.wait(2)
        self.play(GrowFromCenter(brace_T),
                  TransformByGlyphMap(qpro_T, qpro_T_2,
                                      ([*ir(0,5)], [*ir(6,11)]),
                                      ([*ir(6,10)], [*ir(0,4)]),
                                      ([], [5]),
                                      ), run_time=1.5)
        self.wait(2)
        self.play(TransformByGlyphMap(qpro_T_2, qpro_T_3,
                                      ([0,1], [0,1]),
                                      ([2,3,4], [5,6,7]),
                                      ([], [2,3,4]),
                                      ([*ir(5,11)], []),
                                      ([], [*ir(8,12)]),
                                      ), run_time=1.5)
        self.wait(1.5)
        self.play(TransformByGlyphMap(qpro_T_3, qpro_T_4,
                                      ([0,1], [0,1]),
                                      ([2,3,4], [2,2]),
                                      ([5,6,7], [3,3]),
                                      ([8,9,10,11,12], [4,5,6,6,7]),
                                      ), run_time=1.5)

        self.wait(5)
        self.play(*[FadeOut(mob) for mob in [grid, x_label, y_label, sawtooth, qpro_Q, qpro_N, qpro_T_4,
                                             brace_N, brace_T]], run_time=1)
        self.wait(1)

        grid_2 = Axes(x_range=[300, 2400, 100], y_range=[0, 37500, 5000], x_length=11.5, y_length=3.75,
                    axis_config={"color": COLOR_1, "font_size": 19},
                    x_axis_config={"include_numbers": True, "tick_size": 0.075,
                                   "numbers_with_elongated_ticks": [872]},
                    y_axis_config={"include_numbers": True, "tick_size": 0.075}, tips=False).shift(DOWN*0.6 + RIGHT*0.55)
        
        y_label_2 = grid_2.get_y_axis_label(Tex("Cost $(\$)$").scale(0.85).rotate(90*DEGREES),
                                            edge=LEFT, direction=LEFT, buff=0.265)
        x_label_2 = grid_2.get_x_axis_label(Tex("Order Quantity").scale(0.85),
                                            edge=DOWN, direction=DOWN, buff=0.25)
        
        holding_cost = grid_2.plot(lambda x: 950*10000/x, x_range=[310, 2400],
                                   color=COLOR_2, use_vectorized=True, stroke_width=2)
        ordering_cost = grid_2.plot(lambda x: 0.20*125*x/2, x_range=[310, 2400],
                                    color=COLOR_2, use_vectorized=True, stroke_width=2)
        total_cost = grid_2.plot(lambda x: 950*10000/x + 0.20*125*x/2, x_range=[310 , 2400],
                                    color=COLOR_2, use_vectorized=True, stroke_width=3)

        h_text = Tex("Holding Cost", color=COLOR_2).scale(0.9).move_to(grid_2.c2p(1500, 14650, 0))
        o_text = Tex("Ordering Cost", color=COLOR_2).scale(0.9).move_to(grid_2.c2p(1510, 3550, 0))
        TRC_text = Tex(r"\textbf{TRC}", color=COLOR_2).scale(1.1).move_to(grid_2.c2p(1400, 27000, 0))
        opt_point = Dot(point=grid_2.c2p(872, 21794.5, 0), radius=0.065)
        opt_vline = grid_2.get_vertical_line(grid_2.c2p(872, 21794.495),
                                             line_config={"dashed_ratio": 1},
                                             stroke_width=2)
        opt_trc = MathTex(r"\approx 21\small{,}794", font_size=30).move_to(grid_2.c2p(872, 21794 + 3000, 0))
        twice_point = Dot(point=grid_2.c2p(411, 28251.9, 0), radius=0.065)
        twice_vline = grid_2.get_vertical_line(grid_2.c2p(411, 28251.9),
                                             line_config={"dashed_ratio": 1},
                                             stroke_width=2)
        twice_trc = MathTex(r"\approx 28\small{,}252", font_size=30).move_to(grid_2.c2p(525, 28252 + 2500, 0))
        col = VGroup(opt_point, opt_vline, opt_trc, twice_point, twice_vline, twice_trc).set_color(COLOR_3)

        self.play(FadeIn(grid_2), FadeIn(x_label_2), FadeIn(y_label_2),
                  Create(holding_cost), Create(ordering_cost), Create(total_cost),
                  Write(h_text), Write(o_text), Write(TRC_text), run_time=1)
        self.wait(2)
        self.play(Create(opt_vline), run_time=1)
        self.wait(3.25)
        self.play(LaggedStart(FadeIn(opt_point), Write(opt_trc),
                              lag_ratio=0.4, run_time=1.25))
        self.wait(6.75)

        fifteendays = MathTex(r"\frac{15}{365}(10\small{,}000) \approx 411", color=COLOR_2, font_size=25)
        fifteendays.move_to(grid_2.c2p(532, 11150, 0))
        self.play(LaggedStart(Write(fifteendays),
                              Circumscribe(fifteendays[0][0:2], fade_out=True, stroke_width=2, color=COLOR_3, duration=1),
                              lag_ratio=0.3, run_time=1.75))
        self.wait(6.25)
        self.play(FadeOut(fifteendays), Create(twice_vline), run_time=1)
        self.play(LaggedStart(FadeIn(twice_point), Write(twice_trc),
                              lag_ratio=0.4, run_time=1.25))
        self.wait(4.75)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(2)

class eoq_01_whatif(MovingCameraScene): # Sensitivity Analysis
    def construct(self):
        eoq_872 = MathTex(r"Q = 872 \;\;\text{units}")
        eoq_T = MathTex(r"T = 32 \;\;\text{days}")
        eoq_policy = VGroup(eoq_872, eoq_T).arrange(DOWN, buff=0.35, aligned_edge=LEFT).set_color(COLOR_2)
        eoq_arr = Arrow(LEFT*0.85, RIGHT*0.85,
                        color=COLOR_4, stroke_width=2.25, max_tip_length_to_length_ratio=0.09)
        infeasible = Tex(r"Infeasible", color=COLOR_4)
        eoq_group = VGroup(eoq_policy, eoq_arr, infeasible).arrange(RIGHT, buff=0.25)
        self.play(LaggedStart(AnimationGroup(Write(eoq_872), Write(eoq_T)),
                              Write(eoq_arr),
                              Write(infeasible),
                              lag_ratio=0.35, run_time=1.5))
        self.wait(3.5)

        grid = Axes(x_range=[0, 140, 14], y_range=[0, 1000, 100], x_length=9, y_length=3,
                    axis_config={"color": COLOR_1, "font_size": 20},
                    x_axis_config={"include_numbers": False, "tick_size": 0.015},
                    y_axis_config={"include_numbers": False, "tick_size": 0.05},
                    tips=False).shift(DOWN*0.75 + RIGHT*0.20).scale(1.1)

        # EOQ
        replenishments = 4
        replenishment_period = (872/10_000)*365
        x_values = [i*replenishment_period for n in range(replenishments) for i in (n, n)]
        x_values.append(x_values[-1]+replenishment_period)
        sawtooth_872 = grid.plot_line_graph(
            x_values = x_values,
            y_values = [872 if i % 2 else 0 for i in range(len(x_values))],
            line_color=COLOR_2, stroke_width=2.75, add_vertex_dots=False,
        )
        dots = MathTex(r"...", font_size=55, color=COLOR_2).move_to(grid.c2p(132,100,0))

        # Q=900
        replenishment_period_900 = (900/10_000)*365
        x_values_900 = [i*replenishment_period_900 for n in range(replenishments) for i in (n, n)]
        x_values_900.append(x_values_900[-1]+replenishment_period_900)
        sawtooth_900 = grid.plot_line_graph(
            x_values = x_values_900,
            y_values = [900 if i % 2 else 0 for i in range(len(x_values_900))],
            line_color=COLOR_4, stroke_width=2.25, add_vertex_dots=False,
        )
        eoq_900_txt = MathTex(r"Q=900", color=COLOR_4, font_size=28).move_to(grid.c2p(50, 900, 0))

        # Q=800
        replenishment_period_800 = (800/10_000)*365
        x_values_800 = [i*replenishment_period_800 for n in range(replenishments) for i in (n, n)]
        x_values_800.append(x_values_800[-1]+replenishment_period_800)
        sawtooth_800 = grid.plot_line_graph(
            x_values = x_values_800,
            y_values = [800 if i % 2 else 0 for i in range(len(x_values_800))],
            line_color=COLOR_4, stroke_width=2.25, add_vertex_dots=False,
        )
        eoq_800_txt = MathTex(r"Q=800", color=COLOR_4, font_size=28).move_to(grid.c2p(47, 800, 0))

        self.play(LaggedStart(eoq_group.animate.shift(UP*2),
                              AnimationGroup(*[FadeIn(mob) for mob in [grid,
                                                                       #x_label,
                                                                       #y_label,
                                                                       dots,
                                                                       sawtooth_872]]),
                              lag_ratio=0.35, run_time=1.5))

        self.play(FadeIn(sawtooth_900), FadeIn(eoq_900_txt), sawtooth_872.animate.fade(0.685),
                  run_time=0.75)
        self.wait(1)
        self.play(FadeOut(sawtooth_900), FadeOut(eoq_900_txt),
                  run_time=0.75)       
        self.play(FadeIn(sawtooth_800), FadeIn(eoq_800_txt),
                  run_time=0.75)

        self.wait(2)
        week_or_month = Tex(r"Weeks or Months", color=COLOR_4, font_size=30).next_to(grid, DOWN*0.75)
        week_fig = Rectangle(width=0.035, height=0.15, stroke_width=0, fill_color=COLOR_4, fill_opacity=1)
        week_dots = VGroup(*[week_fig.copy().move_to(grid.c2p(p,0,0)) for p in list(range(14,140,14))])
        self.play(LaggedStart(Write(week_or_month),
                              Create(week_dots),
                              lag_ratio=0.25, run_time=1.5))
        self.wait(4.5)
        self.wait(1 + 0.75)

        notdemand = MathTex(r"D \neq 10\small{,}000 \; \text{?}",
                            font_size=30, color=COLOR_4).move_to(infeasible.get_center() + [0.75,0,0])
        self.play(LaggedStart(eoq_group.animate.shift(LEFT*2),
                              Write(notdemand),
                              lag_ratio=0.35, run_time=1.5))
        self.wait(3.5)
        self.wait(0.5 + 1)
        self.wait(1)

        all_g = VGroup(grid, sawtooth_872, sawtooth_800, eoq_800_txt, dots,
                       notdemand, eoq_group, week_or_month, week_dots)
        sensitivity = Tex(r"Sensitivity Analysis", font_size=40, color=COLOR_1).next_to(grid, UP*5)
        self.play(LaggedStart(all_g.animate.scale(0.85).shift(DOWN*0.75),
                              Write(sensitivity),
                              lag_ratio=0.35, run_time=1.75))
        self.wait(6.75)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(1)

class eoq_01_11(MovingCameraScene):  # Ending
    def construct(self):
        formula_and_surr.shift(LEFT*2)
        arr1 = Arrow(formula[0][6].get_edge_center(RIGHT) + [3,0,0],
                     formula[0][6].get_edge_center(RIGHT),
                     color=MRED, max_tip_length_to_length_ratio=0.05, stroke_width=3)
        arr2 = Arrow(formula[0][-2].get_edge_center(RIGHT) + [3.25,0,0],
                     formula[0][-2].get_edge_center(RIGHT),
                     color=MRED, max_tip_length_to_length_ratio=0.05, stroke_width=3)
        estimates = Tex(r" These are \\estimates", font_size=38).next_to(formula_and_surr, RIGHT*9.65)
        self.play(FadeIn(formula_and_surr), run_time=1)
        self.wait(3.25)
        self.play(GrowArrow(arr1), GrowArrow(arr2), Write(estimates), run_time=1)
        self.wait(15)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(1)
        balance = FramedImage("img/8_balance.png", width=10)
        self.play(FadeIn(balance), run_time=1)
        self.wait(30)
        variations = Tex(r"$\bullet\;$ Sensitivity Analysis\\$\bullet\;$ Variations of the EOQ model\\$\bullet\;$ More advanced models",
                         font_size=30, tex_environment="flushleft")
        self.play(LaggedStart(FadeOut(balance), FadeIn(variations), lag_ratio=0.25, run_time=1.5))
        self.wait(10)

class eoq_01_thumbnail(Scene):
    def construct(self):
        lot = Lot(rows=7, cols=7, buff=0.05, stroke_width=2.25).scale(2)
        
        formula.scale(1.15)
        formula_and_surr.scale(1.25)
        eoq_txt = Tex(r"$EOQ$", color=COLOR_1, font_size=100)
        arr = Arrow(LEFT*1.5, RIGHT*1.5, color=COLOR_3)
        eoq_group = VGroup(formula_and_surr, arr, eoq_txt).arrange(RIGHT, buff=0.75).to_edge(UP)

        #lot.set_color_by_gradient(COLOR_3, DRED, DBLUE, COLOR_1)
        lot.set_color_by_gradient(COLOR_1, DBLUE, DRED, COLOR_3)
        
        [lot[i].set_color("#f9f9f9") for i in [1,2,3,4,5,6,
                                               9,10,11,12,13,
                                               17,18,19,20,
                                               25,26,27,
                                               33,34,
                                               41]]
        [l.set(stroke_color=COLOR_1) for l in lot]

        lot2 = lot.copy()
        lot3 = lot.copy()

        lots = VGroup(lot, lot2, lot3).arrange(RIGHT, buff=0.125).scale(1).shift(DOWN*1.5)

        rect = Rectangle(width=config.frame_width,
                         height=1.35,
                         color=COLOR_2, fill_color=DBLUE, fill_opacity=0.95)
        txt = Tex(r"\textbf{ECONOMIC ORDER QUANTITY}", font_size=105, color=WHITE).move_to(rect.get_center())
        head = VGroup(rect, txt).to_edge(UP)#.shift(DOWN*0.25)

        self.add(eoq_group,
                 lots,
                 #head
                 )

class cover(Scene):
    def construct(self):
        img = ImageMobject(r"img/logo.png").scale(0.25)
        self.add(img)

class eqtest(Scene): # Use font size 50
    def construct(self):
        expA = MathTex(r"10\small{,}000T = 872", font_size=50)
        expB = MathTex(r"T = \frac{872}{10\small{,}000}", font_size=50)
        self.add(expA)
        self.play(TransformByGlyphMap(expA, expB,
                                      ([*ir(0,5)], [*ir(6,11)]),
                                      ([*ir(6,10)], [*ir(0,4)]),
                                      ([], [5]),
                                      #([], [])
                                      ), run_time=2)

class mod_01(Scene): # Origins
    def construct(self):

        lot = Lot(rows=5, cols=5, buff=0.125)
        surr_i = SurroundingRectangle(lot, color=COLOR_1, buff=0.12, stroke_width=4, corner_radius=0.1)
        node_i = VGroup(lot, surr_i).scale(1.25)
        node_j = surr_i.copy()
        VGroup(node_i, node_j).arrange(RIGHT, buff=3)
        supplier_txt = Tex(r"Supplier", font_size=40).next_to(node_i, DOWN*1)

        arrLR = Arrow(node_i.get_edge_center(RIGHT), node_j.get_edge_center(LEFT), 
                      color=COLOR_3, stroke_width=4, max_tip_length_to_length_ratio=0.075,
                      buff=0.1).shift(DOWN*0.5)
        arrRL = Arrow(node_j.get_edge_center(LEFT), node_i.get_edge_center(RIGHT),
                      color=COLOR_3, stroke_width=4, max_tip_length_to_length_ratio=0.075,
                      buff=0.1).shift(UP*0.5)

        more_apparent = Tex(r"\textbf{More Apparent}\\Ordering Costs",
                            tex_environment="flushleft", font_size=33, color=COLOR_3).next_to(arrRL, UP*2)
        less_apparent = Tex(r"\textbf{Less Visible}\\Holding Costs\\(capital interest, depreciation)",
                            tex_environment="flushleft", font_size=33, color=COLOR_3).next_to(node_j, DOWN*1.5)
        
        lot_pos2 = lot.copy().set_opacity(0.5).move_to(node_j.get_center())
        lot_pos2[0].fade(1)

        self.add(#img,
                 node_i, node_j,
                 supplier_txt,
                 arrRL, arrLR,
                 more_apparent, less_apparent,
                 lot_pos2,
                 )
        
class mod_02(Scene): # General font resize and Costs changes
    def construct(self):
        
        grid = Axes(x_range=[0, 140, 14], y_range=[0, 1000, 100], x_length=9, y_length=3,
                    axis_config={"color": COLOR_1, "font_size": 20},
                    x_axis_config={"include_numbers": False, "tick_size": 0.035},
                    y_axis_config={"include_numbers": False, "tick_size": 0.05},
                    tips=False).shift(DOWN*0.75 + RIGHT*0.20).scale(1.1)

        week_or_month = Tex(r"Weeks or Months", color=COLOR_4, font_size=30).next_to(grid, DOWN*0.75)
        week_fig = Rectangle(width=0.035, height=0.15, stroke_width=0, fill_color=COLOR_4, fill_opacity=1)
        week_dots = VGroup(*[week_fig.copy().move_to(grid.c2p(p,0,0)) for p in list(range(14,140,14))])

        self.add(grid, week_or_month,
                 week_dots
                 )
        