import pandas as pd

# Baca data kuesioner
df = pd.read_csv("data.csv")

# Ambil kolom pertanyaan Q1 - Q17
questions = [f"Q{i}" for i in range(1, 18)]
total_respon = df[questions].size

# Mapping skor
scale_score = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

target_question = input().lower()

if target_question == "q1":
    counts = df[questions].stack().value_counts()
    scale = counts.idxmax()
    count = counts.max()
    percent = round(count / total_respon * 100, 1)
    print(f"{scale}|{count}|{percent}")

elif target_question == "q2":
    counts = df[questions].stack().value_counts()
    scale = counts.idxmin()
    count = counts.min()
    percent = round(count / total_respon * 100, 1)
    print(f"{scale}|{count}|{percent}")

elif target_question == "q3":
    result = df[questions].apply(lambda x: (x == "SS").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q4":
    result = df[questions].apply(lambda x: (x == "S").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q5":
    result = df[questions].apply(lambda x: (x == "CS").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q6":
    result = df[questions].apply(lambda x: (x == "CTS").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q7":
    result = df[questions].apply(lambda x: (x == "TS").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q8":
    result = df[questions].apply(lambda x: (x == "STS").sum())
    q = result.idxmax()
    count = result.max()
    percent = round(count / len(df) * 100, 1)
    print(f"{q}|{count}|{percent}")

elif target_question == "q9":
    result = []
    for q in questions:
        count = (df[q] == "STS").sum()
        if count > 0:
            percent = round(count / len(df) * 100, 1)
            result.append(f"{q}:{percent}")
    print("|".join(result))

elif target_question == "q10":
    scores = df[questions].replace(scale_score)
    avg = scores.stack().mean()
    print(f"{avg:.2f}")

elif target_question == "q11":
    scores = df[questions].replace(scale_score)
    avg = scores.mean()
    q = avg.idxmax()
    print(f"{q}:{avg.max():.2f}")

elif target_question == "q12":
    scores = df[questions].replace(scale_score)
    avg = scores.mean()
    q = avg.idxmin()
    print(f"{q}:{avg.min():.2f}")

elif target_question == "q13":
    data = df[questions].stack()
    positif = data.isin(["SS", "S"]).sum()
    netral = (data == "CS").sum()
    negatif = data.isin(["CTS", "TS", "STS"]).sum()

    p_pos = round(positif / total_respon * 100, 1)
    p_net = round(netral / total_respon * 100, 1)
    p_neg = round(negatif / total_respon * 100, 1)

    print(f"positif={positif}:{p_pos}|netral={netral}:{p_net}|negatif={negatif}:{p_neg}")
