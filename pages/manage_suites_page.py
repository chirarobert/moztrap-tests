#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import PageRegion
from pages.base_page import MozTrapBasePage
from pages.regions.filter import Filter
from pages.page import PageRegion


class MozTrapManageSuitesPage(MozTrapBasePage):

    _page_title = 'Manage-Suites'

    _test_suite_item_locator = (By.CSS_SELECTOR, '#manage-suites-form .listitem')

    @property
    def filter_form(self):
        return Filter(self.testsetup)

    def go_to_manage_suites_page(self):
        self.selenium.get(self.base_url + '/manage/suites/')
        self.is_the_current_page

    @property
    def test_suites(self):
        return [self.TestSuiteItem(self.testsetup, web_element)
                for web_element in self.find_elements(*self._test_suite_item_locator)]

    def delete_suite(self, name='Test Suite'):
        self._get_suite(name).delete()

    def view_cases(self, name='Test Suite'):
        return self._get_suite(name).view_cases()

    def edit_suite(self, name='Test Suite'):
        return self._get_suite(name).edit()

    def _get_suite(self, name='Test Suite'):
        for suite in self.test_suites:
            if suite.name == name:
                return suite
        raise NameError(u'test suite with %s name not found' % names)

    @property
    def test_suites(self):
        return [self.TestSuiteItem(self.testsetup, web_element)
                for web_element in self.find_elements(*self._test_suite_item_locator)]

    class TestSuiteItem(PageRegion):

        _delete_suite_locator = (By.CSS_SELECTOR, '.action-delete')
        _edit_suite_locator = (By.CSS_SELECTOR, '.edit-link')
        _view_cases_locator = (By.CSS_SELECTOR, '.casecount .drill-link')
        _suite_title_locator = (By.CSS_SELECTOR, '.title')

        @property
        def name(self):
            return self.find_element(*self._suite_title_locator).text

        def delete(self):
            self.find_element(*self._delete_suite_locator).click()
            self.wait_for_ajax()

        def edit(self):
            self.find_element(*self._edit_suite_locator).click()
            from pages.edit_suite_page import MozTrapEditSuitePage
            return MozTrapEditSuitePage(self.testsetup)

        def view_cases(self):
            self.find_element(*self._view_cases_locator).click()
            from pages.manage_cases_page import MozTrapManageCasesPage
            return MozTrapManageCasesPage(self.testsetup)
