import numpy as np
import matplotlib.pyplot as plt
#from utils import plot_lines

def main():
    a1 = np.array([[1,2,3], 
               [3,2,1],[2,2,1]])
    
    x = np.linalg.det(a1)
    print(x)




if __name__ == "__main__":
    main()
