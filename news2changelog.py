from datetime import date
from re import compile as recompile

regex=recompile(r'^Version (?P<major>[.0-9]+)[.](?P<minor>[.0-9]+) '
                r'\(released (?P<year>[0-9]+)-(?P<month>[0-9]+)-(?P<day>[0-9]+)\)$')

def iter_changes(lines):
    version=None
    changes={}
    for line in filter(None,lines):
        match=regex.match(line)
        if match:
            version=int(match['major']),int(match['minor'])
            year,month,day=int(match['year']),int(match['month']),int(match['day'])
            changes[version]={'date':date.fromisoformat(f'{year:04}-{month:02}-{day:02}'),
                              'logs':[]}
        elif version:
            changes[version]['logs'].append(f'   {line}')
    for version in reversed(sorted(changes.keys())):
        yield version,changes[version]['date'],changes[version]['logs']

if __name__=='__main__':
    with open('cryptodev-linux/NEWS',mode='rt',encoding='utf8') as news,\
         open('debian/changelog',mode='wt',encoding='utf8') as changelog:
        for (major,minor),logdate,logs in iter_changes(map(str.rstrip,news)):
            print(f'cryptodev-linux ({major}.{minor}-1) unstable; urgency=low',
                  file=changelog)
            print(file=changelog)
            for line in logs:
                print(line,file=changelog)
            print(file=changelog)
            print(' -- Maintaincer <user@email.address> ',
                  f'{logdate:%a, %d %b %Y %T +0000}',
                  file=changelog)
            print(file=changelog)

# Local Variables:
# coding: utf-8
# mode: python
# python-indent-offset: 4
# indent-tabs-mode: nil
# End:
