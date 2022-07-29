# ZeventQuizz - The best Quizz in the world

![Pytest](https://github.com/Seedsir/zeventquizz/actions/workflows/pytest.yml/badge.svg)

## Requirements
- Docker
- Docker compose
- minikube
- kubectl
- helm

## Test localy without docker
- run ```gunicorn```

## Test app localy with docker
- inside the repo run ```docker-compose up```
- You can call ```http://localhost:5000```

## To deploy locally
- Run ```docker-compose up``` to build the image
- run ```eval $(minikube docker-env)```
- Start minikube: ```minikube start```
- Run ```minikube tunnel``` to make future services available
- Run ```helm install zeventquizz .``` to deploy the app on minikube
- To check: ```kubectl get services``` you should have a zeventquizz line with an external ip
- You can call this ip on port 5000

## To uninstall the app
- run ```helm uninstall zevent```

## You change the code and want to redeploy
- rebuild the image ```docker-compose rebuild```
- then upgrade the release ```helm upgrade zeventquizz .```

