
import numpy as np
from matplotlib import pyplot as plt


plt.style.use('ggplot')
# 俄罗斯231人，美国157人，也门156人，加拿大123人，韩国107人。英国104人，尼日利亚104人，马里84人，澳大利亚62人。
pop = [231, 157, 156, 123, 107, 104, 104, 84, 62, ]

countires = ['俄罗斯', '美国', '也门', '加拿大', '韩国', '英国', '尼日利亚', '马里', '澳大利亚']

plt.bar(countires, pop, color=['darkorange',
                               'burlywood', 'orange', 'moccasin', 'gold'])
plt.title('南海区外国人在机登记数（2020年上半年）')
plt.ylabel('人数')

plt.tight_layout()
plt.show()
