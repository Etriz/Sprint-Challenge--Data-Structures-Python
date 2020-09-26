class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []

    def append(self, item):
        from datetime import datetime

        data = item, datetime.now()

        if len(self.q) < self.capacity:
            self.q.append(data)
            return
        else:
            oldest = datetime.now()
            replaceIndex = -1
            for i, elem in enumerate(self.q):
                # print(i, elem[1])
                if elem[1] < oldest:
                    oldest = elem[1]
                    replaceIndex = i
            self.q[replaceIndex] = data
            # print(f"replaceindex: {replaceIndex}")

    def get(self):
        ret = []
        for elem in self.q:
            ret.append(elem[0])
        # print(ret)
        return ret