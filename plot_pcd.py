from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def get_pts(infile):
    data = np.loadtxt(infile, delimiter=' ')
    return data[:,0], data[:,1], data[:,2] #returns X,Y,Z points skipping the first 12 lines
    
def plot_file(infile):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x,y,z = get_pts(infile)
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def plot_plane(plane, inliers, ax):
    a,b,c,d = plane
    grid_x = np.linspace(min(inliers[:,0]), max(inliers[:,0]), 10)
    grid_y = np.linspace(min(inliers[:,1]), max(inliers[:,1]), 10)
    xx, yy = np.meshgrid(grid_x, grid_y)
    
    # ax + by + cz = -d
    # z = (-d - ax - by)/c
    z = (-d -(a * xx) -(b * yy))/c
    ax.plot_surface(xx, yy, z, alpha=0.5)


def plot_plane_fit(outliers, inliers, plane):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(outliers[:,0], outliers[:,1], outliers[:,2], c='r', marker='o')
    ax.scatter(inliers[:,0], inliers[:,1], inliers[:,2], c='g', marker='o')
    plot_plane(plane, inliers, ax)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    
if __name__ == '__main__':
    infile = 'points.txt'
    plot_file(infile)