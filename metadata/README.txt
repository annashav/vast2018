<View dataflow.png for a diagram of the data flow>
This is a list of changes that have been made to the metadata csv,

Versions: AllBirds_clean(1-5)
Changes: - Date Column split into Year, Month and Day column. (Missing values represented by 0)
         - Format of data fixed
         - Entries in the "Time" column that gave general times like "Morning" or "Dusk" changed to AM/PM                      and placed into separate column.

Versions: AllBirds_[COLUMN]
Changes: - Subset of entries with valid values in the given COLUMN.
           - ex. AllBirds_Time contain only rows with valid Time entries 