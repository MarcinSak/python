import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(2)
    
    t.pensize(2)
    t.pencolor("yellow")
    t.fillcolor("yellow")
    
    def draw_star_shape(size):
        t.begin_fill()
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
    
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    
    draw_star_shape(200)
    
    turtle.done()

if __name__ == "__main__":
    draw_star()
