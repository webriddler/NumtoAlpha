#!/usr/bin/env python
# coding: utf-8

# # *Num - Alpha* 

# In[8]:


num=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens=["Ten","Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
wrd=""
r=1
numeric_data=input("Enter the Number : ")
if numeric_data.isdigit() is True:
    if numeric_data[0]!="0":
        if len(numeric_data)==7:
            if numeric_data[0]=="1":
                wrd+=tens[int(numeric_data[1])]+ " Lakhs "
                numeric_data=numeric_data[2::]
                while int(numeric_data[0])==0 and r<5:
                    numeric_data=numeric_data[1::]
                    r=r+1
            else:
                wrd+=nty[int(numeric_data[0])]+ " "+num[int(numeric_data[1])] + " Lakhs "
                numeric_data=numeric_data[2::]
                while int(numeric_data[0])==0 and r<5:
                    numeric_data=numeric_data[1::]
                    r=r+1
        if len(numeric_data)==6:
            wrd+=num[int(numeric_data[0])]+ " Lakhs "
            numeric_data=numeric_data[1::]
            while int(numeric_data[0])==0 and r<5:
                numeric_data=numeric_data[1::]
                r=r+1
        if len(numeric_data)==5:
            if numeric_data[0]=="1":
                wrd+=tens[int(numeric_data[1])]+ " Thousand "
                numeric_data=numeric_data[2::]
            else:
                wrd+=nty[int(numeric_data[0])]+ " "+num[int(numeric_data[1])] + " Thousand "
                numeric_data=numeric_data[2::]
        if len(numeric_data)==4:
            wrd+=num[int(numeric_data[0])]+" Thousand "
            numeric_data=numeric_data[1::]
        if len(numeric_data)==3:
            if numeric_data[0]!="0":
                wrd+=num[int(numeric_data[0])]+" Hundred "
                numeric_data=numeric_data[1::]
            else:
                numeric_data=numeric_data[1::]
        if len(numeric_data)<=2:
            if len(numeric_data)==1:
                wrd+=num[int(numeric_data)]
            elif int(numeric_data)<20:
                if numeric_data[0]=="0":
                    wrd+=num[int(numeric_data[1])]
                else:
                    wrd+=tens[int(numeric_data[1])]
            else:
                wrd+=str(nty[int(numeric_data[0])])+" "+str(num[int(numeric_data[1])])
        else:
            print("Only upto 9999999")
    else:
        print("Zero at First place is not Acceptable")

else:
    print('Not a Number Try Again !')
print(wrd)

