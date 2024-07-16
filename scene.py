#!/usr/bin/env python3
from manim import *

class Animation(Scene):
    def construct(self):
        # Mobject instances definition section
        title = Text("Théorème du point fixe")
        ax = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": True, "exclude_origin_tick": False},
        ).scale(0.6)
        
        # Remove decimal numbers from axes
        ax.y_axis.numbers.set_opacity(0)
        ax.x_axis.numbers.set_opacity(0)
        
        # Add integer labels
        for i in range(-2, 3):
            if i != 0:
                ax.add(Text(str(i), font_size=16).next_to(ax.c2p(i, 0), DOWN, buff=0.1))
                ax.add(Text(str(i), font_size=16).next_to(ax.c2p(0, i), LEFT, buff=0.1))
        
        # Add a unified zero label at the origin
        zero_label = Text("0", font_size=16).next_to(ax.c2p(0, 0), DL, buff=0.1)
        labels = ax.get_axis_labels(
            Text("x", font_size=20),
            Text("y", font_size=20)
        )
        
        linear_graph = ax.plot(lambda x: x, x_range=[-2, 2], color=BLUE)
        quadratic_graph = ax.plot(lambda x: -x**2/4 + 1, x_range=[-2, 2], color=GREEN)
        
        # Find intersection point
        intersection_point = ax.c2p(0.8, 0.8)  # Approximate intersection
        point = Dot(intersection_point, color=RED)
        
        # Add x0 and f(x0) labels and dotted lines
        x0 = ax.get_x_axis().number_to_point(0.8)
        fx0 = ax.get_y_axis().number_to_point(0.8)
        x0_label = Text("x₀", font_size=16).next_to(x0, DOWN, buff=0.1)
        fx0_label = Text("f(x₀)", font_size=16).next_to(fx0, LEFT, buff=0.1)
        
        dotted_line_1 = DashedLine(intersection_point, x0, color=YELLOW)
        dotted_line_2 = DashedLine(intersection_point, fx0, color=YELLOW)
        
        # Add legends for the curves
        linear_legend = MathTex("y = x", color=BLUE).scale(0.8)
        quadratic_legend = MathTex("y = -\\frac{1}{4}x^2 + 1", color=GREEN).scale(0.8)
        legend_group = VGroup(linear_legend, quadratic_legend).arrange(DOWN, aligned_edge=LEFT)
        legend_group.to_corner(UR, buff=0.5)
        
        # Animations section
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.scale(0.5).to_edge(UP))
        self.wait(1)
        self.play(Write(ax, run_time=4))
        self.play(Write(zero_label), Write(labels))
        self.wait(2)
        self.play(Write(linear_graph), run_time=4)
        self.wait(1)
        self.play(Write(quadratic_graph), run_time=4)
        self.wait(2)
        self.play(FadeIn(point), run_time=1)
        self.wait(2)
        self.play(Create(dotted_line_1), Create(dotted_line_2))
        self.play(Write(x0_label), Write(fx0_label))
        self.wait(2)
        self.play(Write(legend_group))
        self.wait(10)
