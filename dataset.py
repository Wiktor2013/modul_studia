from random import shuffle   # ten import zapewnia odpowiednie mieszanie danych


class Dataset:
    labels = None
    data = None
    train = None
    test = None
    validate = None

    def load_data(self, filename, header=True, delimiter=','):
        with open(filename, "r") as f:
            self.labels = []
            self.data = []
            if header:
                self.labels = f.readline().replace("\n", "").split(delimiter)
            for row in f:
                if row != "\n":
                    self.data.append(row.replace("\n", "").split(delimiter))

    def show_labels(self):
        print(self.labels if self.labels else "No labels in dataset")

    def show_data(self, start=None, stop=None):
        if self.data:
            for i in range(len(self.data)):
                if start is not None and stop is not None:
                    if start <= i < stop:
                        print(self.data[i])
                else:
                    print(self.data[i])
        else:
            print("No data in dataset")

    def split_data(self, train_ratio, test_ratio, validate_ratio):
        if train_ratio + test_ratio + validate_ratio != 1:
            print("Incorrect ratio, must be sum of 1")
            return
        train_count = train_ratio * len(self.data)
        test_count = test_ratio * len(self.data)

        shuffle(self.data)
        self.train = []
        self.test = []
        self.validate = []
        for i in range(len(self.data)):
            if i < train_count:
                self.train.append(self.data[i])
            elif i < train_count + test_count:
                self.test.append(self.data[i])
            else:
                self.validate.append(self.data[i])

    def freq(self, label):
        if label not in self.labels:
            print("Label not exist!")
            return
        col_no = self.labels.index(label)
        fr = {}
        for d in self.data:
            value = d[col_no]
            if value not in fr:
                fr[value] = 1
            else:
                fr[value] += 1
        print(fr)

    def save_sets(self, filename, data, delimiter=","):
        with open(filename, "w") as f:
            for d in data:
                line = delimiter.join(d)
                f.write(line + "\n")
