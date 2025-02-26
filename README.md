# 🛠️ CraftMyAI

## Personalized AI Solutions for Businesses and Individuals

![CraftMyAI Banner](https://images.pexels.com/photos/6153068/pexels-photo-6153068.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)

[Visit Website](https://craftmyai-solutions.streamlit.app/) | [Contact Us](mailto:help.craftmyai@gmail.com)

## 🚀 About CraftMyAI

CraftMyAI specializes in developing custom AI solutions tailored to the unique needs of businesses and individuals. We believe in making AI accessible to everyone, regardless of technical background or business size.

### Our Mission

Deliver high-quality AI solutions with seamless support, making advanced technology accessible to all businesses.

### Why Choose Us?

- 🤖 **Personalized AI solutions** built specifically for your needs
- 🛠️ **1-month free support** after project delivery
- 💰 **Transparent pricing** based on project complexity
- 🚀 **Affordable MVPs** to kickstart your ideas
- 🎨 **Customization at every step** of the development process

## 📋 Features

- **Request Portal**: Submit your AI project requirements through our easy-to-use form
- **Project Tracking**: Keep track of your project's status
- **Admin Dashboard**: For our team to manage projects and client communications
- **Feedback System**: Share your experience to help us continuously improve

## 💻 Tech Stack

- **Frontend & Backend**: Streamlit
- **Database**: SQLite
- **Email Integration**: Native email client integration

## 🔧 Installation & Setup

### Prerequisites

- Python 3.7+
- pip

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/craftmyai/craftmyai-platform.git
cd craftmyai-platform
```

2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create secrets file**

Create a `secrets.toml` file in the `.streamlit` directory in the root folder with the following variables:

```
ADMIN_USERS=[admin1,admin2]
ADMIN_PASSWORDS=[password1,password2]
```

5. **Run the application**

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 🔒 Admin Access

For admin access, use the credentials defined in your `.env` file. The admin dashboard allows:

- Managing project requests
- Assigning projects to team members
- Updating availability status
- Adding new projects directly

## 📱 Usage

### For Clients

1. Visit the website
2. Navigate to "Request AI Solution"
3. Fill out the project details form
4. Submit your request
5. Our team will contact you to discuss your project further

### For Admins

1. Log in to the Admin Panel
2. View pending project assignments
3. Accept or reject project assignments
4. Manage assigned projects
5. Add new projects as needed

## 🤝 Contributing

We welcome contributions to improve CraftMyAI. Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📞 Contact

- **Email**: help.craftmyai@gmail.com

## 📃 License

This project is licensed under the MIT License - see the LICENSE file for details.