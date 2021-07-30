class Codec:
    def compress(self, data):
        res = ''
        i = 0
        while i < len(data):
            curr, l = data[i], 0
            while i < len(data) and  data[i] == curr:
                i += 1
                l += 1
            res += curr + str(l)

        return res


    def decompress(self, data):
        res = ''
        for i in range(0, len(data), 2):
            c, l = data[i], data[i + 1]
            res += ''.join([c for _ in range(int(l))])
        return res

if __name__ == '__main__':
    for _ in range(int(input())):
        codec = Codec()
        data = input()
        compressed = codec.compress(data)
        decompressed = codec.decompress(compressed)
        print(decompressed)
