import numpy as np
import random
import matplotlib.pyplot as plt


class Food():
    def __init__(self):
        pass
    def generate(self,seed,H,W,snake_body):
        self.seed = seed
        random.seed(self.seed)
        self.tx = random.randint(1,W-2)
        self.ty = random.randint(1,H-2)

        while (self.tx,self.ty) in snake_body:
            self.tx = random.randint(1, W - 2)
            self.ty = random.randint(1, H - 2)

    def get_food_pos(self):
        return (self.tx,self.ty)


class Map():
    def __init__(self,H,W,tx,ty):
        self.w = W
        self.h = H
        self.tx = tx
        self.ty = ty

    def map_flush(self,tx,ty):
        self.tx = tx
        self.ty = ty

    def get_map(self,snake_body):
        total_map = np.ones((self.h,self.w))

        total_map[self.ty][self.tx] = 2

        for i in range(0,self.h):
            total_map[i][0] = 0
            total_map[i][self.w-1]=0

        for i in range(0,self.w):
            total_map[0][i] = 0
            total_map[self.h-1][i]=0
        for each in snake_body:
            total_map[each[1]][each[0]] = 0

        return total_map


if __name__ == '__main__':
    W = 51
    H = 51
    random.seed(729608)

    i=5
    while i:
        seed = random.randint(0, 729608)
        food = Food()
        food.generate(seed,H,W)
        (tx,ty) = food.get_food_pos()

        total_map = Map(H,W,tx,ty).get_map([(0,1),(0,2),(0,3),(0,4),(0,5)])

        plt.figure(figsize=(8,8))
        plt.imshow(total_map,cmap='rainbow',vmin=0,vmax=2)
        plt.show()

        i-=1

