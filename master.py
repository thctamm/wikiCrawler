import string, json, re, csv, os.path
import initializer
import degrees

DEFAULT_DEPTH = 3;
DEFAULT_ITERS = 3;

def main(source, target):

    iters = DEFAULT_ITERS

    if not os.path.isfile('./data/' + target + ".csv"):
        with open('./data/' + target + "_0.csv", 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|')
            writer.writerow([target])
        for i in range(1, DEFAULT_DEPTH):
            print("initializing level: " + str(i) + "...")
            initializer.main("./data/" + target + "_" + str(i-1) + ".csv", "./data/" + target + "_" + str(i) + ".csv")

        with open('./data/' + target + ".csv", 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|')
            writer.writerow([target])
            for i in range(1, DEFAULT_DEPTH):
                writer.writerow(["./data/" + target + "_" + str(i) + ".csv"])

    return degrees.main(source, './data/' + target + ".csv", iters)
