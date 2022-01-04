from dataset import Dataset

data = Dataset()
data.load_data("iris.data", header=True)
data.show_labels()
data.show_data(start=46, stop=54)
data.split_data(test_ratio=0.1, train_ratio=0.8, validate_ratio=0.1)
data.freq("name")
data.save_sets("result_test.csv", data.test)
data.save_sets("result_train.csv", data.train)
data.save_sets("result_validate.csv", data.validate)

