#https://projects.raspberrypi.org/en/projects/getting-started-with-guis/1
#Documentation: https://lawsie.github.io/guizero/
from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def doBooking():
    info("Booking", "Thank you for booking")
    print(filmChoice.value)
    print(vipSeat.value)
    print(rowChoice.value)

app = App(title="Second GUI app", width=300, height=200, layout="grid")
#Grid 0,0 top left

filmDescription = Text(app, text="Which Film?", grid=[0,0], align='left')
filmChoice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")

seatDescription = Text(app, text="Seat type", grid=[0,1], align='left')
vipSeat = CheckBox(app, text="VIP Seat?", grid=[1,1], align="left")

rowDescription = Text(app, text="Seat Location", grid=[0,2], align='left')
rowChoice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"], ["Back", "B"]], selected="M", horizontal=True, grid=[1,2], align="left")

bookSeats = PushButton(app, command=doBooking, text="Book Seat", grid=[1,3], align='left')

app.display()