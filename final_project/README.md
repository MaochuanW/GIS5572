**Introduction**

This final project for GIS 5572 focuses on developing an automated, real-time pipeline system to monitor the spread of the Brown marmorated stink bug in Minnesota. The pipeline leverages three distinct models - Gravity, Monte Carlo, and Huff - to simulate the potential dispersion patterns of this invasive species on a monthly basis, based on user-specified input for the year and month.

The automated system processes the output from these models and subsequently uploads the results to a PostGIS database using the shp2pgsql tool. The final map representation, showcasing the spread patterns of the Brown marmorated stink bug, is generated in GeoJSON format and uploaded to ArcGIS Online for easy access and visualization.

In addition, this project employs Google Cloud Run service to host the resulting map layers. This is achieved by utilizing a Dockerfile and requirements file to create a containerized application, ensuring seamless deployment and management of the hosted map layers.

By implementing an automated pipeline system with real-time capabilities for monitoring the Brown marmorated stink bug, this project aims to provide a valuable tool for researchers, policymakers, and stakeholders in Minnesota to better understand and combat the spread of this invasive species.

**Author**
Maochuan Wang
Yaxuan Zhang