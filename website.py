import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1444464666168-49d633b86797?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");   

             background-size:   
 cover;
             background-position: top center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
# HTML code as a multi-line string
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>deeplearning13</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-size: cover;
            color: white;
            font-family: 'Roboto', sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        
        h1 {
            background-color: rgba(0, 128, 0, 0.8);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        
        }
        .upload-form {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        input[type="file"] {
            margin: 10px 0;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: white;
            color: black;
            font-size: 16px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: green;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: darkgreen;
        }
        img {
            margin-top: 20px;
            max-width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }
        
 
    </style>
</head>
<body>
    <h1>Deteksi Klasifikasi Suara Kicauan Burung di Taman Nasional Way Kambas berbasis Deep Learning - Metode Transfer Learning (Arsitektur ConvNeXt)</h1>
    
    <h3>Yuk, Upload disini audionya</h3>
    <div class="upload-form">
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="audio" accept="audio/*" required>
            <input type="submit" value="Upload Audio">
        </form>
    </div>

    <div class="footer">
        <h2><stronng>Kelompok 13 Deep Learning</strong></h2>
        <div>
            <img class="logo" src="https://img.notionusercontent.com/s3/prod-files-secure%2F8cc0a41b-f9e2-4d9a-89b6-094a058ad494%2Fd594354d-d217-4ab5-b188-d31cc44df70f%2F13__1_-removebg-preview.png/freeze?exp=1731781811&sig=jCv2enD3Ca5vs4_NHzkhm36X4QnRGy2YtT0XHxWYhbg" alt="Logo ITE">
        </div>
        <h3>Beranggotakan</h3>
        <h4>Rizki Adrian Bennovry-121450073 | Project Manager</h4>
        <h4>Alber Analafean-121450146 | Research & Development Manager</h4>
        <h4>NabIlah Andika Fitriani-121450139 | Data Collection & Processing Manager</h4>
        <h4>Catherine Firdhasari Maulina Sinaga-121450072 | Modelling Manager </h4>
        <h4>Helma Lia Putri-121450100 | Modelling Manager</h4>

        <div> 
        <img src="https://img.notionusercontent.com/s3/prod-files-secure%2Fb0b4b79c-5177-448e-9165-4c94954ca2e5%2F48785cbc-2351-40f6-ba8c-ed067724e62d%2FScreenshot_2024-11-16_024946.png/freeze?exp=1731701279&sig=bwwwamNJyODSO_kI51QpD3pr5D-VVQM6ZXxwOQZ2jHk" alt="Logo 0" width="75" height="75">
        <img src="https://img.notionusercontent.com/s3/prod-files-secure%2Fb0b4b79c-5177-448e-9165-4c94954ca2e5%2F74a7d55a-9eed-40c6-ae67-42c77432d433%2F01._Logo_itera.png/freeze?exp=1731700710&sig=wRncR5IAnxyI9C6C9lxNrfQpHI8U9IZ_VVSPSgtRGbk" alt="Logo 1" width="75" height="75">    
        <img src="https://img.notionusercontent.com/s3/prod-files-secure%2Fb0b4b79c-5177-448e-9165-4c94954ca2e5%2F3d0d1b32-b8fc-471d-9931-cf2574fbda70%2FLogo-FSains.png/freeze?exp=1731700469&sig=m0nf6_V7_yI87n2FRu3qpHInCkuq3Bcwj9hpivkJXg8" alt="Logo 2" width="75" height="75"> 
        </div>
        <h5><strong>Program Studi Sains Data, Fakultas Sains, Institut Teknologi Sumatera - Taman Nasional Way Kambas</strong></h5>
        <h5><strong>Dibuat untuk memenuhi Project Based Learning Mata Kuliah SD4102 Deep Learning</strong></h5>
        <h2><strong>#ITERAFORSUMATERA</strong></h5>
    </div>
        
</body>
</html>
"""

# Display the HTML in Streamlit
st.components.v1.html(html_code, height=1200, scrolling=False)

