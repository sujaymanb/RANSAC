import numpy as np
import fit_plane
import plot_pcd

def select_not(data, indices):
    mask = np.ones(len(data), bool)
    mask[indices] = 0
    other_data = data[mask]
    return other_data

# load point cloud (x y z r g b)
points = np.loadtxt("points.txt", delimiter=' ')
points = points[:,:3]

ransac = fit_plane.Planar()
plane, inliers = ransac.fit(points, 0.01)
outlier_pts = select_not(points, inliers)
plot_pcd.plot_plane_fit(outlier_pts, points[inliers], plane)
