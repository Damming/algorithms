def dice_loss(input, targets, epsilon=1e-6):
    N = targets.size()[0]

    input = input.view(N, -1)
    targets = targets.view(N, -1)

    intersection = input * targets
    dice = (2 * intersection.sum(1) + epsilon) / (input.sum(1) + targets.sum(1) + epsilon)

    loss = 1 - dice.sum() / N
    return loss
