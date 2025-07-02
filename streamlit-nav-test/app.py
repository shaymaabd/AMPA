import streamlit as st
from streamlit_navigation_bar import st_navbar

ALL_PAGES = [
    st.Page(page="app_pages/page_1.py"),
    st.Page(page="app_pages/page_2.py")
]

ALL_PAGES_TITLE = [
    "page1",
    "page2"
]


stNavbarOut = st_navbar(
    ALL_PAGES_TITLE,
    allow_reselect=False,
    key="navBarMain",
)

# st.session_state["counter"] = 0

# if st.session_state[]

def getPage(navBarPageSelected: str):
    for i in range(0, len(ALL_PAGES_TITLE)):
        if navBarPageSelected == ALL_PAGES_TITLE[i]:
            return (ALL_PAGES[i])
    return (None)


if st.session_state["navBarMain"] and st.session_state["navBarMain"][0]:
    # st.write(st.session_state["navBarMain"][0])
    pageToSwitch = getPage(st.session_state["navBarMain"][0])
    # st.write(pageToSwitch)
    if pageToSwitch:
        st.session_state["navBarMain"][0] = None
        st.switch_page(pageToSwitch)

pg = st.navigation(ALL_PAGES)

pg.run()
