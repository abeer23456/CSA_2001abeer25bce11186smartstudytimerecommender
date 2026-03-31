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
                print("enter a number between", low, "and", high)
        except:
            print("invalid input try again")

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
        return "Very High"

def gettip(p):
    if p == "Very High":
        return "Start immediately and revise daily."
    elif p == "High":
        return "Give this subject strong focus."
    elif p == "Moderate":
        return "Maintain regular study sessions."
    else:
        return "Light revision should be enough."

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
    table = table.sort_values(by="Recommended Study Time (hours)", ascending=False)

    print("\n" + "="*95)
    print("FINAL STUDY PLAN")
    print("="*95)
    print(table.to_string(index=False))
    print("="*95)

    total = table["Recommended Study Time in hours"].sum()
    print("\nTotal recommended study time for all subjects:", round(total,2), "hours")

print("="*60)
print("SMART STUDY TIME RECOMMENDER")
print("="*60)

df = makedata()
model = trainit(df)

n = asknum("enter the number of subjects ", 1, 20)

for i in range(1, n+1):
    print("\nentering details for subject", i)
    print("-"*40)

    sub = input("enter subject name ").strip()
    a = asknum("enter subject difficulty from 1 to 5  ", 1, 5)
    b = asknum("enter days left before exam (1-30) ", 1, 30)
    c = asknum("enter preparation level from 1 to 5  ", 1, 5)
    d = asknum("enter subject importance from 1 to 5 ", 1, 5)

    hrs = predictit(model, a, b, c, d)
    p = getpriority(hrs)
    tip = gettip(p)

    allresults.append({
        "Subject": sub,
        "Difficulty": a,
        "Days Left": b,
        "Preparation": c,
        "Importance": d,
        "Recommended Study Time (hours)": hrs,
        "Priority": p,
        "Advice": tip
    })

showall(allresults)
