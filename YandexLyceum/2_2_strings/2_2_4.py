a = "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
b = '1234567890@#–—$_&-+()/*":;!?,.~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]<> '
number = int(input())
shifr = str(input())
total = 0
for i in range(len(shifr)):
    for j in range(len(a)):
        if shifr[i] == a[j]:
            j += number + number
            if j > 64:
                j = j - 64
                print(a[j], end="")
            else:
                print(a[j], end="")
    else:
        if shifr[i] in b:
            print(shifr[i], end="")