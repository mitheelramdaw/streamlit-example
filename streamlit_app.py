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
    
    messages = [
        "Thank you for the best time of my life Florence. I created this so you can type your relationship thoughts here my love. Happy Anniversary my baby. I love you eternally",
        ''' 
Hey you donut,
I missed you immensely while you were away
It’s like I could feel you going further and further away
Like a kit flying further in the wind
But I still feel our love anchored like the reel of the kite that’s there no matter how far the kit flies 
(This is very different, me expressing my emotions to used to doing it but I’m getting more used to it being in our relationship)

Every day we spend apart feels like I’m at see and can see the land but it goes farther and farther away as the days past
But in reality the island is there it’s just the illusion that’s created by each passing day
No this does not mean my feelings are fading it just feels like I’m away from my happy place
If anything my love for you grows stronger each passing moment 

I have not felt this way about anyone else before
I love you Florence, A LOT A LOT
Whenever I get news you’re the first person I think of
You’re the first person I want to share my news with
You’re my first and last thought (yes even the nights I fall asleep early, I apologise for that but even those nights you are my last thought)
I constantly think about you and us and our future together
I always want to improve and be a better boyfriend
I know I’m not perfect I’m far from that, but I’m trying my best for you and for us
I will get better as time goes on 


You’re my everything and I mean that when I say it.
All I want is to make you happy and give you the best that I possibly can.
There is no other person I would rather spend my life with than you .
I chose you and I will always chose you Florence./
~ Love Your Boyfriend
~ Tio''',
        "Baby,\nI am sorry I fall asleep sometimes without saying goodnight...",
        ''' 
Baby,

I am sorry I fail asleep sometimes without saying goodnight
I know it doesn’t seem like I’m trying not to sleep but I am
I wait up and then all of a sudden I’ve fallen asleep
I try to stay up to not let you down so I don’t say goodnight at a that moment because I want to talk to you
But then I end up crashing and sleeping and not saying goodnight 
So it’s a paradox, by trying not to let you down I end up letting you down


I love you so much and I know saying goodnight before we sleep is important to you 
I do take it seriously and I try my best to do it every night
I’m sorry that I mess api and don’t do it she nights
I hope you know this doesn’t mean my feelings for you are any different because I fall asleep before saying goodnight some nights
I also hope it doest change how you view me and our relationship

I am trying my best and I’m going to try better
I know you have told me to say goodnight even mid conversation 
I am working on getting better at that
I love you and I’m going to do my best to make you happy and keep us together
You are the best thing to happen to me 
I hope you know that I don’t talk you for granted
I am immensely appreciative to have you in my life and as my amazing girlfriend


I am sorry and I apologise for all of my shortcomings and mess ups 
~ Love Your Boyfriend
~ Tio''',
        '''
Every time I look into your eyes
It’s like I’m look into the night sky at the stars
Sitting besides you in the lecture rooms it feels out of this world
It’s kinda like sitting on mars
Your smile as bright as the sun
Whenever I’m with you i feel better than a kid having fun
I love your hair, I love your nose
You’re more mesmerising than any rose 
I love your height 
Marry you ? I just might
When I’m with you, I get this feeling 
The feeling of love get’s me high as a kite
For you I will always fight
With you in my future it seems real bright

I love you
My intentions are always true 
You love me, 
Sorry I always update you when I go and p
You fill my heart with joy and glee
With you in my life I feel free
I will always support you like the roots of a tree

You are Gods favourite creation
You are my entire inspiration 
You are an angel 
You are my princess
Like in a fable
For you my love I must confess

You are a diamond in the rough
I know being in a relationship is tough
You can always call my bluff
When I pretend to be fine but I’m stuck like a golf ball in the rough
You see through me like glass
I love my chain that looks like brass
I love that you believe I am the genius in and out of the glass

When I hear “Florence” all I can do is smile
Just as I do when I type this text file
I haven’t seen you in a while
To come and see you i’d walk that mile
My love for you would overflow the Nile
My love for you is so strong it couldn’t be contained in a vile

I mumble and I fumble
I fall and I learn 
For your presence I yearn 
I’m sure you are tired of me talking
I say I love you 
Now it’s your turn 

I love you baby

~ Love Your Boyfriend 
~ Tio


''',
        '''
Hey baby

I miss you, I constantly think about you
I smile, I frown, I laugh, I ponder
I ride the emotional rollercoaster of missing you
I think about you
I hear your voice
I think of your kindness, your generosity, your beautiful heart and personality
I miss speaking to you

Your calls make me so excited, hearing your voice soothes me like no other
I feel calm, I feel collected
I am happy I am ecstatic
I feel the waves of emotions that are just the surface of feelings I have for you

I want to spend my life with you
And I hope and pray that we do stay together
You make me a better version of myself
You give me a different perspective
Together we are the dream team

I love you with every fibre of my being
You are my motivation and inspiration to be a good person
Thank you for give me the opportunity to be your boyfriend
I cannot express how grateful I am to be part of your life 
Thank you for choosing me and being with me 
I am eternally grateful to have you in my life and to call you my girlfriend

I love you like a mathematician loves math
I love you like a developer loves code
I love you like how Ronaldo loves football
I love you like a baker loves bread
I love you like Florence loves Too

I love you Florence

~ Love Your Boyfriend
~ Tio''',
    ]
    
    if num_messages > len(messages):
        messages.extend([""] * (num_messages - len(messages)))

    for i in range(num_messages):
        st.subheader(f"Message {i + 1}")
        user_wish = st.text_area(f"Leave your message {i + 1} here", height=150, key=f"message_{i}", value=messages[i])
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
