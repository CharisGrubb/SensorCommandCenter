## **Author:**             Charis Grubb
## **Create Date:**        September 2nd, 2024
## **Last Updated:**       September 2nd, 2024




#### Non-Functional Requirements

- System shall have the ability to simulate motion and temperature sensors for demonstration.
- System shall be able to alert based on a defined trigger. 
- Triggers for alerts shall be customizable.
- The system shall offer a desktop GUI interface version and a web interface version for network.
- The system shall allow to connect to external database for long term data storage and reporting. 
- The system shall offer an array of reports and dashboard analysis. 
- The command center service shall offer an ability for data and readings to be pushed to the app rather than just pulled.
- No input should be automatically trusted by the system. 
- The system shall have Fail Safe mechanisms. 




#### Functional Requirements 
- System shall offer a service dedicated to integrating to Shelly Sensors via API. 
- The command center service system shall have an API with options for getting and posting data.
- The command center service system API shall require authentication.
- The command center service system API shall house an internal small database that holds configurations and cached data. 
- All input shall go through a sanitization and validation process.
- Every function/action result from an external caller (ex. POST request through an API endpoint) shall be authenticated **before** any action begins. 
- Every function/action shall have logging. 
- Every function/action shall have exception handling around it to ensure the system fails into a safe state. 
- External Database connections offered: MSSQL, Oracle, PostgreSQL, MySQL. 
- The system shall have a failover if it is unable to log to the database, in order to cache logs locally. 
- They system shall have a mechanism to push cached logs into the database once connection is reestablished.
- All registered sensors should have a corresponding UUID known as the sensor ID. The sensor_id should be created upon sensor registration with the app.