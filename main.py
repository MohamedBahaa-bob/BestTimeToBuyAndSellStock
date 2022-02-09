# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maxProfit(self, prices) -> int:
        i = 0
        j = 1
        res = 0
        while j < len(prices):
            if prices[j] - prices[i] >= res:
                res = prices[j] - prices[i]
                j += 1
            else:
                if prices[j] < prices[i]:
                    i = j
                    j += 1
                else:
                    j += 1
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfit([7, 6, 4, 3, 1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
