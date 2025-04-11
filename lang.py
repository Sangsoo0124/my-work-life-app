# lang.py
TEXTS = {
    "ko": {
        "title": "나의 직장 생활 최적화 수준 알아보기",
        "intro": "이 애플리케이션은 퇴직까지 남은 연수를 기반으로 직장 생활의 최적화 점수를 시뮬레이션합니다. 가치와 스트레스 항목에 점수를 입력하여 결과를 확인하세요.",
        "basic_info": "1. 기본 정보 입력",
        "remaining_years": "퇴직까지 남은 연수 (년):",
        "value_input": "2. 가치 점수 입력",
        "value_desc": "가치(Value)는 '나는 내 급여 수준을 중요하게 생각한다', '나는 새롭게 배우는 것을 중요하게 생각한다', '나는 업무 만족도를 중요하게 생각한다'로 구성됩니다. 각 항목을 0~10점으로 입력하세요.",
        "value_salary": "나는 내 급여 수준을 중요하게 생각한다 (0~10점):",
        "value_learning": "나는 새롭게 배우는 것을 중요하게 생각한다 (0~10점):",
        "value_job_satisfaction": "나는 업무 만족도를 중요하게 생각한다 (0~10점):",
        "current_value_sum": "현재 가치 합계 (입력값 기준):",
        "value_sum_note": "※ '현재 가치 합계'는 입력하신 점수를 그대로 합한 값입니다. 시뮬레이션 결과의 '가치 합계'는 시간이 지나면서 변동된 값을 반영합니다.",
        "stress_input": "3. 스트레스 점수 입력",
        "stress_desc": "스트레스(Stress)는 '나는 내 신체적 건강 이상 신호에 대해 마음이 쓰인다', '나는 정시 퇴근 또는 휴가를 내서 정신적인 안정을 취하고 싶다', '나는 재정적 불안정에 대해 마음이 쓰인다'로 구성됩니다. 각 항목을 0~10점으로 입력하세요.",
        "stress_health": "나는 내 신체적 건강 이상 신호에 대해 마음이 쓰인다 (0~10점):",
        "stress_rest": "나는 정시 퇴근 또는 휴가를 내서 정신적인 안정을 취하고 싶다 (0~10점):",
        "stress_financial": "나는 재정적 불안정에 대해 마음이 쓰인다 (0~10점):",
        "current_stress_sum": "현재 스트레스 합계 (입력값 기준):",
        "stress_zero_warning": "스트레스 합계가 0이면 최적화 점수를 계산할 수 없습니다. 최소 0.1 이상의 값을 입력해주세요.",
        "advanced_settings": "고급 설정 (선택)",
        "wage_peak_years": "임금피크제 적용 시점 (퇴직 몇 년 전):",
        "wage_peak_years_desc": "퇴직 몇 년 전부터 급여가 줄어드는지 설정합니다. 예: 2년 전으로 설정하면 퇴직 2년 전부터 급여가 감소합니다.",
        "wage_peak_reduction": "임금피크제 급여 감소 비율 (%):",
        "wage_peak_reduction_desc": "임금피크제가 적용될 때 급여가 얼마나 줄어드는지 설정합니다. 예: 15%로 설정하면 급여가 15% 감소합니다.",
        "health_increase_rate": "건강 문제 증가율 (연간):",
        "health_increase_rate_desc": "시간이 지남에 따라 건강 문제에 대한 걱정이 얼마나 더 커질지를 설정합니다. 값이 클수록 매년 건강 스트레스가 더 많이 증가합니다.",
        "rest_increase_rate": "휴가 욕구 증가율 (연간):",
        "rest_increase_rate_desc": "시간이 지남에 따라 휴식(휴가, 정시 퇴근)에 대한 욕구가 얼마나 더 커질지를 설정합니다. 값이 클수록 매년 휴식 필요성이 더 많이 증가합니다.",
        "financial_increase_rate": "재정적 불안정 증가율 (연간):",
        "financial_increase_rate_desc": "시간이 지남에 따라 재정적 불안감(돈 걱정)이 얼마나 더 커질지를 설정합니다. 값이 클수록 매년 재정적 스트레스가 더 많이 증가합니다.",
        "learning_increase_rate": "학습 증가율 (연간):",
        "learning_increase_rate_desc": "시간이 지남에 따라 새로운 배움에 대한 성취감이 얼마나 더 커질지를 설정합니다. 값이 클수록 매년 학습 성취감이 더 많이 증가합니다.",
        "simulation_results": "시뮬레이션 결과",
        "yearly_scores": "연도별 최적화 점수",
        "trend": "연도별 추이",
        "select_display": "표시할 항목 선택",
        "show_value": "가치 합계 표시",
        "show_stress": "스트레스 합계 표시",
        "show_optimization": "최적화 점수 표시",
        "trend_title": "연도별 추이",
        "result_analysis": "결과 분석",
        "result_desc": "본 시뮬레이션은 입력하신 퇴직 연수와 가치/스트레스 점수를 기반으로 직장 생활의 최적화 점수를 예측한 결과입니다.",
        "value_sum_desc": "- **가치 합계**: '나는 내 급여 수준을 중요하게 생각한다', '나는 새롭게 배우는 것을 중요하게 생각한다', '나는 업무 만족도를 중요하게 생각한다'의 점수를 합한 값입니다. 시간이 지나면서 급여와 학습 성취감이 변동될 수 있습니다.",
        "stress_sum_desc": "- **스트레스 합계**: '나는 내 신체적 건강 이상 신호에 대해 마음이 쓰인다', '나는 정시 퇴근 또는 휴가를 내서 정신적인 안정을 취하고 싶다', '나는 재정적 불안정에 대해 마음이 쓰인다'의 점수를 합한 값입니다. 시간이 지나면서 각 항목이 증가할 수 있습니다.",
        "optimization_score_desc": "- **최적화 점수**: 가치 합계를 스트레스 합계로 나눈 값으로, 점수가 높을수록 직장 생활이 더 효율적이고 만족스러운 상태임을 의미합니다.",
        "analysis_summary": "분석 요약",
        "value_trend": "- **가치 변화 추이**: {overall_trend} {max_change_desc}",
        "stress_trend": "- **스트레스 변화 추이**: {overall_trend} {max_change_desc}",
        "optimization_trend": "- **최적화 수준 변화 추이**: {overall_trend} {max_change_desc}",
        "stats_summary": "통계 요약",
        "max_score": "- **최대 최적화 점수**: {max_score:.2f} (연도: {year})",
        "min_score": "- **최소 최적화 점수**: {min_score:.2f} (연도: {year})",
        "avg_score": "- **평균 최적화 점수**: {avg_score:.2f}",
        "std_score": "- **표준편차**: {std_score:.2f}",
        "suggestions": "제언",
        "suggestions_title": "더 나은 직장 생활을 위한 나만의 전략",
        "health_care": "건강 관리 강화",
        "health_care_desc": "나이 들수록 건강 관련 스트레스가 증가하므로, 조기에 건강 관리 루틴을 도입하는 것이 중요합니다. 정기적인 건강 검진을 통해 잠재적인 건강 문제를 조기에 발견하고, 꾸준한 운동과 균형 잡힌 식단을 유지하여 신체적 건강 이상을 최소화하세요. 또한, 스트레스 관리 프로그램이나 명상과 같은 정신적 건강 관리 방법을 병행하면 장기적으로 더 나은 삶의 질을 유지할 수 있습니다.",
        "financial_plan": "재정 계획 수립",
        "financial_plan_desc": "임금피크제로 인해 퇴직 2년 전부터 급여가 감소하기 전에 철저한 재정 계획을 세우는 것이 필수입니다. 저축과 투자를 통해 퇴직 후에도 안정적인 재정 상태를 유지할 수 있도록 준비하고, 불필요한 지출을 줄이는 습관을 들이세요. 추가적으로, 부수입 창출을 위한 방안(예: 부업, 재테크)을 고려하여 급여 감소에 따른 가치 하락을 완화할 수 있습니다.",
        "work_efficiency": "업무 효율화 및 학습 기회 활용",
        "work_efficiency_desc": "새로운 배움의 가치는 시간이 지남에 따라 점차 증가하므로, 이를 적극적으로 활용하는 것이 중요합니다. 소규모 프로젝트나 새로운 기술 학습 기회를 통해 업무 역량을 강화하고, 이를 통해 직장에서의 경쟁력을 높이세요. 또한, 업무 효율화를 위해 시간 관리 기술을 익히고, 불필요한 업무 부담을 줄이는 방법을 모색하여 더 나은 워라밸을 유지할 수 있습니다.",
        "stress_management": "스트레스 관리",
        "stress_management_desc": "'나는 정시 퇴근 또는 휴가를 내서 정신적인 안정을 취하고 싶다'가 증가하는 시점에 맞춰 적절한 휴식을 취하는 것이 필요합니다. 유연 근무제를 활용하거나, 정기적으로 짧은 휴가를 계획하여 피로를 해소하고 정신적 안정감을 유지하세요. 또한, 취미 생활이나 가족과의 시간을 늘려 스트레스를 해소하는 방법을 적극적으로 찾아보는 것이 좋습니다。",
        "social_relations": "사회적 관계 강화",
        "social_relations_desc": "직장 생활 중 동료, 가족, 친구와의 관계는 정신적 안정과 직장 생활의 만족도에 큰 영향을 미칩니다. 정기적으로 동료들과 소통하며 팀워크를 강화하고, 가족이나 친구들과의 시간을 늘려 사회적 지지망을 구축하세요. 또한, 퇴직 후에도 지속적인 관계를 유지할 수 있도록 네트워킹 활동에 참여하거나 지역 커뮤니티 활동에 적극적으로 참여하는 것이 좋습니다。",
        "retirement_plan": "퇴직 후 계획",
        "retirement_plan_desc": "퇴직이 가까워질수록 최적화 점수가 낮아지므로, 퇴직 후의 삶에 대한 구체적인 계획을 미리 세우는 것이 중요합니다. 재취업, 취미 활동, 봉사 활동 등 퇴직 후에도 의미 있는 시간을 보낼 수 있는 방안을 고민하고, 이를 위해 필요한 준비(예: 관련 기술 학습, 네트워킹)를 지금부터 시작하세요. 또한, 퇴직 후 건강 관리와 재정적 안정성을 유지하기 위한 장기적인 계획을 수립하여 전환기의 스트레스를 줄이는 데 집중해야 합니다。",
        "simulation_note": "이 시뮬레이션은 가정에 기반한 결과이므로, 실제 상황에 따라 조정될 수 있습니다. 추가적인 변수나 조건을 반영하고 싶다면 입력 값을 수정하여 다시 시뮬레이션을 실행해보세요.",
        "note": "참고: 이 애플리케이션은 Streamlit을 통해 실행됩니다. 로컬 환경에서 실행하려면 `streamlit run app.py` 명령어를 사용하세요。"
    },
    "en": {
        "title": "Assess My Work-Life Optimization Level",
        "intro": "This application simulates your work-life optimization score based on the years remaining until retirement. Enter your value and stress scores to see the results.",
        "basic_info": "1. Basic Information",
        "remaining_years": "Years until retirement:",
        "value_input": "2. Value Scores",
        "value_desc": "Value consists of 'I value my salary level', 'I value learning new things', and 'I value job satisfaction'. Enter each item on a scale of 0 to 10.",
        "value_salary": "I value my salary level (0-10):",
        "value_learning": "I value learning new things (0-10):",
        "value_job_satisfaction": "I value job satisfaction (0-10):",
        "current_value_sum": "Current Value Sum (based on inputs):",
        "value_sum_note": "※ The 'Current Value Sum' is the direct sum of your input scores. The 'Value Sum' in the simulation results reflects values that change over time.",
        "stress_input": "3. Stress Scores",
        "stress_desc": "Stress consists of 'I am concerned about physical health issues', 'I want to leave work on time or take a vacation for mental stability', and 'I am concerned about financial instability'. Enter each item on a scale of 0 to 10.",
        "stress_health": "I am concerned about physical health issues (0-10):",
        "stress_rest": "I want to leave work on time or take a vacation for mental stability (0-10):",
        "stress_financial": "I am concerned about financial instability (0-10):",
        "current_stress_sum": "Current Stress Sum (based on inputs):",
        "stress_zero_warning": "If the stress sum is 0, the optimization score cannot be calculated. Please enter a value of at least 0.1.",
        "advanced_settings": "Advanced Settings (Optional)",
        "wage_peak_years": "Wage peak system application (years before retirement):",
        "wage_peak_years_desc": "Sets how many years before retirement your salary will start to decrease. For example, setting it to 2 means your salary will decrease starting 2 years before retirement.",
        "wage_peak_reduction": "Wage peak system salary reduction rate (%):",
        "wage_peak_reduction_desc": "Sets how much your salary will decrease when the wage peak system is applied. For example, setting it to 15% means your salary will decrease by 15%.",
        "health_increase_rate": "Health concern increase rate (yearly):",
        "health_increase_rate_desc": "Sets how much your concern about health issues will increase over time. A higher value means your health-related stress will increase more each year.",
        "rest_increase_rate": "Vacation need increase rate (yearly):",
        "rest_increase_rate_desc": "Sets how much your need for rest (vacation, leaving work on time) will increase over time. A higher value means your need for rest will increase more each year.",
        "financial_increase_rate": "Financial instability increase rate (yearly):",
        "financial_increase_rate_desc": "Sets how much your concern about financial instability (money worries) will increase over time. A higher value means your financial stress will increase more each year.",
        "learning_increase_rate": "Learning increase rate (yearly):",
        "learning_increase_rate_desc": "Sets how much your sense of achievement from learning new things will increase over time. A higher value means your learning achievement will increase more each year.",
        "simulation_results": "Simulation Results",
        "yearly_scores": "Yearly Optimization Scores",
        "trend": "Yearly Trends",
        "select_display": "Select Items to Display",
        "show_value": "Show Value Sum",
        "show_stress": "Show Stress Sum",
        "show_optimization": "Show Optimization Score",
        "trend_title": "Yearly Trends",
        "result_analysis": "Result Analysis",
        "result_desc": "This simulation predicts your work-life optimization score based on the years until retirement and your value/stress scores.",
        "value_sum_desc": "- **Value Sum**: The sum of scores for 'I value my salary level', 'I value learning new things', and 'I value job satisfaction'. This may change over time due to salary and learning achievement fluctuations.",
        "stress_sum_desc": "- **Stress Sum**: The sum of scores for 'I am concerned about physical health issues', 'I want to leave work on time or take a vacation for mental stability', and 'I am concerned about financial instability'. These may increase over time.",
        "optimization_score_desc": "- **Optimization Score**: The value sum divided by the stress sum. A higher score indicates a more efficient and satisfying work-life.",
        "analysis_summary": "Analysis Summary",
        "value_trend": "- **Value Trend**: {overall_trend} {max_change_desc}",
        "stress_trend": "- **Stress Trend**: {overall_trend} {max_change_desc}",
        "optimization_trend": "- **Optimization Trend**: {overall_trend} {max_change_desc}",
        "stats_summary": "Statistical Summary",
        "max_score": "- **Maximum Optimization Score**: {max_score:.2f} (Year: {year})",
        "min_score": "- **Minimum Optimization Score**: {min_score:.2f} (Year: {year})",
        "avg_score": "- **Average Optimization Score**: {avg_score:.2f}",
        "std_score": "- **Standard Deviation**: {std_score:.2f}",
        "suggestions": "Suggestions",
        "suggestions_title": "Strategies for a Better Work-Life",
        "health_care": "Strengthen Health Care",
        "health_care_desc": "As you age, health-related stress increases, so it’s important to establish a health care routine early. Regular check-ups can help detect potential health issues early, and maintaining consistent exercise and a balanced diet can minimize physical health problems. Additionally, incorporating mental health practices like stress management programs or meditation can help maintain a better quality of life in the long term.",
        "financial_plan": "Establish a Financial Plan",
        "financial_plan_desc": "It’s essential to create a thorough financial plan before your salary decreases due to the wage peak system two years before retirement. Save and invest to ensure financial stability after retirement, and develop habits to reduce unnecessary spending. Additionally, consider ways to generate extra income (e.g., side jobs, investments) to mitigate the impact of a salary reduction.",
        "work_efficiency": "Enhance Work Efficiency and Seize Learning Opportunities",
        "work_efficiency_desc": "The value of learning new things increases over time, so it’s important to actively take advantage of this. Engage in small projects or learn new skills to enhance your work capabilities and increase your competitiveness at work. Additionally, learn time management techniques to improve work efficiency and reduce unnecessary workload, helping you maintain a better work-life balance.",
        "stress_management": "Manage Stress",
        "stress_management_desc": "As the desire to 'leave work on time or take a vacation for mental stability' increases, it’s necessary to take appropriate breaks. Utilize flexible work arrangements or plan regular short vacations to relieve fatigue and maintain mental stability. Additionally, increase time spent on hobbies or with family to find effective ways to reduce stress.",
        "social_relations": "Strengthen Social Relationships",
        "social_relations_desc": "Relationships with colleagues, family, and friends during your work-life significantly impact mental stability and job satisfaction. Regularly communicate with colleagues to strengthen teamwork, and spend more time with family or friends to build a social support network. Additionally, participate in networking activities or local community events to maintain relationships even after retirement.",
        "retirement_plan": "Plan for Retirement",
        "retirement_plan_desc": "As retirement approaches, your optimization score decreases, so it’s important to plan for life after retirement in advance. Consider options like re-employment, hobbies, or volunteer activities to spend meaningful time after retirement, and start preparing now (e.g., learning relevant skills, networking). Additionally, establish long-term plans to maintain health care and financial stability after retirement to reduce stress during the transition.",
        "simulation_note": "This simulation is based on assumptions, so results may vary depending on actual circumstances. If you want to reflect additional variables or conditions, modify the input values and run the simulation again.",
        "note": "Note: This application runs on Streamlit. To run it locally, use the command `streamlit run app.py`."
    }
}