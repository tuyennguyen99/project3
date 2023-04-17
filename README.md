# TechConf Registration Website
## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:
Location: East Asia

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |Basic, Gen5 Compute Generation. Cost per vCore = $47.38 + (Cost per GB/month = $0.14) x 5GB selected    | $48.07              |
| *Azure Service Bus*   | Basic ~0.05$/1M operations/month       | $0             |
| Azure Web App         | Linux OS Free tier        | $0             |
| Azure Functions App   | Consumption        | $0             |
| Total                   |         | $48.07              | 


## Architecture Explanation
The TechConf website is a simple website, simple feature and small datasets. 
- Azure Web App is a good choice to reduce delivery effort with CI/CD supported.
- Azure Web App also have scalability by app service plan. We can consider the plan that suitable for application.
- The app service's Free tier and basic plan of Azure Postgres database already suitable with the TechConf website.
The pain point of TechConf website has been resolved with Azure Function - ServiceBusQueueTrigger and Service bus
- Migrating from the normal http request sending email and updating notification to the Azure service bus has resolved the HTTP timeout issue.
- Implementing, setting up, deloying azure function, the service bus doesn't take too much effort. We can manage all the resource in the portal with useful tools provided by Microsoft (Cost Analysis, Budget alert, Monitoring, Automate deployment, etc.). All those setting up actions is completed within 2 hours.
- Azure functions is a serverless solution, so we don't need to write more code and just focus on the logic. In the Techconf app, we use ServiceBusQueueTrigger, we just need to implement the logic to update the notification and send email to all attendees. Azure service bus will handle other related works.
- Azure service bus help to decouple applications and services from each other as a message broker. In Techconf app, using Azure service bus help to move the long time process logic (send email to all attendees and update notification status) out of HTTP request to avoid HTTP timeout. 
For each HTTP request to submit notification, 1 message will be sent and service bus will take that message and process the logic by the connected ServiceBusQueueTrigger.

- Setting up Service bus:
   1. Create Service Bus namespace in azure portal.
   2. Create queue in service bus namespace.
- Implementing, deploying Azure function ServiceBusQueueTrigger just take a few steps.
   1. Create azure function ServiceBusQueueTrigger
   2. Implement code logic for ServiceBusQueueTrigger
   3. User azure tools, azure cli or CI/CD to deploy function.
   4. Implement send message logic in the application.
   5. Setup connection string to connect Trigger with service bus namespace.
   6. Setup connection to connect Trigger with Azure Postgres Database

