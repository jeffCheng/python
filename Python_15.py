class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("Internet")