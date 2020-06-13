import assignment as test

data = test.read_dataset("assignment_lake_george_data.csv")
print(test.largest_area(data))
print(test.average_volume(data))
print(test.most_average_rainfall(data))
print(test.hottest_month(data))
test.area_vs_volume(data)
test.plot_volumes(test.lake_george_simple_model(data, 55))
test.plot_volumes(test.lake_george_complex_model(data))
print(test.evaluate_model(data, test.lake_george_simple_model(data, 55)))
print(test.evaluate_model(data, test.lake_george_complex_model(data)))
