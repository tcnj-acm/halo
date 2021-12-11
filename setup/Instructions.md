# Instructions

*How to use setup scripts for database*

Right now, the database is centralized to MySQL through HPC in TCNJ. Before, we were working with sqlite3. The database was not ignored in the repo and everyone would be pulling and pushing. Merge conflicts would arise because of this. 

Before we migrated to a centralized DB, I built a system that would allow people to populate the database every time they pull a branch to begin work. When pushing, the database is ignored. Should a feature be developed wherein data is required, it is the developer's responsibility to build test data and add script file that can populate the tables accordingly.

TODO: Add a script template for people to use to build test data



## How to use

1. Activate `pipenv` shell 

2. Navigate to the setup directory

3. Run `sh run_create_db.sh`

   