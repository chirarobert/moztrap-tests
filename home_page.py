#!/usr/bin/env python
#
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Case Conductor
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from base_page import CaseConductorBasePage


class CaseConductorHomePage(CaseConductorBasePage):

    _page_title = 'Mozilla Case Conductor'
    _select_locator = u'css=.selectruns .finder .carousel .colcontent .title:contains(%(item_name)s)'
    _submit_locator = u'css=.drilldown .environment .form-actions button'

    def go_to_homepage_page(self):
        self.selenium.open('/')
        self.is_the_current_page

    def select_item(self, name):
        _select_locator = self._select_locator % {'item_name': name}

        self.click(_select_locator)
        self.wait_for_ajax()

    def go_to_run_test(self, product_name, cycle_name, run_name):
        self.select_item(product_name)
        self.select_item(cycle_name)
        self.select_item(run_name)
        self.click(self._submit_locator, wait_flag=True)