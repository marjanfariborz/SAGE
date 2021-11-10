
def correctness(oracle, filename):
    with open(filename, "r") as graph:
        for line in graph.readlines():
            src, dst = line.split(',')
            vid = str(src[4:])
            value = str(dst[6:])
            if vid in oracle:
                v = str(oracle[vid]).split()
                value = value.split()
                if v != value:
                    print("*****",vid, type(v), type(value), v == value, "\n")
            else:
                print(vid, value)
