import json
import math
import random
import os


class KMeans(object):
    # TO-DO: Richard
    def __init__(self, dataset=None):
        file_path = os.path.dirname(os.path.realpath(__file__))
        if dataset is None:
            self.mega_dataset = json.loads(open(file_path + '/dataset.json', 'r').read())
        else:
            self.mega_dataset = json.loads(dataset)

    def _ED(self, point1, point2):
        result = 0
        for i in xrange(len(point1)):
            result += pow(point2[i] - point1[i], 2)

        return math.sqrt(result)

    def _closest(self, datum, centroids):
        closest_index = None
        closest_distance = None
        for i, point in enumerate(centroids):
            dist = self._ED(datum, point)
            if closest_index is None or dist < closest_distance:
                closest_index = i
                closest_distance = dist
        return closest_index

    def _avg(self, li):
        return sum(li) / float(len(li))

    def _get_centroid(self, data):
        try:
            datum_len = range(len(next(iter(data))))
            result = [0 for x in datum_len]

            for datum in data:
                for i, value in enumerate(datum):
                    result[i] += value
            for i in datum_len:
                result[i] /= float(len(data))

            return tuple(result)
        except StopIteration:
            return ([0, 0, 0])

    def _kmeans(self, k, iterations=100):
        clusters = [set() for _ in xrange(k)]
        centroids = random.sample(self.dataset, k)
        # init data to clusters
        for datum in self.dataset:
            i = random.choice(range(k))
            clusters[i].add(datum)
        for _ in xrange(iterations):
            for datum in self.dataset:
                # remove from clusters
                for c in clusters:
                    try:
                        c.remove(datum)
                    except KeyError:
                        pass
                # get closest centroid index
                closest_index = self._closest(datum, centroids)
                # add to the new cluster
                clusters[closest_index].add(datum)

            # update centroids
            centroids = [self._get_centroid(c) for c in clusters]

        return clusters, centroids

    def calculate(self, attr, to_file=False):
        self.dataset = []
        for data in self.mega_dataset[attr]:
            self.dataset.append(tuple(data))
        self.dataset = set(self.dataset)

        champ2stat = {}
        for i in xrange(len(self.mega_dataset['champions'])):
            champ2stat[tuple(self.mega_dataset[attr][i])] = self.mega_dataset['champions'][i]

        clusters, centroids = self._kmeans(len(self.mega_dataset[attr][0]), 100)
        champ2cluster = []

        for i, c in enumerate(clusters):
            new_c = []
            champ2cluster.append(new_c)
            new_c.append(tuple(centroids[i]))

            for champ in c:
                new_c.append(champ2stat[champ])

        if to_file:
            f = open('output/' + attr + '_output.json', 'w')
            f.write(json.dumps(champ2cluster, indent=4))
            f.close()

        return champ2cluster

# Example:
