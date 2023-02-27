import paddle
import numpy as np

data = paddle.randn([1000000, 15000]) # 创建一个 1000000 x 1000 的张量
while True:
    _ = data.numpy() # 重复使用张量，占用显存
