import gc
import memutil
from doomed import Doomed


def main():
    print("Running gc demo!")
    gc.enable()

    v1 = Doomed()
    v2 = Doomed()

    v1.friends.append(v2)
    v2.friends.append(v1)

    id1 = id(v1)
    id2 = id(v2)
    print(f"Step 1: Ref counts are {memutil.refs(id1)} & {memutil.refs(id2)}")

    v1 = None
    v2 = None
    print(f"Step 2: Ref counts are {memutil.refs(id1)} & {memutil.refs(id2)}")

    data = []
    for i in range(1_000):
        x = i ** 2
        data.append(list(str(x) * 100))

    print(f"Step 3: Ref counts are {memutil.refs(id1)} & {memutil.refs(id2)}")

    print("End of method!")


if __name__ == '__main__':
    main()
