import random as rand
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math
import datetime, time

from palette import EARTHY, BRIGHT
from line import *

#Genetic Algorithm for initial circle packing

IMAGE_SIZE = 10000 # max 1e4
BACKGROUND = 10
NUM_ATTEMPTS = 10000

def create_lines(attempts):
    lines = []
    for i in range(attempts):
        l = Line(rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE))
        # l = Line.from_point_slope(rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE), rand.uniform(-10, 10), rand.randint(0, IMAGE_SIZE))
        if not l.out_of_bounds(IMAGE_SIZE, IMAGE_SIZE) and not any([l.intersects(other) for other in lines]):
            lines.append(l)
    return lines


if __name__ == '__main__':
    start = time.time()

    img = Image.new('RGB', (IMAGE_SIZE, IMAGE_SIZE), color = (BACKGROUND, BACKGROUND, BACKGROUND))
    draw = ImageDraw.Draw(img)

    lines = create_lines(NUM_ATTEMPTS)

    for l in lines:
        color = rand.choice(BRIGHT)
        draw.line([(l.x_1, l.y_1), (l.x_2, l.y_2)], fill=color, width=l.width) # type: ignore
        draw.ellipse((l.x_1 - l.width/2, l.y_1 - l.width/2, l.x_1 + l.width/2, l.y_1 + l.width/2), fill=color)
        draw.ellipse((l.x_2 - l.width/2, l.y_2 - l.width/2, l.x_2 + l.width/2, l.y_2 + l.width/2), fill=color)


    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    img_size = int(math.log10(IMAGE_SIZE))
    num_attempts = int(math.log10(NUM_ATTEMPTS))
    print(f'IMG Created: {round(time.time() - start, 5)} sec')
    img.save(f'./output/s_1e{img_size}_a_1e{num_attempts}_{timestamp}.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print(f'Runtime: {round(time.time() - start, 5)} sec')