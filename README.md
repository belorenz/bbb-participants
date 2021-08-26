# bbb-participants
Extracts participants of `BigBlueButton` 2.3 (also 2.2) conferences from the log file.
It can either print the result or send it via E-Mail.
The result is a list of all conferences including their participants sorted by starting time of the conference.


```plain
Übersicht der BigBlueButton Konferenzen am 11.11.2020



Testraum (8:32Uhr - 11:56Uhr)
	Walter Waltersen (0:00:00)
	Silke Silkens (0:06:39)
	Carolin Carolinsen (0:01:31)


Raum14 Drittmittelprojekte (9:48Uhr - 17:3Uhr)
	Sara Nachname (6:11:57)
	Joanna Döhla (6:45:52)
	Barbara Sara (5:57:27)

```


The script also allows to exclude some conferences.
The output is written in german, but can easily be changed to a different language with little effort (basically just change `self.subject` + "Uhr").

## Usage

```console
usage: python3 bbb-participants [-h] [--logfile L] [--print] [--host_sender H]
                        [--port_sender P] [--login_sender l]
                        [--password_sender p] [--mail_to m] [--mail_from M]

optional arguments:
  -h, --help           show this help message and exit
  --logfile L          logfile to parse.
  --print              Print participants to stdout instead of sending it by
                       mail.
  --host_sender H      Hostname of mail server to send report from.
  --port_sender P      Port of mail server to send report from.
  --login_sender l     Login for email account to send report from.
  --password_sender p  Password for email account to send report from.
  --mail_to m          E-Mail address to send report to.
  --mail_from M        E-Mail address to send report from.

```



By default `bbb-participants` uses the log file of today (/var/log/bigbluebuttong/bbb-web.log). 

## Automation
You can create an cronjob at 23:59 to extract the participants from today.
With the `--logfile` parameter any older log can be parsed as well.
```console
./bbb-participants --mail_to unclepeter@mail.com --login_sender MyEmailUsername --password_sender MySecurePassword --host_sender hostname.emailserverhosting.com --port-sender 1337 --mail_from MyEmailUsername@email.com 
```
