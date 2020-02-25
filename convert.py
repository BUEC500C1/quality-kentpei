def convert_num(num):
        #dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',
        #10:'X',9:'IX',5:'V',4:'IV'}
        if not isinstance(num, int):
            return "Wrong Type"
        if num <= 0 or num >= 4000:
            return "illegal input"
        dic = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
                [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
                [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
                [   1, 'I']]
        str = ''
        i = 0
        while num > 0:
            while dic[i][0] > num:
                i += 1
            str += dic[i][1]
            num -= dic[i][0]
        return str
'''
if __name__ == "__main__":
    s = Solution()
    print(s.convert(4393))
'''
