from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open('randomtext.txt', 'r').read()

python_mask = np.array(PIL.Image.open('367783.png'))

colormap = ImageColorGenerator(python_mask)

wc = WordCloud(stopwords=STOPWORDS,
               mask=python_mask,
               background_color="white",
               contour_color="black",
               contour_width=3,
               min_font_size=3,
               max_words=400).generate(text)
wc.recolor(color_func=colormap)
plt.imshow(wc)
plt.axis("off")
plt.show()
