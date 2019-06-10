from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

path = "F:\\Deep\\Images_png\\004236_01_02\\193.png"

img = misc.imread(path)
ori_img = (img-32768)
ori_img = np.array(ori_img).astype(np.float32)
ori_img_n = (ori_img-np.min(ori_img))/(np.max(ori_img)-np.min(ori_img))
# plt.imshow(ori_img_n)
# plt.title('image')  # 
# plt.show()

misc.imsave('New_CT.png', ori_img_n)