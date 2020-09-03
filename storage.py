import argparse
import os
import tempfile
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Storage script")
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    parser.add_argument('--key', action="store", dest="key")
    parser.add_argument('--val', action="store", dest="val")
    args = parser.parse_args()
    str = json.dumps({args.key: args.val})
    if args.val is not None:
        mode = 'r+' if os.path.exists(storage_path) else 'w+'
        with open(storage_path, mode) as f:
            data = {}
            if os.stat(storage_path).st_size != 0:
                data = json.load(f)
                if data.get(args.key):
                    data[args.key] += ", " + args.val
                else:
                    data[args.key] = args.val
            else:
                data[args.key] = args.val
            f.seek(0)
            json.dump(data, f)
    else:
        if os.path.exists(storage_path) and os.stat(storage_path).st_size != 0:
            with open(storage_path, 'r+') as f:
                data = json.load(f)
                print(data.get(args.key, "None"))
        else:
            print("None")