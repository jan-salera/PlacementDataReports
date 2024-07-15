import streamlit as st

def research_readings(size = [3,3,3], pagelink= "https://www.google.com/", custom = "insert label here"):
        M1, M2, M3  = st.columns(size)
        with M1:
            st.write("")
        with M2:
            st.write("")
            st.page_link(page = pagelink, label = custom)
        with M3:
            st.write("")

number = st.slider("Drag the slide bar to unlock a new level of information with our recommended research and readings!", 0, 80, 40, 20, format = "")

if number == 0:
    research_readings([1,8.5,8], "https://www.careers.egr.msu.edu/_files/ugd/bc0367_faa49c899d6f44b3b8471d235776e681.pdf",':green[**The Co-Op Experience - A Lasting Impact by Dr. Phil Gardner and Garth Motschenbacher**]')
    with st.container(border=True):
        st.image("TheCoopExperience.png")

elif number == 20:
    research_readings([1,11,2.65], "https://joinhandshake.com/wp-content/themes/handshake/dist/assets/downloads/network-trends/gen-z-career-goals-ai-economy.pdf?view=true", ':green[**Handshake Network Trends Report: The Class of 2024 sets their sights on the future**]')
    st.image("HandshakeFuture.png")
elif number == 40:
    research_readings([1,24,10],"https://www.careers.egr.msu.edu/_files/ugd/bc0367_b684a1faf5c64d0eb711a136ce31f72f.pdf",':green[**Factors Relating to Faculty Engagement in Cooperative Education by Dr. Bernadette Friedrich**]')
    with st.container(border=True):
        st.image("CooperativeEd.png")
elif number == 60:
    research_readings([1,3,2.65], "https://joinhandshake.com/blog/network-trends/how-gen-z-defines-flexibility/",':green[**Handshake Network Trends Report: How Gen Z defines “flexibility”**]')
    st.image("HandshakeGenZArticle.png")

elif number == 80:
    research_readings([3,6.28,3], "https://ceri.msu.edu/_assets/pdfs/folder College%20Recruiting%20Outlook%202022-2023.pdf", ':green[**College Hiring Outlook 2023 - by Dr. Phil Gardner**]')
    st.image("CollegeHiringOutlook.png")
