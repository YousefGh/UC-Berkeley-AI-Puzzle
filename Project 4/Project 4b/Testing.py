from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import matplotlib.pyplot as plt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

# xorData = [
#     [0, 0, 0],
#     [1, 0, 1],
#     [0, 1, 1],
#     [1, 1, 0]
# ]

# Q5:
# accuracies = [testPenData()[1] for i in xrange(5)]
# print "PenData: "
# PenDataAccuracies = []
# for i in xrange(5):
#     print "Iteration", i+1
#     PenDataAccuracies.append(testPenData()[1])
#
# print "accuracies: ", PenDataAccuracies
# print "avg:", average(PenDataAccuracies)
# print "std:", stDeviation(PenDataAccuracies)
# print "max:", max(PenDataAccuracies)
#
# print "carData: "
# carDataAccuracies = []
# for i in xrange(5):
#     print "Iteration", i+1
#     carDataAccuracies.append(testCarData()[1])
#
# print "accuracies: ", carDataAccuracies
# print "avg:", average(carDataAccuracies)
# print "std:", stDeviation(carDataAccuracies)
# print "max:", max(carDataAccuracies)


# Q6:
dvAccAverageY = []
ivNeuronsX = []
neurons = 0
print "\t\tPen Data\n"
print "\t\t\t#Neurons VS Accuracy | Pen Data"
print "# Neurons\t\t  Accuracies \t\t Avg., Std, Max"
while neurons <= 40:
    print  neurons,'\t\t\t',
    penDataAccuracies = [testPenData([neurons])[1] for i in xrange(5)]
    # accuracies = [i for i in xrange(5)]
    print penDataAccuracies,
    print '\t ', average(penDataAccuracies),'  ', stDeviation(penDataAccuracies),'  ', max(penDataAccuracies)

    ivNeuronsX.append(neurons)
    dvAccAverageY.append(average(penDataAccuracies))

    neurons += 5

print "\n\n\n"


# evenly sampled time at 200ms intervals

x = ivNeuronsX
y = dvAccAverageY
fig = plt.figure()
plt.plot(x,y, 'o--')
fig.suptitle('# Neurons VS Accuracy', fontsize=24)
plt.xlabel('# Neurons', fontsize=18)
plt.ylabel('Accuracy', fontsize=16)
fig.savefig('testPenData.png')


plt.show()

dvAccAverageY = []
ivNeuronsX = []

neurons = 0
print "\t\tCar Data\n"
print "\t\t\t#Neurons VS Accuracy | Car Data"
print "# Neurons\t\t  Accuracies \t\t Avg., Std, Max"
while neurons <= 40:
    print  neurons,'\t\t\t',
    carDataAccuracies = [testPenData([neurons])[1] for i in xrange(5)]
    # accuracies = [i for i in xrange(5)]
    print carDataAccuracies,
    print '\t ', average(carDataAccuracies),'  ', stDeviation(carDataAccuracies),'  ', max(carDataAccuracies)

    ivNeuronsX.append(neurons)
    dvAccAverageY.append(average(carDataAccuracies))

    neurons += 5

x = ivNeuronsX
y = dvAccAverageY
fig = plt.figure()
plt.plot(x,y, 'o--')
fig.suptitle('# Neurons VS Accuracy | Car Data', fontsize=24)
plt.xlabel('# Neurons', fontsize=18)
plt.ylabel('Accuracy', fontsize=16)
fig.savefig('testCarData.png')

plt.show()