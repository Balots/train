#№1. download
python3 -m venv ./my_env 
. ./my_env/bin/activate   
cd /var/lib/jenkins/workspace/download/model		 	
python3 -m ensurepip --upgrade
pip3 install setuptools
pip3 install -r requirements.txt    
python3 ./download.py
#-----------------------

#№2. train_model 
echo "Start train model"	   
python3 ./train_model.py > best_model.txt 
#------------------------

#3. deploy 		   
export BUILD_ID=dontKillMe         
export JENKINS_NODE_COOKIE=dontKillMe
path_model=$(cat best_model.txt) 
mlflow models serve -m $path_model -p 5003 --no-conda & 
#------------------------

#4. healthy (status service)
curl http://192.168.3.23:8080/invocations -H"Content-Type:application/json"  --data '{"inputs": [[ -1.275938045, -1.2340347 , -1.41327673,  0.76150439,  2.20097247, -0.410937195,  0.58931542,  0.1135538,  0.58931542]]}'


#Pipeline - для объедения задач в последовательный конвеер
#pipeline_cars
pipeline {
    agent any

    stages {
        stage('Download') {
            steps {
                
                build job: 'download'
            }
        }
        
        stage ('Train') {
            
            steps {
                build job: 'train_model'
            
            }
        }
        
        stage ('Deploy') {
            steps {
                build job: 'deploy'
            }
        }
        
        stage ('Status') {
            steps {
                build job: 'healthy'
            }
        }
    }
}

