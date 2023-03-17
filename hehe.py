import paddle
import numpy as np

data = paddle.randn([1000000, 10000]) # 创建一个 1000000 x 10000 的张量
while True:
    _ = data.numpy() # 重复使用张量，占用显存
