import  torch
from    torch import autograd
from torch.utils.data import Dataset
from PIL import Image
import  os

# Dataset：提供一种方式去获取数据及其label。主要功能：1、如何获取每一个数据及其label；2、告诉我们总共有多少的数据
# Dataloader：为后面的网络提供不同的数据形式

img_path = "D:\\download\\数据集\\hymenoptera_data\\train\\ants\\0013035.jpg"
img = Image.open(img_path)
img.size
img.show()

img_path_list = os.listdir("D:\\download\\数据集\\hymenoptera_data\\train\\ants")
class MyData(Dataset):
    def __init__(self):
        pass







# x = torch.tensor(1.)
# a = torch.tensor(1., requires_grad=True)
# b = torch.tensor(2., requires_grad=True)
# c = torch.tensor(3., requires_grad=True)
#
# y = a**2 * x + b * x + c
#
# print('before:', a.grad, b.grad, c.grad)
# grads = autograd.grad(y, [a, b, c])
# print('after :', grads[0], grads[1], grads[2])