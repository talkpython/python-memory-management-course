import gc
import memutil
from doomed import Doomed


def main():
    print("Running reference counting demo!")
    gc.disable()

    v1 = Doomed()
    oid = id(v1)
    print(f"Step 1: Ref count is {memutil.refs(oid)}")

    v2 = v1
    print(f"Step 2: Ref count is {memutil.refs(oid)}")

    v2 = None
    print(f"Step 3: Ref count is {memutil.refs(oid)}")

    v1 = None
    print(f"Step 4: Ref count is {memutil.refs(oid)}")

    print("End of method!")


if __name__ == '__main__':
    main()
