from main import toodoo


def test_click_required_attr(runner):
    result = runner.invoke(toodoo, ['issues.json'])
    assert result.exception
    assert result.output.splitlines() == [
        'Import 2 Odoo',
        '...',
    ]


def test_click_set_attrs(runner):
    result = runner.invoke(
        toodoo,
        ['issues.json',
         '-u', 'sample_map_users_bit_odoo.csv',
         '-s', 'sample_map_status_bit_odoo.csv',
         '-f', 'sample_map_fields_name.csv'])
    assert not result.exception
    assert result.output.splitlines() == [
        'Import 2 Odoo',
        '...',
        'Generate file: odoo_import_me.csv'
    ]
