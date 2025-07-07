import streamlit as st
from PIL import Image




# Sidebar
st.sidebar.title("About")
# st.sidebar.markdown("## Sections")
with st.sidebar:
    selection=st.radio("Details", ["Professional Summary", "Skills", "Projects & internships","Certifications & Licenses","Contact Information"])
# side = ["About Me", "Skills", "Projects", "Contact Information"]
# selection = st.sidebar.radio("Details",side)

# Main Page
st.subheader("PROFILE")
# st.image("GVS.jpg", caption="Picture")
image = Image.open("GVS2.png")
width, height = image.size
st.image(image, width=300)
st.title("GUDURU VENKATASAI")

if selection == "Professional Summary":
    st.header("Professional Summary")
    st.text("Dedicated and passionate Electrical and Electronics Engineering student, excelling in both core engineering and software development. Has a solid foundation in core engineering and programming. Proficient in Python, circuit design, and MATLAB, with practical exposure to substation systems. Known for being adaptable, always eager to learn and driven to contribute to impactful projects..")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/guduru-venkatasai-5aaa69294/)")
    st.markdown("[GitHub](https://github.com/Venkatasaiguduru)")

elif selection == "Skills":
    st.header("Technical Skills")
    st.write("Programming Languages: Python programming")
    st.write("Basic Data structures and algorithms")
    st.write("Internet of Things")
    st.write("Basic Artifical intellience")
    st.write("Basic Matlab & Simulation")
    st.write("Circuit Design in Tinkercad")
    
    st.header("Soft skills")
    st.write("Team work")
    st.write("Leadership skills")
    st.text("Time Management")
    st.header("Other skills")
    st.write("Graphic Design like Logos,banners,Thumbnails etc..")
    

elif selection == "Projects & internships":
    st.header("Projects")
    st.subheader("1.LPG GAS DETECTION AND ACTIVATION OF EXHAUST FAN ")
    st.text("Designed and implemented a system to detect LPG gas leakage and automatically activate an exhaust fan and sent out leaked gas out through chimney for residential safety. Integrated audible and visual alerts using a buzzer and LEDs for immediate notification.Technologies Used: MQ-6 Gas Sensor, ESP 32, Relay Module, Buzzer, LED, Power Supply Module, Breadboard.")
    st.link_button("View project","https://www.linkedin.com/posts/guduru-venkatasai-5aaa69294_innovation-engineering-automation-activity-7267555123470438401-H_3p?utm_source=share&utm_medium=member_desktop")
    st.subheader("2.Non-Isolated DC-DC Quadratic Voltage Multiplier")
    st.text("Designed a compact DC-DC converter to boost 24V input to 120V output using a smart topology. Employed a single-switch architecture and a quadratic voltage multiplier circuit with effective use of inductors and capacitors.Achieved high voltage gain with minimal ripple, supporting the shift to clean energy mobility Technologies Used: MOSFET (power switch), Inductors, Diodes, Capacitors, Voltage Multiplier Cell (VMC), PWM control, MATLAB/Simulink.")
    st.link_button("View project","https://www.linkedin.com/posts/venkatasaiguduru_dcdcconverter-boostconverter-hydrogenvehicles-activity-7327332590850363392-dSVj?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEdZHhIBRVNnCEsWAXyPGVYYq4F7fXWnzW4")
    st.header("Internships")
    st.subheader("Industrial Training – TS TRANSCO 220/132/33 kV Substation peddur ,Sircilla, Telangana")
    st.text("Gained hands-on exposure to substation operations, high-voltage equipment, and grid infrastructure. Observed real-time load management and system protection mechanisms in power transmission.Assisted in routine inspections, relay testing, and maintenance procedures.Developed a deeper understanding of power distribution, fault analysis, and switchgear operations.")
    st.subheader("ANSYS ELECTROMAGNETIC ANALYSIS VIRTUAL INTERNSHIP! by AICTE,EDUSKILLS")
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



