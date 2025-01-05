import sqlite3

conn = sqlite3.connect('tvef.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS exploits (
        exploit_id INTEGER PRIMARY KEY,
        exploit_name TEXT NOT NULL,
        cvss_score REAL NOT NULL,
        classification TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        telegram_version TEXT NOT NULL,
        exploit_code TEXT NOT NULL
    )
''')

exploits = [
    {
        'exploit_name': 'CVE-2022-30190',
        'cvss_score': 9.8,
        'classification': 'Critical',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Microsoft Office',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/ms_office_clickonce_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-26134',
        'cvss_score': 9.4,
        'classification': 'Critical',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Atlassian Confluence',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/atlassian_confluence_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-23277',
        'cvss_score': 9.1,
        'classification': 'Critical',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Adobe Acrobat Reader',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/adobe_acrobat_reader_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-21907',
        'cvss_score': 8.8,
        'classification': 'High',
        'category': 'Elevation of Privilege',
        'description': 'Elevation of privilege vulnerability in Windows Common Log File System Driver',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/ms16_135_win32k_eop.rb'
    },
    {
        'exploit_name': 'CVE-2022-21449',
        'cvss_score': 8.6,
        'classification': 'High',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Apache HTTP Server',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/apache_http_server_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-20664',
        'cvss_score': 8.4,
        'classification': 'High',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Microsoft Exchange Server',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/http/ms_exchange_server_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-19293',
        'cvss_score': 8.2,
        'classification': 'High',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Drupal',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/drupal_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-18485',
        'cvss_score': 8.0,
        'classification': 'High',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Spring Framework',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/spring_framework_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-17480',
        'cvss_score': 7.9,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Puppet',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/puppet_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-16763',
        'cvss_score': 7.8,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Grafana',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/grafana_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-15628',
        'cvss_score': 7.6,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Apache Struts',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/struts2_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-14345',
        'cvss_score': 7.4,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in Jenkins',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/jenkins_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-13808',
        'cvss_score': 7.2,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in F5 BIG-IP',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/f5_bigip_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-12774',
        'cvss_score': 7.0,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in FortiOS',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/fortios_rce.rb'
    },
    {
        'exploit_name': 'CVE-2022-11547',
        'cvss_score': 6.8,
        'classification': 'Medium',
        'category': 'RCE',
        'description': 'Remote code execution vulnerability in OpenWRT',
        'telegram_version': 'N/A',
        'exploit_code': 'https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/openwrt_rce.rb'
    }
]

for exploit in exploits:
    cursor.execute('''
        INSERT INTO exploits (
            exploit_name,
            cvss_score,
            classification,
            category,
            description,
            telegram_version,
            exploit_code
        ) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
    ''', (
        exploit['exploit_name'],
        exploit['cvss_score'],
        exploit['classification'],
        exploit['category'],
        exploit['description'],
        exploit['telegram_version'],
        exploit['exploit_code']
    ))

conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        report_id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_type TEXT NOT NULL,
        report_data TEXT
    )
''')

conn.commit()
conn.close()
