import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
resim = "blank_states_img.gif"
screen.addshape(resim)
turtle.shape(resim)

data = pandas.read_csv("50_states.csv")
data_state = data["state"].to_list()
data_x = data["x"].to_list()
data_y = data["y"].to_list()
skor = 0
while True:
    cevap = screen.textinput(title=f"{skor}/50 Eyalet isimi gir", prompt="Bir eyalet ismi giriniz?")
    cevap = cevap.title()
    if cevap == "Exit":
        screen.exitonclick()
        break
    for state in data_state:
        if cevap == state:
            skor += 1
            sayi = data_state.index(cevap)
            koordinat_x = data_x[sayi]
            koordinat_y = data_y[sayi]
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(koordinat_x,koordinat_y)
            new_turtle.write(f"{cevap}",align="center")
            new_turtle.penup()
            new_turtle.goto(x= koordinat_x,y= koordinat_y)
            data_state.remove(cevap)

dt = pandas.DataFrame(data_state)
dt.to_csv("Bulunamayan_eyaletler.csv")








