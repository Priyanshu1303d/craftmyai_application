import os
import urllib.parse

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ACCEPTING_PROJECTS = os.getenv("ACCEPTING_PROJECTS", "False").lower() == "true"
REOPEN_DATE = os.getenv("REOPEN_DATE", "TBA")

# Set page config
st.set_page_config(page_title="CraftMyAI - AI Solutions", page_icon="🛠️", layout="wide")

# Center align the app
st.markdown(
    """
    <style>
        .block-container { max-width: 800px; margin: auto; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("CraftMyAI")
page = st.sidebar.radio(
    "",
    ["🏠 Home", "📩 Request AI Solution", "📝 Feedback", "📞 Contact Us", "ℹ️ About Us"],
)

# Home Page
if page == "🏠 Home":
    st.title("🛠️ Welcome to CraftMyAI ")

    if ACCEPTING_PROJECTS:
        st.success("✅ We are currently accepting new requests!")
    else:
        st.warning(
            f"⚠️ We are **not accepting new requests** right now. Next availability: **{REOPEN_DATE}**."
        )

    st.subheader("Get your custom AI solutions, tailored to your needs.")
    st.markdown(
        """
        - 🤖 **Personalized AI solutions** for businesses and individuals
        - 🛠️ **1-month free support** after delivery
        - 💰 **Transparent pricing based on complexity**
        - 🚀 **Affordable MVPs to kickstart your idea**
        - 🎨 **Customization at every step**
        
        🔥 **Let's bring your AI vision to life!**
    """
    )
    st.image(
        "https://images.pexels.com/photos/6153068/pexels-photo-6153068.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        width=800,
    )

# Request AI Solution Form
elif page == "📩 Request AI Solution":
    st.title("📩 Request Your AI Solution")

    if not ACCEPTING_PROJECTS:
        st.warning(
            f"🚧 We are not accepting new requests until **{REOPEN_DATE}**. You can still submit, and we will respond when available."
        )

    with st.form("ai_request_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        project_details = st.text_area("Project Description")
        budget = st.number_input("Estimated Budget (in INR)", min_value=0, step=100)
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        if name and email and project_details:
            recipient_email = "help.craftmyai@gmail.com"
            subject = urllib.parse.quote("New AI Solution Request")
            body = urllib.parse.quote(
                f"Name: {name}\nEmail: {email}\nBudget: ₹{budget}\n\nProject Details:\n{project_details}"
            )
            mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"
            st.success(
                f"✅ Thank you {name}! Click the button below to send your request via Gmail."
            )
            st.markdown(f"📩 [Send Email]({mailto_link})", unsafe_allow_html=True)
        else:
            st.error("⚠️ Please fill in all required fields before submitting.")

# Feedback Page
elif page == "📝 Feedback":
    st.title("📝 CraftMyAI Feedback Form")
    st.write("We value your feedback! Help us improve by sharing your thoughts.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    rating = st.slider("Rate your experience (1-5)", 1, 5, 3)
    feedback = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        if name and email and feedback:
            recipient_email = "help.craftmyai@gmail.com"
            subject = urllib.parse.quote("CraftMyAI Feedback")
            body = urllib.parse.quote(
                f"Name: {name}\nEmail: {email}\nRating: {rating}/5\n\nFeedback:\n{feedback}"
            )
            mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"
            st.success(
                f"✅ Thank you {name}! Click the button below to send your feedback via Gmail."
            )
            st.markdown(f"📝 [Send Feedback]({mailto_link})", unsafe_allow_html=True)
        else:
            st.error("⚠️ Please complete all fields before submitting.")

    st.write("---")

# Contact Us Page
elif page == "📞 Contact Us":
    st.title("📞 Contact Us")
    st.write("Have questions or want to discuss an AI project? Reach out to us!")

    with st.form("contact_form"):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_contact = st.form_submit_button("Send Message")

    if submit_contact:
        if contact_name and contact_email and message:
            recipient_email = "help.craftmyai@gmail.com"
            subject = urllib.parse.quote("Contact Request")
            body = urllib.parse.quote(
                f"Name: {contact_name}\nEmail: {contact_email}\n\nMessage:\n{message}"
            )
            mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"
            st.success(
                f"✅ Thank you {contact_name}! Click the button below to send your message via Gmail."
            )
            st.markdown(f"📞 [Send Message]({mailto_link})", unsafe_allow_html=True)
        else:
            st.error("⚠️ Please fill in all fields before submitting.")

# About Us Page
elif page == "ℹ️ About Us":
    st.title("ℹ️ About CraftMyAI")
    st.write(
        "We specialize in developing AI solutions tailored for businesses and individuals."
    )
    st.markdown(
        """
        - 🎯 **Mission:** Deliver high-quality AI solutions with seamless support.
        - 🌍 **Vision:** Making AI accessible to businesses of all sizes.
    """
    )
