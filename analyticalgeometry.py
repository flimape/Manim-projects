from manim import *

class geo(Scene):
    def construct(self):
        
        flimape = Tex('@flimape')
        text = Tex('Distance between two points proof')
        
        self.play(
            Write(text),
            run_time=2
        )

        self.wait(3)

        self.play(
            Transform(text,flimape)
        )

        self.wait(2)

        self.play(
            Unwrite(
                VGroup(
                    text,
                    flimape
                )
            )   
        )


        ax = Axes(
            x_range=[0, 6], 
            y_range=[0, 4],
            x_length = 9,
            y_length = 4
            )

        ax.to_edge(ORIGIN)
        labels = ax.get_axis_labels()

        self.play(
            DrawBorderThenFill(ax),
            run_time=3
        )

        self.play(
            Write(labels)
        )

        dot_a = Dot(ax.coords_to_point(1,1))
        txt_a = MathTex(r'A(x_1,y_1)').next_to(dot_a, UP)
        
        dot_b = Dot(ax.coords_to_point(5,3))
        txt_b = MathTex(r'B(x_2,y_2)').next_to(dot_b)

        vg = VGroup(
            dot_a,
            dot_b
        )

        self.play(
            Create(vg),
            run_time=1
        )

        vg1 = VGroup(
            txt_a,
            txt_b
        )

        self.play(
            Write(vg1),
            run_time=1
        )

        line = Line(dot_a,dot_b).set_color(RED)
        
        brace = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        txt_brace = Tex('d').next_to([0,0,0],UP*2+LEFT*0.3)
        
        self.play(
            Create(line),
            run_time=1
        )

        self.play(
            Create(brace),
            run_time=1
        )

        self.play(
            Write(txt_brace),
            run_time=1
        )

        self.wait(2)

        v_brace = VGroup(
            brace,
            txt_brace
        )

        text = Tex('d = ?').to_edge(UR)
        
        self.play(
            Transform(
                v_brace,
                text
            ),
            run_time=3
        )

        dot_tri =  Dot(ax.coords_to_point(0,3))
        dot_txt = MathTex(r'(0,y_2)').next_to(dot_tri, LEFT)
        dott = Dot(ax.coords_to_point(5,3))

        d_line = DashedLine(dot_tri, dott)

        vg_dot = VGroup(
            dot_tri,
            dot_txt
        )

        self.play(
            Create(vg_dot),
        )

        self.play(
            Create(d_line),
            run_time=3
        )

        dot_tri1 = Dot(ax.coords_to_point(0,1))
        dot_txt1 = MathTex(r'(0,y_1)').next_to(dot_tri1,LEFT)

        d_line1 = DashedLine(dot_tri1, Dot(ax.coords_to_point(5,1)))

        vg_dot1 = VGroup(
            dot_tri1,
            dot_txt1
        )

        self.play(
            Create(vg_dot1),
            run_time=2
        )

        self.play(
            Create(d_line1),
            run_time=3
        )

        dot_x = Dot(ax.coords_to_point(1,0))
        dot_x_txt = MathTex(
            r'(x_1,0)').next_to(
             dot_x,
             DOWN*2
            )
        
        vg_x = VGroup(
            dot_x,
            dot_x_txt
        )

        line_x = DashedLine(Dot(ax.coords_to_point(1,0)),dot_a )

        self.play(
            Write(vg_x),
            run_time=2
        )

        self.play(
            Create(line_x),
            run_time=3
        )

        dot_f = Dot(ax.coords_to_point(5,1))

        self.play(
            Create(
                dot_f
            )
        )

        dot_x2 = Dot(ax.coords_to_point(5,0))
        dot_x2_txt = MathTex(
            r'(x_2,0)').next_to(
                dot_x2,
                DOWN*2
            )

        line_x2 = DashedLine(dot_x2,dot_b)

        vg_x2 = VGroup(
            dot_x2,
            dot_x2_txt
        )

        self.play(
            Write(vg_x2),
        )

        self.play(
            Create(line_x2),
            run_time=3
        )

        x_brace = Brace(Line(dot_x, dot_x2))
        x_bracetxt = MathTex(r'x_2 - x_1').next_to(x_brace,DOWN*0.3)
        
        brace_vg = VGroup(
            x_brace,
            x_bracetxt
        )
        
        self.play(
            Create(x_brace),
            run_time=2
        )

        self.play(
            Create(x_bracetxt),
            run_time=2
        )

        self.play(
            brace_vg.animate.shift(UP*1)
        )

        liney = Line(Dot([-4.5,1,0]),Dot([-4.5,-1,0]))
        
        y_brace = Brace(liney,LEFT)
        ybrace_txt = MathTex(r'y_2 - y_1').next_to(y_brace,LEFT)
        
        self.play(
            Create(y_brace),
            run_time=2
        )

        self.play(
            Create(
                ybrace_txt
            ),
            run_time=2
        )

        self.wait(2)
        
        yy_brace = Brace(
                Line(
                    Dot(
                        ax.coords_to_point(5,1)
                        ),
                    Dot(
                        ax.coords_to_point(5,3)
                )
            ),RIGHT
        )

        yybrace_txt = MathTex(r'y_2 - y_1').next_to(yy_brace,RIGHT)
        
        vgy = VGroup(
            y_brace,
            ybrace_txt
        )
        
        yy_vg = VGroup(
            yy_brace,
            yybrace_txt
        )

        yyy_vg = VGroup(
            yy_vg,
            vgy
        )

        self.play(
            Transform(
                vgy,
                yy_vg
            ),
            run_time=2
        )

        line1 = Line(dot_a,Dot(ax.coords_to_point(5,1))).set_color(RED)
        line2 = Line(dot_b,Dot(ax.coords_to_point(5,1))).set_color(RED)

        self.play(
            Create(line1),
            Create(line2)
        )

        all_group = VGroup(
            ax,
            txt_a,
            labels,
            txt_b,
            v_brace,
            vg_dot,
            d_line1,
            vg_dot1,
            vg_x,
            vg_x2,
            vg_dot,
            vg_dot1,
            d_line,
            d_line1,
            line_x2,
            line_x
        )

        self.play(
            Unwrite(all_group)
        )

        self.wait(2)

        tri_vg = VGroup(
            vgy,
            yy_vg,
            yyy_vg,
            brace_vg,
            line,
            line1,
            line2,
            dot_a,
            dot_b,
            dot_f
        )
        
        self.play(
            tri_vg.animate.scale(0.8).shift(LEFT*2)
            )
        
        self.play(
            tri_vg.animate.shift(UP*1+ LEFT*2),
            run_time = 2
        )

        p = Tex('Pythagorean theorem').next_to(Dot([1,1,0]))
       
        p1 = MathTex(
            'd^2 =', 
            '(x_2 - x_1)^2 +',
            '(y_2 - y_1)^2'
        ).next_to(p,DOWN)

        self.play(
            Create(p),
            run_time=1
        )

        self.play(
            Create(p1[0]),
            run_time=1
        )

        self.play(
            ReplacementTransform(brace_vg,p1[1]),
            run_time=5
        )

        self.play(
            ReplacementTransform(yyy_vg,p1[2]),
            run_time=5
        )


        final = MathTex(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}').next_to(p1,DOWN)

        self.play(
            Create(final),
            run_time=3
        )

        self.wait(5)