# -*- coding: utf-8 -*-

#基数排序（radix sort）属于“分配式排序”（distribution sort），
# 又称“桶子法”（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，
# 将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，
# 其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，
# 基数排序法的效率高于其它的稳定性排序法。

# stable


class RadixSort(object):
    def radixsort(self, list, d):
        for k in xrange(d):  # d轮排序
            s = [[] for i in xrange(10)]  # 因为每一位数字都是0~9，故建立10个桶
            '''对于数组中的元素，首先按照最低有效数字进行
               排序，然后由低位向高位进行。'''
            for i in list:
                '''对于3个元素的数组[977, 87, 960]，第一轮排序首先按照个位数字相同的
                   放在一个桶s[7]=[977],s[7]=[977,87],s[0]=[960]
                   执行后list=[960,977,87].第二轮按照十位数，s[6]=[960],s[7]=[977]
                   s[8]=[87],执行后list=[960,977,87].第三轮按照百位，s[9]=[960]
                   s[9]=[960,977],s[0]=87,执行后list=[87,960,977],结束。'''
                s[i / (10 ** k) % 10].append(i)  # 977/10=97(小数舍去),87/100=0
            list = [j for i in s for j in i]
        return list


if __name__ == "__main__":
    lists = [32,12,24,242,44]
    print RadixSort().radixsort(lists,3)
