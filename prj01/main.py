scores = [80, 85, 70, 90]
# temp =[]
# for x in scores:
#     temp.append(x+5)
# scores=temp

total=0
for x in scores:
    total +=x
    avg=total/len(scores)
print(total)
print(avg)