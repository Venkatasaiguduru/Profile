import streamlit as st
from PIL import Image




# Sidebar
st.sidebar.title("About")
# st.sidebar.markdown("## Sections")
with st.sidebar:
    selection=st.radio("Details", ["About Me", "Skills", "Projects & internships","Certifications & Licenses","Contact Information"])
# side = ["About Me", "Skills", "Projects", "Contact Information"]
# selection = st.sidebar.radio("Details",side)

# Main Page
st.subheader("PROFILE")
# st.image("GVS.jpg", caption="Picture")
image = Image.open("GVS2.png")
width, height = image.size
st.image(image, width=300)
st.title("GUDURU VENKATASAI")

if selection == "About Me":
    st.header("About Me")
    st.text("Dedicated Electrical and Electronics Engineering, excelling in both core engineering & software development. With a solid foundation in core engineering and a proficient in python programming & basic java. passionate, adaptable, and always eager to learn and contribute to impactful project.")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/guduru-venkatasai-5aaa69294/)")
    st.markdown("[GitHub](https://github.com/Venkatasaiguduru)")

elif selection == "Skills":
    st.header("Technical Skills")
    st.text("Programming Languages: Python programming and Basic Java")
    st.write("Internet of Things")
    # st.write("Basic Java")
    st.write("Basic Artifical intellience")
    st.write("Basic Matlab & Simulation")
    
    st.header("Soft skills")
    st.write("Team work")
    st.write("Leadership skills")
    st.text("Time Management")
    st.header("Other skills")
    st.write("Graphic Design like Logos,banners,Thumbnails etc..")
    

elif selection == "Projects & internships":
    st.header("Projects")
    st.subheader("1.LPG GAS DETECTION AND ACTIVATION OF EXHAUST FAN ")
    st.text("The project aims to develop an automatic LPG gas leakage detection system that can sense the presence of leaked gas and activate an exhaust fan to vent the gas out, thus reducing the risk of accidents. Additionally, the system should provide alerts to ensure timely awareness and action")
    st.link_button("View project","https://www.linkedin.com/posts/guduru-venkatasai-5aaa69294_innovation-engineering-automation-activity-7267555123470438401-H_3p?utm_source=share&utm_medium=member_desktop")
    st.header("Internships")
    st.subheader("1.ANSYS ELECTROMAGNETIC ANALYSIS VIRTUAL INTERNSHIP! by AICTE,EDUSKILLS")
    st.text("Platforms: AICTE National Internship Portal, Eduskills foundation & Ansys.") 
    st.text("Description: The internship focuses on electromagnetic analysis, offering practical knowledge and online courses.Completed a virtual internship focused on electromagnetic analysis using ANSYS software.Earned a course completion certificate and an internship certificate from AICTE and EduSkills")
    st.text("Duration: Typically 2 months")
    st.link_button("Click to View","https://www.linkedin.com/posts/guduru-venkatasai-5aaa69294_internship-certification-activity-7241672347718447104-5JAX?utm_source=share&utm_medium=member_desktop")
    st.subheader("GOOGLE AI-ML by AICTE,EDUSKILLS")
    st.text("Platforms: AICTE National Internship Portal, Eduskills foundation & Google.") 
    st.text("Description: The internship focuses on AI & ML, offering extreme knowledge and online courses.Completed a virtual internship focused on AI & ML,Earned a course completion certificate and an internship certificate from AICTE and EduSkills")
    st.text("Duration: Typically 2 months")
    st.link_button("Click to View","https://www.linkedin.com/posts/guduru-venkatasai-5aaa69294_google-ai-ml-activity-7274737669757091840-bhNG?utm_source=share&utm_medium=member_desktop")
elif selection == "Certifications & Licenses":
    st.header("Certifications & Licenses")
    st.write("1.Career Essentials in Generative AI by Microsoft and LinkedIn")
    st.link_button("Click to View","https://www.linkedin.com/learning/certificates/5734f5d2d0900ded3c90b0e27568a99e73eee850a1134f883b9a5cd1018a33e5?trk=share_certificate")
    st.text("2.Introduction to IoT")
    st.link_button("Click to View","https://www.credly.com/badges/636b9d0e-2d93-461c-8d53-344fb2fee0b2/linked_in_profile")
    st.text("3.Python Essentials 1")
    st.link_button("Click to View","https://www.credly.com/badges/b14d2c0e-2581-45ba-9771-2620b47b6867/public_url")
    st.text("4.Python Essentials 2")
    st.link_button("Click to View","https://www.credly.com/badges/5ed6a191-2c50-49d1-aa63-f8b499d65ccd/public_url")


elif selection == "Contact Information":
    st.header("Contact Information")
    st.text("Email: venkatasaiguduru@gmail.com")
    st.text("Phone: 8688931401")



