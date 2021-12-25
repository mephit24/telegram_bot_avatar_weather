import os.path
PATH, _ = os.path.split(os.path.abspath(__file__))  #Get path to script

def pic(picname):
    import cairosvg
    #Check file existing
    if not os.path.exists(f"{PATH}/data/{picname}.png"):

        #Convert icon to png and write to file
        cairosvg.svg2png(url=f"https://yastatic.net/weather/i/icons/funky/dark/{picname}.svg", \
            write_to=f"{PATH}/data/{picname}.png", parent_height=300, parent_width=300, scale=7)



