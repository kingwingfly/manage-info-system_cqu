MEMBERS = ["王翼翔", "谭涵", "伍洛欧", "吴樱", "杨宇轩", "张蕴泽", "李可馨"]
TOTAL = 100

def verify_contribute(cs: list[dict[str, float]]) -> bool:
    return all(sum(c.values()) == 1 for c in cs) & all(set(c.keys()).issubset(MEMBERS) for c in cs)

def score(W: list[int], C: list[dict[str, float]]) -> dict[str, float]:
    return {m: TOTAL * sum(W[i] * c.get(m, 0) for i, c in enumerate(C)) for m in MEMBERS}

if __name__ == "__main__":
    W = [1]
    C = [
        # {"王翼翔": 0, "谭涵": 0, "伍洛欧": 0, "吴樱": 0, "杨宇轩": 0, "张蕴泽": 0, "李可馨": 0}
        {"王翼翔": 0.2, "谭涵": 0.2, "吴樱": 0.2, "杨宇轩": 0.4}, # 作业1贡献权重
    ]
    if verify_contribute(C):
        print("Contribution Verified.")
        print(score(W, C))
    else:
        print("Invalid Contribution.")