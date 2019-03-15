# -*- coding:UTF-8 -*-
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt


class MLFastLearn(object):
    def __init__(self):
        pass

    def newton(self, x0, niter, threshold, f, fgrad):
        """
        Newton method to find solve to f(x)
        """
        iter = 0
        while niter > 0:
            # print(f(x0))
            # print(fgrad(x0))
            # print(f(x0) / fgrad(x0))
            x1 = x0 - f(x0) / fgrad(x0)
            if f(x1) < threshold:
                break
            x0 = x1
            iter += 1
            print(str(iter) + " x= " + str(x1))
            niter -= 1
        return x1

    def biSection(self, a, b, threshold, f):
        """
        bisection to find solve to f(x) when x in (a,b) and f(a)*f(b)<0
        """
        iter = 0
        while a < b:
            mid = a + abs(b - a) / 2.0
            if abs(f(mid)) < threshold:
                return mid
            if f(mid) * f(b) < 0:
                a = mid
            if f(a) * f(mid) < 0:
                b = mid
            iter += 1
            print(str(iter) + " a= " + str(a) + ", b= " + str(b))

    def binomial(self):
        # 计算组合数
        # 二项分布概率计算公式
        def getp(m, n, pa):
            if m < n:
                return 0.0
            return comb(m, n) * (pa ** n) * ((1 - pa) ** (m - n))

        # 获得画图数据
        klist = np.arange(21)
        plist = [getp(m=20, n=k, pa=0.75) for k in klist]
        plt.plot(klist, plist)
        plt.xlabel('number of good apples')
        plt.ylabel('k-distribution proba')
        plt.title('distribution proba')
        plt.xticks(np.arange(0, 22, 1))
        plt.grid()
        plt.show()

    def gaussian(self):
        # 均值
        def average(data):
            return np.sum(data) / len(data)

        # 标准差
        def sigma(data, avg):
            sigma_squ = np.sum(np.power((data - avg), 2)) / len(data)
            return np.power(sigma_squ, 0.5)

        # gaussian-distribution prob
        def prob(data, avg, sig):
            sqrt_2pi = np.power(2 * np.pi, 0.5)
            coef = 1 / (sqrt_2pi * sig)
            powcoef = -1 / (2 * np.power(sig, 2))
            mypow = powcoef * (np.power((data - avg), 2))
            return coef * (np.exp(mypow))

        # 样本数据
        data = np.array([0.79, 0.78, 0.8, 0.79, 0.77, 0.81, 0.74, 0.85, 0.8,
                         0.77, 0.81, 0.85, 0.85, 0.83, 0.83, 0.8, 0.83, 0.71,
                         0.76, 0.8])
        # 根据样本求高斯分布的平均数
        ave = average(data)
        print(ave)
        # 根据样本求高斯分布的标准差
        sig = sigma(data, ave)
        # 拿到数据
        x = np.arange(0.5, 1.0, 0.01)
        p = prob(x, ave, sig)
        # 绘制函数
        plt.plot(x, p)
        plt.grid()
        plt.xlabel('apple quality factor')
        plt.ylabel('prob density')
        plt.yticks(np.arange(0, 12, 1))
        plt.title('Gaussian distribution')
        plt.show()

    def norm_tour(self):
        # 定义L1正则化项
        def L1(w1, w2):
            return np.abs(w1) + np.abs(w2)
            # 定义L2正则化项

        def L2(w1, w2):
            return (w1 ** 2 + w2 ** 2)

        # 数据数目
        n = 256
        # 定义x, y
        x = np.linspace(-2, 2, n)
        y = np.linspace(-2, 2, n)
        # 生成网格数据
        X, Y = np.meshgrid(x, y)
        # 填充等高线的颜色, 6是等高线分为几部分
        plt.contourf(X, Y, L2(X, Y), 6, alpha=0.75, cmap=plt.cm.hot)
        # C = plt.contour(X, Y, L2(X, Y), 6, colors = 'black', linewidth = 0.2)
        plt.show()


if __name__ == '__main__':
    ml = MLFastLearn()

    # nt = ml.newton(50, 100, 1e-10, lambda x: x * x - 11 * x + 10, lambda x: 2 * x - 11)
    # print("solve= " + str(nt))

    # bs = ml.biSection(5, 50, 1e-10, lambda x: x * x - 11 * x + 10)
    # print("solve= " + str(bs))

    # ml.binomial()

    # ml.gaussian()

    # ml.norm_tour()

    ml.dt_regression()