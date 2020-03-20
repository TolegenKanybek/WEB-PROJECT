def xyzThere(str):
        result = False
        for i in range(len(str)-2):
            if "xyz"==str[i:i + 3]:
                if i == 0 or str[i - 1] != '.':
                    return True
        return result
    

    xyz_there('abcxyz')