from manim import *

class poten(MovingCameraScene):

    def construct(self):
        
        txt = Tex('How can i find half of $2^{10729027}$?')
        pot = MathTex('2^{10729027}').to_edge(LEFT*11)
        metade = MathTex(r'\frac{x}{2}').to_edge(RIGHT*11)
        half = MathTex(r'\frac{2^{10729027}}{2}')
        propriedade = MathTex(
            r'\frac{a^{x}}{a^{y}} = a^{x-y}')
        text = Tex('Quotient of like bases')
        apply = Tex('Then, applying the property, we have:').to_edge(UL)
        app = MathTex(r'\frac{2^{10729027}}{2} = 2^{10729027-1}')
        fi = MathTex(r'2^{10729026}')
        framebox1 = SurroundingRectangle(app, buff =1)
        framebox2 = SurroundingRectangle(fi,buff=1)
        self.play(
            Create(
                txt
                 )
        )
        self.play(
            txt.animate.shift(UP*7),
            run_time = 6
        )
        
        self.play(
            Create(pot),
            Create(metade)
        )

        self.play(
            pot.animate.shift(LEFT * 5 + UP * 3),
            metade.animate.shift(RIGHT * 5 + UP * 3),
            run_time=3
        )
        self.play(
            pot.animate.shift(RIGHT * 5 + DOWN * 3),
            Transform(pot,half),
            metade.animate.shift(LEFT*5 + DOWN*3),
            Transform(metade,half), 
            run_time=3
            )

        self.play(
            Unwrite(VGroup(pot, half, metade)
            )
        )

        self.play(
            Create(text)
        )
        self.play(
            text.animate.shift(UP*1),
            run_time=2    
        )

        self.play(
            Create(propriedade),
            run_time=4
        )

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=propriedade.width * 1.2))
        self.wait(1)
        self.play(
            Unwrite(propriedade),
            Unwrite(text)
            )
        self.play(Restore(self.camera.frame))


        self.play(
            Create(apply),
            run_time=4
        )
        self.play(
            Create(app),
            run_time=5
        )
        
        self.play(
            Create(framebox1)
        )
        self.wait()

        self.play(
            Transform(app,fi),
            Transform(framebox1,framebox2),
            run_time=5
        )
        
        self.play(
            Unwrite(VGroup(apply,framebox1,framebox2,app,fi))
        )

        text = Tex('Follow on Instagram:').to_edge(UL,buff = 1)
        text1 = Tex('@pipocamath')
        
        self.play(Write(text), run_time = 3)
        self.play(Write(text1), run_time = 3)
       
        thanks = Tex('Thanks for watching!').to_edge(DR,buff = 1)

        self.play(Write(thanks), run_time=3)
        self.wait()   
