# bbb-participants
Extracts participants `BigBlueButton` 2.2 conferences from the log file and sends them to an E-Mail address.

By default `bbb-participants` uses the log file of today (/var/log/bigbluebuttong/bbb-web.log). I created an cronjob at 23:59 to extract the participants from today.
With the `--logfile` parameter any older log can be parsed as well.

The result is a list of all conferences including their participants sorted by starting time of the conference. 
The output is in german, but can easily be changed to a different language with little effort (basically `self.subject` + "Uhr").

## usage

    ./bbb-participants --mail_to unclepeter@mail.com --login_sender MyEmailUsername --password_sender MySecurePassword --host_sender hostname.emailserverhosting.com  --mail_from MyEmailUsername@email.com
