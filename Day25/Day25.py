with open('input.txt') as f:
    lines = f.read().splitlines()


def get_distance(a, b):
    distance = 0
    for i in range(4):
        distance += abs(a[i] - b[i])
    return distance


data = {}
list_of_points = []
i = 0
for line in lines:
    data[i] = tuple(map(int, line.split(',')))
    list_of_points.append(i)
    i += 1

for k, v in data.items():
    print(k, v)

answer = 0
while len(list_of_points) > 0:
    answer += 1
    # Setup constellation with first entry of list of points
    cluster = []
    cluster.append(list_of_points[0])
    del list_of_points[0]
    while True:
        # For every point, check weather it belongs to current constellation
        org_list = list_of_points.copy()
        for point in org_list:
            org_cluster = cluster.copy()
            for target in org_cluster:
                if get_distance(data[point], data[target]) <= 3:
                    cluster.append(point)
                    list_of_points.remove(point)
                    break
        # if current cluster has grown, check again if other points are able to join; if not grown max size is reached
        if org_list == list_of_points:
            # No update; thus break
            break
    print(f'Constellation {answer} finished: {cluster}')
