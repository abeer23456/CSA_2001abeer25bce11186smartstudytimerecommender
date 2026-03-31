import pandas as pd
from sklearn.tree import DecisionTreeRegressor

a = 0
b = 0
c = 0
d = 0
allresults = []

def makedata():
    info = {
        "difficulty": [1,2,3,4,5,5,4,3,2,1,5,4,2,3,1,4,5,3,2,4],
        "daysleft": [15,12,10,7,3,2,5,8,14,20,1,4,11,6,18,9,2,7,13,5],
        "preparation": [5,4,3,2,1,2,3,4,5,4,1,2,4,3,5,2,1,3,4,2],
        "importance": [1,2,3,4,5,5,4,3,2,1,5,4,2,3,1,4,5,3,2,4],
        "studyhours": [1,2,4,7,12,11,8,5,2,1,13,9,3,6,1,8,12,5,2,7]
    }
    return pd.DataFrame(info)

def trainit(df):
    x = df[["difficulty","daysleft","preparation","importance"]]
    y = df["studyhours"]
    model = DecisionTreeRegressor(random_state=42)
    model.fit(x, y)
    return model

def asknum(msg, low, high):
    while True:
        try:
            val = int(input(msg))
            if low <= val <= high:
                return val
            else:
                print("enter number between", low, "and", high)
        except:
            print("wrong input try again")

def fixhours(h, days, prep):
    if days <= 3:
        h = h + 1
    if prep >= 4:
        h = h - 0.5
    if h < 1:
        h = 1
    return round(h, 2)

def getpriority(h):
    if h <= 2:
        return "Low"
    elif h <= 5:
        return "Moderate"
    elif h <= 8:
        return "High"
    else:
        return "Very high"

def gettip(p):
    if p == "Very high":
        return "start now revise daily"
    elif p == "High":
        return "focus more on this"
    elif p == "Moderate":
        return "keep studying regularly"
    else:
        return "light revision ok"

def predictit(model, a, b, c, d):
    test = pd.DataFrame({
        "difficulty": [a],
        "daysleft": [b],
        "preparation": [c],
        "importance": [d]
    })
    out = model.predict(test)[0]
    out = fixhours(out, b, c)
    return out

def showall(stuff):
    table = pd.DataFrame(stuff)
    table = table.sort_values(by="Study time in hours", ascending=False)

    print("\n" + "="*80)
    print("Final study plan")
    print("="*80)
    print(table.to_string(index=False))
    print("="*80)

    total = table["Study time in hours"].sum()
    print("\nTotal time needed:", round(total,2), "hours")

print("="*50)
print("Smart study recommender")
print("="*50)

df = makedata()
model = trainit(df)

n = asknum("enter number of subjects ", 1, 20)

for i in range(1, n+1):
    print("\nsubject", i)
    print("-"*30)

    sub = input("enter subject name ").strip()
    a = asknum("difficulty 1-5 ", 1, 5)
    b = asknum("days left 1-30 ", 1, 30)
    c = asknum("prep level 1-5 ", 1, 5)
    d = asknum("importance 1-5 ", 1, 5)

    hrs = predictit(model, a, b, c, d)
    p = getpriority(hrs)
    tip = gettip(p)

    allresults.append({
        "Subject": sub,
        "Difficulty": a,
        "Days left": b,
        "Preparation": c,
        "Importance": d,
        "Study time in hours": hrs,
        "Priority": p,
        "Advice": tip
    })

showall(allresults)
