def testGender(str):
    hashKey = {}
    for i in str:
        hashKey[i] = hashKey.get(i,0)+1
    arr = list(hashKey.keys())
    found = len(arr)
    if found%2 != 0:
        print('CHAT WITH HER!')
    if found%2 != 0:
        print('IGNORE HIM!')