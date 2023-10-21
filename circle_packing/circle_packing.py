import random as rand
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math
import datetime, time

from palette import EARTHY
from circle import *
from circle_utils import *

#Genetic Algorithm for initial circle packing

IMAGE_SIZE = 10000 # max 1e4
BACKGROUND = 10
NUM_ATTEMPTS = 10000

def create_circles(attempts):
    circles = []
    for i in range(attempts):
        c = circle(rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE), rand.randint(0, IMAGE_SIZE // 3))
        if not c.out_of_bounds(IMAGE_SIZE, IMAGE_SIZE, pick_outline_width(c.r)) and not any([c.intersects(other, pick_outline_width(c.r + other.r)) for other in circles]):
            circles.append(c)
    return circles


if __name__ == '__main__':
    start = time.time()

    img = Image.new('RGB', (IMAGE_SIZE, IMAGE_SIZE), color = (BACKGROUND, BACKGROUND, BACKGROUND))
    draw = ImageDraw.Draw(img)

    circles = create_circles(NUM_ATTEMPTS)

    for c in circles:
        draw.ellipse((c.x - c.r, c.y - c.r, c.x + c.r, c.y + c.r), outline=(rand.choice(EARTHY)), width=pick_outline_width(c.r * 2)) # type: ignore

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    img_size = int(math.log10(IMAGE_SIZE))
    num_attempts = int(math.log10(NUM_ATTEMPTS))
    print(f'IMG Created: {round(time.time() - start, 5)} sec')
    img.save(f'./output/s_1e{img_size}_a_1e{num_attempts}_{timestamp}.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print(f'Runtime: {round(time.time() - start, 5)} sec')