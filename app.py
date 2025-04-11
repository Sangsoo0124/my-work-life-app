# app.py
import streamlit as st
import pandas as pd
from utils import calculate_simulation_data, create_trend_graph, analyze_trends
from config import SIMULATION_CONFIG
from lang import TEXTS

# Streamlit 페이지 설정
st.set_page_config(page_title="나의 직장 생활 최적화 수준 알아보기", layout="centered")

# CSS 스타일링
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
        padding: 10px;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        font-size: 24px !important;
        color: #2c3e50;
        text-align: center;
    }
    .stMarkdown, .stHeader {
        font-size: 16px !important;
        color: #34495e;
    }
    .stSlider > div > div > div > div {
        background-color: #3498db !important;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        width: 100%;
        padding: 10px;
        font-size: 16px;
    }
    .stDataFrame {
        font-size: 14px !important;
    }
    .warning {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px;
        border-radius: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "remaining_years" not in st.session_state:
    st.session_state.remaining_years = 8
if "value_salary" not in st.session_state:
    st.session_state.value_salary = 7.0
if "value_learning" not in st.session_state:
    st.session_state.value_learning = 3.0
if "value_job_satisfaction" not in st.session_state:
    st.session_state.value_job_satisfaction = 5.0
if "stress_health" not in st.session_state:
    st.session_state.stress_health = 2.0
if "stress_rest" not in st.session_state:
    st.session_state.stress_rest = 3.0
if "stress_financial" not in st.session_state:
    st.session_state.stress_financial = 4.0

# 언어 선택
language = st.selectbox("언어 선택 / Select Language", ["한국어 (ko)", "English (en)"], key="language")
lang_code = "ko" if language == "한국어 (ko)" else "en"

# 제목 및 소개
st.title(TEXTS[lang_code]["title"])
st.markdown(TEXTS[lang_code]["intro"])

# 1. 기본 정보 입력
st.header(TEXTS[lang_code]["basic_info"])
remaining_years = st.number_input(
    TEXTS[lang_code]["remaining_years"],
    min_value=1,
    max_value=30,
    value=st.session_state.remaining_years,
    key="remaining_years_input"
)
st.session_state.remaining_years = remaining_years

# 2. 가치 점수 입력
st.header(TEXTS[lang_code]["value_input"])
st.markdown(TEXTS[lang_code]["value_desc"])
value_salary = st.slider(
    TEXTS[lang_code]["value_salary"],
    0.0, 10.0,
    value=st.session_state.value_salary,
    step=0.5,
    key="value_salary_input"
)
value_learning = st.slider(
    TEXTS[lang_code]["value_learning"],
    0.0, 10.0,
    value=st.session_state.value_learning,
    step=0.5,
    key="value_learning_input"
)
value_job_satisfaction = st.slider(
    TEXTS[lang_code]["value_job_satisfaction"],
    0.0, 10.0,
    value=st.session_state.value_job_satisfaction,
    step=0.5,
    key="value_job_satisfaction_input"
)
st.session_state.value_salary = value_salary
st.session_state.value_learning = value_learning
st.session_state.value_job_satisfaction = value_job_satisfaction
st.markdown(f"{TEXTS[lang_code]['current_value_sum']} {value_salary + value_learning + value_job_satisfaction:.2f}")
st.markdown(TEXTS[lang_code]["value_sum_note"])

# 3. 스트레스 점수 입력
st.header(TEXTS[lang_code]["stress_input"])
st.markdown(TEXTS[lang_code]["stress_desc"])
stress_health = st.slider(
    TEXTS[lang_code]["stress_health"],
    0.0, 10.0,
    value=st.session_state.stress_health,
    step=0.5,
    key="stress_health_input"
)
stress_rest = st.slider(
    TEXTS[lang_code]["stress_rest"],
    0.0, 10.0,
    value=st.session_state.stress_rest,
    step=0.5,
    key="stress_rest_input"
)
stress_financial = st.slider(
    TEXTS[lang_code]["stress_financial"],
    0.0, 10.0,
    value=st.session_state.stress_financial,
    step=0.5,
    key="stress_financial_input"
)
st.session_state.stress_health = stress_health
st.session_state.stress_rest = stress_rest
st.session_state.stress_financial = stress_financial
st.markdown(f"{TEXTS[lang_code]['current_stress_sum']} {stress_health + stress_rest + stress_financial:.2f}")

# 스트레스 합계 유효성 검사
if stress_health + stress_rest + stress_financial == 0:
    st.markdown(f"<div class='warning'>{TEXTS[lang_code]['stress_zero_warning']}</div>", unsafe_allow_html=True)
    st.stop()

# 4. 고급 설정
st.header(TEXTS[lang_code]["advanced_settings"])
with st.expander("설정 열기"):
    wage_peak_years = st.number_input(
        TEXTS[lang_code]["wage_peak_years"],
        min_value=0,
        max_value=10,
        value=2
    )
    st.markdown(f"<small>{TEXTS[lang_code]['wage_peak_years_desc']}</small>", unsafe_allow_html=True)
    
    wage_peak_reduction = st.slider(
        TEXTS[lang_code]["wage_peak_reduction"],
        0,
        50,
        int(SIMULATION_CONFIG["wage_peak_reduction"] * 100)
    )
    st.markdown(f"<small>{TEXTS[lang_code]['wage_peak_reduction_desc']}</small>", unsafe_allow_html=True)
    
    health_increase_rate = st.slider(
        TEXTS[lang_code]["health_increase_rate"],
        0.0,
        1.0,
        SIMULATION_CONFIG["health_increase_rate"],
        step=0.1
    )
    st.markdown(f"<small>{TEXTS[lang_code]['health_increase_rate_desc']}</small>", unsafe_allow_html=True)
    
    rest_increase_rate = st.slider(
        TEXTS[lang_code]["rest_increase_rate"],
        0.0,
        1.0,
        SIMULATION_CONFIG["rest_increase_rate"],
        step=0.1
    )
    st.markdown(f"<small>{TEXTS[lang_code]['rest_increase_rate_desc']}</small>", unsafe_allow_html=True)
    
    financial_increase_rate = st.slider(
        TEXTS[lang_code]["financial_increase_rate"],
        0.0,
        1.0,
        SIMULATION_CONFIG["financial_increase_rate"],
        step=0.1
    )
    st.markdown(f"<small>{TEXTS[lang_code]['financial_increase_rate_desc']}</small>", unsafe_allow_html=True)
    
    learning_increase_rate = st.slider(
        TEXTS[lang_code]["learning_increase_rate"],
        0.0,
        1.0,
        SIMULATION_CONFIG["learning_increase_rate"],
        step=0.1
    )
    st.markdown(f"<small>{TEXTS[lang_code]['learning_increase_rate_desc']}</small>", unsafe_allow_html=True)

# 5. 시뮬레이션 실행 (자동 갱신)
df = calculate_simulation_data(
    remaining_years, value_salary, value_learning, value_job_satisfaction,
    stress_health, stress_rest, stress_financial,
    wage_peak_years, wage_peak_reduction,
    health_increase_rate, rest_increase_rate,
    financial_increase_rate, learning_increase_rate
)

# 6. 결과 출력
st.header(TEXTS[lang_code]["simulation_results"])
st.markdown(f"### {TEXTS[lang_code]['yearly_scores']}")
st.dataframe(df)

# 7. 그래프 시각화
st.markdown(f"### {TEXTS[lang_code]['trend']}")
st.markdown(TEXTS[lang_code]["select_display"])
show_value = st.checkbox(TEXTS[lang_code]["show_value"], value=True)
show_stress = st.checkbox(TEXTS[lang_code]["show_stress"], value=True)
show_optimization = st.checkbox(TEXTS[lang_code]["show_optimization"], value=True)
fig = create_trend_graph(df, show_value, show_stress, show_optimization, lang_code, TEXTS)
st.plotly_chart(fig, use_container_width=True)

# 8. 결과 분석
st.markdown(f"### {TEXTS[lang_code]['result_analysis']}")
st.markdown(TEXTS[lang_code]["result_desc"])
st.markdown(TEXTS[lang_code]["value_sum_desc"])
st.markdown(TEXTS[lang_code]["stress_sum_desc"])
st.markdown(TEXTS[lang_code]["optimization_score_desc"])

# 분석 요약
st.markdown(f"#### {TEXTS[lang_code]['analysis_summary']}")
trends = analyze_trends(df)
st.markdown(TEXTS[lang_code]["value_trend"].format(
    overall_trend=trends["value"]["overall_trend"],
    max_change_desc=trends["value"]["max_change_desc"]
))
st.markdown(TEXTS[lang_code]["stress_trend"].format(
    overall_trend=trends["stress"]["overall_trend"],
    max_change_desc=trends["stress"]["max_change_desc"]
))
st.markdown(TEXTS[lang_code]["optimization_trend"].format(
    overall_trend=trends["optimization"]["overall_trend"],
    max_change_desc=trends["optimization"]["max_change_desc"]
))

# 통계 요약
st.markdown(f"#### {TEXTS[lang_code]['stats_summary']}")
max_score = df["내 최적화 점수"].max()
max_year = df.loc[df["내 최적화 점수"].idxmax(), "연도"]
min_score = df["내 최적화 점수"].min()
min_year = df.loc[df["내 최적화 점수"].idxmin(), "연도"]
avg_score = df["내 최적화 점수"].mean()
std_score = df["내 최적화 점수"].std()
st.markdown(TEXTS[lang_code]["max_score"].format(max_score=max_score, year=max_year))
st.markdown(TEXTS[lang_code]["min_score"].format(min_score=min_score, year=min_year))
st.markdown(TEXTS[lang_code]["avg_score"].format(avg_score=avg_score))
st.markdown(TEXTS[lang_code]["std_score"].format(std_score=std_score))

# 9. 제언
st.markdown(f"### {TEXTS[lang_code]['suggestions']}")
st.markdown(f"#### {TEXTS[lang_code]['suggestions_title']}")
st.markdown(f"**{TEXTS[lang_code]['health_care']}**")
st.markdown(TEXTS[lang_code]["health_care_desc"])
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['financial_plan']}**")
st.markdown(TEXTS[lang_code]["financial_plan_desc"])
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['work_efficiency']}**")
st.markdown(TEXTS[lang_code]["work_efficiency_desc"])
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['stress_management']}**")
st.markdown(TEXTS[lang_code]["stress_management_desc"])
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['social_relations']}**")
st.markdown(TEXTS[lang_code]["social_relations_desc"])
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['retirement_plan']}**")
st.markdown(TEXTS[lang_code]["retirement_plan_desc"])
st.markdown("---")
st.markdown(TEXTS[lang_code]["simulation_note"])

# 실행 안내
st.markdown("---")
st.markdown(f"**{TEXTS[lang_code]['note']}**")