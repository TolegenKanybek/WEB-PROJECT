def countCode(str):
        count = 0
        for i in range(len(str)-3):
            if "co"==str[i: i + 2]:
                if str[i + 3] == 'e':
                    count=count+1
        return count


count_code('aaacodebbb')

    