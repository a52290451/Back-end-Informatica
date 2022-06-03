docker.exe build -t ndmunozc/tendencias-back .
docker.exe run -d -p 5000:5000 ndmunozc/tendencias-back:latest .