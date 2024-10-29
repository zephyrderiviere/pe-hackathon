from common import*


def first(couple):
    a, b = couple
    return a

def second(couple):
    a, b = couple
    return b

def dist(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)


def min_link(i, j, data, cluster):
    #Calculates the minimum link between clusters number i and j
    data_i = data[cluster == i]
    data_j = data[cluster == j]

    

    dist_min = dist(first(data_i[0]), second(data_i[0]), first(data_j[0]), second(data_j[0]))

    for (x1, y1) in data_i:
        for (x2, y2) in data_j:
            dist = dist(x1, y1, x2, y2)
            if (dist < dist_min):
                dist_min = dist

    return dist_min




def HCA(data, max_dist):
    #data is an array of couple (x, y)
    #We make clusters of the different couples according to the HCA algorithm

    #max_dist is the maximum allowed distance between two elements of the same cluster

    #default clustering (1 per cluster)
    clusters = np.arange(len(data))

    for ()
