# def bin32(num):
#     return '{:032b}'.format(num)[::-1]

# a=int(input())
# ans=[]
# while(a):
#     ans.append(str(int(bin32(a),2)))
#     try:
#         a=int(input())
#     except:
#         a=0
# print(",".join(ans))

def bin32(num):
    return '{:032b}'.format(num)[::-1]

a=11
ans=[]
while(a):

    try:
        a=int(input())
        if a:
            ans.append(str(int(bin32(a),2)))
        else:
            break
    except:
        break
print(",".join(ans))

