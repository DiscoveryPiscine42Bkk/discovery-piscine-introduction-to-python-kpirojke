import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    for arg in args:
        if arg.endswith("ism"):
            continue
        print(f"{arg}ism")