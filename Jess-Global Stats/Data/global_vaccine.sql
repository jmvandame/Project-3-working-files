
DROP TABLE "global_vaccine"
CREATE TABLE "global_vaccine" (
    "Country" VARCHAR(100)   NOT NULL,
    "Capital" VARCHAR(100)   NOT NULL,
    "Latitude" FLOAT   NOT NULL,
    "Longitude" FLOAT   NOT NULL,
    "First_Vaccine_Date" DATE   NOT NULL,
    "Total_Vaccinations" FLOAT   NOT NULL,
    "Persons_Vaccinated_with_1_Dose" FLOAT   NOT NULL,
    "Persons_Fully_Vaccinated" FLOAT   NOT NULL,
    "Nunber_of_Vaccine_Types_Used" FLOAT   NOT NULL,
    "Vaccines_Used" VARCHAR(1000)   NOT NULL,
    "Data_as_of" DATE   NOT NULL,
    CONSTRAINT "pk_global_vaccine" PRIMARY KEY (
        "Country"
     )
);
SELECT *
FROM global_vaccine

