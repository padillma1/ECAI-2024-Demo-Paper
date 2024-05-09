#default log. reg.

import torch
import torch.nn as nn


class Baseline(nn.Module):
    def __init__(self, input_dim=13, output_dim=1):
        super(Baseline, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))
    
#one (hidden) layer NN
#import torch
#import torch.nn as nn

#class Baseline(nn.Module):
#    def __init__(self, input_dim=13, hidden_dim=8,output_dim=1):
#        super(Baseline, self).__init__()
#        self.linear1 = nn.Linear(input_dim, hidden_dim)
#        self.relu = nn.ReLU()
#        self.linear2 = nn.Linear(hidden_dim, output_dim)

#    def forward(self, x):
#        x = self.linear1(x)
#        x = self.relu(x)
#        x = self.linear2(x)
#        return torch.sigmoid(x)

#two (hidden) layer NN - not mentioned in paper despite initially using it to compare to one layer NN
#class Baseline(nn.Module):
#    def __init__(self, input_dim=13, hidden1_dim=8, hidden2_dim=4, output_dim=1):
#        super(Baseline, self).__init__()
#        self.linear1 = nn.Linear(input_dim, hidden1_dim)
#        self.relu1 = nn.ReLU()
#        self.linear2 = nn.Linear(hidden1_dim, hidden2_dim)
#        self.relu2 = nn.ReLU()
#       self.linear3 = nn.Linear(hidden2_dim, output_dim)

#    def forward(self, x):
#        x = self.linear1(x)
#        x = self.relu1(x)
#        x = self.linear2(x)
#        x = self.relu2(x)
#        x = self.linear3(x)
#        return torch.sigmoid(x)





 