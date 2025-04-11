# utils.py
import pandas as pd
import plotly.graph_objects as go
from config import SIMULATION_CONFIG

def calculate_simulation_data(remaining_years, value_salary, value_learning, value_job_satisfaction, 
                              stress_health, stress_rest, stress_financial, 
                              wage_peak_years, wage_peak_reduction, 
                              health_increase_rate, rest_increase_rate, 
                              financial_increase_rate, learning_increase_rate):
    years = list(range(2025, 2025 + remaining_years))
    data = {
        "연도": [],
        "가치 합계": [],
        "스트레스 합계": [],
        "내 최적화 점수": [],
    }

    current_salary = value_salary
    current_learning = value_learning
    current_job_satisfaction = value_job_satisfaction
    current_health = stress_health
    current_rest = stress_rest
    current_financial_stress = stress_financial

    # max_learning 동적으로 설정
    max_learning = max(value_learning, 5.0)

    for i in range(remaining_years):
        year = 2025 + i
        if i >= remaining_years - wage_peak_years:
            current_salary = value_salary * (1 - wage_peak_reduction / 100)
        else:
            current_salary = value_salary

        current_learning = min(value_learning + (i * learning_increase_rate), max_learning)
        current_job_satisfaction = value_job_satisfaction
        current_health = min(stress_health + (i * health_increase_rate), SIMULATION_CONFIG["max_stress"])
        current_rest = min(stress_rest + (i * rest_increase_rate), SIMULATION_CONFIG["max_stress"])
        current_financial_stress = min(stress_financial + (i * financial_increase_rate), SIMULATION_CONFIG["max_stress"])

        total_value = (current_salary + current_learning + current_job_satisfaction)
        total_stress = (current_health + current_rest + current_financial_stress)

        optimization_score = total_value / total_stress if total_stress != 0 else 0

        data["연도"].append(year)
        data["가치 합계"].append(round(total_value, 2))
        data["스트레스 합계"].append(round(total_stress, 2))
        data["내 최적화 점수"].append(round(optimization_score, 2))

    return pd.DataFrame(data)

def analyze_trends(df):
    # 연도별 변화율 계산
    value_changes = []
    stress_changes = []
    optimization_changes = []

    for i in range(1, len(df)):
        # 가치 합계 변화율
        prev_value = df["가치 합계"].iloc[i-1]
        curr_value = df["가치 합계"].iloc[i]
        value_change = (curr_value - prev_value) / prev_value * 100 if prev_value != 0 else 0
        value_changes.append((df["연도"].iloc[i], value_change))

        # 스트레스 합계 변화율
        prev_stress = df["스트레스 합계"].iloc[i-1]
        curr_stress = df["스트레스 합계"].iloc[i]
        stress_change = (curr_stress - prev_stress) / prev_stress * 100 if prev_stress != 0 else 0
        stress_changes.append((df["연도"].iloc[i], stress_change))

        # 최적화 점수 변화율
        prev_opt = df["내 최적화 점수"].iloc[i-1]
        curr_opt = df["내 최적화 점수"].iloc[i]
        opt_change = (curr_opt - prev_opt) / prev_opt * 100 if prev_opt != 0 else 0
        optimization_changes.append((df["연도"].iloc[i], opt_change))

    # 전체 추이 분석
    value_trend = "가치 합계는 시뮬레이션 기간 동안 대체로 증가하는 경향을 보입니다." if sum(c[1] for c in value_changes) > 0 else "가치 합계는 시뮬레이션 기간 동안 대체로 감소하는 경향을 보입니다."
    stress_trend = "스트레스 합계는 시뮬레이션 기간 동안 대체로 증가하는 경향을 보입니다." if sum(c[1] for c in stress_changes) > 0 else "스트레스 합계는 시뮬레이션 기간 동안 대체로 감소하는 경향을 보입니다."
    opt_trend = "최적화 점수는 시뮬레이션 기간 동안 대체로 감소하는 경향을 보입니다." if sum(c[1] for c in optimization_changes) < 0 else "최적화 점수는 시뮬레이션 기간 동안 대체로 증가하는 경향을 보입니다."

    # 가장 큰 변화가 일어난 연도
    max_value_change = max(value_changes, key=lambda x: abs(x[1]), default=(0, 0))
    max_stress_change = max(stress_changes, key=lambda x: abs(x[1]), default=(0, 0))
    max_opt_change = max(optimization_changes, key=lambda x: abs(x[1]), default=(0, 0))

    # 변화가 큰 연도에 대한 설명
    value_max_desc = f"특히 {max_value_change[0]}년에는 가치 합계가 {max_value_change[1]:.1f}% 변화하며 가장 큰 변동을 보였습니다. 이는 {'임금피크제 적용으로 급여가 감소한 영향이 큽니다.' if max_value_change[1] < 0 else '학습 성취감이 증가한 결과로 보입니다.'}"
    stress_max_desc = f"특히 {max_stress_change[0]}년에는 스트레스 합계가 {max_stress_change[1]:.1f}% 증가하며 가장 큰 변동을 보였습니다. 이는 건강 문제와 휴가 욕구가 증가한 영향으로, 이 시기에 스트레스 관리와 워라밸 조정이 필요합니다."
    opt_max_desc = f"특히 {max_opt_change[0]}년에는 최적화 점수가 {max_opt_change[1]:.1f}% 변화하며 가장 큰 변동을 보였습니다. 이는 {'스트레스 증가로 인해 직장 생활 만족도가 낮아진 결과입니다.' if max_opt_change[1] < 0 else '가치 합계가 증가하여 직장 생활 만족도가 높아진 결과입니다.'}"

    return {
        "value": {"overall_trend": value_trend, "max_change_desc": value_max_desc},
        "stress": {"overall_trend": stress_trend, "max_change_desc": stress_max_desc},
        "optimization": {"overall_trend": opt_trend, "max_change_desc": opt_max_desc}
    }

def create_trend_graph(df, show_value, show_stress, show_optimization, lang_code, TEXTS):
    # 빈 그래프 생성 (기본 선 제거)
    fig = go.Figure()

    # 사용자가 선택한 항목만 추가
    if show_value:
        fig.add_scatter(x=df["연도"], y=df["가치 합계"], mode="lines+markers", name=TEXTS[lang_code]["show_value"], line=dict(color="#00cc96"))
    if show_stress:
        fig.add_scatter(x=df["연도"], y=df["스트레스 합계"], mode="lines+markers", name=TEXTS[lang_code]["show_stress"], line=dict(color="#ef553b"))
    if show_optimization:
        fig.add_scatter(x=df["연도"], y=df["내 최적화 점수"], mode="lines+markers", name=TEXTS[lang_code]["show_optimization"], line=dict(color="#3498db"))

    # 레이아웃 설정
    fig.update_layout(
        template="plotly_white",
        width=600,
        height=400,
        title=TEXTS[lang_code]["trend_title"],
        title_x=0.5,
        xaxis_title=TEXTS[lang_code]["trend_title"].split(" ")[0],  # "연도별 추이" → "연도"
        yaxis_title="Index"
    )
    return fig