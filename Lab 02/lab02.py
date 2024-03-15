import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv

def load_data(file_path):
    data = []
    species = []
    species_mapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            data.append([float(val) for val in row[:4]])
            species.append(species_mapping[row[4]])

    # Trasponiamo la matrice per avere un record per ogni colonna
    matrix = np.array(data).T
    species_array = np.array(species)
    return matrix, species_array

def hist_plot(D, L):
    M0 = (L == 0)
    D0 = D[:, M0]

    M1 = (L == 1)
    D1 = D[:, M1]

    M2= (L == 2)
    D2 = D[:, M2]

    features = {0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'}
    
    for i in range(4):
        plt.figure()
        plt.xlabel(features[i])
        plt.hist(D0[i, :], bins=10, density=True, alpha = 0.4, label="Setosa")
        plt.hist(D1[i, :], bins=10, density=True, alpha = 0.4, label="Versicolor")
        plt.hist(D2[i, :], bins=10, density=True, alpha = 0.4, label="Virginica")

        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        plt.savefig('histograms/hist_%d.pdf' % i)
    plt.show()

def scatter_plot(D, L):
    D0 = D[:, L==0]
    D1 = D[:, L==1]
    D2 = D[:, L==2]

    features = {0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'}
    
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            plt.figure()
            plt.xlabel(features[i])
            plt.ylabel(features[j])
            plt.scatter(D0[i, :], D0[j, :], label="Setosa")
            plt.scatter(D1[i, :], D1[j, :], label="Versicolor")
            plt.scatter(D2[i, :], D2[j, :], label="Virginica")

            plt.legend()
            plt.tight_layout()
            plt.savefig('scatter/scatt_%d.pdf' % i)
        plt.show()


if __name__ == '__main__':
    D, L = load_data("iris.csv")
    #print(f"{L}")
    #hist_plot(D, L)
    scatter_plot(D, L)

