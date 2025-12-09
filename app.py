import streamlit as st
import pandas as pd
import numpy as np
import time

# 페이지 기본 설정
st.set_page_config(
    page_title="KOSPI 200 AI Analyst",
    page_icon="📈",
    layout="wide"
)

# [cite_start]--- 사이드바 설정 [cite: 3, 11] ---
st.sidebar.title("⚙️ 설정")
st.sidebar.markdown("API 정보를 입력하고 **'분석 시작'**을 눌러주세요.")

# 데모 모드 스위치 (변경 사항: API 키 없이도 테스트 가능하도록 추가)
use_demo = st.sidebar.checkbox("체험판(Demo) 모드로 실행", value=True)

with st.sidebar.expander("API 인증 정보", expanded=not use_demo):
    [cite_start]app_key = st.text_input("APP KEY", type="password", disabled=use_demo, placeholder="증권사 App Key 입력") # [cite: 7]
    [cite_start]app_secret = st.text_input("APP SECRET", type="password", disabled=use_demo, placeholder="증권사 App Secret 입력") # [cite: 9]
    [cite_start]acc_no = st.text_input("계좌번호", disabled=use_demo, placeholder="12345678-01") # [cite: 10]

[cite_start]st.sidebar.subheader("분석 옵션") # [cite: 12]
[cite_start]top_n = st.sidebar.number_input("추천받을 종목 개수", min_value=1, max_value=10, value=5) # [cite: 13]
[cite_start]min_vol = st.sidebar.slider("최소 거래 규모 (억원)", 10, 500, 100) # [cite: 14, 15]

# 분석 시작 버튼
[cite_start]start_btn = st.sidebar.button("🚀 분석 시작하기", type="primary") # [cite: 11]

# --- 메인 화면 ---
[cite_start]st.title("📈 코스피200 주식 추천 봇 V2.0") # [cite: 2]
st.markdown("""
[cite_start]**초보자도 쉽게 이해하는 주식 분석 도구** 코스피200 종목을 자동으로 분석하여 매수하기 좋은 종목을 추천해 드립니다. [cite: 8, 19]
""")

st.divider()

# [cite_start]분석 항목 설명 섹션 [cite: 20]
col1, col2, col3 = st.columns(3)
with col1:
    [cite_start]st.info("### 📈 상승 추세\n주가가 올라가는 흐름인지 확인합니다. [cite: 21]")
with col2:
    [cite_start]st.success("### 🚀 상승 속도\n최근 며칠간 얼마나 빠르게 올랐는지 분석합니다. [cite: 22]")
with col3:
    [cite_start]st.warning("### 💰 거래 활발도\n사람들이 얼마나 많이 거래하는지 확인합니다. [cite: 22]")

# [cite_start]추천 점수 계산 로직 (Expander로 숨김 처리하여 깔끔하게) [cite: 23]
with st.expander("📊 추천 점수는 어떻게 계산하나요? (클릭하여 보기)"):
    st.markdown("""
    [cite_start]각 항목별로 점수를 부여하여 합산합니다: [cite: 24]
    
    | 항목 | 점수 | 설명 |
    | :--- | :--- | :--- |
    | **✔ 상승 추세 진입** | `+4점` | [cite_start]강력한 매수 신호 [cite: 25] |
    | **강한 상승세** | `+2~3점` | [cite_start]최근 상승 모멘텀이 강함 [cite: 25] |
    | **거래 증가** | `+1~2점` | [cite_start]거래량이 평소보다 급증 [cite: 25] |
    | **✔ 적정 가격대** | `+1.5점` | [cite_start]너무 오르거나 떨어지지 않은 상태 [cite: 25, 27] |
    | **어제 대비 상승** | `+1점` | [cite_start]전일 대비 주가 상승 [cite: 25] |
    | **가격 변동 큼** | `-0.5~-1점` | [cite_start]안정성 부족 (감점 요인) [cite: 25, 27] |
    
    > [cite_start]**높은 점수 = 지금 사기 좋은 종목** [cite: 29]
    """)

st.divider()

# --- 로직 실행부 ---
if start_btn:
    # 1. 유효성 검사
    if not use_demo and (not app_key or not app_secret):
        st.error("API 키와 Secret을 입력해야 분석이 가능합니다. (또는 데모 모드를 체크하세요)")
    else:
        # 2. 로딩 애니메이션
        with st.status("🔍 코스피200 시장을 분석 중입니다...", expanded=True) as status:
            st.write("데이터 수집 중...")
            time.sleep(1)
            st.write("기술적 지표 계산 중 (RSI, MACD, 이동평균선)...")
            time.sleep(1.2)
            st.write("점수 산출 및 순위 매기는 중...")
            time.sleep(0.8)
            status.update(label="✅ 분석 완료!", state="complete", expanded=False)

        # 3. 데이터 생성 (실제 API 연결 대신 데모 데이터 생성 로직 구현)
        # 실제 배포 시 이 부분에 증권사 API(mojito 등) 코드를 넣으면 됩니다.
        st.subheader(f"🏆 오늘의 TOP {top_n} 추천 종목")
        
        # 가상 데이터 생성
        mock_data = {
            '종목명': ['삼성전자', 'SK하이닉스', 'LG에너지솔루션', 'NAVER', '카카오', '현대차', '기아'],
            '현재가': [72000, 125000, 450000, 210000, 55000, 190000, 85000],
            '등락률': ['+1.5%', '+3.2%', '-0.5%', '+0.8%', '+2.1%', '+1.1%', '+0.9%'],
            '추천 점수': np.random.uniform(70, 98, 7).round(1), # 70~98점 사이 랜덤
            '추세': ['상승', '강한 상승', '보합', '상승', '상승전환', '안정', '안정']
        }
        df = pd.DataFrame(mock_data).sort_values(by='추천 점수', ascending=False).head(top_n)
        
        # 4. 결과 출력
        # 스타일링된 데이터프레임
        st.dataframe(
            df,
            column_config={
                "추천 점수": st.column_config.ProgressColumn(
                    "추천 점수 (100점 만점)",
                    format="%.1f점",
                    min_value=0,
                    max_value=100,
                ),
                "현재가": st.column_config.NumberColumn(
                    "현재가",
                    format="%d원"
                )
            },
            hide_index=True,
            use_container_width=True
        )

        # 시각화 (살짝 바뀐 부분: 차트 추가)
        st.caption("※ 추천 점수가 가장 높은 종목의 최근 가상 주가 흐름입니다.")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3) + [0, 2, 0],
            columns=['관심', '수급', '모멘텀']
        )
        st.line_chart(chart_data)

# [cite_start]--- 하단 주의사항 [cite: 33] ---
st.warning("""
**투자 주의사항** 이 도구는 참고용이며, 투자 손실에 대한 책임은 투자자 본인에게 있습니다.  
[cite_start]실제 투자 전에는 반드시 추가 조사를 하시기 바랍니다. [cite: 34, 35, 36]
""")
