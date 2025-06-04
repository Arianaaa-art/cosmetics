import streamlit as st

def set_global_styles():
    st.markdown("""
    <style>
    .subheading {
        color: #d64280;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #d64280;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 10px 30px;
        cursor: pointer;
        margin: 5px;
    }
    .stButton>button:hover {
        background-color: #a5185a;
    }
    </style>
    """, unsafe_allow_html=True)

def set_background_color(color):
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-color: {color};
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def home_page():
    set_global_styles()
    set_background_color("#f3d9e0")
    st.markdown('<h1 style="color:#c81b6e; text-align: center;">Find your own cosmetics</h1>', unsafe_allow_html=True)
    st.markdown('<h5 style="color:#c81b6e; text-align: center;">If you want to learn how to do makeup, or if you want to know about various cosmetics, use this website!</h5>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        if st.button("Introduction",icon="🤍"):
            st.session_state.page = 'introduction'
    with cols[1]:
        if st.button("Cosmetics types", icon="🐰"):
            st.session_state.page = 'cosmetics_types'
            
def introduction_page():
    set_global_styles()
    set_background_color("#f3d9e0")
    st.markdown('<h1 style="color:#c81b6e; text-align: center;">Introduction Page</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: black; text-align: center;">This website is about helping you to learn how to use these different types of cosmetics.</p>', unsafe_allow_html=True)

    if st.button("Learn How to Use"):
        st.write("If you want to know these types of cosmetics please return to the home page and click “Cosmetics Types” you will see more specific classification of cosmetics.")
        st.write("Choose what type of cosmetics you want to learn and understand.(Include: Skincare, Base make up, Color make up, make up removal)")
        st.write("After you click into these different cosmetics, you will see the specific cosmetics such as foundation, blush, powder and lipstick......")
    if st.button("Return to Home"):
        st.session_state.page = 'home'



def cosmetics_types_page():
    set_global_styles()
    set_background_color("#f3e5f5")
    st.markdown('<h1 style="color:#c81b6e; text-align: center;">Cosmetics Types</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#c81b6e; text-align: center;">Select a type of cosmetics to learn more.</p>', unsafe_allow_html=True)

    if st.button("Return to homepage"):
        st.session_state.page = 'home'
    cols = st.columns(2)
    with cols[0]:
        if st.button("Skincare"):
            st.session_state.page = 'skincare'
    with cols[1]:
        if st.button("Base make up"):
            st.session_state.page = 'base_makeup'

    cols2 = st.columns(2)
    with cols2[0]:
        if st.button("Color make up"):
            st.session_state.page = 'color_makeup'
    with cols2[1]:
        if st.button("Make up removal"):
            st.session_state.page = 'makeup_removal'

def skincare_page():
    set_global_styles()
    set_background_color("#f3deeb")
    st.markdown('<h1 style="color:#d64280; text-align: center;">Skincare</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d64280; text-align: center;">Select a skincare product to learn more.</p>', unsafe_allow_html=True)

    if st.button("Sunscreen"):
        st.session_state.page = 'sunscreen'
    if st.button("Sheet Mask"):
        st.session_state.page = 'sheet_mask'
    if st.button("Cleanser"):
        st.session_state.page = 'cleanser'

    if st.button("Return to Cosmetics Types"):
        st.session_state.page = 'cosmetics_types'

def base_makeup_page():
    set_global_styles()
    set_background_color("#f3d9e0")
    st.markdown('<h1 style="color:#d64280; text-align: center;">Base Make up</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d64280; text-align: center;">Select a base makeup product to learn more.</p>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        if st.button("Foundation"):
            st.session_state.page = 'foundation'
    with cols[1]:
        if st.button("Powder"):
            st.session_state.page = 'powder'

    # Return button
    if st.button("Return to Cosmetics Types"):
        st.session_state.page = 'cosmetics_types'

def sunscreen_page():
    set_global_styles()
    set_background_color("#f3e5f5")
    st.markdown('<h1 style="color:#d64280; text-align: center;">Sunscreen</h1>', unsafe_allow_html=True)

    try:
        st.image('/Users/chipichipi/PycharmProjects/sunscreen.png', caption='Sunscreen Product', use_container_width=True)
    except Exception as e:
        st.error(f"Failed to load image: {str(e)}")

    st.markdown('<div class="subheading">Introduction</div>', unsafe_allow_html=True)
    st.write("Sunscreen is a skin care product specially designed to resist ultraviolet (UV) radiation. It reduces the damage caused by UV radiation to the skin through physical blocking or chemical absorption.")

    st.markdown('<div class="subheading">How to use</div>', unsafe_allow_html=True)
    st.write("Apply 15-30 minutes before going out, and reapply every 2 hours (especially after swimming or sweating).")
    st.write("The amount should be sufficient (about the size of a coin for the face). It works better when combined with sun-protective clothing and hats.")
    st.write("Use it without any makeup at all.")
    st.write("Children should choose products with mild and specific formulas.")

    if st.button("Return to Cosmetics Types"):
        st.session_state.page = 'cosmetics_types'

def sheet_mask_page():
    set_global_styles()
    set_background_color("#f3deeb")
    st.markdown('<h1 style="color:#d64280; text-align: center;">Sheet Mask</h1>', unsafe_allow_html=True)

    try:
        st.image('/Users/chipichipi/PycharmProjects/HIII.png', caption='Sheet Mask Product', use_container_width=True)
    except Exception as e:
        st.error(f"Failed to load image: {str(e)}")

    st.markdown('<div class="subheading">Introduction</div>', unsafe_allow_html=True)
    st.write("Sheet Mask is a type of skin care product that is made by soaking essence liquid into fibrous materials (such as silk, non-woven fabric or bio-fibers). It is specially designed for intensive care of the skin.")

    st.markdown('<div class="subheading">How to use</div>', unsafe_allow_html=True)
    st.write("Cleanse the face: Before using the mask, thoroughly clean the face.")
    st.write("Unfold and fit snugly: Take out the mask and unfold it. Gently press to make the mask fully adhere to the face.")
    st.write("Let it stand and absorb: Leave it on for 15-20 minutes (refer to the packaging instructions for the specific time).")
    st.write("Post-care: After removing the mask, gently pat the remaining essence until it is absorbed. (No need to wash off)")

    if st.button("Return to Skincare"):
        st.session_state.page = 'skincare'

def cleanser_page():
    set_global_styles()
    set_background_color("#f3d9e0")
    st.markdown('<h1 style="color:#d64280; text-align: center;">Cleanser</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="subheading">Introduction</div>', unsafe_allow_html=True)
        st.write(
            "Cleanser, which stands for 'cleaning agent', is mainly used for cleaning the skin or surfaces of objects. In the field of skin care, it usually refers to facial cleanser, which is used to remove oil, dirt and makeup.")

        st.markdown('<div class="subheading">How to use</div>', unsafe_allow_html=True)
        st.write("1. Moisten the face, then take an appropriate amount of the product in your palm.")
        st.write("2. After creating bubbles by rubbing, massage the face in circular motions for 1 minute.")
        st.write("3. Rinse thoroughly with clean water to remove any residue.")

    with col2:
        try:
            st.image('/Users/chipichipi/PycharmProjects/cleanser.png', caption='Cleanser Product', use_container_width=True)
        except Exception as e:
            st.error(f"Failed to load image: {str(e)}")

    if st.button("Return to Skincare"):
        st.session_state.page = 'skincare'

def foundation_page():
        set_global_styles()
        set_background_color("#f3deeb")  # Light purple background color
        st.markdown('<h1 style="color:#d64280; text-align: center;">Foundation</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])  # Create a two-column layout

        with col1:
            # Introduction section
            st.markdown('<div class="subheading">Introduction</div>', unsafe_allow_html=True)
            st.write(
                "Foundation (foundation) is the core product for base makeup, used to even out skin tone, cover blemishes and adjust skin texture (such as matte or glossy effect).")

            # How to use section
            st.markdown('<div class="subheading">How to use</div>', unsafe_allow_html=True)
            st.write("1. After skin care: Apply sunscreen (if it doesn't have SPF value).")
            st.write(
                "2. Take an appropriate amount of foundation on the back of your hand or a tool, and gently pat/push it outwards from the center of the face.")

        with col2:
            # Add the image to the foundation page (image path needs to be updated)
            try:
                st.image('/Users/chipichipi/PycharmProjects/foundation2.png', caption='Foundation Product',
                         use_container_width=True)
            except Exception as e:
                st.error(f"Failed to load image: {str(e)}")

        # Return button to go back to the base makeup page
        if st.button("Return to Base Make up"):
            st.session_state.page = 'base_makeup'

def powder_page():
        set_global_styles()
        set_background_color("#f3deeb")  # Light purple background color
        st.markdown('<h1 style="color:#d64280; text-align: center;">Powder</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])  # Create a two-column layout

        with col1:
            # Introduction section
            st.markdown('<div class="subheading">Introduction</div>', unsafe_allow_html=True)
            st.write(
                "Powder (such as loose powder or compact powder) is a finishing product in makeup, mainly used to absorb oil and fix the makeup.")

            # How to use section
            st.markdown('<div class="subheading">How to use</div>', unsafe_allow_html=True)
            st.write("Step for makeup:")
            st.write(
                "After completing the base makeup, use a powder puff or a powder brush to dip a small amount of loose powder or powder compact.")
            st.write(
                "Gently press the powder on the areas prone to oiliness (such as the forehead, nose, and chin), and gently sweep it on the other areas.")

        with col2:
            # Add the image to the powder page (image path needs to be updated)
            try:
                st.image('/Users/chipichipi/PycharmProjects/powder.png', caption='Powder Product',
                         use_container_width=True)
            except Exception as e:
                st.error(f"Failed to load image: {str(e)}")

        # Return button to go back to the base makeup page
        if st.button("Return to Base Make up"):
            st.session_state.page = 'base_makeup'

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def main():
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "introduction":
        introduction_page()
    elif st.session_state.page == "cosmetics_types":
        cosmetics_types_page()
    elif st.session_state.page == "skincare":
        skincare_page()
    elif st.session_state.page == "sunscreen":
        sunscreen_page()
    elif st.session_state.page == "sheet_mask":
        sheet_mask_page()
    elif st.session_state.page == "cleanser":
        cleanser_page()
    elif st.session_state.page == "base_makeup":
        base_makeup_page()
    elif st.session_state.page == "foundation":
        foundation_page()
    elif st.session_state.page == "powder":
        powder_page()

if __name__ == "__main__":
    main()