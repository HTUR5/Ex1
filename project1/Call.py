class Call:

    def __init__(self, name, time, source, dest, ud, flag: int = 0, idElev: int = 0):
        self.name = name
        self.time = time
        self.source = source
        self.dest = dest
        self.flag = flag
        self.idElev = 0
        self.ud=ud

    def __str__(self):
        row = [self.name, self.time, self.source, self.dest, self.flag, self.idElev]
        return row
        # return f"{self.name},{self.time},{self.source},{self.dest},{self.flag},{self.idElev}"

    def setElevator(self, _id):
        self.idElev = _id


