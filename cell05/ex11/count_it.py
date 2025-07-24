import sys
def main():
    args = sys.args[1:]
    if len(args) == 0:
        print("none")
    else:
        print(f"parameters: {len(args)}")
        for arg in args:
            print(f"{arg}: {len(arg)}")
if __name__ == "__main__":
    main()