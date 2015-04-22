# bitbucket_issues_to_odoo_tasks

A durty script to import issues from Bitbucket to [odoo]  former OpenERP


    python main.py  <bitbucket_json_file.json> [-u <users_map.csv>]  [-s <status_map.csv>]  [-f <fields_map.csv>]


##What you need ?

1. Export the  Bitbucket issues.
    2. Go to  _settings/import/export/_  in your  BitBucket repo or  you may use the following url passing _user_ and _repo_ as parameters.

        ```
        http://bitbucket.org/api/1.0/repositories/<user>/<repo>/issues/export/zip
        ```

    It will create a _zip_ file, and will show you a link do download the file.

2. Download the _.zip_ file e extract the _json_ (_ex.:db-1.0.json_).

###What does it import ?
 -  Assingned user
 -  last updated date
 -  issue status
 -  issue description
 -  issue title

###What it does NOT ?

It will not import ... _yet_ !
 - Files attached
 - Followers  
 - comments.
 - tags...

## How !

Before actually due the migration, you need to map some issues data (status, users, ... ) from Bitbucket to [odoo], so you may have different issues types or status for each system.

If you do so, you may use a CSV file to "tell"the script how to translate ...

_ex.: Bitbucket "open" status, to "new" task. on [odoo]_

or

_a user on bitbucket named "ze123" with a odoo name "José Silva"_

Be aware ...

1. Users: Users on ODOO have no nickname (at least, I didint found yet).
2. STATUS: issues status will become task stages on Kanban board.
3. fields: bitbucket issue has a _title_ field, odoo has _summary_  and the list goes on .

On this repo you will find 3 sample files, one for each case ... just rewrite it.

If you nedd no mapping just

    python main.py  <db-1.0.json or whatever you renamed it>

or if you have mapping  ... 

    python main.py  <bitbucket_json_file.json> [-u <users_map.csv>]  [-s <status_map.csv>]  [-f <fields_map.csv>]

In this repo, you will find an output sample CSV file named _sample_  output_odoo_import_me.csv_

[odoo]: Http://www.odooo.com "odoo site"


====================


1. ir no settings do repo para exportar as issues 

    https://bitbucket.org/<username>/<reponame>/admin

1. acesse o menu _import/export_

    https://bitbucket.org/<username>/<reponame>/admin/issues/import-export

1. clique no botão _start export_

 Aguarde, enquanto o bitbucket constroi o arquivo de exportação.
 Quando o arquivo estiver disponível, um link de ddownload (ZIP file) será mostrado em um dialog.



1. Baixe o arquivo e decompacte-o ...


