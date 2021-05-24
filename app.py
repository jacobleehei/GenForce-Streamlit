import streamlit as st

st.set_page_config(
        page_title="GenForce",
        page_icon=":dizzy:",
        layout="wide",
        initial_sidebar_state="expanded",
)

from utils.webFunction import write_page

import src.pages.home
import src.pages.idgan_page
import src.pages.higan_page
import src.pages.itfgan_page


PAGES = {
    'Home': src.pages.home,
    'InterFaceGAN': src.pages.itfgan_page,
    'In-DomainGAN': src.pages.idgan_page,
    'HiGAN': src.pages.higan_page
}


def main():

    with st.sidebar:
        # update message
        st.info("""
            ⭐ **Update**: Added InterFaceGAN, In-DomainGAN and HiGAN. Enjoy!
            """
            )

        # navigation
        st.title('Navigation')
        page_selection = st.radio("Go to", list(PAGES.keys()))

    page = PAGES[page_selection]
    write_page(page)


if __name__ == "__main__":
    main()

