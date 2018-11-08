class Adapter :        

    def adaptData(self, data) :
        log_file = open("log.csv", "a")
        log_line = ""
        for i in range(6) :
            (x, y, z) = data[i]
            log_line += str(x) + "," + str(y) + "," + str(z) + ","
            data[i] = (x*0.02, y*0.02, (z-500)*0.02)
        log_file.write(log_line + "\n")
        log_file.close()
        return data