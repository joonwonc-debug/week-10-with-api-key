import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# 1. 페이지 기본 설정 (가장 먼저 와야 함)
st.set_page_config(
    page_title="Data Insight Hub", # 탭 이름 변경 (친구 것과 다르게)
    page_icon="📊",
    layout="wide"
)

# 2. 스타일 꾸미기 (CSS로 숨길 건 숨기고 폰트 조정)
st.markdown("""
    <style>
    .main {
        background-color: #F5F5F5;
    }
    h1 {
        color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 사이드바 메뉴 (기본 사이드바보다 세련되게)
with st.sidebar:
    selected = option_menu("메뉴 선택", ["홈(Home)", "데이터 분석", "문의하기"], 
        icons=['house', 'bar-chart-fill', 'envelope'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# 4. 메인 기능 구현

# [홈 화면]
if selected == "홈(Home)":
    st.title("🚀 Project Dashboard")
    st.subheader("환영합니다! 나만의 데이터 분석 도구입니다.")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1]) # 화면을 2:1 비율로 나눔
    
    with col1:
        st.info("💡 이 앱은 Streamlit을 활용하여 데이터를 시각화하는 프로젝트입니다.")
        st.write("이곳에 프로젝트에 대한 간단한 설명을 적으세요. 친구의 앱과는 다르게, 우리는 레이아웃을 좌우로 나누어 훨씬 전문적으로 보이게 만들었습니다.")
        
    with col2:
        # 간단한 인터랙션 요소
        st.success("오늘의 기분은?")
        mood = st.slider("점수를 매겨보세요", 0, 100, 50)
        if mood > 80:
            st.write("기분이 아주 좋으시군요! 🎉")
        else:
            st.write("화이팅입니다! 💪")

# [데이터 분석 화면] - 여기가 핵심 기능
elif selected == "데이터 분석":
    st.title("📈 데이터 시각화")
    
    # 탭 기능 사용 (스크롤을 줄여줌)
    tab1, tab2 = st.tabs(["📊 차트 보기", "📋 데이터 보기"])
    
    # 가상의 데이터 생성 (친구의 앱 기능에 맞춰 수정 가능)
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A_Team', 'B_Team', 'C_Team']
    )
    
    with tab1:
        st.write("### 실시간 현황 차트")
        st.line_chart(data)
        if st.button("분석 결과 확인"):
            st.balloons() # 풍선 효과
            st.write("분석이 완료되었습니다!")
            
    with tab2:
        st.write("### 원본 데이터")
        st.dataframe(data, use_container_width=True)

# [문의하기 화면]
elif selected == "문의하기":
    st.title("📧 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("이름")
        message = st.text_area("메시지")
        submitted = st.form_submit_button("전송하기")
        
        if submitted:
            st.success(f"감사합니다, {name}님! 메시지가 전송되었습니다.")
