# Backend-TDL
- BACKEND-TDL is a django rest framework API to serve Frontend-TDL. A to-do-list application. This api is used for user management, authentification, and CRUD of the tasks.
## Installation
1. clone the repository
2. Create a python virtual environment (Pipenv for example)
3. Install all the dependencies in the requirements.txt with pip install -r requirements.txt
4. Create a .env inside the config folder with the next variables:
   
- SECRET_KEY=(Your secret key)
- EMAIL_HOST_USER=your host user
- EMAIL_HOST_PASSWORD=your email host password
- BACKEND_URL=http://localhost:8000
- FRONTEND_URL=http://localhost:5173
5. Open docker in your desktop
6. run docker-compose up -d --build
7. Enjoy
  
## License

This project is licensed under the [MIT License](LICENSE). You are free to modify and extend this API to suit your needs.

## Contributing

We welcome contributions! If you'd like to improve this project, feel free to fork this repository, make your changes, and submit a pull request.

If you encounter issues or have questions, please open an issue in the repository, and we will do our best to assist you.

