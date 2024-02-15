from manim import *
from main_theme import *

class Sawtooth(VGroup):
    def __init__(self, teeth=6, color=COLOR_2, labels=True, horizon=365, xlength=10, Q=400, ylength=2, **kwargs):
        super().__init__()
        self.teeth = teeth
        self.color = color
        self.horizon, self.Q = horizon, Q
        self.xlength, self.ylength = xlength, ylength
        self.xstep = self.horizon/self.teeth
        self.ystep = self.Q//4

        self.grid = Axes(x_range=[0, self.horizon, self.xstep],
                    y_range=[0, self.Q, self.ystep],
                    x_length=self.xlength, y_length=self.ylength,
                    axis_config={"include_numbers": False, "tick_size": 0.025},
                    tips=False)
        self.labels = VGroup()
        if labels:
            self.labels.add(self.grid.get_x_axis_label(Tex("Time").scale(0.8), edge=DOWN, direction=DOWN, buff=0.3))
            self.labels.add(self.grid.get_y_axis_label(Tex("Inventory").scale(0.8).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.275))
        
        # In order to accept float steps
        self.xvalues = np.arange(0, self.horizon, self.xstep).tolist()
        onhand_values = [val for x in self.xvalues for val in (x, x)] + [self.horizon]
        self.sawtooth = self.grid.plot_line_graph(x_values=onhand_values,
                                                  y_values=[self.Q if i % 2 else 0 for i in range(len(onhand_values))],
                                                  line_color=self.color, stroke_width=3, add_vertex_dots=False)

        self.add(self.grid, self.sawtooth, self.labels)

    def leadtime(self, foo=0.25, color=GREEN) -> VGroup:
        pos_values = [val for x in self.xvalues[:-1] for val in (x, x)] + [self.horizon - self.xstep] # One tooth less
        self.position = self.grid.plot_line_graph(x_values=pos_values,
                                                  y_values=[self.Q if i % 2 else 0 for i in range(len(pos_values))],
                                                  stroke_width=2.75, add_vertex_dots=False)
        self.position = DashedVMobject(self.position["line_graph"], num_dashes=150)
        self.position.set_color(color).shift(RIGHT*(self.xlength/self.teeth)*(1-foo) + # foo% of cycle length
                                             UP*(self.ylength*foo))
        self.position.set_z_index(self.sawtooth.z_index - 1) # Send to background
        #self.add(self.position)
        return self.position # Return mobject in order to control plotting