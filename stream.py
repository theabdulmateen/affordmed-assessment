class ToyTCPStream:
    d = {}
    pointer = 1

    def receive(self, chunk, data):
        self.d[chunk] = data

    def read(self, size):
        curr = 1
        data = ''
        while curr <= size:
            if self.pointer not in self.d:
                return (data, len(data))
            data = data + self.d[self.pointer]
            curr += len(self.d[self.pointer])
            self.pointer += len(self.d[self.pointer])
        return (data[:size], curr)

if __name__ == "__main__":
    t = ToyTCPStream()
    for _ in range(int(input())):
        case = int(input())
        if case == 1:
            chunk = int(input())
            data = input()
            t.receive(chunk, data)
        elif case == 2:
            size = int(input())
            res, s = t.read(size)
            print(res, s)
