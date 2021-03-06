=========================
Leave Management in hours
=========================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fhr-lightgray.png?logo=github
    :target: https://github.com/OCA/hr/tree/11.0/hr_holidays_hour
    :alt: OCA/hr
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/hr-11-0/hr-11-0-hr_holidays_hour
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/116/11.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

The standard Odoo application "Leave Management" allows employees to create
leave allocations and requests by defining their duration in days.

By installing this module, the duration of the leaves will be expressed in hours,
instead of days. In the leave form, a new field "duration" (in hours) will be displayed
and the original field "duration" (in days) will be hidden.

As an example, let's say that a working day for an employee is 8 hours:

* 1 day = 8 hours
* 2 days = 16 hours
* 0.5 days (half day) = 4 hours
* 0.125 days = 1 hour

etc...

If the employee wants to request a leave of one hour:

* with the standard Odoo app "Leave Management" the employee would write 0.125 days
* with module "hr_holidays_hour" installed, the employee writes 1.0 hour

If the employee wants to request half a day:

* with the standard Odoo app "Leave Management" the employee would write 0.5 days
* with module "hr_holidays_hour" installed, the employee writes 4.0 hours


In case a working time schedule is defined for an employee, the duration (in hours) will be
automatically filled while setting the starting date and the ending date of a leave request.

**Table of contents**

.. contents::
   :local:

Usage
=====

To request a leave, an employee can:

#. From menu Leaves, create a Leave Request by setting the duration in hours (instead of days)

To allocate hours for an employee:

#. From menu Leaves, create an Allocation Request by setting the duration in hours (instead of days)

To fully benefit from this module, the HR Officer should set a working time schedule for the employees.
The duration (in hours) will be automatically filled while setting the start and the end date of a leave.
In thi cas, the employee requesting a leave is still able to adjust the hours manually.

To set a working schedule for an employee:

#. From menu Employees -> Employees, select one employee
#. Set the "Working Time" field

If the "Working Time" is not set for the employee, but the employee has a contract with
a working schedule, the duration (in hours) will be automatically filled as well.

#. From menu Employees -> Employees, select one employee
#. Click on Contracts and select the employee's actual contract
#. Set the "Working Schedule" field

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/hr/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/hr/issues/new?body=module:%20hr_holidays_hour%0Aversion:%2011.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Onestein

Contributors
~~~~~~~~~~~~

* Antonio Esposito <a.esposito@onestein.nl>
* Andrea Stirpe <a.stirpe@onestein.nl>

Other credits
~~~~~~~~~~~~~

Tests for `resource_calendar` are repeated from the Odoo SA standard module `resource`.

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/hr <https://github.com/OCA/hr/tree/11.0/hr_holidays_hour>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
