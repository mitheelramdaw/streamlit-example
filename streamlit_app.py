import streamlit as st

def main():
    st.markdown(
        """
        <style>
            /* Custom CSS styling for dark mode */
            body {
                background-color: #222831;
                color: #ffffff;
            }
            .stApp {
                background-color: #393e46;
                padding: 20px;
                border-radius: 10px;
            }
            .stApp header {
                text-align: center;
                margin-bottom: 20px;
                font-size: 24px;
                color: #f05454;
            }
            .stApp footer {
                text-align: center;
                margin-top: 30px;
                font-size: 18px;
                color: #eeeeee;
            }
            .stSidebar {
                background-color: #4e525a;
                padding: 20px;
                border-radius: 10px;
            }
            .profile {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }
            .profile img {
                border-radius: 50%;
                width: 60px;
                height: 60px;
                margin-right: 10px;
            }
            .profile-name {
                font-size: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Florence and Tio's Anniversary Celebration")
    st.markdown("💖 Happy Anniversary Florence and Tio! 💖")
    
    # Profile section
    st.markdown('<div class="profile"><img src="https://via.placeholder.com/60" alt="Profile Image"><div class="profile-name">Florence Tio\'s Girlfriend</div></div>', unsafe_allow_html=True)
    
    st.markdown(
        "Welcome to this special celebration of love and togetherness. "
        "Share your messages, memories, images, and videos to make this day even more memorable!"
    )
    
    st.sidebar.header("Upload Media")
    uploaded_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    uploaded_video = st.sidebar.file_uploader("Upload Video", type=["mp4"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    
    if uploaded_video:
        st.video(uploaded_video, format="video/mp4")

    st.markdown("---")
    st.header("Share Your Wishes")
    
    num_messages = st.number_input("Number of Messages", min_value=1, value=1, step=1)
    
    for i in range(num_messages):
        st.subheader(f"Message {i + 1}")
        user_wish = st.text_area(f"Leave your message {i + 1} here", height=150, key=f"message_{i}")
        submit_button = st.button(f"Save Message {i + 1}")

        if submit_button and user_wish:
            st.success(f"Message {i + 1} saved!")
            st.markdown(f"**Message {i + 1}:** {user_wish}")

    st.markdown("---")
    st.write("Let's cherish the moments and celebrate the love!")
    
    st.sidebar.markdown("---")
    st.sidebar.write("Created with ❤️ by Tio")

if __name__ == "__main__":
    main()
