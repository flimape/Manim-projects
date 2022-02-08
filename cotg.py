from manim import *

class cotg(MovingCameraScene):
    def construct(self):
        
        flimape = Tex('@flimape')

        self.play(
            Create(flimape),
            run_time=3)

        self.wait(2)

        self.play(
            Unwrite(flimape)
        )
        
        dot_a = Dot([-1,1,0])
        dot_b = Dot([-3,2,0])
        dot_c = Dot([0,2,0])
        
        tri = Polygon(
            [-1,3,0],
            [-3,1,0],
            [4,1,0],
            stroke_color = RED
            )
        
        self.play(
            Create(
                tri
            ),
            run_time = 2
        )

        self.play(
            tri.animate.shift(LEFT*1)
        )

        a = Tex('c').next_to(dot_a, DOWN)
        b = Tex('b').next_to(dot_b,LEFT + UP*0.3)
        c = Tex('a').next_to(dot_c,RIGHT*2 + UP *0.7)

        self.play(
            Create(a),
            Create(b),
            Create(c)
        )
        
        dota = Dot([-2,3,0])
        dotb = Dot([-4,1,0])
        dotc = Dot([3,1,0])

        line_b = Line(dotb,dota)
        line_a = Line(dotb,dotc)
        line_c = Line(dotc,dota)
        line_d = Line(dotc,dotb)

        gama = Angle(line_b,
                line_c,
                radius=0.3,
                quadrant=(-1,-1)
                )
        
        gama_value = MathTex(r'\gamma').next_to(gama,DOWN*1)
        
        self.play(
            Create(gama),
            Create(gama_value)
        )
        
        dotalpha = Dot([-3.1,1,0])
        
        alpha = Angle(line_b,
                line_a,
                radius = 0.5,
                other_angle=True
                )
        alpha_value = MathTex(r'\alpha').next_to(dotalpha,UP*0.5)


        self.play(
            Create(alpha),
            Create(alpha_value)
        )
        
        beta = Angle(line_c,
                line_d,
                radius=1.5
                )
        
        beta_value = MathTex(r'\beta').next_to(beta,LEFT*1.3)
        
        self.play(
            Create(beta),
            Create(beta_value)
        )
        
        doth = Dot([-2,1,0])
        doth_line = Line(doth,dotb)
        
        height = DashedLine(dota,doth)
        
        r_angle = Angle(
                height,
                doth_line,
                radius = 0.3,
                other_angle=True,
                quadrant= (-1,-1),
                dot = True
        )   
        
        heighttxt = Tex('h').next_to(height)
        
        self.play(
            Create(height),
            Create(heighttxt),
            run_time=2
        )

        self.play(
            Create(r_angle),
            run_time=1
        )

        
        area = Polygon(
            [-2,3,0],
            [-4,1,0],
            [3,1,0],
            stroke_color = RED,
            fill_color = ORANGE,
            fill_opacity = 0.5
            )   
        
        s = MathTex(r's = triangle_{area} = \frac{ch}{2} ')
        s1 = MathTex(r'Proof: s = \frac{a^2 + b^2 + c^2}{4(cot\alpha+cot\beta+cot\gamma)}')
        
        self.play(
            Create(area),
            run_time=3
        )
        self.play(
            Write(s),
            run_time=3
        )


        self.play(
            Transform(
                s,
                s1
            ),
            run_time=3
        )

        self.wait(3)
        
        self.play(
            Unwrite(
                VGroup(
                    s,
                    s1,
                    area
                )
            ),
            run_time=2
        )
        
        tri1 = Polygon(
            [-2,3,0],
            [-4,1,0],
            [-2,1,0],
            stroke_color = WHITE,
        )

        self.play(
            Create(tri1)
        )
        
        areasin = MathTex(r'sin\alpha = \frac{h}{b}').to_edge(LEFT, buff=1)
        areasin2 = MathTex(r'h = bsin\alpha').to_edge(LEFT, buff=1)
        areasin3 = MathTex(r's = \frac{cbsin\alpha}{2} ').to_edge(LEFT, buff=1)
        areasin4 = MathTex(r'cb = \frac{2s}{sin\alpha}')
        areasin4.next_to(areasin2,DOWN*2.5)

        self.play(
            Create(areasin),
            run_time=3
        )
        
        self.wait(2.5)

        self.play(
            Transform(
                areasin,
                areasin2
            ),
            run_time=3
        )

        self.wait(2.5)

        self.play(
            Unwrite(
                VGroup(
                    areasin,
                    areasin2
                )
            ),
            run_time=2
        )

        self.play(
            Unwrite(tri1),
            Create(area),
            Create(areasin3),
            run_time=3
        )

        self.wait(2.5)

        self.play(
            TransformFromCopy(
                areasin2,
                areasin4
            ),
            run_time=3
        )

        self.wait(2.5)

        self.play(
            Unwrite(
                VGroup(
                    areasin3,
                    tri1
                )
            ),
            run_time=2
        )
        
        self.play(
            areasin4.animate.shift(RIGHT*10 + DOWN*1.5),
            run_time=3
        )

        cos = MathTex(r'a^2 = b^2 + c^2 -2cbcos\alpha').to_edge(LEFT, buff=1)

        self.play(
            Write(cos),
            run_time=3
        )

        framebox = SurroundingRectangle(areasin4,buff=0.4)

        self.play(
            Create(framebox),
            run_time=2
        )

        cos1 = MathTex(r'a^2 = b^2 + c^2 -2\frac{2s}{sin\alpha}cos\alpha ')
        
        self.play(
            Transform(cos,cos1),
            TransformMatchingTex(areasin4,cos1),
            Unwrite(framebox),
            run_time=4
        )

        
        
        cotg = MathTex(r'cot\alpha = \frac{cos\alpha}{sin\alpha}').to_edge(DL)

        self.play(
            Create(cotg),
            run_time=3
        )
        
        self.camera.frame.save_state()
        
        self.play(self.camera.frame.animate.move_to(cotg))
        self.play(self.camera.frame.animate.set(width=cotg.width * 1.2))
        self.wait(3)

        self.play(
            Unwrite(
                VGroup(
                    cotg,
                    areasin4
                )
            ),
            run_time=(2.7)
        )
        self.play(Restore(self.camera.frame))

        sub = MathTex(r'a^2 = b^2 + c^2 -4scot\alpha')

        self.play(
            Unwrite(
                VGroup(
                    cos1,
                    cos
                )
            ),
            run_time=2
        )

        self.play(
            Create(sub),
            run_time=3
        )

        linear_system = MathTex(r'c^2 = a^2 + b^2 -4scot\gamma')
        linear_system.next_to(sub,DOWN)
        
        linear_system1 = MathTex(r'b^2 = a^2 + c^2 -4scot\beta')
        linear_system1.next_to(linear_system,DOWN)
        
        self.play(
            TransformFromCopy(
                sub,
                linear_system
            ),
            run_time=3
        )

        self.play(
            TransformFromCopy(
                sub,
                linear_system1
            ),
            run_time=3
        )

        vg = VGroup(
                sub,
                linear_system,
                linear_system1
            )

        brace = Brace(vg,direction=LEFT)
        
        self.play(
            Create(brace),
            run_time=2.5
        )

        self.wait(3)

        self.play(
            Unwrite(
                VGroup(
                    sub,
                    linear_system,
                    linear_system1,
                    brace
                )
            ),
            run_time=3
        )

        dot = Dot([-6.5,-0.5,0])
        f = MathTex(r'a^2 + b^2 + c^2 = 2(a^2 + b^2 + c^2) - 4s(cot\alpha + cot\beta + cot\gamma)')
        f.next_to(dot)

        self.play(
            Create(f),
            run_time=5
        )

        self.wait(3)

        dots = Dot([-4,-2,0])
        f1 = MathTex(r's = \frac{a^2 + b^2 + c^2}{4(cot\alpha+cot\beta+cot\gamma)') 
        f1.next_to(dots)
        
        self.play(
            Transform(
                f,
                f1
            ),
            run_time=2
        )

        framebox1 = SurroundingRectangle(f1, buff=0.8)

        self.play(
            Create(framebox1),
            run_time=2
        )        

        self.wait(5)