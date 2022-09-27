import argparse
import numpy as np
import time
import sys
sys.setrecursionlimit(10000)

class mono_routing():
    def __init__(self, args):
        pass
    def parser(self): #You can modify it by yourself.
        with open("%s" % args.input, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("BoundaryIndex"):
                    value_list = lines.split(' ')
                    self.Bx1 = int(value_list[1])
                    self.By1 = int(value_list[2])
                    self.Bx2 = int(value_list[3])
                    self.By2 = int(value_list[4])
                if lines.startswith("DefaultCost"):
                    value_list = lines.split(' ')
                    self.default_cost = int(value_list[-1])
                if lines.startswith("NumNonDefaultCost"):
                    value_list = lines.split(' ')
                    self.size = int(value_list[-1])
                    break
            
            source_list = list(f[-2].split(' '))
            target_list = list(f[-1].split(' '))
            self.sx = source_list[1]
            self.sy = source_list[2]
            self.tx = target_list[1]
            self.ty = target_list[2]
            num_cost = f[3:3+int(self.size)]
 
        
        """Print parameters"""
        print('BoundaryIndex:', self.Bx1, self.By1, self.Bx2, self.By2)
        print('DefaultCost:', self.default_cost)
        print('NumNonDefaultCost:', self.size)
        for i in range(len(num_cost)):
            print(num_cost[i])
        print('Source:', self.sx, self.sy)
        print('Target:', self.tx, self.ty)


        self.dict = {}
        for i in range(len(num_cost)):
            index = 0
            for j in range(len(num_cost[i])-1, 0, -1):
                if num_cost[i][j] == ' ':
                    index = j
                    break
            data = num_cost[i][:j]
            dataDiff = num_cost[i][j+1:]
            self.dict[data] = int(dataDiff)
        # print(self.dict)
        
    def ReturnEdge(self, x1, y1, x2, y2):
        get = self.dict.get(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2), 0)
        if get != 0:
            del self.dict[str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2)]
        return self.default_cost + get     
  
            
    def routing(self):
        self.routing_path = np.zeros((self.Bx2+self.By2+1, 2), dtype=int)
        self.grid_cost = np.zeros((self.By2+1, self.Bx2+1), dtype=int)
        # ---TODO:
        # Write down your routing algorithm by using dynamic programming.
        # ---

        ########### Initial ################
        # For first row
        self.grid_cost[self.By2][0] = 0
        tmpX = 0
        for i in range(1, self.Bx2+1):
            tmpX += self.ReturnEdge(i-1, 0, i, 0)
            self.grid_cost[self.By2][i] = tmpX

        # For first column
        tmpY = 0
        for j in range(1, self.By2+1):
            tmpY += self.ReturnEdge(0, j-1, 0, j)
            self.grid_cost[self.By2 - j][0] = tmpY

        # print(self.grid_cost)    

        ############ Fill the grid_cost by DP and record the path #################### 
        self.rec = np.zeros((self.By2+1, self.Bx2+1), dtype=str)
        for i in range(1, int(self.tx)+1):
            for j in range(1, int(self.ty)+1):
                a = self.ReturnEdge(i-1, j, i, j)
                b = self.ReturnEdge(i, j-1, i, j)

                if self.grid_cost[self.By2-j][i-1] + a < self.grid_cost[self.By2-j+1][i] + b:
                    self.grid_cost[self.By2-j][i] = self.grid_cost[self.By2-j][i-1] + a
                    self.rec[self.By2-j][i] = "l"
                    
                else:
                    self.grid_cost[self.By2-j][i] = self.grid_cost[self.By2-j+1][i] + b
                    self.rec[self.By2-j][i] = "d"                    

        self.rec[self.By2, :] = 'l'
        self.rec[:, 0] = 'd'
        self.rec[-1, 0] = 'S'

        # First and final step
        self.routing_path[0][0] = self.routing_path[0][1] = 0
        self.routing_path[-1][0] = int(self.ty)
        self.routing_path[-1][1] = int(self.tx)

        # print(self.rec)
        print(self.grid_cost)

        self.FindRoute(self.By2-int(self.ty), int(self.tx), int(self.ty) + int(self.tx))
        # print(self.routing_path)

    def FindRoute(self, j, i, count):
        if count == 0:
            return
        if self.rec[j][i] == "l":
            self.routing_path[count][0] = i
            self.routing_path[count][1] = int(self.ty) - j
            self.FindRoute(j, i-1, count-1)
        elif self.rec[j][i] == "d":
            self.routing_path[count][0] = i
            self.routing_path[count][1] = int(self.ty) - j
            self.FindRoute(j+1, i, count-1)    
                              

    def output(self): # You can modify it by yourself, but the output format should be correct.
        with open("%s" % args.output, 'w', newline='') as file_out:
            file_out.writelines('RoutingCost %d'% self.grid_cost[self.By2-int(self.ty)][int(self.tx)])
            file_out.writelines('\nRoutingPath %d'% len(self.routing_path))
            for i in range(len(self.routing_path)):
                file_out.writelines('\n%d %d'% (self.routing_path[i][0], self.routing_path[i][1]))
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './5x5.in',help="Input file root.")
    parser.add_argument("--output", type=str, default = './5x5.out',help="Output file root.")
    args = parser.parse_args()

    print('#################################################')
    print('#              Monotonic Routing                #')
    print('################################################# \n')

    routing = mono_routing(args)
    """Parser"""
    routing.parser()
    print('################ Parser Down ####################')
    """monotonic route"""
    start = time.time()
    routing.routing()
    print('run time:', round(time.time()-start,3))
    """output"""
    routing.output()