from  manim import *

class trigo(Scene):
    
    def construct(self):
        
        sd = Tex('Geometry')
        sds = Tex('@flimape')

        self.play(
            Create(sd),
            run_time=2
        )

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

        dota  = Dot([-6,0,0]).set_color(BLUE)
        dotatxt = Tex('A').next_to(dota,DOWN)
        
        dotb = Dot([-6,3,0]).set_color(BLUE)
        dotbtxt = Tex('B').next_to(dotb,UP)
        
        dotc = Dot([-3,3,0]).set_color(BLUE)
        dotctxt = Tex('C').next_to(dotc, UP)

        dotd = Dot([-3,0,0]).set_color(BLUE)
        dotdtxt = Tex('D').next_to(dotd, DOWN + LEFT * 0.5)

        dote = Dot([0,0,0]).set_color(BLUE)
        dotetxt = Tex('E').next_to(dote, RIGHT)

        dotf = Dot([-3,1.5,0]).set_color(BLUE)
        dotftxt = Tex('F').next_to(dotf,UP + RIGHT)
        
        line_bc = Line(dotb,dotc).set_color(ORANGE)
        line_cd = Line(dotc,dotd).set_color(ORANGE)
        line2 = Line(dotd,dota).set_color(ORANGE)
        line3 = Line(dota,dotb).set_color(ORANGE)
        line4 = Line(dotb,dote).set_color(ORANGE)
        line5 = Line(dote,dotd).set_color(ORANGE)
        
        linea = Line(dotd,dotf).set_color(ORANGE)
        lineb = Line(dotf,dote).set_color(ORANGE)
        
        ab = Dot([-6,1.5,0])
        abt = Tex('1').next_to(ab,LEFT)
        
        bc = Dot([-4.5,3,0])
        bctxt = Tex('1').next_to(bc,UP)
        
        fe = Dot([-2,1,0])
        fet = Tex('1').next_to(fe,RIGHT + UP *0.5)
        
        ad = Dot([-4.5,0,0])
        adtxt = Tex('1').next_to(ad,DOWN)
        
        ret  = Angle(line2,line3,radius = 0.3,dot = True,quadrant = (-1,1))
        ret2 = Angle(line_bc,line_cd,radius = 0.3, dot = True,quadrant = (-1,1))
        ret3 = Angle(line_cd,line5,radius = 0.3, quadrant = (-1,1), dot = True)
        
        self.play(
            Create(dota),
            Create(dotatxt),
            Create(dotb),
            Create(dotbtxt),
            Create(dotc),
            Create(dotctxt),
            Create(dotd),
            Create(dotdtxt),
            Create(dote),
            Create(dotetxt)
        )

        self.play(
            Create(line_bc),
            run_time = 0.5
        )
        self.play(
            Create(line_cd),
            Create(bctxt),
            run_time = 0.5
        )
        self.play(
            Create(line2),
            Create(ret2),
            Create(linea),
            Create(adtxt),
            run_time = 0.5
        )
        self.play(
            Create(line3),
            Create(abt),
            Create(ret),
            run_time = 0.5
        )
        self.play(
            Create(line4),
            Create(dotf),
            Create(dotftxt),
            Create(lineb),
            run_time = 0.5
            )
        self.play(
            Create(line5),
            Create(fet),
            Create(ret3),
            run_time = 0.5
        )

        
        alpha = Angle(linea,lineb,
        radius = 0.4, 
        quadrant = (-1,1)
        )


        alphatxt = MathTex(r'\alpha').next_to(alpha, DOWN * 0.5 + RIGHT * 0.01)
        self.play(
            Create(alpha),
            Create(alphatxt)
        )

        b1 = Brace(line5)
        b1t = b1.get_text('x')

        self.play(
            Create(b1),
            Create(b1t)
        )
        
        x = Tex('x = ??').to_edge(UR)
        self.play(
            Create(x),
            run_time = 1.5
        )
        self.play(
            Unwrite(x),
            run_time=1.5
        )

        dots = Dot([1,2,0])
        sin = MathTex(r'sin\alpha = \frac{x}{1}')
        sin.next_to(dots)
        sin1 = MathTex(r'x = sin\alpha')
        sin1.next_to(dots)
        
        self.play(
            Create(sin),
            run_time = 4
        )
        self.play(
            Transform(sin,sin1),
            run_time = 2
        )
        
        sint = b1.get_tex(r'sin\alpha')
        
        self.play(
            Transform(b1t,sint),
            Unwrite(
                VGroup(
                    sin,
                    sin1
                )
            ),
            run_time=3
        )

        alpha1 = Angle(linea,lineb,
        radius = 0.4, 
        quadrant = (1,-1)
        )
        alpha1txt = MathTex(r'\alpha').next_to(alpha, UP * 3 + LEFT * 1)

        self.play(
            Create(alpha1),
            Create(alpha1txt),
            run_time=2
        )

        line__ab = Line(dota,dotb)
        line__be = Line(dotb,dote)

        alpha2 = Angle(line__ab,line__be,
        radius = 0.4,
        quadrant = (-1,1)
        )
        alpha2txt = MathTex(r'\alpha').next_to(alpha2,DOWN*1 + RIGHT*0.05)

        self.play(
            Create(alpha2),
            Create(alpha2txt),
            run_time=2
        )

        linet_ab = Line(dota,dotb).set_color(WHITE)
        linet_be = Line(dotb,dote).set_color(WHITE)
        linet_ea = Line(dote,dota).set_color(WHITE)

        self.play(
            Create(linet_ab),
            Create(linet_be),
            Create(linet_ea),
            run_time = 2
        )

        tan = MathTex(r'tan\alpha = \frac{AE}{1}')
        tan.next_to(dots)
        tan1 = MathTex(r'AE = tan\alpha')
        tan1.next_to(dots)

        dotatan = Dot([-6,-1,0])
        dotetan = Dot([0,-1,0])

        linetan = Line(dotatan,dotetan)

        b2 = Brace(linetan)
        b2txt = b2.get_tex(r'tan\alpha')

        self.play(
            Create(tan),
            run_time=3
        )
        self.play(
            Transform(tan,tan1),
            run_time = 3
        )

        self.play(
            Create(b2),
            Create(b2txt),
            run_time = 2
        )

        self.play(
            Unwrite(
                VGroup(
                    tan,
                    tan1,
                    linet_ab,
                    linet_be,
                    linet_ea
                )
            ),
            run_time=3
        )

        p = MathTex(r'tan\alpha = \frac{sin\alpha}{cos\alpha}')
        p.next_to(dots)
        
        p1 = MathTex(r'1 + sin\alpha = \frac{sin\alpha}{cos\alpha}')
        p1.next_to(dots)
        
        self.play(
            Create(p),
            run_time=4
        )

        self.play(
            Transform(p,p1),
            run_time = 3
        )

        self.play(
                Unwrite(
                    VGroup(
                        p,p1
                    )
                )
            )
        
        dotss = Dot([0,2,0])
        
        r = MathTex(r'cos\alpha + cos\alpha sin\alpha = sin\alpha')
        r.next_to(dotss)

        self.play(
            Create(r),
            run_time=3
        )

        r1 = MathTex(r'cos\alpha sin\alpha = sin\alpha - cos\alpha')
        r1.next_to(dotss)

        self.play(
            Transform(r,r1),
            run_time=3
        )

        r2 = MathTex(r'(sin\alpha cos\alpha)^2 = (sin\alpha - cos\alpha)^2')
        r2.next_to(r1,DOWN)

        self.play(
            TransformFromCopy(r1,r2),
            run_time=3
        )

        self.play(
             Unwrite(
                VGroup(
                    r,r1
                )
            )
        )
        self.play(
            r2.animate.shift(UP*2),
            run_time=2
        )

        r3 = MathTex(r'sin^2\alpha cos^2\alpha = 1 - 2sin\alpha cos\alpha')
        r3.next_to(r2, DOWN)

        self.play(
            TransformFromCopy(r2,r3),
            run_time =3
        )
        
        t = MathTex(r'sin\alpha cos\alpha = t')
        t.next_to(r3,DOWN)
        
        t1 = MathTex('t^2 = 1 - 2t')
        t1.next_to(t,DOWN)

        self.play(
            Unwrite(r2),
            run_time=0.5
        )
        self.play(
            Create(t),
            run_time=1
        )

        self.play(
            TransformFromCopy(r3 ,t1),
            run_time=4
        )

        tr = MathTex(r't = \sqrt{2} - 1')
        tr.next_to(dotss)

        self.play(
            Unwrite(
                VGroup(
                   r3,t 
                )
            ),
            Transform(t1,tr),
            run_time=3
        )

        ttt = MathTex(r'sin\alpha cos\alpha = \sqrt{2} - 1')
        ttt.next_to(tr,DOWN)
        
        self.play(
            Create(ttt),
            run_time=3 
        )

        self.play(
            Unwrite(
                VGroup(
                tr,
                t1
                )
            )
        )

        self.play(
            ttt.animate.shift(UP*2),
            run_time=2
        )



        te = MathTex(r'sin^2\alpha (1 - sin^\alpha) = 3 - 2\sqrt{2}')
        te.next_to(ttt,DOWN)
        
        self.play(
            Create(
                te
            ),
            run_time=3
        )

        self.play(
            Unwrite(
                VGroup(
                    ttt
                )
            ),
            run_time=2
        )

        self.play(
            te.animate.shift(UP*1),
            run_time=2
        )

        v = MathTex(r'sin^2\alpha = v')
        v.next_to(te,DOWN)

        self.play(
            Create(v),
            run_time = 3
        )

        vv = MathTex(r'v(1-v) = 3 -2\sqrt{2}')
        vv.next_to(v, DOWN)
        
        self.play(
            TransformFromCopy(
                te,
                vv
            ),
            run_time = 3
        )

        self.play(
            Unwrite(
                VGroup(
                    te,
                    v
                )
            ),
            run_time=2
        )

        self.play(
            vv.animate.shift(UP*1)
        )
        f = MathTex(r'v = \frac{1 + \sqrt{8\sqrt{2}-11}}{2} ')
        f.next_to(vv,DOWN)

        self.play(
            TransformFromCopy(
                vv,
                f
            ),
            run_time=3
        )

        sinf = MathTex(r'sin\alpha = \sqrt{\frac{1 + \sqrt{8\sqrt{2}-11}}{2}}')
        sinf.next_to(dotss)

        self.play(
            Unwrite(
                VGroup(
                    vv,
                    f
                )
            )
        )

        self.play(
            Create(sinf),
            run_time=4
        )

        framebox = SurroundingRectangle(sinf, buff =0.8)

        self.play(
            Create(
                framebox
            ),
            run_time = 3
        )
        self.wait(3)