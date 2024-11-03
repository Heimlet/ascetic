<div align='center'><img src='https://github.com/user-attachments/assets/068c3116-ca87-48b8-a015-57a9bc9e5549'/></div>


<h2>About the project</h2>

<p>This is a ascetic e-commerce website built with Vue3 and CSS and Django DRF. This
website features a modern and intuitive design, with easy-to-use navigation and a
simple shopping experience that puts the focus on the products.</p>

<p>This version provides whole refactored vue components and introduces basic backend that allowes anyone to continue real store development.</p>

<p>Credits for the design goes to <a href='https://github.com/Abderraouf-Rahmani'>Abderraouf</a></p>

👉 Live Demo: <a href='https://ascetic.pykharev.ru/'>Ecommerce Demo</a>

<h3>Built with:</h3>
» Django DRF API <br>
» VueJS <br>
» Docker <br>
» PostgreSQL <br>
» Vanilla CSS

<h2>Screenshots of the Project 📸</h2>
<br>
<h3 align='center'>Home Page 🏡</h3>

<div align='center'>

<img src='https://github.com/user-attachments/assets/f3756a81-a2fb-4dea-bd84-518c303ac245'/>

</div>

<br><br>
<h3 align='center'>Categories Page 👇</h3>

<div align='center'>

<img src='https://github.com/user-attachments/assets/ca542bc3-317b-4a16-921b-35efb563ae47'/>

<br>
<br>
<h3 align='center'>Product Page 🎁</h3>

<div align='center'>

<img src='https://github.com/user-attachments/assets/33c2cf38-93c9-4aea-99a7-17e633554338'/>

<br>
<br>
<h3 align='center'>Shopping Cart 🛒</h3>

<div align='center'>

<img src='https://github.com/user-attachments/assets/37a18ede-7f0a-4d3d-a1a0-2c2d12a6ef74'/>
</div>

<h2> For developers </h2>
<div align="left">
To get started with the project, follow these steps:<br>
  
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

5. Run populate_data management command at backend container. This command creates sample projects introduced at preview.
```
docker-compose exec web python3 manage.py populate_data
```
</div>
<h2> Contact </h2>
<b>Feel free to connect with me on <a href='https://www.linkedin.com/in/pykharev/'>Linkedin</a></b>
