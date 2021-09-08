import torch
from torch import nn
from torch.nn import functional as F


# 纯 focal loss 没有 alpha 只有 gamma，论文中说加了 alpha 稍好一点

class BinaryFocalLoss(torch.nn.Module):

    def __init__(self, gamma=2, reduction='mean'):
        super(BinaryFocalLoss, self).__init__()

        self.gamma = gamma
        self.reduction = reduction

    def forward(self, predict, target):
        p = torch.sigmoid(predict)  # sigmoid获取概率
        loss = - (1 - p) ** self.gamma * target * torch.log(p) \
               - p ** self.gamma * (1 - target) * torch.log(1 - p)

        if self.reduction == 'mean':
            loss = torch.mean(loss)
        elif self.reduction == 'sum':
            loss = torch.sum(loss)
        return loss


class BinaryFocalLossWithAlpha(torch.nn.Module):

    def __init__(self, gamma=2, alpha=0.25, reduction='mean'):
        super(BinaryFocalLossWithAlpha, self).__init__()

        self.gamma = gamma
        self.alpha = alpha
        self.reduction = reduction

    def forward(self, predict, target):
        p = torch.sigmoid(predict)  # sigmoid获取概率
        # 在原始ce上增加动态权重因子，注意alpha的写法，下面多类时不能这样使用
        loss = - self.alpha * (1 - p) ** self.gamma * target * torch.log(p) \
               - (1 - self.alpha) * p ** self.gamma * (1 - target) * torch.log(1 - p)

        if self.reduction == 'mean':
            loss = torch.mean(loss)
        elif self.reduction == 'sum':
            loss = torch.sum(loss)
        return loss


class FocalLoss(nn.Module):

    def __init__(self, gamma=2, reduction='mean'):
        super(FocalLoss, self).__init__()

        self.reduction = reduction
        self.gamma = gamma

    def forward(self, predict, labels):
        """
        :param predict:   预测类别. size:[B,N,C] or [B,C]  分别对应与检测与分类任务, B 批次, N检测框数, C类别数
        :param labels:  实际类别. size:[B,N] or [B]
        """
        predict = predict.view(-1, predict.size(-1))  # B (* N) * C

        p = F.softmax(predict, dim=1)
        p = p.gather(1, labels.view(-1, 1))  # gather()相当于label是几，就取向量里的第几个

        # -(1-pt)**γ * log(pt)
        loss = -torch.mul(torch.pow((1 - p), self.gamma), torch.log(p))

        if self.reduction == 'mean':
            loss = torch.mean(loss)
        elif self.reduction == 'sum':
            loss = torch.sum(loss)
        return loss


class FocalLossWithAlpha(nn.Module):

    def __init__(self, alpha=0.25, gamma=2, num_classes=2, reduction='mean'):
        super(FocalLossWithAlpha, self).__init__()

        self.reduction = reduction
        self.gamma = gamma

        if isinstance(alpha, list):
            assert len(alpha) == num_classes  # α 可以以 list 方式输入，每个值对应不同类别的权重
            self.alpha = torch.Tensor(alpha)
        else:
            assert alpha < 1  # 如果α为一个常数，则降低第一类的影响，在目标检测中为第一类
            self.alpha = torch.zeros(num_classes)
            self.alpha[0] += alpha
            self.alpha[1:] += (1 - alpha)  # α 最终为 [ α, 1-α, 1-α, 1-α, 1-α, ...] size:[num_classes]

    def forward(self, predict, labels):
        """
        :param predict:   预测类别. size:[B,N,C] or [B,C]    分别对应与检测与分类任务, B 批次, N检测框数, C类别数
        :param labels:  实际类别. size:[B,N] or [B]
        """

        predict = predict.view(-1, predict.size(-1))  # B (* N) * C

        p = F.softmax(predict, dim=1)
        p = p.gather(1, labels.view(-1, 1))  # gather()相当于label是几，就取向量里的第几个

        # -(1-pt)**γ * log(pt)
        loss = -torch.mul(torch.pow((1 - p), self.gamma), torch.log(p))

        self.alpha = self.alpha.to(predict.device)
        self.alpha = self.alpha.gather(0, labels.view(-1))
        loss = torch.mul(self.alpha, loss.t())

        if self.reduction == 'mean':
            loss = torch.mean(loss)
        elif self.reduction == 'sum':
            loss = torch.sum(loss)
        return loss
