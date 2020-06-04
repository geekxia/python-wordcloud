import wordcloud
file = open(r'./app.txt', encoding='utf-8')
text = file.read()
wc = wordcloud.WordCloud(
    font_path=r'./yahei.ttc',
    scale=28,
    margin=10,
    background_color='white',
    mode='RGBA'
    )
wc.generate(text)
image = wc.to_image()
image.show()
wc.to_file('./app.png')