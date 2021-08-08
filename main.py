from snake import Snake
from food_map import Map,Food
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import os
import matplotlib.animation as animation


if __name__ == '__main__':
    food = Food()
    H = 10
    W = 20
    global_seed = 729
    random.seed(global_seed)
    seed = random.randint(0, 729608)
    food.generate(seed, H, W,[(1,1)])
    tx, ty = food.get_food_pos()
    food_map = Map(H, W, tx, ty)
    snake = Snake(tx,ty,H,W,hx=1,hy=1)
    snake.get_map(food_map.get_map(snake.body))
    grow_flag = False
    total_map = food_map.get_map(snake.body)
    plt.figure()
    plt.ion()
    while True:
        plt.cla()
        if grow_flag == True:
            seed = random.randint(0, global_seed)
            food.generate(seed,H,W,snake.body)
            tx,ty = food.get_food_pos()
            snake.target_flush(tx,ty)
            food_map.map_flush(tx,ty)

        total_map = food_map.get_map(snake.body)
        snake.get_map(total_map)
        plt.imshow(total_map, cmap='magma', vmin=0, vmax=2)
        plt.pause(0.01)
        grow_flag = snake.move_and_grow()
        print('head:  ',end='')
        print(snake.hx,end=',')
        print(snake.hy)


        print(snake.map)
        die_or_not = snake.die_or_not()
        print('die or not :   ',end='')
        print(die_or_not)
        if (die_or_not):
            break


    plt.show()

    if(die_or_not==True):
        print("score:   ",len(snake.body))
        print("seed:    ",global_seed)



