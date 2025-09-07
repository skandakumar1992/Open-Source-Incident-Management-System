Open-Source Incident Management System

In the VM machine(Ubuntu) the following commands are as follow.

Step 1.
⦁	sudo apt update

⦁	sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

⦁	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

⦁	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

⦁	sudo apt update
⦁	sudo apt install docker-ce docker-ce-cli containerd.io -y

⦁	docker --version
⦁	sudo usermod -aG docker $USER

step 2.Setup Flask App-run.py and app/__init__.py

step 3. Database Models-app/models.py

step 4. Routes & REST APIs-app/routes.py

step 5. Email Utility-app/email_utils.py

step 6. Docker Setup-Dockerfile and requirements.txt

Build and run Docker image:

docker build -t incident-management-app .
docker run -p 5000:5000 incident-management-app

step 7. Push to Git & GitHub
        git init
        git add .
        git commit -m "Initial commit"
        git branch -M main
        git remote add origin https://github.com/skandakumar1992/Open-Source-Incident-Management-System.git
        git push -u origin main

step 8. Sample Data & Demo
        Sample API Calls: 
        1.Create Incident
           POST http://localhost:5000/api/incidents
Content-Type: application/json

{
    "title": "Database Down",
    "description": "Main DB is not reachable",
    "reporter_id": 1,
    "assignee_id": 2
}

         2.Update Incident
           PUT http://localhost:5000/api/incidents/1
Content-Type: application/json

{
    "status": "Resolved"
}

          3.List Incidents
            GET http://localhost:5000/api/incidents
