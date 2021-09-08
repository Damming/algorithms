"""
基于numpy 实现的 非极大值抑制 NMS
"""
import numpy as np


def py_cpu_nms(dets, thresh):
    """
    nms
    :param dets: ndarray [x1,y1,x2,y2,score]
    :param thresh: int
    :return: list[index]
    """
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    order = dets[:, 4].argsort()[::-1]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    keep = []
    while order.size > 0:
        i = order[0]  # 选出概率最大的
        keep.append(i)

        # 交集的坐标
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        #  交集的长宽
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        iou = (w * h) / (area[i] + area[order[1:]] - w * h)
        index = np.where(iou <= thresh)[0]
        
        order = order[index + 1]  # 取交集坐标时没算第0个，这里index补一下
    return keep


dets = np.array([[100, 200, 300, 400, 0.8],
                 [150, 200, 350, 450, 0.9],
                 [100, 400, 150, 500, 0.4]])
keep = py_cpu_nms(dets, 0.5)
print(dets[keep])

