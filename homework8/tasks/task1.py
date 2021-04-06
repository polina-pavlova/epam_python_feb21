from keyword import iskeyword


class KeyValueStorage:
    def __init__(self, path_to_file):
        with open(path_to_file) as fi:
            key_value = [k_v.rstrip().split("=") for k_v in fi.readlines()]

        for k, v in key_value:
            if not k.isidentifier() or iskeyword(k):
                raise ValueError("Wrong key!")
            if v.isdigit():
                v = int(v)
            if k not in self.__dict__:
                setattr(self, k, v)

    def __getitem__(self, item):
        return self.__dict__[item]
