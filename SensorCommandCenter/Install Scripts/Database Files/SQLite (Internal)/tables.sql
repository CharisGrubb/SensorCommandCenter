

CREATE IF NOT EXISTS Users(
    user_id text not null PRIMARY KEY--UUID
    ,username text
    ,user_f_name text
    ,user_l_name text 
    ,user_middle_initial text --additional distinguisher for clients for cases of two users with same first and last name
    ,access_level INT NOT NULL DEFAULT 0, --CRUD operations Binary/bitwise map. READ=1, CREATE=2,UPDATE=4,DELETE=8 
    ,access_until datetime null, --fill in if it's a temp access, NULL if until whenever
    ,account_type text, --Service Account, ALT Acount, AD account, internal account, etc
    ,CHECK(typeof("user_id") = "text" and length("user_id" <=50)) -- Check to control the length of the uuid for data integrity. UUIDs currently are about 36 characters. Allowing extra space for newer uuid types(Security scalability)
    ,CHECK(typeof("user_middle_initial") = "text" and length("user_middle_initial" <=2)) 
  
  ) 



CREATE IF NOT EXISTS Sensors(
    sensor_id text not null PRIMARY KEY--UUID
    ,sensor_name text -- personal identifier/label 
    ,sensor_model text -- Shelly, Bosch, Honeywell, etc...
    ,sensor_type text, -- Temp, motion, etc
    ,import_type int -- 0= manual, 1==auto, 2 = both
    ,create_date datetime,
    ,created_by text REFERENCES Users(User_ID), 
    ,modify_date datetime,
    ,modified_by text  REFERENCES Users(User_ID)--foreign key this to users!
    CHECK(typeof("sensor_id") = "text" and length("sensor_id" <=50))
)


CREATE IF NOT EXISTS Sensor_data_points(
    data_point_id INTEGER PRIMARY KEY --(AKA ROWID) gives each row a unique number id (64 bit signed int)
    ,sensor_id text REFERENCES Sensors(Sensor_id)
    ,int_value integer NULL
    ,dec_number numeric(10,5) NULL --For temps, while real can store a floating point, the numeric type contains more precision, (similar to float vs double in java). 
    ,str_value text NULL
    ,create_date datetime -- time at which this was recorded

)

CREATE IF NOT EXISTS logs(
    log_id INTEGER PRIMARY KEY
    ,user_id text REFERENCES Users(User_ID)
    ,Log_note text
    ,log_type text
    ,log_source text
    ,Create_Date datetime DEFAULT GETDATE(), --Timestamp of action occurred
)