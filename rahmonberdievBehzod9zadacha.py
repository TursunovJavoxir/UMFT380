def process_numbers(a,b,c):
    if(a<b<c) or (a>b>c):
        return a*2, b*2, c*2
    else:
        return -a, -b, -c