import urllib.parse
import streamlit as st
from database import (accept_assignment, add_project, assign_project,
                      delete_project, get_assigned_projects, get_availability,
                      get_pending_assignments, get_projects, init_db,
                      reject_assignment, update_availability)


# Load admin credentials from Streamlit secrets
ADMIN_USERS = st.secrets["ADMIN_USERS"]
ADMIN_PASSWORDS = st.secrets["ADMIN_PASSWORDS"]

# Initialize DB
init_db()

# Load project availability from the database
availability_status = get_availability()
ACCEPTING_PROJECTS = availability_status["accepting"]
REOPEN_DATE = availability_status["reopen_date"]

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
    [
        "🏠 Home",
        "📩 Request AI Solution",
        "📝 Feedback",
        "📞 Contact Us",
        "ℹ️ About Us",
        "🔐 Admin Panel",
    ],
)

# Home Page
if page == "🏠 Home":
    st.title("🛠️ Welcome to CraftMyAI")

    st.write("")
    if ACCEPTING_PROJECTS:
        st.success("✅ We are currently accepting new requests!")
    else:
        st.warning(
            f"⚠️ We are **not accepting new requests** right now. Next availability: **{REOPEN_DATE}**."
        )
    st.write("")

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
    st.write("")
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
    else:

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


# Authentication Variables
if "logged_in_admin" not in st.session_state:
    st.session_state.logged_in_admin = None

# Admin Panel Authentication
if page == "🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    st.write("")
    if st.session_state.logged_in_admin is None:
        admin_username = st.text_input("Admin Username:")
        admin_password = st.text_input("Admin Password:", type="password")

        if st.button("Login"):
            if (
                admin_username in admin_users
                and admin_passwords[admin_users.index(admin_username)] == admin_password
            ):
                st.success(f"✅ Welcome, {admin_username}!")
                st.session_state.logged_in_admin = admin_username  # Store in session
                st.rerun()
            else:
                st.error("❌ Incorrect credentials! Access denied.")
                st.stop()
    else:
        st.success(f"✅ Logged in as {st.session_state.logged_in_admin}")

        if st.button("Logout"):
            st.session_state.logged_in_admin = None
            st.rerun()

        logged_in_admin = st.session_state.logged_in_admin

        # Project Availability Management
        st.write("")
        st.write("")
        st.subheader("Project Availability")
        st.write("")
        accepting_projects = st.checkbox(
            "Accepting New Projects", value=ACCEPTING_PROJECTS
        )
        reopen_date = st.text_input("Reopen Date", REOPEN_DATE)

        if st.button("Update Availability"):
            update_availability(accepting_projects, reopen_date)
            st.success("✅ Availability Updated!")
            st.rerun()
        st.write("")
        st.write("")

        # Pending Project Assignments section
        st.subheader("Pending Project Assignments")
        st.write("")
        pending_assignments = get_pending_assignments(logged_in_admin)

        if not pending_assignments:
            st.info("You have no pending project assignments.")
        else:
            for assignment in pending_assignments:
                st.write("")
                st.write(f"**{assignment[1]}**")
                st.markdown(f"```\n{assignment[2]}\n```")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"✅ Accept", key=f"accept_{assignment[0]}"):
                        accept_assignment(assignment[0])
                        st.success(f"Project '{assignment[1]}' accepted!")
                        st.rerun()
                with col2:
                    if st.button(f"❌ Reject", key=f"reject_{assignment[0]}"):
                        reject_assignment(assignment[0])
                        st.success(f"Project '{assignment[1]}' rejected!")
                        st.rerun()
                st.write("")
        st.write("")
        st.write("")

        # Project Management
        st.subheader("Unassigned Project Requests")
        st.write("")
        project_list = get_projects(assigned=False)
        if not project_list:
            st.info("No unassigned projects.")
        for project in project_list:
            st.write("")
            st.write(f"**{project[1]}**")
            st.markdown(f"```\n{project[2]}\n```")

            # Create a selectbox for admin assignment
            selected_admin = st.selectbox(
                f"Assign to admin:", admin_users, key=f"admin_select_{project[0]}"
            )

            if st.button(f"📝 Assign to {selected_admin}", key=f"assign_{project[0]}"):
                assign_project(project[0], selected_admin, logged_in_admin)
                st.success(f"✅ Project '{project[1]}' assigned to {selected_admin}!")
                st.rerun()
            st.write("")
        st.write("")
        st.write("")

        # Assigned Projects (For logged in admin)
        st.subheader("Your Assigned Projects")
        st.write("")
        assigned_projects = get_assigned_projects(logged_in_admin)

        if not assigned_projects:
            st.info("You have no assigned projects.")
        else:
            for project in assigned_projects:
                st.write(f"**{project[1]}**")
                st.markdown(f"```\n{project[2]}\n```")
                if st.button(f"❌ Delete {project[1]}", key=f"delete_{project[0]}"):
                    delete_project(project[0])
                    st.rerun()
        st.write("")
        st.write("")

        # Add New Project
        st.subheader("Add a New Project")
        st.write("")
        new_project_name = st.text_input("Project Name")
        new_project_description = st.text_area("Project Details")

        if st.button("Add Project") and new_project_name and new_project_description:
            add_project(new_project_name, new_project_description)
            st.success(f"✅ Project '{new_project_name}' added!")
            st.rerun()

        st.write("")
        st.write("")

# TODO: Add a client dashboard with messaging support