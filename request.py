# from tkinter import E


def sort_by_assending_desending():
    import requests
    import json
    # from pprint import pprint

    f=requests.get('https://join.navgurukul.org/api/partners')
    a=json.loads(f.text)
    with open("requts.json","w") as l:
        json.dump(a,l,indent=4)
    # print(s) 
        l=[]
        for i in a:
            for j in a[i]:
                l.append(j["id"])
        # print(l)
        list1=[]
        if user=="1":
            l.sort()
            # print(l)
            for i in l:
                # print(i)
                for j in a:
                    for k in a[j]:
                        for p in k:
                            # print(p)
                            if p=="id":
                                if i==k[p]:
                                    list1.append(k)
                                    print(k)

        elif user=="2":
            l.sort(reverse=True)
            # print(l)
            for i in l:
                for j in a:
                    for k in a[j]:
                        for p in k:
                            # print((p))
                            if p=="id":
                                if i==k[p]:
                                    list1.append(k)
        with open("sort_id.json","w")as f:
            json.dump(list1,f,indent=4)

print("if you want to asending order press[1] and you want to desending order press[2]")
user=input("enter the choice:")
sort_by_assending_desending()
        


