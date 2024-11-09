class Solution:
    def minEnd(self, array_len: int, x: int) -> int:
        target_xor = bin(x)[2:]
        target_xor_list = list(target_xor)
        array_len-=1
        num_binary_representation_list = list(bin(array_len)[2:])
        for i in range(len(target_xor_list)-1,-1,-1):

                if target_xor_list[i]=="0":
                    if len(num_binary_representation_list)==0:
                        break
                    target_xor_list[i]=num_binary_representation_list.pop()
        if len(num_binary_representation_list)==0:
            return int("".join(target_xor_list),base=2)
        else:
            return int("".join(num_binary_representation_list)+"".join(target_xor_list),base=2)
#         target_xor = bin(x)[2:]
        
#         zero_bit_count_in_xor = target_xor.count("0")
        
#         # t = 
#         if 2**zero_bit_count_in_xor>=array_len:
#             # array_len-=1
# #             then answer will be within the given number of bits
#             target_xor_list = list(target_xor)
#             # num_binary_representation =  
#             num_binary_representation_list = list(bin(array_len-1)[2:])
#             # print(target_xor_list,num_binary_representation_list)
#             for i in range(len(target_xor_list)-1,-1,-1):

#                 if target_xor_list[i]=="0":
#                     if len(num_binary_representation_list)==0:
#                         break
#                     target_xor_list[i]=num_binary_representation_list.pop()
#             # print("testing",target_xor_list)
#             return int("".join(target_xor_list),base=2)
#         else:
#             array_len -= 2**zero_bit_count_in_xor # reduce the same bit ones
#             # then find the prefix of bits
#             return int(bin(array_len)[2:]+target_xor,base=2)
#         # print(s)
#         # return 3
"""
4,2 ->7
10
10,11,110,111
10->
"""