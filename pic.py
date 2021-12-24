def pic(picname):
    import cairosvg

    #Convert icon to png and write to file
    cairosvg.svg2png(url=f"https://yastatic.net/weather/i/icons/funky/dark/{picname}.svg", write_to=f"./data/{picname}.png", scale=10)



