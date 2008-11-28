#!/usr/bin/env python
import gettext

gettext.install('test-i18n', './locale', unicode=True)
print _("Greetings")

