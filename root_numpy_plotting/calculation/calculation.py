from util import getWeightsFromBins

# a calculation that can be different in MC and in Data. E.G. reweighting the sample.
class calculationDataMC:
    def __init__(self, function, list_of_branches):
        self.function = function
        self.name = function.__name__
        self.needsDataFlag = True
        self.branches = list_of_branches

    def eval(self, data, dataFlag):
        return self.function(data, dataFlag)


class calculation:
    def __init__(self, function, list_of_branches):
        self.function = function
        self.name = function.__name__
        self.needsDataFlag = False
        self.branches = list_of_branches

    def eval(self, data):
        return self.function(data)

def WeightsToNormalizeToHistogram(variable_in_histogram, histogram):
    '''normalize the weights to the histogram'''
    low_edges = []
    high_edges = []
    normalizations = []
    #get the low bin edges of the histograms
    for bin in range(1, histogram.GetNbinsX() + 1):
        low_edges.append(histogram.GetBinLowEdge(bin))
        high_edges.append(histogram.GetBinLowEdge(bin + 1))
        normalizations.append(histogram.GetBinContent(bin))

    low_edges = np.array(low_edges, np.float)
    high_edges = np.array(high_edges, np.float)
    hist_weights = np.array(normalizations, np.float)

    weights = getWeightsFromBins(variable_in_histogram, low_edges, high_edges, hist_weights)

    return weights

class weightCalculation:
    def __init__(self, function, list_of_branches):
        self.function = function
        self.name = function.__name__
        self.branches = list_of_branches
        self.reweightDictionary = {}

    def eval(self, data, isData, channel):
        if channel in self.reweightDictionary:
            extra_weight = np.ones(len(data))
            for variable, histogram in zip(self.reweightDictionary[channel]["variables"], self.reweightDictionary[channel]["histograms"])
                print("Reweighting variable " + variable.name + " in channel " + channel)
                extra_weight *= WeightsToNormalizeToHistogram(variable.eval(data), histogram)
        return self.function(data, isData) * extra_weight

    def addReweightHistogram(channel, variable, histogram):
        if channel not in self.reweightDictionary:
            self.reweightDictionary[channel] = {}
            self.reweightDictionary[channel]["variable"] = []
            self.reweightDictionary[channel]["histograms"] = []
            self.reweightDictionary[channel]["variable"].append(variable)
            self.reweightDictionary[channel]["histograms"].append(histogram)
            ##make sure that we always read the variable that we need for the histogram reweighting
            self.branches += variable.branches
        else:
            self.reweightDictionary[channel]["variables"].append(variable)
            self.reweightDictionary[channel]["histograms"].append(histogram)
            ##make sure that we always read the variable that we need for the histogram reweighting
            self.branches += variable.branches




