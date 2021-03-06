class SqlQueries:
    create_dimension_table = ("""
        CREATE TABLE IF NOT EXISTS public.dimension_state (
        state_key varchar(2) NOT NULL,
        state_name varchar(256),
        average_age float8,
        female_urban_population bigint,
        male_urban_population bigint,
        total_urban_population bigint,
        CONSTRAINT state_key_pkey PRIMARY KEY(state_key))
    """)
    create_fact_table = ("""
        CREATE TABLE IF NOT EXISTS public.fact_arrivals ( 
        state_key varchar(2),
        month integer,
        year integer,
        average_age_arrivals float8,
        F bigint,
        M bigint,
        U bigint,
        X bigint,
        business bigint,
        pleasure bigint,
        student bigint,
        average_temperature float8,
        CONSTRAINT arrivals_id_pkey PRIMARY KEY(state_key, month, year),
        CONSTRAINT state_key_fk
        FOREIGN KEY (state_key)
        REFERENCES dimension_state(state_key))
    """)
