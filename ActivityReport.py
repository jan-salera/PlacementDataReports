import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np    


#Annual Activity Report Section 
with st.expander("**Activity Reports From Prior Years**"):
    K1, K2, K3 = st.columns(3)
    with K1:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_4586c10b1b31439bbe69da616e0e3315.pdf", label= ":green[**2020-2021 Activity Report**]")
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_767f829043174861b77a83a2742a1096.pdf", label= ":green[**2017-2018 Activity Report**]")
        
    with K2:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_63a24da526604d86b872fef02fe33e18.pdf", label= ":green[**2019-2020 Activity Report**]")
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_e1d90f9b3daf445fb275bde81048dbb2.pdf", label= ":green[**2016-2017 Activity Report**]")
        
        
    with K3:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_013d842090f14402855558e2ad91aac7.pdf", label= ":green[**2018-2019 Activity Report**]")