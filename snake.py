import numpy as np
import random

class Snake():
    def __init__(self,tx,ty,H,W,hx=1,hy=1):
        self.hx = hx
        self.hy = hy
        self.tx = tx
        self.ty = ty
        self.h = H
        self.w = W
        self.body = [(hx,hy)]

    def target_flush(self,tx,ty):
        self.tx = tx
        self.ty = ty

    def get_map(self,total_map):
        self.map = total_map

    def edge_judge(self,qx,qy,H,W):
        judgement = [1,1,1,1]
        if qx == 0:
            judgement[0] = 0
        if qx == W-2:
            judgement[1] = 0
        if qy==0:
            judgement[2]=0
        if qy==H-2:
            judgement[3] = 0

        return judgement

    def safe_judge(self,qx,qy,H,W):
        judgement = self.edge_judge(qx,qy,H,W)
        i_list = [(qx-1,qy),(qx+1,qy),(qx,qy-1),(qx,qy+1)]
        result = [0,0,0,0]
        for index,each in enumerate(judgement):
            if(each!=0):
                if (self.map[i_list[index][1]][i_list[index][0]]!=0):
                    result[index]=1
        #print('result:  ',result)
        return result

    def find_neighbor(self,qx,qy,H,W):
        neighbor = []
        judgement = self.safe_judge(qx,qy,H,W)
        if judgement[0]:
            neighbor.append((qx-1,qy))
        if judgement[1]:
            neighbor.append((qx+1,qy))
        if judgement[2]:
            neighbor.append((qx,qy-1))
        if judgement[3]:
            neighbor.append((qx,qy+1))

        return neighbor

    def find_argmin(self,target_list,distance_matrix):
        min = self.h * self.w *2
        argmin = (-1,-1)
        for each in target_list:
            if distance_matrix[each[1]][each[0]]<min:
                min = distance_matrix[each[1]][each[0]]
                argmin = each
        print("next_pos:  ",end=' ')
        print(argmin)

        return argmin

    def bfs_get_distance(self):
        Queue = []
        Queue.append((self.tx,self.ty))
        visited = np.zeros((self.h,self.w))
        big_number = self.h * self.w +1
        distance = np.ones((self.h,self.w)) * big_number
        distance[self.ty][self.tx] = 0

        while(len(Queue)):
            qx,qy = Queue.pop(0)
            temp = distance[qy][qx]

            if visited[qy][qx]==0:
                visited[qy][qx] = 1
                neighbor  = self.find_neighbor(qx,qy,self.h,self.w)
                for each in neighbor:
                    Queue.append(each)
                    distance[each[1]][each[0]] = min(distance[each[1]][each[0]],temp+1)

        return distance

    def random_move(self):
        random_judgement = self.edge_judge(self.hx,self.hy,self.h,self.w)
        random_choose = [(self.hx-1,self.hy),(self.hx+1,self.hy),(self.hx,self.hy-1),(self.hx,self.hy+1)]
        able_to_choose = []
        for i,each in enumerate(random_judgement):
            if each !=0:
                able_to_choose.append(random_choose[i])

        if(len(able_to_choose)==0):
            return random.choice(random_choose)

        return random.choice(able_to_choose)


    def move(self):
        distance = self.bfs_get_distance()
        print(distance)
        head_neighbor = self.find_neighbor(self.hx,self.hy,self.h,self.w)
        next_pos = self.find_argmin(head_neighbor,distance)
        if(next_pos==(-1,-1)):
            next_pos = self.random_move()
        last_tail = self.body.pop(0)
        self.body.append(next_pos)
        self.hx = self.body[-1][0]
        self.hy = self.body[-1][1]

        return last_tail


    def move_and_grow(self):
        last_tail = self.move()
        grow_flag = False
        if self.hx == self.tx and self.hy == self.ty:
            self.body.insert(0,last_tail)
            grow_flag = True

        return grow_flag

    def die_or_not(self):
        if(self.map[self.hy][self.hx]==0):
            return True
        return False

if __name__ == '__main__':
    snake = Snake(0,0,2,2,1,1)
    print(snake.body)
    while(len(snake.body)!=2):
        snake.move_and_grow()
        print(snake.body)

