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
- Implementing, setting up, deloying azure function, the service bus doesn't take too much effort.
