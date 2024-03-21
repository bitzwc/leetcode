class Gift:
    def getValue(self, gifts, n):
        hongbao={}
        for h in gifts:
            if h in hongbao.keys():
                hongbao[h]=hongbao[h]+1
            else:
                hongbao[h]=1
        print hongbao
        result={value:key for key,value in hongbao.items()}
        print result
        r=max(result.keys())
        if r>n/2.0:
            return result[r]
        else:
            return 0

