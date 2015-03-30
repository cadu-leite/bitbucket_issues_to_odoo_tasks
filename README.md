# bitbucket_issues_to_odoo_tasks
A durty script to import issues from BitBucket export file, into ODOO csv file


##Waht it does ?

After export the  Bitbucket issues to a JSON file, from the _settings/import/export/_  in your  Bitnucket repo.
Download the _.zip_ file e extract the json.

This script will import all the issues to an ODOO project 

in the repo, you may find an output sample CSV file (_sample_output_odoo_import_me.csv_)


###What it import:
 -  Assingned user
 -  last updated date
 -  issues status
 -  issue description
 -  issue title


###What it does not import ?

It will not import _yet_
 - Files atacheds
 - Followers
 - comments.
 - tags...

## How !

to migrate issues from BitBucket to ODOO
We need to map :

1. Users: Users on ODOO have no nickname (at last, i didint found yet).
2. STATUS: issues status will task stages on Kanban board.
3. fields: You may use the sample file on this repo.

On this repo you will find a simple sample file for every case ... its simple, just rewrite it.


