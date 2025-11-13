import pandas as pd

def load_test_cases(path):
    df = pd.read_csv(path, encoding="utf-8-sig")
    data = []
    for _, row in df.iterrows():
        data.append((
            row["TC_ID"],
            row["테스트_케이스명"],
            row["설명"],
            row["사전조건"],
            row["테스트_절차"],
            row["기대_결과"],
            row["테스트_데이터"],
            row["우선순위"],
            row["자동화"]
        ))
    return data
