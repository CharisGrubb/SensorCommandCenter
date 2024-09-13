CREATE IF NOT EXISTS Sensors(
    sensor_id text not null PRIMARY KEY--UUID
    ,sensor_name text -- personal identifier/label 
    ,sensor_model text -- Shelly, Bosch, Honeywell, etc...
)