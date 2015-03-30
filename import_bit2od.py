
"""


REFERENCES:

https://github.com/tiangolo/bitbucket_issues_to_redmine_csv/blob/master/bitbucket_issues_to_redmine_csv.py

usage

1 - the maps files muts have NO spaces after comma (wrong ex.:  'xxx, nnnn' - ex.: xxx,nnn)



"""
import json
import csv
from dateutil.parser import parse as date_parse

VERBOSE = False
USER_MAP_FILE = None
STATUS_MAP_FILE = None
FIELDS_MAP_FILE = None
OUTPUT_FILE = None

USER_MAP = {}
STATUS_MAP = {}
FIELDS_MAP = {}


def render_translation_file(csv_map_file):
    map_file = open(csv_map_file)
    map_reader = csv.reader(map_file)
    dict_rendered = dict([row for row in map_reader])
    map_file.close()
    return dict_rendered


def get_issues(bibucket_json_file):
    '''
     loads json file content.
    '''
    file_opened = open(bibucket_json_file)
    json_data = file_opened.read()
    data = json.loads(json_data)
    file_opened.close()

    return data


def create_odoo_csv(bitbucket_json_file):

    data = get_issues(bitbucket_json_file)

    issues = data['issues']

    csv_file = open(OUTPUT_FILE, 'wb')

    #w = csv.DictWriter(csv_file, data['issues'][0].keys(), )
    w = csv.DictWriter(csv_file, data['issues'][0].keys(),  )
    # ['Stage', 'Description', '', '', '', 'Task Summary', '', '', '', 'Assigned to', '', '', '', '', 'Last Stage Update', '', ''])
    #w.writeheader()

    if FIELDS_MAP is not None:
        w.writerow(FIELDS_MAP)

    values = []

    for issue in issues:

        if issue['created_on'] is not None:
            # date parse and trandform to Odoo import format. (yyyy-mm-dd hh:mm:ss)
            issue['created_on'] = date_parse(issue['created_on']).strftime("%Y-%m-%d %H:%M:%S")

        if issue['updated_on'] is not None:
            # date parse and trandform to Odoo import format. (yyyy-mm-dd hh:mm:ss)
            issue['updated_on'] = date_parse(issue['updated_on']).strftime("%Y-%m-%d %H:%M:%S")

        if issue['assignee'] is not None:
            issue['assignee'] = USER_MAP[issue['assignee']]
        else:
            # todo: fix this workaround
            issue['assignee'] = "Administrator"  # seems ODOO does not accept empty assign_to field.

        issue['status'] = STATUS_MAP[issue['status']]

        for key in issue.keys():

            if issue[key] is None:
                issue[key] = ' '
            if isinstance(issue[key], int):
                issue[key] = str(issue[key])

            if isinstance(issue[key], list):
                issue[key] = "[ %s ]" % ("\t".join(values))

            try:  # WORKROUND
                # todo: need fix
                issue[key] = issue[key].encode('utf-8')
            except:
                issue[key] = issue[key]
            issue[key] = issue[key].replace("\n", " ").replace("\r", " ").replace(",", ";")
        # issue['content'] = "%s %s" % (issue['title'], issue['content'])  ## no longer needed since I discovered there is a summary and a description field.

        w.writerow(issue)

    csv_file.close()


def main(bitbucket_json_file,  **kwargs):
    global OUTPUT_FILE
    global USER_MAP
    global STATUS_MAP
    global FIELDS_MAP

    if USER_MAP_FILE:
        USER_MAP = render_translation_file(USER_MAP_FILE)

    if STATUS_MAP_FILE:
        STATUS_MAP = render_translation_file(STATUS_MAP_FILE)

    if FIELDS_MAP_FILE:
        FIELDS_MAP = render_translation_file(FIELDS_MAP_FILE)

    if OUTPUT_FILE is None:
        OUTPUT_FILE = "odoo_import_me.csv"

    create_odoo_csv(bitbucket_json_file)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    # ARGUMENTS
    parser.add_argument('bitbucket_json_file', help='a Bitbucket Issues file exported (fomart = JSON)')

    parser.add_argument('-o', '--output', help='a csv Issues file ready to ODOO')
    parser.add_argument('-u', '--user-map-file', help='a CSV file with two columns, one with a Bitbucket username and another with the corresponding ODOO username.')
    parser.add_argument('-s', '--status-map-file', help='a CSV file with two columns, one with a Bitbucket workflow status and another with the corresponding ODOO task stages.')
    parser.add_argument('-f', '--fields-map-file', help='a CSV file with two columns, one with a Bitbucket field(column) names and another with the corresponding ODOO field(column) names.')

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    VERBOSE = args.verbose
    USER_MAP_FILE = args.user_map_file
    STATUS_MAP_FILE = args.status_map_file
    OUTPUT_FILE = args.output
    FIELDS_MAP_FILE = args.fields_map_file

    main(args.bitbucket_json_file)
