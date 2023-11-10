from main_theme import *

class eoq_01_01(MovingCameraScene):

    def construct(self):

        eoq_full_text = Tex(r"Economic Order Quantity")
        eoq_text = MathTex(r"EOQ")

        self.play(Write(eoq_full_text), run_time=1)
        self.play(ReplacementTransform(eoq_full_text, eoq_text), run_time=1)

        self.wait(1)

        op_scm_text = Tex(r"Operations Management\\Supply Chain Management")
        self.play(eoq_text.animate.move_to([0,1.5,0]), run_time=0.5, rate_func=smooth)
        self.wait(1)
        self.play(Write(op_scm_text), run_time=1.5)

        formula = MathTex(r"Q^{*} = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=RED).move_to([0, 0, 0])
        formula_surr = SurroundingRectangle(formula, color=RED, buff=0.4, corner_radius=0.25)
        formula_and_surr = VGroup(formula, formula_surr)
        self.play(FadeOut(op_scm_text), run_time=0.5)
        self.play(ReplacementTransform(eoq_text, formula), run_time=1)
        self.play(Create(formula_surr), run_time=1)
    
        #Axis
        grid = Axes(
            x_range=[0, 365, 30], y_range=[0, 500, 100],
            x_length=11, y_length=3.5,
            axis_config={
                "color": BLACK,
                #"include_numbers": True,
                #"decimal_number_config": {"color":BLACK, "num_decimal_places": 0},
                #"numbers_to_include": np.arange(0, 52, 5), # If only specific numbers are to be shown
                "font_size": 24,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label(Tex("$y:$ Inventory").scale(0.65).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label = grid.get_x_axis_label(Tex("$x:$ Time").scale(0.65),
                                        edge=DOWN, direction=DOWN, buff=0.3)

        self.wait(1)
        self.play(Create(grid), Write(x_label), Write(y_label), run_time=1.75)

        q_dot = Dot(point=grid.c2p(0, 400, 0), radius=0.05, color=RED)
        self.play(ReplacementTransform(formula_and_surr, q_dot), run_time=1, rate_func=smooth)

        # EOQ: D = 2400, ct=100, ce=3 => Q = 400
        replenishments = 6
        replenishment_period = (400/2400)*365
        x_values = [i * replenishment_period for n in range(replenishments) for i in (n, n)] + [365]

        sawtooth = grid.plot_line_graph(
            x_values = x_values,
            y_values = [400 if i % 2 else 0 for i in range(len(x_values))],
            line_color = RED,
            stroke_width = 3,
            add_vertex_dots=False,
        )

        self.play(Create(sawtooth, run_time=1.25, rate_func=linear))

        # foo = Tex(r"Uno. Dos. Tres. Probando.").move_to([0,1.5,0])
        # math = MathTex(r"P\left(\bigcup_{i=1}^{n}A_{i} \right) = \sum_{1}^{n} P(A_{i})")
        
        # self.play(Write(foo, run_time=1))
        # self.play(Write(math, run_time=1))

        # marmota1 = Tex(r"text1").move_to([5, 2.5, 0])
        # self.play(self.camera.frame.animate.move_to(marmota1))
        # self.play(Write(marmota1, run_time=1))

        # self.play(self.camera.frame.animate.scale(2))

        # marmota2 = Tex(r"text1", font_size=120).move_to([3.5, 5, 0])
        # self.play(Write(marmota2, run_time=1))

        grid_2= Axes(
            x_range=[0, 1600, 200], y_range=[0, 3000, 500],
            x_length=11, y_length=3.5,
            axis_config={
                "color": BLACK,
                #"include_numbers": True,
                #"decimal_number_config": {"color":BLACK, "num_decimal_places": 0},
                #"numbers_to_include": np.arange(0, 52, 5), # If only specific numbers are to be shown
                "font_size": 24,
            },
            tips=False,
        )

        y_label_2 = grid.get_y_axis_label(Tex("$y:$ Cost").scale(0.65).rotate(90 * DEGREES),
                                        edge=LEFT, direction=LEFT, buff=0.3)
        x_label_2 = grid.get_x_axis_label(Tex("$x:$ Order Quantity").scale(0.65),
                                        edge=DOWN, direction=DOWN, buff=0.3)
        
        q_dot_2 = Dot(point=grid_2.c2p(400, 0, 0), radius=0.05, color=RED)

        self.play(ReplacementTransform(grid, grid_2),
                  ReplacementTransform(x_label, x_label_2), ReplacementTransform(y_label, y_label_2),
                  FadeOut(sawtooth),
                  ReplacementTransform(q_dot, q_dot_2),
                  run_time=1, rate_func=smooth
        )

        x_values_2 = np.arange(1, 1600, 20)
        holding_cost = grid_2.plot_line_graph(
            x_values = x_values_2,
            y_values = [3*x/2 for x in x_values_2],
            line_color = RED,
            stroke_width = 2,
            add_vertex_dots=False,
        )
        setup_cost = grid_2.plot_line_graph(
            x_values = np.arange(80, 1600, 20),
            y_values = [100*2400/x for x in np.arange(80, 1600, 20)],
            line_color = RED,
            stroke_width = 2,
            add_vertex_dots=False,
        )

        total_cost = grid_2.plot_line_graph(
            x_values = np.arange(80, 1600, 20),
            y_values = [3*x/2 + 100*2400/x for x in np.arange(80, 1600, 20)],
            line_color = RED,
            stroke_width = 4,
            add_vertex_dots=False,
        )

        
        opt_point = Dot(point=grid_2.c2p(400, 1200, 0), radius=0.05, color=DARK_BLUE)
        min_text = Tex("Minimum Total Cost", font_size=20, color=DARK_BLUE).move_to(grid_2.c2p(500, 1500, 0))

        line_1 = Line(start=q_dot_2.get_center(), end=grid_2.c2p(400, 1200, 0), stroke_width=1, color=RED)

        self.play(Create(holding_cost), Create(setup_cost),
                  run_time=1, rate_func=linear)
        self.play(Create(total_cost), Create(line_1),
                  run_time=0.75, rate_func=smooth
        )

        self.play(Create(opt_point), Write(min_text),
                  run_time=0.50, rate_func=smooth
        )

        self.wait(0.75)

        holding_text = Tex(r"Holding cost", font_size=25, color=DARK_BLUE).move_to(grid_2.c2p(1000, 1200, 0))
        setup_text = Tex(r"Ordering cost", font_size=25, color=DARK_BLUE).move_to(grid_2.c2p(800, 500, 0))
        self.play(holding_cost.animate.set_color(DARK_BLUE), Write(holding_text), run_time=0.5)
        self.play(holding_cost.animate.set_color(RED), holding_text.animate.set_color(RED), run_time=0.5)
        self.play(setup_cost.animate.set_color(DARK_BLUE), Write(setup_text), run_time=0.5)
        self.play(setup_cost.animate.set_color(RED), setup_text.animate.set_color(RED), run_time=0.5)

        self.wait(2)

class eoq_01_02(MovingCameraScene):

    def construct(self):

        eoq_full_text = Tex(r"Economic Order Quantity")
        eoq_text = MathTex(r"EOQ")