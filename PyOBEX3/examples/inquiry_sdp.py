import bluetooth

def get_sdp_svc(target):
  services = bluetooth.find_service(address=target)

  if len(services) > 0:
      print("found %d services on %s" % (len(services), target ))
      print()
  else:
      print("no services found")

  for svc in services:
      print("Service Name: %s"    % svc["name"])
      print("    Host:        %s" % svc["host"])
      print("    Description: %s" % svc["description"])
      print("    Provided By: %s" % svc["provider"])
      print("    Protocol:    %s" % svc["protocol"])
      print("    channel/PSM: %s" % svc["port"])
      print("    svc classes: %s "% svc["service-classes"])
      print("    profiles:    %s "% svc["profiles"])
      print("    service id:  %s "% svc["service-id"])
      print()
  return services


ds = bluetooth.discover_devices(lookup_names = True)
for d1 in ds:
  print(d1)
  addr, name = d1
  if name.find('acer') >= 0:
     print('use addr to search service {} - {}'.format(name, addr) )
     get_sdp_svc(addr)
#[('94:35:0A:9A:44:B5', 'HS3000'), ('00:15:83:3A:E9:6A', 'mikechenday.ddns.net'), ('00:18:60:F9:50:7A', 'acer S56')]


"""
# >python pbapclient.py 00:18:60:F9:50:7A
example: acer phone
Service Name: b'OBEX Phonebook Access Server\x00'
    Host:        00:18:60:F9:50:7A
    Description:
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 22
    svc classes: [b'112f']
    profiles:    [(b'1130', 257)]
    service id:  None

# >python pushclient.py 00:18:60:F9:50:7A 23 hello.txt
Service Name: b'OBEX Object Push\x00'
    Host:        00:18:60:F9:50:7A
    Description:
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 23
    svc classes: [b'1105']
    profiles:    [(b'1105', 256)]
    service id:  None

# install bluetooth ftp from google-store
# >python get_files.py 00:18:60:F9:50:7A /
Service Name: b'OBEX FTP\x00'
    Host:        00:18:60:F9:50:7A
    Description:
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 23
    svc classes: ['00001106-0000-1000-8000-00805F9B34FB']
    profiles:    []
    service id:  None

"""

