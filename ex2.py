def interest_year(p,r,n):
    return p*(1+r)**n


p=30000000
r=0.051
n=3

result = interest_year(p,r,n)
print('총액: {0}, 원금:{1}, 이자:{2}'.format(result,p,result-p))
print('총액: %0.2f, 원금:%d, 이자:%0.2f'%(result,p,result-p))
