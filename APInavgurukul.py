def sort_by_assending_desending():
    import requests
    import json
    # from pprint import pprint

    f=requests.get('https://join.navgurukul.org/api/partners')
    s=json.loads(f.text)
    with open("requts.json","w") as l:
        json.dump(s,l,indent=4)
    #   print(s) 
        l=[]
        for i in s:
            for j in s[i]:
                l.append(j["id"])
        print(l)
        list1=[]
        if user=="1":
            l.sort()
            print(l)


    with open("sort_id.json","w")as f:
        json.dump(list1,f,indent=4)

print("if you want to asending order press[1] and you want to desending order press[2]")
user=input("enter the choice:")
sort_by_assending_desending()
        
