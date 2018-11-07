
class Adapter :
    def adaptData(self, data) :
        for i in range(6) :
            (x, y, z) = data[i]
            data[i] = (x*0.02, y*0.02, (z-500)*0.02)
        return data