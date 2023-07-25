class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        list1, list2 = [],[]

        for i in arr2:
            for j in arr1:
                if i == j : list1.append(i)

        for i in arr1:
            if i not in arr2: list2.append(i)
        
        list2.sort()

        return list1 + list2