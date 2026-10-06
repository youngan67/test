import pandas as pd
import streamlit as st
from pathlib import Path

st.title("test 철도 데이터 분석 보드")

# df = pd.read_csv("/content/drive/MyDrive/CSLEE_철도청/엔지니어링 데이터분석_실습/data/analysis_result.csv")
app_folder = Path(__file__).resolve().parent
df = pd.read_csv(app_folder / "data" / "analysis_result.csv")

st.dataframe(df)

numeric_columns = df.select_dtypes(include="number").columns.tolist()

if numeric_columns:
    selected = st.selectbox("확인할 지표", numeric_columns)
    st.line_chart(df[selected])
