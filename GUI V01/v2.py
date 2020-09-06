from guizero import App, PushButton, Box, Window, Text

widthPx = 1280
heightPx = 1024
#print(widthPx, widthPx //2)
app = App(title="Main Window", width=widthPx, height=heightPx)

marginPx = 20 # px

quarterHeight = (heightPx - marginPx *2) // 2 

buttonWidthPx = 400
buttonHeightPx = 200

debug = False

# Float off edges
topOffset = Box(app, width='fill', height=marginPx, border=False)
outMarginBox = Box(app, width=widthPx-marginPx*2, height=heightPx-marginPx*2, border=debug)

#Split in half
halfWidthPx = (widthPx - marginPx*2) // 2
leftBox = Box(outMarginBox, width=halfWidthPx, height='fill', align='left', border=debug)
rightBox = Box(outMarginBox, width=halfWidthPx, height='fill', align='right', border=debug)

#Split each Vertical Half in half Horizontally
topLeftBox = Box(leftBox, width='fill', height=quarterHeight, align='top',border=debug)
bottomLeftBox = Box(leftBox, width='fill', height=quarterHeight, align='bottom',border=debug)

topRightBox = Box(rightBox, width='fill', height=quarterHeight, align='top',border=debug)
bottomRightBox = Box(rightBox, width='fill', height=quarterHeight, align='bottom',border=debug)

#Float buttons in center of each quarter
offsetHeight = (quarterHeight - buttonHeightPx ) //2
topOffset1 = Box(topLeftBox, width='fill', height=offsetHeight, border=False)
topLeftFloat = Box(topLeftBox, width=buttonWidthPx, height=buttonHeightPx, border=debug)

topOffset2 = Box(bottomLeftBox, width='fill', height=offsetHeight, border=False)
bottomLeftFloat = Box(bottomLeftBox, width=buttonWidthPx, height=buttonHeightPx, border=debug)

topOffset3 = Box(topRightBox, width='fill', height=offsetHeight, border=False)
topRightFloat = Box(topRightBox, width=buttonWidthPx, height=buttonHeightPx, border=debug)

topOffset4 = Box(bottomRightBox, width='fill', height=offsetHeight, border=False)
bottomRightFloat = Box(bottomRightBox, width=buttonWidthPx, height=buttonHeightPx, border=debug)


preset = PushButton(topLeftFloat, text="Load from Preset", width='fill' , height='fill')
disk = PushButton(topRightFloat, text="Load from Disk", width='fill', height='fill')


network = PushButton(bottomLeftFloat, text="Load from Network", width='fill', height='fill')
settings = PushButton(bottomRightFloat, text="Settings", width='fill', height='fill')



app.display()