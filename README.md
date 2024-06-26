Step-by-Step Process to Run Word Count and PageRank with PySpark on Kubernetes
Step 1: Prepare the Input Data
•	Create an input file that represents the graph structure. Each line in the file represents a directed edge between two nodes.
•	Upload the input file to a Google Cloud Storage (GCS) bucket.
Step 2: Create the PySpark Script
•	Write a PySpark script to implement the PageRank algorithm. The script reads the input data, computes PageRank values, and writes the output to GCS.
•	Upload the PySpark script to the GCS bucket.
Step 3: Set Up Kubernetes and Spark
•	Set up a Kubernetes cluster if you don’t have one already.
•	Install Spark on your local machine or Cloud Shell environment to use spark-submit.
Step 4: Submit the PySpark Job to Kubernetes
•	Use the spark-submit command to submit the PySpark job to the Kubernetes cluster. This command specifies the master URL, deployment mode, Docker image, and paths to the PySpark script and input data on GCS.
Step 5: Monitor and Verify the Job
•	Monitor the status of the Spark job using kubectl commands to ensure that the job is running successfully.
•	Check the output files in the specified GCS bucket to verify the results of the PageRank computation.

Overview of the Procedure
1.	Prepare Input Data:
o	Create and upload the graph representation file to GCS.
2.	Create PySpark Script:
o	Write and upload the PySpark script to GCS.
3.	Set Up Environment:
o	Ensure Kubernetes cluster is set up.
o	Install and configure Spark.
4.	Submit the Job:
o	Use spark-submit to run the job on Kubernetes.
5.	Verify Output:
o	Monitor the job status and verify the output in GCS.
