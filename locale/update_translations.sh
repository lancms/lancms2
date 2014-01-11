


#xgettext -i */*.py -i -klang -o locale/messages.pot --from-code=UTF-8 --copyright-holder="LANCMS and it's creators" --package-name='LANCMS' --msgid-bugs-address='bugs.launchpad.net' --package-version='2.0-alpha'

#./manage.py makemessages --all -e html -e py -l en-us
./manage.py makemessages -l en_US -d django -s
