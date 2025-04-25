```mermaid 

graph LR;

db1[(Embedded Database)]-->DB_Interface;
db2[(Optional External Database)]-->DB_Interface;
DB_Interface-->DB_Handler;
DB_Handler;
subgraph API;
Sensors-->AUTH;
Users-->AUTH;
Health-->AUTH;
end;
AUTH-->DB_Handler;
Logging-->DB_Handler;
```