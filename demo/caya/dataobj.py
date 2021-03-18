import json
import os
import zipfile

class DataObj:
    def __init__(self, workspace="dataobj", name="default"):
        self.workspace = workspace
        self.name = name
        self.home = self.homepath()
        self.iter_pos = 0
        self.read()
    
    def keys(self):
        return list(self.data.keys())

    def new(self):
        self.data = {}

    def homepath(self):
        return os.path.expanduser("~").replace(os.sep, "/")

    def workpath(self):
        return f"{self.home}/{self.workspace}"

    def filepath(self):
        return "%s/%s" % (self.workpath(), self.name)

    def read(self):
        if os.path.exists(self.filepath()):
            try:
                with zipfile.ZipFile(self.filepath(), "r") as fr:
                    self.data = json.loads(fr.read(self.name))
            except:
                self.new()
        else:
            self.new()

    def save(self):
        os.makedirs(self.workpath(), exist_ok=True)
        with zipfile.ZipFile(self.filepath(), "w") as fw:
            fw.writestr(self.name, json.dumps(self.data))

    def __enter__(self):
        return self

    def __exit__(self, exctype, excvalue, traceback):
        self.save()

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data.get(key)

    def __delitem__(self, key):
        if key in self.data.keys():
            del(self.data[key])

    def __del__(self):
        self.save()

    def __iter__(self):
        return self

    def __next__(self):
        keys = self.keys()
        if self.iter_pos == len(keys):
            self.iter_pos = 0
            raise StopIteration()
        buf = self.data[keys[self.iter_pos]]
        self.iter_pos += 1
        return buf

if __name__ == "__main__":
    d = DataObj("test","wow")
    d["hello"] = "hello world"
    del d

    d = DataObj("test","wow")
    print(d["hello"])

