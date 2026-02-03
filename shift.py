from ortools.sat.python import cp_model

# モデル作成
model = cp_model.CpModel()

# スタッフと日数
staff = ['A', 'B', 'C']
days = range(7)

# 夜勤の例（Trueなら夜勤）
night_shift = ['A']  # 夜勤担当者例

# 変数: staff s が day d に勤務するか
# NewVoolVarは0と1だけの変数を取るためのもの　model.newBoolvar(name)nameはラベル
work = {}
for s in staff:
    for d in days:
        work[(s,d)] = model.NewBoolVar(f'{s}_day{d}')

# 制約1: 1日に必要な人数
for d in days:
    if d in [5,6]:  # 土日d == 5 or d == 6の意味　inは5か6がdの中に含まれているか　sumは合計している
        # pythonは配列番号は文字でもよい、文字指定していて、boolvarでラベリングの文字が入っている
        model.Add(sum(work[(s,d)] for s in staff) >= 2)
    else:
        model.Add(sum(work[(s,d)] for s in staff) >= 1)

# 制約2: 連続勤務は最大5日
# range(n)で0からn-1を返す
for s in staff:
    for start_day in range(len(days) - 5):
        model.Add(sum(work[(s,start_day + i)] for i in range(6)) <= 5)

# 制約3: 夜勤の翌日は休み
# .OnlyEnforceIf(work[(s,d)])が1の時にmodel.Add(work[(s,d+1)] == 0)を適用する　明示的にOnlyEnforceIf(work[(s,d)]==1)
# if分はまだ値が確定していないので無理
for s in night_shift:
    for d in range(len(days)-1):
        model.Add(work[(s,d+1)] == 0).OnlyEnforceIf(work[(s,d)])

# 制約4: 希望シフト（例: Aは火曜(1)と木曜(3)に働きたい）
preferred = {('A',1), ('A',3)}
for s,d in preferred:
    # できれば働くように目的関数で加点
    pass  # 後で目的関数に組み込み

# 目的関数: 希望勤務を最大化
model.Maximize(sum(work[(s,d)] for s,d in preferred))

# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

# | 定数                       | 意味                     |
# | ------------------------ | ---------------------- |
# | `cp_model.OPTIMAL`       | 制約を満たす **最適解** が見つかった  |
# | `cp_model.FEASIBLE`      | 制約を満たす **解はあるが最適かは不明** |
# | `cp_model.INFEASIBLE`    | 解なし（制約が矛盾している）         |
# | `cp_model.MODEL_INVALID` | モデルの書き方が間違っている         |


if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    # end=""で改行せずに出力
    for d in days:
        print(f"Day {d}: ", end="")
        for s in staff:
            if solver.Value(work[(s,d)]):
                print(s, end=" ")
        print()
else:
    print("解なし")
