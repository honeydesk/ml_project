# ml_project
Welcome to Machine Learning Housing Corporation! The first task you are asked to perform is to build a model of housing prices in California using the California cen‐ sus data. This data has metrics such as the population, median income, median hous‐ ing price, and so on for each block group in California. Block groups are the smallest geographical unit for which the US Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people). We will just call them “dis‐ tricts” for short. Your model should learn from this data and be able to predict the median housing price in any district, given all the other metrics.

Main step for machine Learning Projects.

   1. Look at the big picture.
   2. Get the data.
   3. Discover and visualize the data to gain insights.
   4. Prepare the data for Machine Learning algorithms.
   5. Select a model and train it.
   6. Fine-tune your model.
   7. Present your solution.
   8. Launch, monitor, and maintain your system.

## Application url
[My_web_App -> HousingPreditor](https://ml-regression-tool2.herokuapp.com/) 

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = honeywarid@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir
