# Cross regional resilient ML service!

Use Case

As the customers adopt cloud, application resiliency and high availability are critical components of their cloud architecture. 
Enterprise customers are adopting AI/ML at a rapid pace and would like ML applications to follow the same resiliency architecture as their other apps.
Azure PaaS Services like Azure ML and AKS offer availability SLA which apply within a single region.

Current resiliency architecture offered by Azure ML and AKS does not protect system from a regional failure.
Regional outage could result in application downtime for Customers or their ability to access predictive model service hosted on Azure ML attached AKS cluster

Design Decisions

Azure ML webservice hosted on attached AKS
Cross regional load balancing between two AKS clusters with Azure Front Door
Use Azure Function to wrap Azure ML webservice
Use Front door vs Traffic manager for latency

![image](https://user-images.githubusercontent.com/79932367/119146104-4c7a5880-ba18-11eb-986d-5ffd54fb59b7.png)

![image](https://user-images.githubusercontent.com/79932367/119147466-9e6fae00-ba19-11eb-858e-12b7784b4b87.png)









