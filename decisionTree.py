from data import Data
import math

class DecisionTree:

    in_data = [] # list of instances

    def __init__(self,pathname,G):
        self.pathname = pathname
        self.G = G

    def group_data(self, data, index, group):
        for i in range(index,index+int(len(data)/self.G)):
            group.append(data[i])


    def nb_occurences(self, groups):
        g_nbOccur = []
        for g in groups:
            nSetosa, nVersicolor, nVirginica = 0, 0, 0

            # computer nb of occurences
            for instance in g:
                if instance[4] == 'Iris-setosa':
                    nSetosa+=1
                elif instance[4] == 'Iris-virginica':
                    nVirginica+=1
                else:
                    nVersicolor+=1
            
            # append nb occurences to a list
            g_nbOccur.append([nSetosa,nVirginica,nVersicolor])

        return g_nbOccur

    def entropy(self, k, k_instance, total_instance):
        entropy = 0
        for i in range(k):
            if len(k_instance[i]) != 0:
                entropy+= len(k_instance[i])/len(total_instance)*math.log(len(k_instance[i])/len(total_instance),2)

        return -entropy

    def group_entropy(self, k, k_instance, total_instance):
        entropy = 0
        for i in range(k):
            if k_instance[i] != 0:
                entropy+= (k_instance[i]/len(total_instance))*math.log(k_instance[i]/len(total_instance),2)

        return -entropy

    def disc(self, k, g_entropy, data_entropy, k_instance, total_instance):
        sum = 0
        for g in g_entropy:
            sum+=(len(k_instance)/len(total_instance))*g
        return data_entropy-sum

    def discriminative_power(self):

        disc_list = [] # list of each attribute's discriminative power

        # read and parse data
        data = Data(self.pathname)
        in_data = data.read_data()

        nrows = data.get_nrows(in_data) # number of rows
        ncols = data.get_ncols(in_data) # number of columns
        print("# rows: "+str(nrows)+"   # cols:"+str(ncols))

        # pick the "i"th attribute as a highest disc power
        for i in range(ncols-1):
            # sort the data due to "i"th attribute   
            in_sorted = data.sort_data(i)
            # data.print_data(in_sorted)

            # partition the data into G groups and computer the # of occurences of each species   
            groups = [[] for x in range(self.G)] # group data: short, average, long due to size of flower
            group_index = 0
            for j in range(0,len(in_sorted)-int(nrows%self.G),int(nrows/self.G)):
                self.group_data(in_sorted, j, groups[group_index])
                group_index+=1

            # iris_setosa, iris_versicolor, iris_virginica = self.nb_occurences(groups) # list of nb of species in each group
            g_nbOccur = self.nb_occurences(groups)

            # compute dataset entropy and entropy of each group
            dataset_entropy = self.entropy(self.G, groups, in_sorted)
            
            g_entropy = [] # array of group entropies
            for g in g_nbOccur:
                g_entropy.append(self.group_entropy(len(g),g,groups[0]))

            # compute the discriminative power of attribute i
            disc = self.disc(self.G, g_entropy, dataset_entropy, groups[0], in_data)
            disc_list.append(disc)

            print("\nAttribute "+str(i+1)+": \t ################################################"+
            "#########################################")
            print("Dataset entropy: "+str(dataset_entropy))
            print("Discriminative power: "+str(disc))
            for j in range(len(g_nbOccur)):
                print("iris_setosa:\t "+str(g_nbOccur[j][0])+
                "\tiris_versicolor:"+str(g_nbOccur[j][1])+
                "\tiris_virginica:"+str(g_nbOccur[j][2])+
                "\tGroup entropy: "+str(g_entropy[j]))

        return disc_list


    def dtree(self):
        
        disc_list = self.discriminative_power()
        print(disc_list)