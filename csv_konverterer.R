## Converts the raw NVE offshore windspeed RDS file into a CSV that the
## rest of the pipeline (splitting_data.py, program.py, Masteroppgaven.ipynb)
## expects to find in the project root.
##
## Run this first, before splitting_data.py:
##   Rscript rcdtodvc.R

rds_path <- "offshore_windspeeds_NVE_areas.rds"
csv_path <- "offshore_windspeeds_NVE_areas.csv"

df <- readRDS(rds_path)

cat("Rows:", nrow(df), " Cols:", ncol(df), "\n")
str(df)

write.csv(df, csv_path, row.names = FALSE, fileEncoding = "UTF-8")

cat("Saved", nrow(df), "rows to", csv_path, "\n")