import random
import numpy as np

class Planar:
    """
    Planar RANSAC
    """

    def __init__(self):
        self.inliers = []
        self.params = []

    def fit(self, pts, thresh=0.05, minPts=100, maxIter=1000):
        n = pts.shape[0]
        best_fit = []
        best_pts = []

        for it in range(maxIter):
            # sample 3 random points
            ids = random.sample(range(0, n), 3)
            pt_samples = pts[ids]

            # find the plane equation described by those points
            vecA = pt_samples[1, :] - pt_samples[0, :]
            vecB = pt_samples[2, :] - pt_samples[0, :]

            # Cross product to get normal vector
            vecC = np.cross(vecA, vecB)

            # plane eq: C0x + C1y + C0z = -k
            vecC = vecC / np.linalg.norm(vecC)
            k = -np.sum(np.multiply(vecC, pt_samples[1, :]))
            plane = [vecC[0], vecC[1], vecC[2], k]

            # distance from pt to plane
            pt_id_inliers = []
            dist_pt = (plane[0] * pts[:, 0] + plane[1] * pts[:, 1] + plane[2] * pts[:, 2] + plane[3]) / np.sqrt(plane[0] ** 2 + plane[1] ** 2 + plane[2] ** 2)

            # find consensus pts
            pt_id_inliers = np.where(np.abs(dist_pt) <= thresh)[0]
            
            # if consensus > threshold, update best fit params
            if len(pt_id_inliers) > len(best_pts):
                best_fit = plane
                best_pts = pt_id_inliers

            self.inliers = best_pts
            self.params = best_fit

        return self.params, self.inliers
