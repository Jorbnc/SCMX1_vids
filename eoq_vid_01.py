from main_theme import *

class eoq_01(MovingCameraScene):

    def construct(self):

        formula = MathTex(r"Q^{*} = \sqrt{\frac{2Dc_{t}}{c_{e}}}", color=RED).move_to([0, 0, 0])
        formula_surr = SurroundingRectangle(formula, color=RED, buff=0.5, corner_radius=0.5)
        formula_and_surr = VGroup(formula, formula_surr)
        self.play(Write(formula), Create(formula_surr), run_time=1.5)
    
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

        #q_dot = Circle(radius=0.5, color=RED, fill_opacity=1).move_to([-0.3,0.75,0])
        q_dot = Dot(point=grid.c2p(0, 400, 0), color=RED)
        self.play(Transform(formula_and_surr, q_dot), run_time=1, rate_func=smooth)

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

        self.play(Create(sawtooth, run_time=1.5, rate_func=linear))

        # foo = Tex(r"Uno. Dos. Tres. Probando.").move_to([0,1.5,0])
        # math = MathTex(r"P\left(\bigcup_{i=1}^{n}A_{i} \right) = \sum_{1}^{n} P(A_{i})")
        
        # self.play(Write(foo, run_time=1))
        # self.play(Write(math, run_time=1))

        # marmota1 = Tex(r"Hola marmota!").move_to([5, 2.5, 0])
        # self.play(self.camera.frame.animate.move_to(marmota1))
        # self.play(Write(marmota1, run_time=1))

        # self.play(self.camera.frame.animate.scale(2))

        # marmota2 = Tex(r"Hola Mi Amor\\ Te Amo <3", font_size=120).move_to([3.5, 5, 0])
        # self.play(Write(marmota2, run_time=1))

        self.wait(2)