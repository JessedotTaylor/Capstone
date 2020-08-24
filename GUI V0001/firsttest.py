from guizero import App, Text, TextBox, PushButton, Slider

def sayMyName():
    welcomeMessage.value = myName.value

def changeTextSize(sliderValue):
    welcomeMessage.size = sliderValue

app = App(title="Hello World")

welcomeMessage = Text(app, text="Welcome to the app", size=40, font="Times New Roman", color="lightblue")
myName = TextBox(app, width=50)
updateText = PushButton(app, command=sayMyName, text="Display my name")
textSize = Slider(app, command=changeTextSize, start=10, end=80)

app.display()