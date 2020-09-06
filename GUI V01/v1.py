from guizero import App, PushButton, Box, Window, Text

widthPx = 1280
heightPx = 1024
#print(widthPx, widthPx //2)
app = App(title="Main Window", width=widthPx, height=heightPx)

presetWindow = Window(app, title="Preset Window")
presetText = Text(presetWindow, text="Hello")
presetWindow.hide()

page = "main"

def setPage(cmd):
    page = cmd
    print(page)
    if page == 'preset':
        presetWindow.show(wait=True)



topBox = Box(app, width='fill', height='fill', align='top', border=True)
preset = PushButton(topBox, text="Load from Preset", width=30 , height='fill', align='left', command=setPage("preset"))
disk = PushButton(topBox, text="Load from Disk", width=30, height='fill', align='right', command=setPage("disk"))

bottomBox = Box(app, width='fill', height='fill', align='bottom', border=True)
network = PushButton(bottomBox, text="Load from Network", width=30, height='fill', align='left', command=setPage("network"))
settings = PushButton(bottomBox, text="Settings", width=30, height='fill', align='right', command=setPage("settings"))
    #print(preset.value, disk.value, network.value, settings.value)

app.display()