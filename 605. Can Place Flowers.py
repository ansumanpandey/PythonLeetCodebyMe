class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        if(len(flowerbed)>2):
            if(flowerbed[0]==0 and flowerbed[1]==0):
                flowerbed[0]=1
                cnt=cnt+1
            if(flowerbed[-1]==0 and flowerbed[-2]==0):
                flowerbed[-1]=1
                cnt=cnt+1
            for i in range(1,(len(flowerbed)-1)):       
                if (flowerbed[i]==0):
                    if(flowerbed[i+1]!=1 and flowerbed[i-1]!=1):
                        cnt=cnt+1
                        flowerbed[i]=1
        else:
            if(len(flowerbed)==1 and flowerbed[0]==0):
                cnt=cnt+1
            if(len(flowerbed)==2 and flowerbed[0]==0 and flowerbed[1]==0):
                cnt=cnt+1
        if(cnt>=n):
            return True
        else:
            return False


