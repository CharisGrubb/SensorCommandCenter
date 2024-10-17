
#### Services Flow

```mermaid


flowchart TD



    SCC[Sensor Command Center Main Service]
    AlertServe[Alerting Service]

    webUI[Web Application User Interface]
    desktopApp[Desktop Application]

    SimServ[Simmulation Service]



    SimServ --> SCC
    AlertServe --> SCC
    
    webUI --> SCC
    webUI --> AlertServe

    desktopApp --> SCC
    desktopApp --> AlertServe

```
