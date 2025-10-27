import torch

class PolicyGradient(torch.nn.Module):
  def __init__(self, num_features, num_actions):
    super().__init__()
    self.linear = torch.nn.Linear(num_features, num_actions)
    torch.nn.init.xavier_uniform_(self.linear.weight)
    torch.nn.init.zeros_(self.linear.bias)

@staticmethod
def np_to_torch(x):

def forward(self, states):

def get_action():
