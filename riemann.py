from distutils.command.build_scripts import first_line_re
from tkinter.ttk import LabeledScale
from manim import *

class calculus(Scene):
    def construct(self):
        
        sd = Tex('Definite integral as the limit of a Riemann Sum')
        sds = Tex('@flimape')

        self.play(
            Create(sd),
            run_time=2
        )

        self.wait(3)

        self.play(
            Transform(
                sd,sds
            ),
            run_time=3
        )

        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=2
        )

        ax1 = Axes(
            x_range=[-1, 8, 1],
            y_range=[-1, 8, 1],
            x_length=13,
            y_length=6,
        )
        labels = ax1.get_axis_labels()
        
        func1 = ax1.plot(lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x - 5) + 5, color = RED,x_range=[0.2,7])
        
        self.play(
            DrawBorderThenFill(ax1),
            Create(labels),
            run_time=3
        )

        self.play(
            Create(
                func1
            ),
            run_time=2
        )

        self.wait(2)

        area = ax1.get_area(func1,x_range = [1,7])

        a = MathTex(r'a').next_to(Dot(ax1.coords_to_point(1,0)),DOWN).set_color(YELLOW)
        b = MathTex(r'b').next_to(Dot(ax1.coords_to_point(7,0)),DOWN).set_color(YELLOW)
        
        self.play(
            Create(a),
            Create(b),
            run_time=1
        )

        self.play(
            Create(area),
            run_time=2
        )
        
        tex = Tex('How to find the area?')

        self.play(
            Write(tex),
            run_time=1
        )
        
        self.wait(2)
        
        self.play(
            Unwrite(
                    VGroup(
                    area,
                    tex
                ),run_time=1.5
            )
        )

        x0 = MathTex(r'x_0').next_to(Dot(ax1.coords_to_point(1,0)),DOWN).set_color(YELLOW)
        xn = MathTex(r'x_n').next_to(Dot(ax1.coords_to_point(7,0)),DOWN).set_color(YELLOW)
    
        self.wait(1.2)

        self.play(
            Transform(a,x0),
            Transform(b,xn),
            run_time=1
        )

        x4 = MathTex(r'x_{i-1}').next_to(Dot(ax1.coords_to_point(3,0)),DOWN).set_color(YELLOW)

        x5 = MathTex(r'x_i').next_to(Dot(ax1.coords_to_point(4,0)),DOWN).set_color(YELLOW)

        self.play(
            Create(x4),
            run_time=1
        )
        
        self.play(
            Create(x5),
            run_time=1
        )

        self.wait(1)

        brace = Brace(
            Line(
                Dot(ax1.coords_to_point(3,0,0)),
                Dot(ax1.coords_to_point(4,0,0))
            )
        )

        xvg = VGroup(
            x4,
            x5
        )

        self.play(
            Unwrite(xvg),
            run_time=3
        )

        bracetxt = MathTex(r'\Delta x_i = x_i - x_{i-1}').next_to(brace,DOWN)

        self.play(
            Create(brace),
            Create(bracetxt),
            run_time=2
        )

        self.wait(1)

        bracet = MathTex(r'\Delta x_i').next_to(brace,DOWN)

        self.play(
            Transform(
                bracetxt,
                bracet
            ),
            run_time=2
        )

        self.wait(0.5)

        bracen = Brace(
            Line(
                Dot(ax1.coords_to_point(1,0,0)),
                Dot(ax1.coords_to_point(7,0,0))
            ),UP
        )

        bracentxt = MathTex(r'\Delta x_in').next_to(bracen, UP)

        self.play(
            Create(bracen),
            run_time=2
        )

        self.play(
            Create(bracentxt),
            run_time=2
        )

        self.wait(1)
            
        self.play(
            VGroup(
                bracetxt,
                bracet,
                brace
            ).animate.shift(LEFT*1.5)
        )
       
        ci = MathTex('c_i').next_to(Dot(ax1.coords_to_point(3.5,0,0)),DOWN)
        lineci = DashedLine(Dot(ax1.coords_to_point(3.5,0,0)), Dot(ax1.coords_to_point(3.5,6,0)))
        
        self.play(
            Create(ci),
            run_time=1
        )

        dot_a = Dot(ax1.coords_to_point(3.5,6,0))

        self.play(
            Create(lineci),
            Create(dot_a),
            run_time=3
        )
        
        lineci2 = DashedLine(Dot(ax1.coords_to_point(3.5,6,0)),Dot(ax1.coords_to_point(0, 6,0)))
        fci = MathTex(r'f(c_i)').next_to(Dot(ax1.coords_to_point(0, 6,0)),LEFT)

        self.play(
            Create(lineci2),
            run_time=3
        )

        dot_f = Dot(ax1.coords_to_point(0, 6,0))
        
        self.play(
            Create(dot_f),
            Create(fci),
            run_time=2
        )

        self.play(
            Unwrite(
                VGroup(
                ci,
                bracen,
                bracentxt
                ),
                run_time=1
            )
        )

        self.play(
            VGroup(
                bracetxt,
                bracet,
                brace
            ).animate.shift(RIGHT*1.5)
        )

        self.wait(2)

        dx_list = [1, 0.7,0.5, 0.3, 0.1, 0.05, 0.025, 0.01]
        rectangles = VGroup(
            *[
                ax1.get_riemann_rectangles(
                    graph=func1,
                    stroke_width=0.1,
                    stroke_color=YELLOW,
                    x_range=[1,7],
                    dx=dx
                )
                for dx in dx_list
            ]
        )
        
        first_area = rectangles[0]
        for k in range(1,len(dx_list)):
            new_area = rectangles[k]
            
        self.play(
            DrawBorderThenFill(first_area),
            run_time=3
        )

        all = VGroup(
            ax1,
            func1,
            labels,
            a,
            b,
            x0,
            xn,
            bracetxt,
            bracet,
            brace,
            fci,
            lineci,
            lineci2,
            dot_f,
            dot_a,
            first_area,
        )
        
        self.play(
            all.animate.scale(0.6).shift(LEFT*3+UP*1),
            run_time=3
        )

        sum = MathTex(r'A = \sum_{i = 1}^n f(c_i) \Delta x_i').next_to(ORIGIN,DOWN*5)

        self.play(
            Create(sum),
            run_time=2
        )

        self.wait(2)

        self.play(
            Unwrite(
                sum
            ),
            run_time=2
        )

        self.wait(0.5)

        self.play(
             all.animate.scale(1.65).shift(RIGHT*3+DOWN*1)
        )

        self.wait(1)

        for k in range(1,len(dx_list)):
            new_area = rectangles[k]
            
            self.play(
                Transform(
                    first_area,
                    new_area
                ),
                Unwrite(
                    VGroup(
                        fci,
                        lineci2,
                        dot_a,
                        dot_f,
                        bracetxt,
                        bracet,
                        brace
                    ),
                run_time=3
            )
        )
        new_all = VGroup(
            ax1,
            func1,
            labels,
            a,
            b,
            x0,
            xn,
            bracetxt,
            bracet,
            brace,
            fci,
            lineci,
            lineci2,
            dot_f,
            dot_a,
            first_area,
            new_area
        )

        self.play(
            new_all.animate.scale(0.6).shift(LEFT*3+UP*1)
        )

        a = MathTex(r'\lim_{max\Delta xi} \sum_{i=0}^n f(c_i) \Delta x_i').next_to(ORIGIN,DOWN*5)
        
        self.play(
            Create(
                a
            ),
            run_time=4
        )

        self.wait(2)

        aa = MathTex(r'\int_a^b f(x)dx').next_to(ORIGIN,DOWN*5)

        self.play(
            Transform(
                a,
                aa
            ),
            run_time=3
        )

        self.wait(0.8)

        framebox = SurroundingRectangle(aa,buff=0.5)

        self.play(
            Create(
                framebox
            ),run_time=2
        )

        self.wait(5) 
