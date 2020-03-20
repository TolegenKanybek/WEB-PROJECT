def catDog(str):
    cat_cnt = 0
    dog_cnt = 0
        for i in range(len(str)-2):
            if "cat"== str[i:i + 3]:
                cat_cnt=cat_cnt+1
            if "dog"==str[i:i + 3]:
                dog_cnt=dog_cnt+1
        return cat_cnt == dog_cnt


cat_dog('catdog')
    