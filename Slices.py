import numpy as np


def slice_me(a, slices):
    slices_mean = dict()
    means = []
    for slice in slices:
        covered = a[slice[0]:(slice[1] + 1)]
        avg = np.mean(covered)
        means.append(avg)
        if avg not in slices_mean:
            slices_mean[avg] = slice

    min_mean = min(means)
    pair = slices_mean.get(min_mean)
    starting_position = pair[0]

    return starting_position


slice_ex = [(1, 2), (3, 4), (1, 4), (7, 8)]
print(slice_me([4, 2, 2, 5, 1, 5, 8, 2, 2], slice_ex))
