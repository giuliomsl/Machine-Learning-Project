import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv

import numpy as np
import csv

def load_data(file_path):
    data = []
    labels = []
    label_mapping = {'0': 0, '1': 1}

    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            # Assicurati di rimuovere gli spazi bianchi extra da ciascun elemento della riga
            row = [elem.strip() for elem in row]
            # Converti i primi 6 valori in float e aggiungili alla lista dei dati
            data.append([float(val) for val in row[:6]])
            # Mappa l'etichetta binaria all'ultimo elemento della riga
            labels.append(label_mapping[row[6]])

    # Non è necessario trasporre la matrice in questo caso
    matrix = np.array(data).T
    label_array = np.array(labels)
    return matrix, label_array


def hist_plot(D, L):
    M0 = (L == 0)
    D0 = D[:, M0]

    M1 = (L == 1)
    D1 = D[:, M1]

    features = {0: 'Feature 1',
        1: 'Feature 2',
        2: 'Feature 3',
        3: 'Feature 4',
        4: 'Feature 5',
        5: 'Feature 6'}
    
    for i in range(6):
        plt.figure()
        plt.xlabel(features[i])
        plt.hist(D0[i, :], bins=10, density=True, alpha = 0.4, label="False")
        plt.hist(D1[i, :], bins=10, density=True, alpha = 0.4, label="True")

        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        #plt.savefig('histograms/hist_%d.pdf' % i)
    plt.show()

def scatter_plot(D, L):
    D0 = D[:, L==0]
    D1 = D[:, L==1]

    features = {0: 'Feature 1',
        1: 'Feature 2',
        2: 'Feature 3',
        3: 'Feature 4',
        4: 'Feature 5',
        5: 'Feature 6'}
    
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            plt.figure()
            plt.xlabel(features[i])
            plt.ylabel(features[j])
            plt.scatter(D0[i, :], D0[j, :], label="False")
            plt.scatter(D1[i, :], D1[j, :], label="True")

            plt.legend()
            plt.tight_layout()
            #plt.savefig('scatter/scatt_%d_%d.pdf' % (i, j))
        plt.show()


if __name__ == '__main__':
    D, L = load_data("trainData.txt")
    #hist_plot(D, L)
    scatter_plot(D, L)

