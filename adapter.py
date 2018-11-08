
DELTA_THRESHOLD = 50
class Adapter :

    def __init__(self) :
        self.prev_raw_1 = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.prev_1 = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.prev_2 = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
    
    def adaptData(self, data, prev_raw_1, prev_1, prev_2) :
        delta = abs(data - prev_raw_1)
        if delta > DELTA_THRESHOLD :
            td = prev_1
        else :
            td = data
        # td = data
        return 0.6*td + 0.3*prev_1 + 0.1*prev_2

    def adaptDataSet(self, data) :
        # log_file = open("log.csv", "a")
        # log_line = ""
        for i in range(6) :
            (x, y, z) = data[i]
            sx = self.adaptData(x, self.prev_raw_1[i][0], self.prev_1[i][0], self.prev_2[i][0])
            sy = self.adaptData(y, self.prev_raw_1[i][1], self.prev_1[i][1], self.prev_2[i][1])
            sz = self.adaptData(z, self.prev_raw_1[i][2], self.prev_1[i][2], self.prev_2[i][2])

            self.prev_2[i][0] = self.prev_1[i][0]
            self.prev_2[i][1] = self.prev_1[i][1]
            self.prev_2[i][2] = self.prev_1[i][2]

            self.prev_raw_1[i][0] = x
            self.prev_raw_1[i][1] = y
            self.prev_raw_1[i][2] = z

            self.prev_1[i][0] = sx
            self.prev_1[i][1] = sy
            self.prev_1[i][2] = sz

            # log_line += str(sx) + "," + str(sy) + "," + str(sz) + ","
            data[i] = (sx*0.02, sy*0.02, (sz-500)*0.02)
        # log_file.write(log_line + "\n")
        # log_file.close()
        return data