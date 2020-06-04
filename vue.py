import wordcloud
file = open(r'./vue.txt', encoding='utf-8')
text = file.read()
wc = wordcloud.WordCloud(
    font_path=r'./yahei.ttc',
    scale=32,
    margin=10,
    background_color='white',
    mode='RGBA'
    )
wc.generate(text)
image = wc.to_image()
image.show()
wc.to_file('./vue.png')