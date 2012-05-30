# encoding: utf-8

"""Release information about TurboMail."""


from textwrap import dedent


name = "TurboMail"
version = "3.0.3"
description = "TurboMail is a mail delivery subsystem and MIME message generation framework for Python."
long_description = dedent("""\
    TurboMail 3 offers:

    * Simplified creation of complex messages, including rich text, attachments, 
      and more.
    * Modular delivery managers including the blocking immediate manager and the
      threaded on demand manager.
    * Modular back-ends ('transports') including SMTP and in-memory (debug)
    * Easier debugging when using the debug back-end in concert with the immediate 
      manager.
    * A plugin architecture with a sample plugin for altered message encoding.
    * Automatic integration into TurboGears 1.x.

    Python includes several standard packages for handling e-mail. These libraries 
    are independent of each-other, their documentation is hard-to-follow, and their 
    examples are hardly real-world. TurboMail ties these dispersant elements 
    together with an elegant and extensible API, freeing you (the developer) from 
    drudge-work, strained eyes, and loss of hair, even for the most complicated 
    use-cases.
    """)

author = "Alice Bevan-McGregor"
email = "alice+turbomail@gothcandy.com"
url = "http://www.python-turbomail.org/"
download_url = "http://cheeseshop.python.org/pypi/TurboMail/"
copyright = u"© 2007-2009 Alice Bevan-McGregor, and contributors"
license="MIT"
