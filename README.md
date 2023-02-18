# Prueba tecnica

Instructions for running the script

1. Install the required packages with "$ pip install -r requirements.txt"
2. Set enviroment variable "covid19_database" with the URI of the desired database, in my case I used elephantSQL free plan.
3. Run "python3 main.py" th get the data from the dataset and push it to the Postgres table
4. Different url can be passed via parameter e.x. "python3 main.py https://analisi.transparenciacatalunya.cat/resource/irki-p3c7"
