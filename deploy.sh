
# chmod +x <script>
# run with:
#   bash deploy.sh
docker build -t flaskapp:latest .
docker run -it -d -p 5000:5000 flaskapp
echo Running [flaskapp] on http://localhost:5000
docker ps
