# bitbucket_issues_to_odoo_tasks
A durty script to import issues from BitBucket export file, into ODOO csv file


>python import_bit2od.py  <bitbucket_json_file.json> -u <users_map.csv>  -s <status_map.csv>  -f <fields_map.csv>


##Waht it does ?

After export the  BitBucket issues to a JSON file, from the _settings/import/export/_  in your  BitBucket repo.
Download the _.zip_ file e extract the json.

    https://bitbucket.org/api/1.0/repositories/<user>/<repo>/issues/export/zip

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
you will need to map :

1. Users: Users on ODOO have no nickname (at last, i didint found yet).
2. STATUS: issues status will task stages on Kanban board.
3. fields: You may use the sample file on this repo.

On this repo you will find a simple sample file for every case ... its simple, just rewrite it.

You need also, a bitbucket export file on JSON format. [Docs here](https://confluence.atlassian.com/display/BITBUCKET/Export+or+import+issue+data) On Export topic.
