# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-09-23

"""Example Google style docstrings"""


import torch
import torch.nn as nn

# CrossEntropyLoss
model = nn.Linear(10, 3)
criterion = nn.CrossEntropyLoss()

x = torch.randn(16, 10)
y = torch.randint(0, 3, size=(16,))  # (16, )
logits = model(x)  # (16, 3)

loss = criterion(logits, y)


from collections import OrderedDict

# NLL
model = nn.Sequential(
    nn.Linear(10, 3),
    nn.LogSoftmax()
)

# negative log likelihood loss
criterion = nn.NLLLoss()

x = torch.randn(16, 10)
y = torch.randint(0, 3, size=(16,))  # (16, )
out = model(x)  # (16, 3)

loss = criterion(out, y)