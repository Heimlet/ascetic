[//]: # (<div align='center'><img src=''/></div>)

<h2>About the project</h2>

<p>This is a ascetic e-commerce website built with Vue3 and CSS and Django DRF. This
website features a modern and intuitive design, with easy-to-use navigation and a
simple shopping experience that puts the focus on the products.</p>

<p>Credits for the design goes to <a href='https://github.com/Abderraouf-Rahmani'>Abderraouf</a></p>

👉 Live Demo: <a href='https://example.com'>Ecommerce Demo</a>

<h3>Build with:</h3>

» Docker <br>
» Django DRF API <br>
» Vanilla CSS <br>
» VueJS

<h2>Screenshots of the Project 📸</h2>
<br>
<h3 align='center'>Home Page 🏡</h3>

<div align='center'>

[//]: # (<img src=''/>)
</div>

<br><br>
<h3 align='center'>Categories Page 👇</h3>

<div align='center'>

[//]: # (<img src=''/>)

<br>
<br>
<h3 align='center'>Product Page 🎁</h3>

<div align='center'>

[//]: # (<img src=''/>)

<br>
<br>
<h3 align='center'>Shopping Cart 🛒</h3>

<div align='center'>

[//]: # (<img src=''/>)
</div>


## For developers
To get started with the project, follow these steps:
1. Install Docker

2. Clone the repository:
```
git clone https://github.com/Heimlet/ascetic.git
cd ascetic
```

3. Set up and modify .env file from .env.example
```
cp .env.example .env
```

4. Run Docker Container
```
docker-compose up --build -d
```

5. Run populate_data management command at backend container
```
docker-compose exec web python3 manage.py populate_data
```